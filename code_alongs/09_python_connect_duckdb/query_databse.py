from database import DatabaseDatafram
from constant import DATABASE_PATH

class QueryDatabase():
    def __init__(self, sql_query) -> None:
        with DatabaseDatafram(DATABASE_PATH) as db:
            self.df = db.query(sql_query)