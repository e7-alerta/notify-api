PUSH_TEMPLATE = (
    "🚨 Alerta Vecinal: {alert_type} en {place_name} 🚨",
    "🚨 Alerta Vecinal: {alert_type} en {place_name} 🚨\n\n"
    "{greeting}, {contact_name}.\n\n"
    "{alert_owner} de {place_name} nos informó de un {alert_type} en su {place_type} ubicada en {place_address}.\n\n"
    "🔍 {mensaje_adicional}\n\n"
    "👮‍♂️ Estamos confirmando la situación y nos estamos comunicando con las autoridades.\n\n"
    "📲 Te mantendremos informado/a.\n\n"
    "⚠️ ¡Por favor, mantente alerta y toma precauciones!"
)

CHAT_TEMPLATE = (
    "",
    "🚨 Alerta Vecinal: {alert_type} en {place_name} 🚨\n\n"
    "{greeting}, {contact_name}.\n\n"
    "{alert_owner} de {place_name} nos informó de un {alert_type} en su {place_type} ubicada en {place_address}.\n\n"
    "🔍 {mensaje_adicional}\n\n"
    "👮‍♂️ Estamos confirmando la situación y nos estamos comunicando con las autoridades.\n\n"
    "📲 Te mantendremos informado/a.\n\n"
    "⚠️ ¡Por favor, mantente alerta y toma precauciones!"
)

VOICE_TEMPLATE = (
    "",
    "🚨 Alerta Vecinal: {alert_type} en {place_name} 🚨\n\n"
    "{greeting}, {contact_name}.\n\n"
    "{alert_owner} de {place_name} nos informó de un {alert_type} en su {place_type} ubicada en {place_address}.\n\n"
    "🔍 {mensaje_adicional}\n\n"
    "👮‍♂️ Estamos confirmando la situación y nos estamos comunicando con las autoridades.\n\n"
    "📲 Te mantendremos informado/a.\n\n"
    "⚠️ ¡Por favor, mantente alerta y toma precauciones!"
)


class MessageGenerator:
    def __init__(self):
        pass

    def generate_message(self, message_type, alert_type, placeInfo: dict, phoneInfo: dict, mensaje_adicional: str = ""):
        title = ""
        message = ""

        if message_type == "push_notification":
            title = PUSH_TEMPLATE[0].format(**placeInfo, alert_type=alert_type)
            message = PUSH_TEMPLATE[1].format(alert_type=alert_type, **placeInfo, **phoneInfo, mensaje_adicional=mensaje_adicional)
            print(message)

        elif message_type == "chat_message":
            message = CHAT_TEMPLATE[1].format(alert_type=alert_type, **placeInfo, **phoneInfo, mensaje_adicional=mensaje_adicional)
        elif message_type == "voice_message":
            message = VOICE_TEMPLATE[1].format(alert_type=alert_type, **placeInfo, **phoneInfo, mensaje_adicional=mensaje_adicional)
        else:
            raise ValueError("Invalid message type.")

        return title, message


if __name__ == '__main__':
    message_generator = MessageGenerator()
    alert_type = "Robo"
    placeInfo = {
        "place_name": "La casa de la abuela",
        "tipo_alerta": "Robo",
        "alert_owner": "Mabel",
        "place_type": "carnicería",
        "place_address": "Av. Rivadavia 1234",
    }
    mensaje_adicional = "El ladrón tiene una remera roja"
    phoneInfo = {
        "nombre_contacto": "Juan",
    }

    # (title,message) = message_generator.generate_message("push_notification", alert_type, placeInfo, phoneInfo, mensaje_adicional)
    # print(title)
    # print(message)
    (title, message) = message_generator.generate_message("chat_message", alert_type, placeInfo, phoneInfo, mensaje_adicional)
    print(message)
    # (title, message) = message_generator.generate_message("voice_message", alert_type, placeInfo, phoneInfo, mensaje_adicional)
    # print(message)
