from pprint import pprint
import requests
from bs4 import BeautifulSoup


def findSubRegions(node):
    return node.find_all('ul')


def findRegionName(node):
    return node.find('span', class_="primary-node-name").contents[0]


def loadAllNodes(nodes):
    for node in nodes:
        sub_nodes = findSubRegions(node)
        print(findRegionName(node), " - SubNodes: ", len(sub_nodes))
        print(sub_nodes)


def findSubUl(node):
    return node.find('ul')


def start():
    base_url = "https://www.thecrag.com"
    url = base_url + "/de/klettern/world"
    resp = requests.get(url)
    results = BeautifulSoup(resp.content, 'html.parser')

    world_list = results.find('ul', class_="embed-menu")
    world_name = findRegionName(world_list)

    # print(world_name)
    # print(world_list)

    europe = world_list.find_all('span', class_="primary-node-name")

    print(europe)

    europe_a = europe[1].parent
    print(europe_a)
    europe_href = europe_a["href"]
    print(europe_href)

    europe_resp = requests.get(base_url + europe_href)

    europe_soup = BeautifulSoup(europe_resp.content, 'html.parser')

    europe_list = europe_soup.find('li', attrs={'class': 'open-submenu'})

    europe_list_ul = europe_list.find('ul')

    print(europe_list)
    print(europe_list_ul)


if __name__ == "__main__":
    start()
