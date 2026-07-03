import datetime
from typing import TypedDict, NotRequired

class User(TypedDict):
  id: NotRequired[int]
  name: str
  email: str
  password: str
  date_last_period: datetime.date
  rest_offset_before: NotRequired[int]
  rest_offset_after: NotRequired[int]
  calendar_url: NotRequired[str]

class UpdateUserPayload(TypedDict):
  name: NotRequired[str]
  email: NotRequired[str]
  date_last_period: NotRequired[datetime.date]
  rest_offset_before: NotRequired[int]
  rest_offset_after: NotRequired[int]
  calendar_url: NotRequired[str]
