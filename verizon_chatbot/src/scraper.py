import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from typing import List, Dict
from src.config import settings
import urllib.parse
import time
import logging

class VerizonScraper:
    def __init__(self):
        self.base_url = settings.VERIZON_COMMUNITY_URL
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument("--no-sandbox")
        self.chrome_options.add_argument("--disable-dev-shm-usage")
        
    def search_community(self, query: str) -> List[Dict]:
        try:
            driver = webdriver.Chrome(options=self.chrome_options)
            # query_text = urllib.parse.quote("t5/forums/searchpage/tab/message?advanced=false&allow_punctuation=false&q=")
            query_encode = urllib.parse.quote(query)
            query_url = "t5/forums/searchpage/tab/message?advanced=false&allow_punctuation=false&q="
            search_url = f"{self.base_url}{query_url}{query_encode}"

            driver.get(search_url)
            time.sleep(2)  # Wait for dynamic content to load
            
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            results = []
            
            for result in soup.find_all('div', class_='search-result'):
                title = result.find('h3').text.strip()
                snippet = result.find('div', class_='search-snippet').text.strip()
                url = result.find('a')['href']
                
                results.append({
                    'title': title,
                    'snippet': snippet,
                    'url': url
                })
            
            return results[:5]  # Return top 5 results
            
        except Exception as e:
            logging.error(f"Error searching community: {str(e)}")
            return []
        
        finally:
            driver.quit()