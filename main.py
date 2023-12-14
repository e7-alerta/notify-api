from typing import List

from fastapi import FastAPI

import forms

from manager import notifier

from pydantic import BaseModel

app = FastAPI()


# async def notify_place_alert(form: NotifyPlaceAlertForm):

@app.post("/notify/place_alert")
async def notify_place_alert(bodyForm: dict):
    print("[ notify place alert ] ", bodyForm)

    # alert type
    alert_type = bodyForm["changes"]["alert_type"]
    place = forms.PlaceInfo(
        id=bodyForm["place"]["id"],
        status=bodyForm["place"]["status"],
        place_type=bodyForm["place"]["place_type"],
        place_name=bodyForm["place"]["name"],
        phone=bodyForm["place"]["phone"],
        contacto=bodyForm["place"]["contacto"],
        place_address=bodyForm["place"]["street"] + " " + str(bodyForm["place"]["street_number"]),
        street=bodyForm["place"]["street"],
        street_number=bodyForm["place"]["street_number"],
        geolocation=bodyForm["place"]["geopoint"],
        neighborhood=bodyForm["place"]["neighborhood"],
        subregion=bodyForm["place"]["subregion"]
    )

    contacts: List[forms.ContactInfo] = []
    for contact in bodyForm["contacts"]:
        print("[ hidrate a contact ] ", contact)
        contacts.append(
            forms.ContactInfo(
                id=contact["id"],
                status=contact["status"],
                name=contact["name"],
                contact_type=contact["contact_type"],
                tags=contact["tags"],
                photo=contact["photo"],
                phone=contact["phone"],
                address=contact["address"],
                guardia_vecinal=contact["guardia_vecinal"],
                family=contact["family"],
                collaborator=contact["collaborator"],
                owner=contact["owner"]
            )
        )

    phones: List[forms.PhoneInfo] = []
    for phone in bodyForm["phones"]:
        print("[ hidrate a phone ] ", phone)
        phones.append(
            forms.PhoneInfo(
                id=phone["id"],
                push_token=phone["push_token"],
                status=phone["status"],
                name=phone["name"],
                phone_number=phone["phone_number"],
                contact=phone["contact"],
                alerted=phone["alerted"]
            )
        )

    form = forms.NotifyPlaceAlertForm(
        place_id=bodyForm["place"]["id"],
        alert_type=bodyForm["changes"]["alert_type"],
        place=place,
        contacts=contacts,
        phones=phones
    )

    print("[ notify place alert ] ", form)

    notifier.notify_place_alert(form)

    return {
        "status": "success",
        "message": "notificacion de alerta de place realizada"
    }


@app.get("/")
async def root():
    return {"message": "Hello Notify"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8030)
