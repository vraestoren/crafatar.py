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

    def _get(self, endpoint: str) -> bytes:
        return self.session.get(f"{self.api}{endpoint}").content

    def _save(self, content: bytes, location: str = None) -> bool:
        path = Path(location) if location else Path(getcwd())
        with open(path / f"{randint(0, 86400)}-{self.player_uuid}.png", "wb+") as file:
            file.write(content)
        return True

    def get_player_avatar(self, size: int = 100) -> bool:
        return self._save(self._get(f"/avatars/{self.player_uuid}?size={size}"))

    def get_player_head(self) -> bool:
        return self._save(self._get(f"/renders/head/{self.player_uuid}"))

    def get_player_body(self) -> bool:
        return self._save(self._get(f"/renders/body/{self.player_uuid}"))

    def get_player_skin(self) -> bool:
        return self._save(self._get(f"/skins/{self.player_uuid}"))

    def get_player_cape(self) -> bool:
        return self._save(self._get(f"/capes/{self.player_uuid}"))
