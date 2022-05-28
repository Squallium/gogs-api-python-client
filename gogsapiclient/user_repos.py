from baseapiclient.endpoint import Endpoint
from baseapiclient.response import BaseModel, Response
from baseapiclient.server import Server
from gogsapiclient.repos import RepoModel


class UserRepos(Endpoint):
    base_path = '/api/v1/user/repos'

    def __init__(self, server) -> None:
        super().__init__()

        self.server = server

        self._base_path = self.base_path

    def create(self, body):
        response: Response = self._post(api_version=Server.VERSION_V1, body=body, model_class=RepoModel)
        response.ok_status = 201
        return response


    def get_all(self):
        return self._get(api_version=Server.VERSION_V1, model_class=ReposModel)


class ReposModel(BaseModel):

    def __init__(self, data) -> None:
        self.repos: [RepoModel] = None

        super().__init__(data)

        if isinstance(data, list) and len(data) > 0:
            self.repos = []
            for repo in data:
                self.repos.append(RepoModel(repo))

class RepoHelper:

    def __init__(self, name, description, private=True) -> None:
        super().__init__()

        self.name = name
        self.description = description
        self.private = private

    def create_body(self):
        return {
            'name': self.name,
            'description': self.description,
            'private': self.private
        }