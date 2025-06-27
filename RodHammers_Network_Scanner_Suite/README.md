# RodHammer's Network Scanner Suite

**RodHammer's Network Scanner Suite** is a professional-grade toolkit designed for cybersecurity professionals, ethical hackers, and penetration testers. It offers a modular, extensible platform with multiple advanced scanning tools bundled into one Python-based suite.

---

## Tools Included

1. **Advanced TCP Scanner**  
   Fast, threaded TCP port scanner with state detection (open, closed, filtered) and optional service resolution.

2. **Advanced UDP Scanner** *(Coming Soon)*  
   Non-intrusive UDP port scanner with timeout handling and optional packet inspection.

3. **Advanced OS Detector** *(Planned)*  
   Uses TTL, TCP/IP stack fingerprinting and banner grabbing to estimate the target operating system.

4. **Advanced SMTP Scanner** *(In Development)*  
   Verifies SMTP servers, checks for open relays, VRFY/EXPN vulnerabilities, and banner details.

5. **Advanced Vulnerability Scanner** *(Planned)*  
   Compares open ports and banners against CVE databases (via plugins or NVD APIs).

6. **All-in-One Scan**  
   Executes all scanning modules in sequence and summarizes results in a professional report.

---

## Features

- Built in Python 3 for portability and extensibility.
- Designed for integration into red-team tools or blue-team audits.
- Clean and easy-to-use terminal UI with numbered menu.
- Uses multithreading for high-speed scans.
- Designed for precision and reliability in professional use.
- Modular architecture — easily expandable.

---

## Target Audience

- Cybersecurity Analysts  
- Penetration Testers  
- Ethical Hackers  
- Security Engineers  
- Networking Students & Trainers

---

## Requirements

- Python 3.7+
- Cross-platform (Linux recommended for full functionality)
- Optional dependencies: `scapy`, `socket`, `concurrent.futures`


## Installation

git clone https://github.com/yourusername/rodhammers-scanner-suite.git
cd rodhammers-scanner-suite
python3 main.py
---

# Disclaimer
This suite is intended for educational and professional 
authorized use only. Always obtain proper permission before 
scanning any system that is not your own.
