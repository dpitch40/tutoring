import requests

from bs4 import BeautifulSoup

def parse_info(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, "lxml")

    info = soup.find("table", class_="infobox")
    d = {}
    for row in info.find_all("tr"):
        label = row.find("th", class_="infobox-label")
        if not label:
                continue
        data = row.find("td", class_="infobox-data")
        d[label.string] = ' '.join(data.stripped_strings)

    return d

print(parse_info(input('gib url  ')))
