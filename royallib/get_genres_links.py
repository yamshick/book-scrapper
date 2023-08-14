import requests
from bs4 import BeautifulSoup

URL = "https://royallib.com/genres"


def get_genres_links(url):
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    text_url_array = []

    container = soup.find("div", {"style": "width:100%"})
    # print(container)
    elements = container.find_all("div")
    for element in elements:
        try:
            links = element.find_all("a")
            for link in links:
                try:
                    text = link.text.strip()
                    url = link["href"] 
                    print(text)
                    print(url)
                    text_url_array.append({text, url})
                except Exception as error:
                    print(error)    
                    print(link)
        except Exception as error:
            print(error)
            print(element)

    return text_url_array


res = get_genres_links(URL)
print(res)