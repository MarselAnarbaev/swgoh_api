import psycopg2

class Connection:
    def __init__(self):
        self.connection = psycopg2.connect(
            user="dev",
            password="dev",
            host="127.0.0.1",
            port="5432",
            database="postgres"
        )