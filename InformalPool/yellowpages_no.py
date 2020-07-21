import requests


class yellowpages:
    def __init__(self):
        self._get = requests.get

    def __str__(self):
        pass

    def __repr__(self):
        pass

    # TODO: fix json response, wtf, list with a dict inside a list with a dict inside list with a dict...wtf
    def check_phonenumber(self, phone_number: str, search_limit: int = 15):
        url = f"https://www.gulesider.no/api/ps?query={phone_number}&sortOrder=default&profile=no&page=1&lat=0&lng=0&limit={search_limit}&client=true"
        return self._get(url).json()["items"]
