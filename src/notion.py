import requests


class Notion:
    url_path = 'https://api.notion.com/v1/'
    notion_version = '2021-05-13'

    def __init__(self, sub_path, integration_token):
        self.sub_path = sub_path
        self.headers = {
            "Authorization": f"Bearer {integration_token}",
            "Content-Type": "application/json",
            "Notion-Version": self.notion_version
        }

    def get(self):
        response = requests.get(
            self.url_path + self.sub_path,
            headers=self.headers
        )
        if response.status_code != requests.codes.ok:
            raise Exception(response.content)
        return response.json()
