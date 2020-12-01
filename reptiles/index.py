from os import path
from os import makedirs
import time
from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup

domain_url = "https://m.ibiquge.net"

download_path = './douban'
if not path.exists(download_path):
    makedirs(download_path)


def get_header():
    ua = UserAgent()
    return {"User-Agent": ua.chrome}


def save_text(content, title):
    global download_path
    file = open(download_path + "/" + title + ".txt", "a", encoding="utf-8")
    file.write(content)
    file.close()
    print(title)


def download(url='https://m.ibiquge.net/23_23717/10583299.html'):
    global domain_url
    headers = get_header()
    r = requests.get(url, headers=headers)
    r.encoding = "utf-8"
    soup = BeautifulSoup(r.text, 'lxml')
    title = soup.find("span", class_='title').getText()
    content = soup.find("div", class_='ReadAjax_content')
    next_url = soup.find("a", id='pb_next')['href'].replace(".html", "")
    now_url = url.replace(".html", "").replace(domain_url, "")

    [s.extract() for s in content("p")]
    content = str(content).replace('<br/><br/>', "\n").replace("</div>", "").replace(
        '<div class="Readarea ReadAjax_content" id="chaptercontent">', "").replace(u'\xa0', '').strip()

    save_text(content, title)
    time.sleep(1)
    if (now_url.split('_')[0] == next_url.split('_')[0]) & (now_url.split('_')[1] == next_url.split('_')[1]):
        download(domain_url + next_url + '.html')


def main():
    global domain_url
    headers = get_header()
    r = requests.get(domain_url + '/23/23717/', headers=headers)
    r.encoding = "utf-8"
    soup = BeautifulSoup(r.text, 'lxml')
    content = soup.find("div", class_='directoryArea')
    urls = content.find_all("a")
    url_list = [url['href'] for url in urls]
    url_list.remove("#bottom")
    print(len(url_list))
    # for url in url_list:
    #     download(domain_url + url)


if __name__ == '__main__':
    main()
    # download()
