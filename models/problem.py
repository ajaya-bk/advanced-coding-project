from models.base_model import BaseModel

class Problem(BaseModel):
    def __init__(self, title, description, location, reporter):
        self.title = title
        self.description = description
        self.location = location
        self.reporter = reporter

    def save(self):
        query = "INSERT INTO problems (title, description, location, reporter) VALUES (?, ?, ?, ?)"
        self.execute_query(query, (self.title, self.description, self.location, self.reporter))

    @staticmethod
    def fetch_all():
        query = "SELECT * FROM problems"
        return super().fetch_all(query)
