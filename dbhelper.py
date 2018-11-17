import sqlite3

class DBHelper:
    """
    This class provides helper functions to communicate 
    with the sqlite database.

    """

    def __init__(self, dbname = 'chatlog.sqlite'):
        """creates database connection"""

        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)

    def setup(self):
        """ creates new table and column """

        stmt = 'CREATE TABLE IF NOT EXISTS msglog (messages text)'
        self.conn.execute(stmt)
        self.conn.commit()

    def add_item(self, item_text):
        """ inserts item into table """

        stmt = 'INSERT INTO msglog (messages) VALUES (?)'
        args = (item_text, )
        self.conn.execute(stmt, args)
        self.conn.commit()
    
    def delete_item(self, item_text):
        """ deletes item from table """

        stmt = 'DELETE FROM msglog WHERE messages = (?)'
        args = (item_text, )
        self.conn.execute(stmt, args)
        self.conn.commit()

    def get_items(self):
        """ gets all items from table """
        
        stmt = 'SELECT messages FROM msglog'
        return [x[0] for x in self.conn.execute(stmt)]