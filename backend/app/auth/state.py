from typing import Any, Dict, List


class AuthPair:
    def __init__(self):
        self.store: Dict[int, List[str]] = {}  # {user_id: [access_token, refresh_token]}

    def post(self, id_user, tokens: Dict[str, str]):
        self.store[id_user] = [tokens["access_token"], tokens["refresh_token"]]

    def get(self, id_user) -> Any:
        return self.store.get(id_user)

