import requests
# import time
# time.sleep(1)
from bs4 import BeautifulSoup

URL = "https://royallib.com/genre/starinnoe/"

# print(soup.pretify())

def get_links_from_genre(url):
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    text_url_array = []

    table_elements = soup.find_all("td")
    for table_element in table_elements:
        try:
            link = table_element.find("a")
            text = link.text.strip()
            url = link["href"]
            text_url_array.append({text, url})
        except Exception as e:
            print(e)

    return text_url_array


res = get_links_from_genre(URL)
print(res)