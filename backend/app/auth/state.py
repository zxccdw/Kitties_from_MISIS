from typing import Any


class AuthPair:
    def __init__(self):
        self.store = {}  # {user_id: [access_token, refresh_token]}

    def post(self, user_id, access_token, refresh_token):
        self.store[user_id] = [access_token, refresh_token]

    def get(self, user_id) -> Any:
        return self.store.get(user_id)
