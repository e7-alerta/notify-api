from dash import DashClient, dash_client


class DashService:

    def __init__(self, dash: DashClient):
        self.dash = dash


    pass


dash_service = DashService(dash_client)