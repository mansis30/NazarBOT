from ddgs import DDGS

def search_by_name(name):
    print(f"[*] NazarBOT: Searching surface web for '{name}'...")
    results = []
    
    
    query = f'"{name}" (site:linkedin.com OR site:github.com OR site:twitter.com)'
    
    try:
        
        ddgs = DDGS()
        raw_results = ddgs.text(query, region='wt-wt', safesearch='off', max_results=10)
        
        for r in raw_results:
            
            title = r.get('title', 'No Title')
            link = r.get('href', 'No Link')
            results.append(f"{title} - {link}")
            
        return results if results else ["No public profiles found."]
    except Exception as e:
        return [f"Search Error: {str(e)}"]