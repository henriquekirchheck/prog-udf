from typing import cast
from dacite.data import Data
import requests
from dataclasses import dataclass
from dacite import from_dict


@dataclass
class LocationRef:
    name: str
    url: str


@dataclass
class CharacterData:
    id: int
    name: str
    status: str
    species: str
    type: str
    gender: str
    image: str
    episode: list[str]
    origin: LocationRef
    location: LocationRef


@dataclass
class LocationData:
    id: int
    name: str
    type: str
    dimension: str
    residents: list[str]
    url: str


@dataclass
class EpisodeData:
    id: int
    name: str
    air_date: str
    episode: str
    characters: list[str]
    url: str


def main():
    r = requests.get("https://rickandmortyapi.com/api/character/214")
    character = from_dict(CharacterData, cast(Data, r.json()))
    print(f"Nome: {character.name}")
    print(f"Status: {character.status}")
    print(f"Genero: {character.gender}")
    print(f"Especie: {character.species}")


if __name__ == "__main__":
    main()
