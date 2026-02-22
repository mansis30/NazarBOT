import os
import requests
import re
import time
from dotenv import load_dotenv



load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

def github_contact_recon(name):
    """
    Scans GitHub code for public mentions of a name associated with 
    emails or phone numbers.
    """
    if not GITHUB_TOKEN:
        return {"error": "Missing GITHUB_TOKEN in .env file."}

    print(f"[*] NazarBOT: Initiating GitHub Recon for '{name}'...")
    
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }

    
    queries = [f'"{name}" email', f'"{name}" phone', f'"{name}" "cell"']
    found_contacts = {"emails": set(), "phones": set(), "sources": []}

    
    email_regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    phone_regex = r'(\+91[\-\s]?)?[0-9]{10}|(\+?\d{1,3}[\-\s]?)?\(?\d{3}\)?[\-\s]?\d{3}[\-\s]?\d{4}'

    for q in queries:
        
        url = f"https://api.github.com/search/code?q={q}"
        try:
            response = requests.get(url, headers=headers, timeout=15)
            
            if response.status_code == 403:
                print("[!] Rate limit hit. Waiting 10s...")
                time.sleep(10)
                continue
            
            if response.status_code == 200:
                items = response.json().get('items', [])
                for item in items[:5]:  
                    file_url = item['html_url']
                    raw_url = file_url.replace('github.com', 'raw.githubusercontent.com').replace('/blob/', '/')
                    
                    
                    file_res = requests.get(raw_url, headers=headers, timeout=10)
                    if file_res.status_code == 200:
                        content = file_res.text
                        
                        
                        emails = re.findall(email_regex, content)
                        phones = re.findall(phone_regex, content)
                        
                        if emails or phones:
                            found_contacts["emails"].update(emails)
                            
                            for p in phones:
                                if isinstance(p, tuple):
                                    found_contacts["phones"].add("".join(p))
                                else:
                                    found_contacts["phones"].add(p)
                            found_contacts["sources"].append(file_url)
            
            
            time.sleep(2)

        except Exception as e:
            print(f"[!] Module Error: {str(e)}")

    return found_contacts