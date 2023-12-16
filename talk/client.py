import requests as requests

from   talk.types import TalkPlace, TalkContact

class TalkClient:
    def __init__(self):
        pass

    def notify_place_alert(self, param):
        pass

    pass

    def talk(self, text):
        pass

    def send_alert(self, place: TalkPlace, contact: TalkContact):
        requests.post("https://talk.vecinos.com.ar/talk/v1/talk/panic_alert",
                      json={
                            "place": {
                                "id": place.id,
                                "name": place.name,
                                "address": place.address,
                                "contact_name": place.contact_name
                            },
                            "contact": {
                                "id": contact.id,
                                "name": contact.name,
                                "phone": contact.phone,
                                "contact_type": contact.contact_type,
                                "place_id": contact.place_id,
                                "chatwoot_id": contact.chatwoot_id,
                                "last_conversation_id": contact.last_conversation_id
                            }
                        }
                      )
        pass


talk_client = TalkClient()
