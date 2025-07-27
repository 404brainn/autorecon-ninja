# 🥷 AutoRecon Ninja

> Automated subdomain enumeration, live host detection, and Nmap scanning — all in one ninja-fast script. Built for recon warriors.

---

## 🚀 Features

- ✅ Asset discovery using **Assetfinder**
- ✅ Deep subdomain enumeration using **Amass**
- ✅ Live host detection using **httpx**
- ✅ Port scanning on live hosts with **Nmap**
- ✅ Results saved in a clean folder structure: `outputs/<target-domain>/`

---

## 📦 Requirements

Make sure the following tools are installed:

- [assetfinder](https://github.com/tomnomnom/assetfinder)
- [amass](https://github.com/owasp-amass/amass)
- [nmap](https://nmap.org/)
- [Python 3.8+](https://www.python.org/)
- Python packages (listed in `requirements.txt`)

### 🛠 Install Python dependencies:

```bash
pip install -r requirements.txt

📁 Output Structure
All results will be stored in a folder like:

bash
Copy code
outputs/
└── target.com/
    ├── assetfinder.txt     # raw results from assetfinder
    ├── amass.txt           # raw results from amass
    ├── subs.txt            # merged and cleaned subdomains
    ├── live.txt            # live domains with title and status
    ├── live_hosts.txt      # just live domains (for Nmap)
    └── nmap.txt            # open port scan report
🔧 Usage
bash
Copy code
python recon.py
Then enter the target domain (e.g., tesla.com) when prompted.

📸 Example Run
bash
Copy code
$ python recon.py

   ___       __              ____                      
  / _ |__ __/ /  ___ ____   / __ \__ _____  ___ ____   
 / __ / // / _ \/ -_) __/  / /_/ / // / _ \/ _ `/ -_)  
/_/ |_\_,_/_.__/\__/_/     \____/\_,_/_//_/\_, /\__/   
                                           /___/  ninja
                      by 404brainn

🌐 Enter target domain (example.com): tesla.com

[+] Running assetfinder...
[+] Running amass...
[+] Probing for live hosts using httpx...
[+] Running Nmap scan on live hosts...

✅ Recon complete! All results saved to: outputs/tesla.com/
🧠 About
This tool is built for bug bounty hunters, penetration testers, and red teamers who want to automate reconnaissance with reliable tools and save clean output for further analysis.

📜 License
MIT License

🤝 Contributing
Feel free to fork, improve, or create pull requests. Add features like:

Screenshot support

Whois lookup

Vulnerability detection

CLI flags

✨ Author
Made with ⚡ by 404brainn
