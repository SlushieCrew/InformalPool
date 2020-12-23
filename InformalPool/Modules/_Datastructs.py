from dataclasses import dataclass, asdict


@dataclass
class AddressStruct:
    postCode: int
    postArea: str
    regionName: str
    xCoord: float
    yCoord: float


@dataclass
class PhonenumberStruct:
    name: str
    phoneNumbers: list
    address: AddressStruct