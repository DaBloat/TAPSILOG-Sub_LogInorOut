# CODE AUTHOR: KYNA
import sqlite3
import random


class UpdateAdmin:
    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email


class RegistrationAdmin:
    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email
        self.security_access = self.security_code()

    def security_code(self):
        range_start = 10 ** (5 - 1)
        range_end = (10 ** 5) - 1
        return random.randint(range_start, range_end)

    def get_security_access(self):
        return self.security_access


class AdminDatabase:
    def __init__(self):
        self.con = sqlite3.connect("databases/admin_database.db")
        self.c = self.con.cursor()

    def create_table(self):
        self.c.execute(''' CREATE TABLE IF NOT EXISTS admin(
                        username TEXT NOT NULL UNIQUE,
                        password TEXT NOT NULL,
                        name TEXT NOT NULL,
                        email TEXT NOT NULL UNIQUE,
                        sec_access INTEGER NOT NULL UNIQUE)''')
        self.con.commit()

    def create_admin(self, user):
        try:
            self.c.execute('''INSERT INTO admin(
                            username, password, name, email,sec_access)
                            VALUES(?,?,?,?,?)''', (user.username, user.password, user.name, user.email, user.security_access))
            self.con.commit()
        except sqlite3.IntegrityError:
            return {'Admin is already Registered!'}

    def delete_admin(self, sec_access):
        self.c.execute('''SELECT * FROM admin WHERE sec_access=?''', (sec_access,))
        value = self.c.fetchone()
        if not value:
            return {'No admin registered to delete!'}
        try:
            self.c.execute('''DELETE FROM admin WHERE sec_access=?''', (sec_access,))
            self.con.commit()
            return {"ADMIN ACCOUNT SUCCESSFULLY DELETED"}
        except:
            return {'Admin account cant find'}

    def update_admin(self, sec_access, user):
        self.c.execute("""SELECT * FROM admin WHERE sec_access =?""", (sec_access,))
        value = self.c.fetchone()
        if not value:
            return {"No admin registered to Update"}
        try:
            self.c.execute('''UPDATE admin
                          SET username = ?, name = ?, email = ?
                          WHERE sec_access = ?''', (user.username, user.name, user.email, sec_access))
            self.con.commit()
        except sqlite3.IntegrityError:
            return {"Admin is already added"}

    def update_pass(self, sec_id, password):
        self.c.execute("""SELECT * FROM admin WHERE sec_access =?""", (sec_id,))
        value = self.c.fetchone()
        if not value:
            return {"No admin registered to Update"}
        try:
            self.c.execute('''UPDATE admin
                                  SET password = ?
                                  WHERE sec_access = ?''',
                           (password, sec_id))
            self.con.commit()
        except sqlite3.IntegrityError:
            return {"Admin is already added"}

    def show_all_admin(self):
        self.c.execute('''SELECT * FROM admin''')
        value = self.c.fetchall()
        return value

    def search_admin(self, username):
        self.c.execute('''SELECT * FROM admin WHERE username=?''', (username,))
        value = self.c.fetchone()
        if not value:
            return {"No admin available"}
        return value

    def search_admin_sec(self, sec_id):
        self.c.execute('''SELECT * FROM admin WHERE sec_access=?''', (sec_id,))
        value = self.c.fetchone()
        if not value:
            return {"No admin available"}
        return value

    def search_admin_email(self, email):
        self.c.execute('''SELECT * FROM admin WHERE email=?''', (email,))
        value = self.c.fetchone()
        if not value:
            return {"No admin available"}
        return value






