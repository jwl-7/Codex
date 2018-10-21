import sqlite3

class DBHelper:
    # This class provides helper functions to communicate 
    # with the sqlite database.

    # creates database connection
    def __init__(self, dbname = 'chatlog.sqlite'):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)

    # creates new table and column
    def setup(self):
        stmt = 'CREATE TABLE IF NOT EXISTS msglog (messages text)'
        self.conn.execute(stmt)
        self.conn.commit()

    # inserts item into table
    def add_item(self, item_text):
        stmt = 'INSERT INTO msglog (messages) VALUES (?)'
        args = (item_text, )
        self.conn.execute(stmt, args)
        self.conn.commit()
    
    # deletes item from table
    def delete_item(self, item_text):
        stmt = 'DELETE FROM msglog WHERE messages = (?)'
        args = (item_text, )
        self.conn.execute(stmt, args)
        self.conn.commit()

    # gets all items from table
    def get_items(self):
        stmt = 'SELECT messages FROM msglog'
        return [x[0] for x in self.conn.execute(stmt)]