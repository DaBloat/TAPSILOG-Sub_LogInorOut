# oop version CRUD howners na gumagana na
import sqlite3


class Homeowner:
    def __init__(self, name, blkno, lotno, pltno, contc, email, vehicle, idnum=None):
        self.name = name
        self.blkno = blkno
        self.idnum = idnum
        self.lotno = lotno
        self.pltno = pltno
        self.contc = contc
        self.email = email
        self.vehicle = vehicle


class HomeownersDB:
    def __init__(self):
        self.conn = sqlite3.connect('databases/HomeownersDB.db')
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS howner (
                            idnum INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            blkno INTEGER NOT NULL,
                            lotno INTEGER NOT NULL,
                            pltno TEXT,
                            contc INTEGER NOT NULL,
                            email TEXT NOT NULL,
                            vehicle INTEGER NOT NULL
                            )''')
        self.conn.commit()

    def create_hmowner(self, user):
        self.conn.execute('''INSERT INTO howner(name, blkno, lotno, pltno, contc, email, vehicle)
                                VALUES(?, ?, ?, ?, ?, ?, ?)''', (user.name, user.blkno, user.lotno, user.pltno, user.contc, user.email, user.vehicle))
        self.conn.commit()

    def get_hmowner(self, idnum):
        cursor = self.conn.execute(f"SELECT * FROM howner WHERE idnum={idnum}")
        howner = cursor.fetchone()
        return howner

    def get_hmowners(self, detail, value):
        if detail == "All":
            self.cursor.execute('SELECT * FROM howner')
            value = self.cursor.fetchall()
            final = []
            for homeowner in value:
                x = [homeowner[1], homeowner[2], homeowner[3], homeowner[4], homeowner[5], homeowner[0], homeowner[6], homeowner[7]]
                final.append(x)
            return final
        elif detail == "Homeowner ID":
            self.cursor.execute('SELECT * FROM howner WHERE idnum = ?', (value,))
            value = self.cursor.fetchall()
            for homeowner in value:
                if not homeowner:
                    return {'error': 'value not found'}
            final = []
            for homeowner in value:
                x = [homeowner[1], homeowner[2], homeowner[3], homeowner[4], homeowner[5], homeowner[0], homeowner[6], homeowner[7]]
                final.append(x)
            return final
        elif detail == "Name":
            self.cursor.execute('SELECT * FROM howner WHERE name = ?', (value,))
            value = self.cursor.fetchall()
            for homeowner in value:
                if not homeowner:
                    return {'error': 'value not found'}
            final = []
            for homeowner in value:
                x = [homeowner[1], homeowner[2], homeowner[3], homeowner[4], homeowner[5], homeowner[0], homeowner[6], homeowner[7]]
                final.append(x)
            return final
        elif detail == "Vehicle":
            self.cursor.execute('SELECT * FROM howner WHERE vehicle = ?', (value,))
            value = self.cursor.fetchall()
            for homeowner in value:
                if not homeowner:
                    return {'error': 'value not found'}
            final = []
            for homeowner in value:
                x = [homeowner[1], homeowner[2], homeowner[3], homeowner[4], homeowner[5], homeowner[0], homeowner[6], homeowner[7]]
                final.append(x)
            return final
        elif detail == "Plate Number":
            self.cursor.execute('SELECT * FROM howner WHERE pltno = ?', (value,))
            value = self.cursor.fetchall()
            for homeowner in value:
                if not homeowner:
                    return {'error': 'value not found'}
            final = []
            for homeowner in value:
                x = [homeowner[1], homeowner[2], homeowner[3], homeowner[4], homeowner[5], homeowner[0], homeowner[6], homeowner[7]]
                final.append(x)
            return final
        elif detail == "Contact Number":
            self.cursor.execute('SELECT * FROM howner WHERE contc = ?', (value,))
            value = self.cursor.fetchall()
            for homeowner in value:
                if not homeowner:
                    return {'error': 'homeowner not found'}
            final = []
            for homeowner in value:
                x = [homeowner[1], homeowner[2], homeowner[3], homeowner[4], homeowner[5], homeowner[0], homeowner[6], homeowner[7]]
                final.append(x)
            return final
        elif detail == "Email":
            self.cursor.execute('SELECT * FROM howner WHERE email = ?', (value,))
            value = self.cursor.fetchall()
            for homeowner in value:
                if not homeowner:
                    return {'error': 'homeowner not found'}
            final = []
            for homeowner in value:
                x = [homeowner[1], homeowner[2], homeowner[3], homeowner[4], homeowner[5], homeowner[0], homeowner[6], homeowner[7]]
                final.append(x)
            return final
        elif detail == "Blck No.":
            self.cursor.execute('SELECT * FROM howner WHERE blkno= ?', (value,))
            value = self.cursor.fetchall()
            for homeowner in value:
                if not homeowner:
                    return {'error': 'value not found'}
            final = []
            for homeowner in value:
                x = [homeowner[1], homeowner[2], homeowner[3], homeowner[4], homeowner[5], homeowner[0], homeowner[6], homeowner[7]]
                final.append(x)
            return final
        elif detail == "Lot No.":
            self.cursor.execute('SELECT * FROM howner WHERE lotno= ?', (value,))
            value = self.cursor.fetchall()
            for homeowner in value:
                if not homeowner:
                    return {'error': 'value not found'}
            final = []
            for homeowner in value:
                x = [homeowner[1], homeowner[2], homeowner[3], homeowner[4], homeowner[5], homeowner[0], homeowner[6], homeowner[7]]
                final.append(x)
            return final


    def upd_hmowner(self, user, idnum):
                self.conn.execute('''UPDATE howner SET name=?, blkno=?, lotno=?, pltno=?, contc=?, email=?, vehicle=?
                                     WHERE idnum=?''', (user.name, user.blkno, user.lotno, user.pltno, user.contc, user.email, user.vehicle, idnum))
                self.conn.commit()


    def del_hmowner(self, idnum):
        self.cursor.execute(f"DELETE FROM howner WHERE idnum={idnum}")
        self.conn.commit()

    def all_homeowner(self):
        self.cursor.execute('''SELECT * FROM howner''')
        value = self.cursor.fetchall()
        return value







