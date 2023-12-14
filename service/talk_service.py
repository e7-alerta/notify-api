from forms import TalkPlaceAlertForm
from talk import TalkClient, talk_client


class TalkService:

    def __init__(self, client: TalkClient):
        self.talker = client
        pass

    def talk(self, text):
        self.talker.talk(text)

    def notify_place_alert(self, form: TalkPlaceAlertForm):
        print("TalkService.notify_place_alert", form)
        return None


talk_service = TalkService(talk_client)
