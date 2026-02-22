import requests
from stem.control import Controller
from stem import SocketError
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def get_tor_session():
    session = requests.Session()
    
    # Define a retry strategy for unstable onion links
    retry_strategy = Retry(
        total=3,                # Try 3 times
        backoff_factor=2,      # Wait 2s, then 4s between tries
        status_forcelist=[429, 500, 502, 503, 504]
    )
    
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    
    session.proxies = {
        'http':  'socks5h://127.0.0.1:9150',
        'https': 'socks5h://127.0.0.1:9150'
    }
    return session

def get_tor_session():
    session = requests.Session()
    # Tor Browser uses 9150 for data on Windows
    session.proxies = {
        'http':  'socks5h://127.0.0.1:9150',
        'https': 'socks5h://127.0.0.1:9150'
    }
    return session

def is_tor_controllable():
    try:
        # Tor Browser uses 9151 for control signals
        from stem.control import Controller
        with Controller.from_port(port=9151) as controller:
            # We use authenticate() without a password 
            # because the Browser defaults to open control for local apps
            controller.authenticate() 
            return controller.is_alive()
    except Exception as e:
        print(f"Debug: Tor check failed on 9151. Error: {e}")
        return False