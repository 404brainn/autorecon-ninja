import os
import subprocess
import httpx
from colorama import Fore, Style, init

init(autoreset=True)

def banner():
    print(Fore.CYAN + r"""
   ___       __              ____                      
  / _ |__ __/ /  ___ ____   / __ \__ _____  ___ ____   
 / __ / // / _ \/ -_) __/  / /_/ / // / _ \/ _ `/ -_)  
/_/ |_\_,_/_.__/\__/_/     \____/\_,_/_//_/\_, /\__/   
                                           /___/  ninja
    """ + Fore.GREEN + "by 404brainn\n")

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
        return result.stdout.strip()
    except Exception as e:
        print(Fore.RED + f"[!] Error running command: {command}")
        return ""

def save_output(path, data):
    with open(path, "w") as f:
        f.write(data)

def main():
    banner()
    domain = input(Fore.YELLOW + "🌐 Enter target domain (example.com): ").strip()

    if not domain:
        print(Fore.RED + "[!] No domain entered.")
        return

    # Create output folder
    output_dir = os.path.join("outputs", domain)
    os.makedirs(output_dir, exist_ok=True)

    print(Fore.CYAN + f"\n🔍 Starting reconnaissance on: {domain}")
    
    print(Fore.YELLOW + "\n[+] Running assetfinder...")
    assetfinder_output = run_command(f"assetfinder {domain}")
    save_output(os.path.join(output_dir, "assetfinder.txt"), assetfinder_output)

    print(Fore.YELLOW + "[+] Running amass...")
    amass_output = run_command(f"amass enum -d {domain}")
    save_output(os.path.join(output_dir, "amass.txt"), amass_output)

    # Merge & deduplicate
    all_subs = set(assetfinder_output.splitlines()) | set(amass_output.splitlines())
    all_subs = sorted([sub for sub in all_subs if domain in sub])
    subs_path = os.path.join(output_dir, "subs.txt")
    save_output(subs_path, "\n".join(all_subs))

    print(Fore.YELLOW + f"[+] Total subdomains found: {len(all_subs)}")

    print(Fore.YELLOW + "\n[+] Probing for live hosts using httpx...")
    live_path = os.path.join(output_dir, "live.txt")
    live_hosts = []
    with open(subs_path, "r") as subs, open(live_path, "w") as live:
        for line in subs:
            url = "http://" + line.strip()
            try:
                r = httpx.get(url, timeout=3, follow_redirects=True)
                title = r.text.split("<title>")[1].split("</title>")[0] if "<title>" in r.text else ""
                status = r.status_code
                live.write(f"{url} - {status} - {title}\n")
                live_hosts.append(line.strip())
            except:
                continue

    # Clean live domains for nmap
    live_hosts_path = os.path.join(output_dir, "live_hosts.txt")
    save_output(live_hosts_path, "\n".join(live_hosts))

    print(Fore.YELLOW + f"[+] Live domains: {len(live_hosts)}")

    print(Fore.YELLOW + "\n[+] Running Nmap scan on live hosts...")
    nmap_output_path = os.path.join(output_dir, "nmap.txt")
    nmap_output = run_command(f"nmap -iL {live_hosts_path} -T4 --open")
    save_output(nmap_output_path, nmap_output)

    print(Fore.GREEN + f"\n✅ Recon complete! All results saved to: {output_dir}")

if __name__ == "__main__":
    main()
