from typing import TypedDict, NotRequired


class UserAuth(TypedDict):
    id: NotRequired[int]
    email: str
    hashed_password: str
