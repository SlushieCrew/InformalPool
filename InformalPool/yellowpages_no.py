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
        if self._get(url).json()["hits"] == 0:
            return f"Found no hits on {phone_number}"
        else:
            for result in self._get(url).json()["items"]:
                return result
                # search_id = result["id"]
                # search_name = result["name"]
                # search_phoneNumbers = result["phoneNumbers"]
                # search_address = result["address"]
                # search_id = result["id"]
                # return f"{search_id}\n{search_name}\n{search_phoneNumbers}\n{search_address}"


# print(yellowpages().check_phonenumber("91317878"))
