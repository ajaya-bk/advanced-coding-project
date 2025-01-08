from models.base_model import BaseModel

class Problem(BaseModel):
    """
    Represents a community problem reported by a user.
    Inherits shared database operations from BaseModel.
    """

    def __init__(self, title, description, location, reporter):
        self.title = title
        self.description = description
        self.location = location
        self.reporter = reporter

    def save(self):
        """
        Saves the problem instance to the database.
        """
        query = "INSERT INTO problems (title, description, location, reporter) VALUES (?, ?, ?, ?)"
        self.execute_query(query, (self.title, self.description, self.location, self.reporter))

    @staticmethod
    def fetch_all():
        """
        Fetches all problems from the database.
        :return: List of all problems.
        """
        query = "SELECT * FROM problems"
        return super().fetch_all(query)
