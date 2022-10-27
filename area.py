from dataclasses import dataclass

@dataclass
class Area:
    name: str
    url: str

    def __init__(self, name: str, url: str):
        self.name = name
        self.url = url
