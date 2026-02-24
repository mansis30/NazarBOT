# NazarBOT👁️ - The All-Seeing Eye

NazarBOT is a sophisticated, modular OSINT reconnaissance tool designed for cybersecurity researchers and digital forensics enthusiasts. It automates the collection of digital footprints across the surface web, dark web, and developer ecosystems, providing a comprehensive analysis of a target's online presence.

---

## 🏗️ Technical Architecture

NazarBOT operates as a multi-layered engine where the GUI communicates with independent reconnaissance modules via asynchronous threading. This ensures that slow network requests do not crash the user interface.



---

## 🚀 Installation & Setup

### 1. Prerequisites
- **Python 3.10+**
- **Tor Browser/Service:** Must be active for Dark Web intelligence modules.
- **GitHub Personal Access Token:** Required for the GitHub Recon module.

### 2. Clone the Repository
```bash
git clone [https://github.com/mansis30/NazarBOT.git](https://github.com/mansis30/NazarBOT.git)
cd NazarBOT
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt

```

# Environment Configuration (Mandatory)

NazarBOT uses environment variables to keep your API tokens secure. Create a .env file in the root folder:

**GITHUB_TOKEN=your_personal_access_token_here**

DO NOT COMMIT THIS FILE TO GITHUB

# HOW TO USE

**Start Tor:** Ensure the Tor Browser is open or the Tor service is active in the background for anonymity.

**Launch GUI:** Run python gui.py to open the visual dashboard.

**Input Target:** Enter a Name or Phone Number in the dashboard search bar.

**Initiate Protocol:** Click the "Initiate Protocol" button to start the multi-module scan.

**Review Results:** Monitor the green console window for real-time intelligence hits as they are found.

**Export Findings:** Retrieve the final, detailed forensic report from the reports/ folder once the status shows "Scan Complete".

