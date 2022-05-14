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

    def get_data(self, _query):
        cursor = self.connection.cursor()
        cursor.execute(_query)
        return cursor.fetchall()

    def get_col_names(self, _query):
        cursor = self.connection.cursor()
        cursor.execute(_query)

    def set_data(self, _query):
        cursor = self.connection.cursor()
        cursor.execute(_query)
        self.connection.commit()

    def close_con(self):
        self.connection.close()