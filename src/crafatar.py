from os import getcwd
from pathlib import Path
from random import randint
from requests import Session

class Crafatar:
    def __init__(self, player_uuid: str) -> None:
        self.api = "https://crafatar.com"
        self.session = Session()
        self.session.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
        }
        self.player_uuid = player_uuid

    def save_file(
            self,
            content: bytes,
            location: str = getcwd()) -> bool:
        with open(
            Path(location).joinpath(f"{randint(0, 86400)}-{self.player_uuid}.png"),  mode="wb+") as file:
            file.write(content)
            file.close()
        return True

    def self.session.get_player_avatar(self, size: int = 100) -> bool:
        response = self.session.get(
            f"{self.api}/avatars/{self.player_uuid}", 
            headers=self.headers).content
        return self.save_file(content=response)

    def self.session.get_player_head(self) -> bool:
        response = self.session.get(
            f"{self.api}/renders/head/{self.player_uuid}").content
        return self.save_file(content=response)

    def self.session.get_player_body(self) -> bool:
        response = self.session.get(
            f"{self.api}/renders/body/{self.player_uuid}").content
        return self.save_file(content=response)

    def self.session.get_player_skin(self) -> bool:
        response = self.session.get(
            f"{self.api}/skins/{self.player_uuid}").content
        return self.save_file(content=response)

    def self.session.get_player_cape(self) -> bool:
        response = self.session.get(
            f"{self.api}/capes/{self.player_uuid}").content
        return self.save_file(content=response)
