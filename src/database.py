from notion import Notion


class Databases(Notion):
    def __init__(self, integration_token):
        super().__init__("databases", integration_token)
        response = self.get()
        self.databases = list(map(lambda d: Database(None, integration_token, d), response["results"]))


class Database(Notion):
    def __init__(self, db_id, integration_token, response=None):
        super().__init__(f"databases/{db_id}", integration_token)
        if response is None:
            response = self.get()

        self.database_id = db_id or response['id']
        self.created_time = response['created_time']
        self.last_edited_time = response['last_edited_time']
        self.title = response['title']
