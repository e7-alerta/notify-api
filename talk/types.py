from typing import Optional

from pydantic import BaseModel


class TalkPlace(BaseModel):
    id: str
    name: str
    address: str
    phone: Optional[str]
    contact_name: str
    pass


class TalkContact(BaseModel):
    id: str
    name: str
    phone: str
    contact_type: str
    place_id: str
    chatwoot_id: str
    last_conversation_id: str
    pass
