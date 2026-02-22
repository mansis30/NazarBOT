import requests

def check_leaks(target):
    print(f"[*] NazarBOT: Checking data breach databases for '{target}'...")
    
    
    url = f"https://leak-lookup.com/api/search" 
    payload = {'key': 'YOUR_FREE_API_KEY_HERE', 'type': 'phone_number', 'query': target}

    try:
        
        response = requests.post(url, data=payload, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            if data['error'] == 'false':
                return data['message'] 
            else:
                return ["No breaches found in public databases."]
        else:
            return [f"Error: API returned status {response.status_code}"]
            
    except Exception as e:
        return [f"Connection to Breach DB failed: {str(e)}"]