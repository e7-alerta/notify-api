from forms import NotifyPlaceAlertForm, NotifyNearPlaceAlertForm, PusherPlaceAlertForm, TalkPlaceAlertForm, \
    SpeakPlaceAlertForm

from service.nearby_service import nearby_service
from service.pusher_service import pusher_service
from service.speak_service import speak_service
from service.talk_service import talk_service


def notify_place_alert(form: NotifyPlaceAlertForm):
    """
    Notify the user of an alert for a place.
    """

    # notify a phones with de app with a push notification
    pusher_service.notify_place_alert(
        PusherPlaceAlertForm(
            place_id=form.place_id,
            alert_type=form.alert_type,
            place=form.place,
            phones=form.phones
        )
    )

    pass


"""
    # notify a contacts with a chat message
    talk_service.notify_place_alert(
        TalkPlaceAlertForm(
            place_id=form.place_id,
            alert_type=form.alert_type,
            place=form.place,
            contacts=form.contacts
        )
    )

    # notify a contacts with a voice message
    speak_service.notify_place_alert(
        SpeakPlaceAlertForm(
            place_id=form.place_id,
            alert_type=form.alert_type,
            place=form.place,
            contacts=form.contacts
        )
    )

    # notify a nearby places
    nearby_service.notify_place_alert(
        NotifyNearPlaceAlertForm(
            place_id=form.place_id,
            alert_type=form.alert_type,
            place=form.place
        )
    )
"""
