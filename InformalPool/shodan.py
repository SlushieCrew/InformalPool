import requests
from InformalPool.validate import validation


class shodan:
    def __init__(self):
        self._get = requests.get
        self.valid = validation()

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def honeypot_detect(self, ip: str, detect_score=0.5) -> str:
        # TODO: implement as that you can enter a domain and that it will resolve it's ip and use that to search for!

        url = f"https://api.shodan.io/labs/honeyscore/{self.valid.validate_ip(ip)}?key=Hgqwf9dHMIE157PNCeqVJc6TVvlyGKiP"
        score = self._get(url).text
        if float(score) >= detect_score:
            return f"{score} - Does NOT look like a real system!!!"

        if float(score) <= detect_score:
            return f"{score} - Looks like a real system!"

