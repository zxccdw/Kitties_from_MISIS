from typing import Any


class AuthPair:
    def __init__(self):
<<<<<<< Updated upstream
        self.store = {}  # {user_id: [access_token, refresh_token]}

    def post(self, user_id, access_token, refresh_token):
        self.store[user_id] = [access_token, refresh_token]

    def get(self, user_id) -> Any:
        return self.store.get(user_id)
=======
        self.success_store = {}  # {token: user_id}
        self.refresh_store = {}  # {token: user_id}

    def post_success(self, token, user_id):
        self.success_store[token] = user_id

    def get_success(self, token) -> Any:
        return self.success_store.get(token)

    def post_refresh(self, token, user_id):
        self.refresh_store[token] = user_id

    def get_refresh(self, token) -> Any:
        return self.refresh_store.get(token)
>>>>>>> Stashed changes
