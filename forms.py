from typing import Optional, List

from pydantic import BaseModel


class PhoneInfo(BaseModel):
    id: Optional[str] = None
    push_token: Optional[str] = None
    status: Optional[str] = None
    name: Optional[str] = None
    phone_number: Optional[str] = None
    contact: Optional[str] = None
    # geopoint: Optional[dict] = None
    alerted: Optional[bool] = None
    # alert_type: Optional[str] = None
    # alert_point: Optional[dict] = None


class ContactInfo(BaseModel):
    id: Optional[str] = None
    status: Optional[str] = None
    name: Optional[str] = None
    contact_type: Optional[str] = None
    tags: Optional[list] = []
    photo: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    # geopoint: Optional[dict] = None
    guardia_vecinal: Optional[bool] = None
    family: Optional[bool] = None
    collaborator: Optional[bool] = None
    owner: Optional[bool] = None


class PlaceInfo(BaseModel):
    id: Optional[str] = None
    status: Optional[str] = None
    place_type: Optional[List[str]] = None
    place_name: Optional[str] = None
    phone: Optional[str] = None
    contacto: Optional[str] = None
    place_address: Optional[str] = None
    street: Optional[str] = None
    street_number: Optional[int] = None
    geolocation: Optional[dict] = None
    neighborhood: Optional[str] = None
    subregion: Optional[str] = None


class NotifyNearPlaceAlertForm(BaseModel):
    place_id: str
    alert_type: str
    place: PlaceInfo


class NotifyPlaceAlertForm(BaseModel):
    place_id: str
    alert_type: str
    place: Optional[PlaceInfo]
    contacts: Optional[List[ContactInfo]] = []
    phones: Optional[List[PhoneInfo]] = []


class PusherPlaceAlertForm(BaseModel):
    place_id: str
    alert_type: str
    place: PlaceInfo
    phones: List[PhoneInfo] = []
    pass


class TalkPlaceAlertForm(BaseModel):
    place_id: str
    alert_type: str
    place: PlaceInfo
    contacts: List[ContactInfo] = []
    pass


class SpeakPlaceAlertForm(BaseModel):
    place_id: str
    alert_type: str
    place: PlaceInfo
    contacts: List[ContactInfo] = []
    pass
