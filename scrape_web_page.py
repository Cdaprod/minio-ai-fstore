import os
import requests
from bs4 import BeautifulSoup

def scrape_web_page(url):
    """
    Scrapes the specified web page and returns the text content.

    Args:
        url (str): The URL of the web page to scrape.

    Returns:
        str: The text content of the web page.
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            page_text = soup.get_text(separator='\n')
            return page_text
        else:
            return f"Failed to retrieve the page. Status code: {response.status_code}"
    except requests.RequestException as e:
        return f"An error occurred while making the request: {str(e)}"

if __name__ == "__main__":
    url = os.environ.get("URL")
    if url:
        result = scrape_web_page(url)
        print(result)
    else:
        print("Error: No URL provided.")