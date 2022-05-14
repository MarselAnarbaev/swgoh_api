import requests
import db.database as database


class Allies:
    def __init__(self):
        self.connection = database.Connection()
        self.guild_data = requests.get('https://swgoh.gg/api/guild/3940/').json()
        self.allies = dict()

    def get_allies(self):
        for ally in self.guild_data['players']:
            self.allies[ally['data']['name']] = ally['data']['ally_code']
        return self.allies

    def truncate_alies(self):
        truncate_query = "truncate allies.codes"
        self.connection.set_data(truncate_query)

    def fill_allies(self):
        for nick, ally_code in self.allies.items():
            insert_query = """
            INSERT INTO allies.codes
            (ally_code, nick)
            VALUES({0}, '{1}');
            """.format(ally_code, nick)

    def update_allies(self):
        self.get_allies()
        self.truncate_alies()
        self.fill_allies()
        self.connection.close_con()

