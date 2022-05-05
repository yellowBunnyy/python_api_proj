import re
from bs4 import BeautifulSoup
import requests


def get_pdf_shourt_cut(data_list):
    patt = r'(href=)"([A-Za-z._0-9]+)'
    agregated_pdf = []
    for data in data_list:
        finded = re.search(patt, str(data))
        if finded:
            agregated_pdf.append(finded.group(2))
    return agregated_pdf[::-1]


def create_all_urls(url, pdf_list):
    pdf_urls = []
    patt = '[.a-z0-9]+$'
    for str_pdf in pdf_list:
        pdf_urls.append(re.sub(patt, str_pdf, url))
    return pdf_urls


def get_all_pdf_urls():
    url = r'http://wwwold.pzh.gov.pl/oldpage/epimeld/grypa/2020/2020.htm'
    req = requests.get(url)
    soup = BeautifulSoup(req.text)
    tr_list = soup.find_all('tr')
    pdf_list = get_pdf_shourt_cut(data_list=tr_list)
    created_pdf_urls = create_all_urls(url, pdf_list=pdf_list)
    return created_pdf_urls


if __name__ == '__main__':
    print(get_all_pdf_urls())
