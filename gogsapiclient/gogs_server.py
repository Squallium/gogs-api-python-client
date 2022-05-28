from baseapiclient.server import Server


class GogsServer(Server):

    def __init__(self, host=None, token=None, verify=None) -> None:
        super().__init__(host, token, verify)

        self.default_headers = {
            'Authorization': f'token {self.token}'
        }
