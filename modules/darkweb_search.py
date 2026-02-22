from bs4 import BeautifulSoup
from core.anonymity import get_tor_session

def search_ahmia(query):
    session = get_tor_session()
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/115.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'
    }

    onion_url = f"http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion/search/?q={query}"
    
    try:
        print(f"[*] NazarBOT: Querying Ahmia for '{query}'...")
        response = session.get(onion_url, headers=headers, timeout=60)
        
        if response.status_code != 200:
            return [{"error": f"Ahmia returned status {response.status_code}"}]

        soup = BeautifulSoup(response.text, 'html.parser')
        results = []
        
        
        for li in soup.find_all('li', class_='result'):
            title_tag = li.find('h4')
            link_tag = li.find('cite')
            
            if title_tag and link_tag:
                results.append({
                    "title": title_tag.get_text().strip(),
                    "link": link_tag.get_text().strip()
                })
        
        return results if results else [{"title": "No results found on Ahmia.", "link": "N/A"}]

    except Exception as e:
        return [{"error": f"Connection failed: {str(e)}"}]