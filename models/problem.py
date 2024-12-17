from models.database import Database

class Problem:
    def __init__(self, title, description, location, reporter):
       
        self.title = title
        self.description = description
        self.location = location
        self.reporter = reporter
        self.db = Database()  # Database connection instance

    def save(self):
       
        query = "INSERT INTO problems (title, description, location, reporter) VALUES (?, ?, ?, ?)"
        self.db.execute_query(query, (self.title, self.description, self.location, self.reporter))

    @staticmethod
    def fetch_all():
        
        db = Database()
        query = "SELECT * FROM problems"
        return db.fetch_all(query)
