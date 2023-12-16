from forms import TalkPlaceAlertForm
from talk import TalkClient, talk_client
from talk.types import TalkContact, TalkPlace


class TalkService:

    def __init__(self, client: TalkClient):
        self.talker = client
        pass

    def talk(self, text):
        self.talker.talk(text)

    def notify_place_alert(self, form: TalkPlaceAlertForm):
        print("TalkService.notify_place_alert", form)

        # itero sobre los contactos
        for contact in form.contacts:
            print("TalkService.notify_place_alert.contact", contact)
            # envio el mensaje
            self.talker.send_alert(
                place=TalkPlace(
                    id=form.place_id,
                    name=form.place.place_name,
                    phone=form.place.phone,
                    address=form.place.place_address,
                    contact_name=form.place.contacto
                ),
                contact=TalkContact(
                    id=contact.id,
                    name=contact.name,
                    phone=contact.phone,
                    contact_type=contact.contact_type,
                    place_id=form.place.id,
                    chatwoot_id=contact.chatwoot_id,
                    last_conversation_id=contact.last_conversation_id
                )
            )
            pass
        pass


talk_service = TalkService(talk_client)
