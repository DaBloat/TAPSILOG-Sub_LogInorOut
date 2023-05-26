# Visitors CRUD
# by jem -_-

import sqlite3

class Visitor:
    def __init__(self, name, vehicle, plate_number, contact, purpose, visitor_id=None):
        self.name = name
        self.vehicle = vehicle
        self.plate_number = plate_number
        self.contact = contact
        self.purpose = purpose
        self.visitor_id = visitor_id


class VisitorDB:
    def __init__(self):
        self.conn = sqlite3.connect("databases/VisitorsDB.db")
        self.cursor = self.conn.cursor()

    def createTable(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Visitors
                            (id INTEGER PRIMARY KEY,
                             name TEXT NOT NULL,
                             vehicle INT CHAR(1) NOT NULL,
                             plate_number TEXT, 
                             contact INT NOT NULL,
                             purpose STR NOT NULL)''')
        self.conn.commit()
        
    def create_visitor(self, visitor):
        self.cursor.execute('''INSERT INTO Visitors(name, vehicle, plate_number, contact, purpose)
                            VALUES(?, ?, ?, ?, ?)''', (visitor.name, visitor.vehicle, visitor.plate_number, visitor.contact, visitor.purpose))
        self.conn.commit()
        visitor_id = self.cursor.lastrowid
        visitor.visitor_id = visitor_id
        return visitor
    
    def get_visitors(self, detail, value):
        if detail == "All":
            self.cursor.execute('SELECT * FROM Visitors')
            visitors = self.cursor.fetchall()
            final = []
            for visitor in visitors:
                x = [visitor[1], visitor[2], visitor[3], visitor[4], visitor[5], visitor[0]]
                final.append(x)
            return final
        elif detail == "Visitor ID":
            self.cursor.execute('SELECT * FROM Visitors WHERE id = ?', (value,))
            visitors = self.cursor.fetchall()
            for visitor in visitors:
                if not visitor:
                    return {'error': 'Visitors not found'}
            final = []
            for visitor in visitors:
                x = [visitor[1], visitor[2], visitor[3], visitor[4], visitor[5], visitor[0]]
                final.append(x)
            return final
        elif detail == "Name":
            self.cursor.execute('SELECT * FROM Visitors WHERE name = ?', (value,))
            visitors = self.cursor.fetchall()
            for visitor in visitors:
                if not visitor:
                    return {'error': 'Visitors not found'}
            final = []
            for visitor in visitors:
                x = [visitor[1], visitor[2], visitor[3], visitor[4], visitor[5], visitor[0]]
                final.append(x)
            return final
        elif detail == "Vehicle":
            self.cursor.execute('SELECT * FROM Visitors WHERE vehicle = ?', (value,))
            visitors = self.cursor.fetchall()
            for visitor in visitors:
                if not visitor:
                    return {'error': 'Visitors not found'}
            final = []
            for visitor in visitors:
                x = [visitor[1], visitor[2], visitor[3], visitor[4], visitor[5], visitor[0]]
                final.append(x)
            return final
        elif detail == "Plate Number":
            self.cursor.execute('SELECT * FROM Visitors WHERE plate_number = ?', (value,))
            visitors = self.cursor.fetchall()
            for visitor in visitors:
                if not visitor:
                    return {'error': 'Visitors not found'}
            final = []
            for visitor in visitors:
                x = [visitor[1], visitor[2], visitor[3], visitor[4], visitor[5], visitor[0]]
                final.append(x)
            return final
        elif detail == "Contact Number":
            self.cursor.execute('SELECT * FROM Visitors WHERE contact = ?', (value,))
            visitors = self.cursor.fetchall()
            for visitor in visitors:
                if not visitor:
                    return {'error': 'Visitor not found'}
            final = []
            for visitor in visitors:
                x = [visitor[1], visitor[2], visitor[3], visitor[4], visitor[5], visitor[0]]
                final.append(x)
            return final
        elif detail == "Purpose":
            self.cursor.execute('SELECT * FROM Visitors WHERE purpose = ?', (value,))
            visitors = self.cursor.fetchall()
            for visitor in visitors:
                if not visitor:
                    return {'error': 'Visitor not found'}
            final = []
            for visitor in visitors:
                x = [visitor[1], visitor[2], visitor[3], visitor[4], visitor[5], visitor[0]]
                final.append(x)
            return final
    
    def get_visitor(self, visitor_id):
        self.cursor.execute('SELECT * FROM Visitors WHERE id = ?', (visitor_id,))
        visitor = self.cursor.fetchone()
        if not visitor:
            return {'error': 'Visitor not found'}
        x = [visitor[1], visitor[2], visitor[3], visitor[4], visitor[5], visitor[0]]
        return x
    
    def update_visitor(self, visitor):
        self.cursor.execute('SELECT * FROM Visitors WHERE id = ?', (visitor.visitor_id,))
        old_visitor = self.cursor.fetchone()
        if not old_visitor:
            return {'error': 'Visitor not found'}
        self.cursor.execute('''UPDATE Visitors
                            SET name = ?, vehicle = ?, plate_number = ?, contact = ?, purpose = ?
                            WHERE id = ?''', (visitor.name, visitor.vehicle, visitor.plate_number, visitor.contact, visitor.purpose, visitor.visitor_id))
        self.conn.commit()
        return visitor
    
    def delete_visitor(self, visitor_id):
        self.cursor.execute('SELECT * FROM Visitors WHERE id = ?', (visitor_id,))
        visitor = self.cursor.fetchone()
        if not visitor:
            return {'error': 'Visitor not found'}
        self.cursor.execute('DELETE FROM Visitors WHERE id = ?', (visitor_id,))
        self.conn.commit()
        return {'message': 'Visitor deleted successfully'}

    def all_visitor(self):
        self.cursor.execute('''SELECT * FROM Visitors''')
        value = self.cursor.fetchall()
        return value



