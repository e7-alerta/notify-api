from pusher import PusherClient, pusher_client
from datetime import datetime

from pusher.client import PushBatchForm


def determinar_momento_dia():
    hora_actual = datetime.now().hour
    return "tarde" if hora_actual >= 12 else "mañana"


class PusherService:
    def __init__(self, client: PusherClient):
        self.pusher = client

    def notify_place_alert(self, PusherPlaceAlertForm):
        """
        Notify a phones with de app with a push notification api.
        :param PusherPlaceAlertForm:
        :return:
        """
        es_mañana = determinar_momento_dia() == "mañana"
        greeting = "Buenos días" if es_mañana else "Buenas tardes"

        print("PusherService.notify_place_alert | ", PusherPlaceAlertForm)
        # notificacion de alerta en un negocio cercano
        # if PusherPlaceAlertForm.alert_type == "near_place_alert":
        self.pusher.push_batch(
            PushBatchForm(
                contacts=list(map(lambda phone: (phone.push_token, {
                    "contact_name": phone.name
                }), PusherPlaceAlertForm.phones)),
                title_template=f"Alerta en {{contact_name}}",
                message_template=f"Alerta en {{contact_name}}"
            )
        )

        return None


pusher_service = PusherService(pusher_client)
