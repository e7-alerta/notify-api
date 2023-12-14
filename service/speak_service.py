from forms import SpeakPlaceAlertForm
from speak.client import SpeakClient, speak_client


class SpeakService:

    def __init__(self, speak: SpeakClient):
        self.speak = speak

    def speak(self, text):
        self.speak.speak(text)

    def notify_place_alert(self, form: SpeakPlaceAlertForm):
        print("SpeakService.notify_place_alert", form)
        return None


speak_service = SpeakService(speak_client)