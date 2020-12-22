import requests
import discord
import json

from discord.ext import commands

from InformalPool.validate import validation
from ._datastructs import PhonenumberStruct, AddressStruct, asdict
from InformalPool.misc import misc


class yellow_cog(commands.Cog):
    def __init__(self):
        self._get = requests.get
        self.valid = validation()
        self.misc = misc()

    @commands.command()
    async def gulesider(self, search_query: str, search_limit: int = 15):
        """
        gulesider - check number or name againt yellowpages api

        Args:
            search_query (str): [who do you want to lookup?]
            search_limit (int, optional): [description]. Defaults to 15.
        """

        result = {}
        url = f"https://www.gulesider.no/api/ps?query={search_query}&sortOrder=default&profile=no&page=1&lat=0&lng=0&limit={search_limit}&client=true"
        if self._get(url).json()["hits"] == 0:
            return f"Found no hits on {search_query}"
        else:
            for response in self._get(url).json()["items"]:
                _id = response["id"]
                _name = response["name"]
                _phoneNumbers = [k for k in list(response["phoneNumbers"])]
                _address = response["address"][0]
                _postcode = _address["postCode"]
                _postArea = _address["postArea"]
                _regionName = _address["regionName"]
                _xCoord = response["location"][0]["xCoord"]
                _yCoord = response["location"][0]["yCoord"]
                result[_id] = asdict(
                    PhonenumberStruct(
                        name=_name,
                        phoneNumbers=_phoneNumbers,
                        address=AddressStruct(
                            postCode=_postcode,
                            postArea=_postArea,
                            regionName=_regionName,
                            xCoord=_xCoord,
                            yCoord=_yCoord,
                        ),
                    )
                )
        del search_query  # else the variable is not propely cleaned
        self.misc.bot_send(self.misc._json_pretty(result), "json")
