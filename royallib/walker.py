import requests
import time
from bs4 import BeautifulSoup


ENTRY_URL = "https://royallib.com/"
WALK_DELAY = 0.001


def is_book_page(page):
    soup = BeautifulSoup(page.content, "html.parser")

    author = soup.find("b", string="Автор:")
    title = soup.find("b", string="Название:")
    genre = soup.find("b", string="Жанр:")
    fb2 = soup.find("a", string="Скачать в формате FB2")
    doc = soup.find("a", string="Скачать в формате DOC")
    rtf = soup.find("a", string="Скачать в формате RTF")
    txt = soup.find("a", string="Скачать в формате TXT")
    html = soup.find("a", string="Скачать в формате HTML")
    epub = soup.find("a", string="Скачать в формате EPUB")
    
    can_download = False
    if fb2 or doc or rtf or txt or html or epub:
        can_download = True

    print('-----')
    print(can_download)
    
    print(author, title, genre, fb2, doc, rtf, txt, html, epub)  

    if author and title and genre and can_download:
        # print(author, title, genre, download)  
        return True

    return False        

def get_is_valid_url(url):
    if 'royallib' in url:
        return True
    else:
        return False

visited_urls = []
def format_url(raw_url):
    is_valid = get_is_valid_url(raw_url)

    if is_valid == False:
        return False

    if raw_url[:2] != '//' and raw_url[:2] != 'ht':
        return False

    proper_url = raw_url
    if raw_url[:2] == '//':
        proper_url = "http:" + raw_url

    if proper_url in visited_urls:
        return False

    return proper_url

library = []
def process(url):
    with open("books.txt", "a") as myfile:
        myfile.write(url + "\n")
    library.append(url)


def walk(url):
    try:
        page = requests.get(url)

        visited_urls.append(url)

        print(url)
        if (is_book_page(page)):
            process(url)
            return

        soup = BeautifulSoup(page.content, "html.parser")

        links = soup.find_all("a")
        urls = [link["href"] for link in links]

        if (len(urls) == 0):
            return

        for raw_url in urls:
            proper_url = format_url(raw_url)
            if proper_url == False:
                continue

            walk(proper_url)
            time.sleep(WALK_DELAY)


        table_elements = soup.find_all("td")
    except Exception as e:
        print(e)
        pass    


walk(ENTRY_URL)

print(library[0:5])
print(len(library))