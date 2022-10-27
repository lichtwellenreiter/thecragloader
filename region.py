from dataclasses import dataclass


@dataclass
class Region:
    name: str
    url: str

    def __init__(self, name: str, url: str):
        self.name = name
        self.url = url
