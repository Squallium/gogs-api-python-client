from baseapiclient.endpoint import Endpoint
from baseapiclient.response import BaseModel


class Repos(Endpoint):
    base_path = '/api/v1/repos/{owner}'

    def __init__(self, server, owner: str) -> None:
        super().__init__()

        self.server = server
        self.owner = owner

        self._base_path = self.base_path.format(
            owner=owner
        )

    def get(self, repo_name):
        return self._get(repo_name, model_class=RepoModel)


class RepoModel(BaseModel):

    def __init__(self, data) -> None:
        self.id: int = None
        self.name: str = None
        self.full_name: str = None
        self.description: str = None
        self.private: bool = None

        self.html_url: str = None
        self.ssh_url: str = None
        self.clone_url: str = None

        super().__init__(data)
