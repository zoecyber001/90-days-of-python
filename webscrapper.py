import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Example: Extracting all the headings (h1, h2, h3)
        headings = soup.find_all(['h1', 'h2', 'h3'])
        for heading in headings:
            print(heading.get_text())
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    url = input("Enter the URL of the website to scrape: ")
    scrape_website(url)
