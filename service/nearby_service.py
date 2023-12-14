from forms import PlaceInfo
from nearby import NearbyClient, nearby_client
from pusher import PusherClient, pusher_client
from talk import TalkClient, talk_client


class NearbyService:
    """
    Service for Nearby Api.
    """

    def __init__(self, nearby: NearbyClient, pusher: PusherClient, talker: TalkClient):
        self.nearby = nearby
        self.pusher = pusher
        self.talker = talker

    def notify_place_alert(self, place_info: PlaceInfo):
        """
        Notify a phones with de app with a push notification api.
        :param param:
        :return:
        """
        # self.nearby.notify_place_alert(place_info)
        pass


nearby_service = NearbyService(nearby_client, pusher_client, talk_client)
