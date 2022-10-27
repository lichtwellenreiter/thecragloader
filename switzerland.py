import requests
from bs4 import BeautifulSoup
from region import Region

if __name__ == "__main__":
    base_url = "https://www.thecrag.com"
    resp = requests.get(base_url + "/de/klettern/switzerland")
    switzerland = BeautifulSoup(resp.content, 'html.parser')

    table = switzerland.find('form', attrs={"class": "donttrackunsaved"})
    # print(table)

    areas = table.find_all('div', attrs={"class": "area"})

    # print(areas[1:])

    regions = []

    for area in areas[1:]:
        name = area.find('div', attrs={"class": "name"})
        region_name = name.find('span', attrs={"class": "primary-node-name"})
        url = name.find('a')
        print(region_name.contents[0], " ", url['href'])
        regions.append(Region(region_name.contents[0], url['href']))

    print(regions)

    for region in regions:
        areas = []
        resp = requests.get(base_url + region.url)

