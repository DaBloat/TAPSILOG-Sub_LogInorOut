import sqlite3


class Logs:
    def __init__(self):
        self.con = sqlite3.connect('databases/logs_in_out_database.db')
        self.c = self.con.cursor()

    def create_table(self):
        self.c.execute(''' CREATE TABLE IF NOT EXISTS log(
                               name TEXT NOT NULL,
                               contact TEXT NOT NULL,
                               date TEXT NOT NULL,
                               time_in TEXT NOT NULL ,y
                               time_out TEXT NOT NULL,
                               type TEXT NOT NULL
                               )''')
        self.con.commit()

    def add_log(self, name, contact, date, time_in, time_out, typec):
        self.c.execute('''INSERT INTO log(
                                    name, contact, date, time_in, time_out, type)
                                    VALUES(?,?,?,?,?, ?)''',
                       (name, contact, date, time_in, time_out, typec))
        self.con.commit()

    def show_log(self):
        self.c.execute('''SELECT * FROM log''')
        value = self.c.fetchall()
        return value

    def show_all_by_dates(self, date):
        self.c.execute('''SELECT * FROM log WHERE date = ?''', (date,))
        value = self.c.fetchall()
        return value


