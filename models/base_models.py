from models.database import Database

class BaseModel:

    db = Database()  

    @staticmethod
    def fetch_all(query):

        return BaseModel.db.fetch_all(query)

    def execute_query(self, query, params=()):

        self.db.execute_query(query, params)
