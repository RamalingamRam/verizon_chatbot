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
            
            # result = soup.find_all('div', class_='lia-quilt lia-quilt-message-search-item lia-quilt-layout-list-item')
            # print(result.get_text())

            for result in soup.find_all('div', class_='lia-quilt lia-quilt-message-search-item lia-quilt-layout-list-item'):
                # print(result.get_text().strip())

                # title = result.find_all('span', class_='lia-search-match-lithium').get_text().strip()
                # title = result.find_all(attrs={'class': 'lia-search-match-lithium'})

                title_text = ''
                for title in result.find_all(lambda tag: tag.name == 'span' and tag.get('class') == ['lia-search-match-lithium']):
                    title_text += title.get_text() + ' '
                    
                title_text = title_text.strip()
                print("_____ START TITLE _________")
                print(title_text)
                print("_____ STOP TITLE _________")
                
                snippet_text = ''
                # st = result.find_all(lambda tag: tag.name == 'span' and tag.get('class') == ['lia-search-match-lithium lia-search-match-lithium'])
                # '<br/>'.join([str(tag) for tag in table])
                
                st = result.find_all('div', class_='lia-truncated-body-container')
                tags = '<br/>'.join([str(tag) for tag in st])
                snippet_soup = BeautifulSoup(tags, 'html.parser')
                snippet_text = snippet_soup.get_text().strip()

                # snippets = snippet_soup.find_all('span', class_='lia-search-match-lithium lia-search-match-lithium')
                # snippet_text = snippets.get_text().strip()

                # for snippet in result.find_all(lambda tag: tag.name == 'span' and tag.get('class') == ['lia-search-match-lithium lia-search-match-lithium']):
                #     snippet_text += snippet.get_text() + ' '

                # snippet_text = snippet_text.strip()
                
                print("_____ START SNIPPET _________")
                print(snippet_text)
                print("_____ STOP SNIPPET _________\n")

                # url_text = result.find('a', class_='page-link lia-link-navigation lia-custom-event', href_=True)
                # tags = soup.select("a.page-link.lia-link-navigation.lia-custom-event[href]")

                link = result.find('a', class_='page-link lia-link-navigation lia-custom-event')
                href = link['href']

                # Remove the query parameters
                cleaned_href = href.split('?')[0]

                # Prepend the base URL
                url_text = f"https://community.verizon.com{cleaned_href}"

                print("\n_____ START URL _________")
                print(url_text)
                print("_____ STOP URL _________")
               
                # tt = result.find_all('span', class_='lia-search-match-lithium')

                # for title in result.find_all('span', class_='lia-search-match-lithium'):
                #     # msg_title = title.get_text()
                #     print(title.text.strip())
                # title = result.find('span', class_='lia-search-match-lithium').text.strip()
                # snippet = result.find('span', class_='lia-truncated-body-container').text.strip()
                # url = result.find('a', class_='page-link lia-link-navigation lia-custom-event')['href']
                
                results.append({
                    'title': title_text,
                    'snippet': snippet_text,
                    'url': url_text
                })
                results.append({
                    'Message': result
                })
            
            return results[:]  # Return top 5 results
            
        except Exception as e:
            logging.error(f"Error searching community: {str(e)}")
            return []
        
        finally:
            driver.quit()