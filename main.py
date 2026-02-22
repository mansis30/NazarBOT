import sys
from core.anonymity import is_tor_controllable
from modules.phone_lookup import get_phone_metadata
from modules.darkweb_search import search_ahmia 
from modules.breach_check import check_leaks 
from modules.surface_web import search_by_name 
from modules.github_recon import github_contact_recon 
from modules.reporter import generate_report

def startup_banner():
    print("\n      NazarBOT v1.0\n    [ The All-Seeing Eye ]\n")

def run_nazar_scan(target):
    """
    This is the core engine. Both the GUI and CLI call this function.
    All modules must stay inside here to be visible in the GUI console.
    """
    startup_banner()
    
    # 0. Connectivity Check
    if not is_tor_controllable():
        print("[-] Critical Failure: Tor is not reachable. Scans aborted.")
        return
    
    print(f"[*] NazarBOT Engine: Analyzing {target}...\n")
    
    # 1. Run Phone Metadata Lookup
    phone_results = get_phone_metadata(target)
    print("--- [ Phone Intelligence ] ---")
    for key, value in phone_results.items():
        print(f"[+] {key}: {value}")

    # 2. Dark Web Search
    print("\n--- [ Dark Web Intelligence ] ---")
    dark_results = search_ahmia(target)
    for res in dark_results:
        if "error" in res:
            print(f"[!] {res['error']}")
        else:
            print(f"[+] Found: {res['title']}")
            print(f"    Link:  {res['link']}")

    # 3. Data Breach Search
    print("\n--- [ Breach Intelligence ] ---")
    leaks = check_leaks(target)
    if not leaks or "No breaches found" in str(leaks):
        print("[+] Status: Target is clean. No leaks found.")
    else:
        for leak in leaks:
            print(f"[!] CRITICAL: Found in leak: {leak}")
    
    # 4. Surface Web Search
    print("\n--- [ Surface Web Mentions ] ---")
    mentions = search_by_name(target)
    for link in mentions:
        print(f"[+] Found Profile/Doc: {link}")

    # 5. GitHub Recon
    print("\n--- [ GitHub Recon Intelligence ] ---")
    recon_data = github_contact_recon(target)
    if "error" in recon_data:
        print(f"[!] {recon_data['error']}")
    else:
        print(f"[+] Found {len(recon_data['emails'])} unique emails and {len(recon_data['phones'])} phones.")
        
        if recon_data["emails"]:
            print("\n[ Emails Found ]")
            for email in sorted(recon_data["emails"]):
                print(f"  - {email}")
        
        if recon_data["phones"]:
            print("\n[ Phone Numbers Found ]")
            for phone in sorted(recon_data["phones"]):
                print(f"  - {phone}")
        
        if recon_data.get("sources"):
            print("\n[ Sources Found ]")
            for source in recon_data["sources"][:3]:
                print(f"  - {source}")

    # 6. Final Reporting
    all_data = {
        "Phone Intelligence": phone_results,
        "Surface Web Mentions": mentions,
        "Dark Web Results": dark_results,
        "GitHub Recon": recon_data,
        "Breach Check": leaks
    }

    generate_report(target, all_data)
    print("\n[*] Scan complete. Report saved in /reports/ directory.")
    print("[*] NazarBOT is going offline.")

# ---------------------------------------------------------
# CLI ENTRY POINT
# ---------------------------------------------------------
if __name__ == "__main__":
    # This block only runs if you play 'main.py' directly
    try:
        target_input = input("Enter search target (Name/Phone): ")
        if target_input.strip():
            run_nazar_scan(target_input)
        else:
            print("[!] Error: Target cannot be empty.")
    except KeyboardInterrupt:
        print("\n[!] User interrupted. Exiting...")
        sys.exit(0)