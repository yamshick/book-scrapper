import requests
# import time
# time.sleep(1)
from bs4 import BeautifulSoup

URL = "https://royallib.com/genre/starinnoe/"

# print(soup.pretify())

def get_links(url):
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    links = []

    table_elements = soup.find_all("td")
    for table_element in table_elements:
        try:
            link = table_element.find("a")
            print(link.text.strip())
            print(link["href"])
            links.push({text: link.text.strip(), url: link["href"]})
        except:
            pass
        #    print('\nerror:')    
        #    print(table_element, end="\n"*2)

    return links


get_links(URL)