from typing import Any, Dict, List


class AuthPair:
    def __init__(self):
        self.store: Dict[int, List[str]] = {}  # {user_id: [access_token, refresh_token]}

    def post(self, user_id, tokens: Dict[str, str]):
        self.store[user_id] = [tokens["access_token"], tokens["refresh_token"]]

    def get(self, user_id) -> Any:
        return self.store.get(user_id)

