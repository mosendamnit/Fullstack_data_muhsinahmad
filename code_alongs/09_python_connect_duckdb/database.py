import duckdb


class Database:

    def __init__(self , db_path ) -> None:
        self.connection = None
        self.db_path = db_path


    def __enter__(self):
        self.connection = duckdb.connect(self.db_path)
        return self
    
    def query (self, query):
        return self.connection.execute(query).fetchall()

    def __exit__ (self , exc_type , exc_value , trackbaclk):
        if self.connection:
            self.connection.close()
        

class DatabaseDatafram(Database):
    def query(self, query):
        return self.connection.execute(query).df()
