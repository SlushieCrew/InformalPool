import requests
import discord
import json

from discord.ext import commands
from loguru import logger as log

from ..Modules._Datastructs import PhonenumberStruct, AddressStruct, asdict
from ..Modules._Utility import _Utility
from ..Modules._Validate import _Validate


class Gulesider(commands.Cog):
    def __init__(self):
        self._load_cog = False
        self._get = requests.get
        self.valid = _Validate()
        self.utility = _Utility()

    @commands.command()
    async def gulesider(self, ctx, search_query: str, search_limit=15):
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
                _address = response["address"]
                _postcode = _address["postCode"]
                _postArea = _address["postArea"]
                _regionName = _address["regionName"]
                # _xCoord = response["location"]["xCoord"]
                # _yCoord = response["location"]["yCoord"]
                result[_id] = asdict(
                    PhonenumberStruct(
                        name=_name,
                        phoneNumbers=_phoneNumbers,
                        address=AddressStruct(
                            postCode=_postcode,
                            postArea=_postArea,
                            regionName=_regionName,
                            xCoord="",
                            yCoord="",
                        ),
                    )
                )
        log.info(result)
        # del search_query  # else the variable is not propely cleaned
        await self.utility.bot_send(ctx, result, lang="json")
