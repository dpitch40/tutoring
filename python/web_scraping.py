import requests
import argparse

from bs4 import BeautifulSoup

def parse_info(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, "lxml")
    soup.find_all("table", class_="infobox")

    info = soup.find("table", class_="infobox")
    d = dict()
    for row in info.find_all("tr"):
        label = row.find("th", class_="infobox-label")
        if not label:
                continue
        data = row.find("td", class_="infobox-data")
        d[label.string] = ' '.join(data.stripped_strings)

    return d

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    args = parser.parse_args()

    print(parse_info(args.url))

if __name__ == '__main__':
    main()
