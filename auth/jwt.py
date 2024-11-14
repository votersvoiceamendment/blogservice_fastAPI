from typing import List
from uuid import UUID

class JWT:
    user_id: UUID
    roles: List[str]

    def __init__(self, user_id: UUID, roles: List[str]) -> None:
        self.user_id = user_id
        self.roles = roles