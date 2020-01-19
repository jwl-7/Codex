"""Database Helper

This module helps the bot interface with the sqlite database.
"""


import sqlite3


class Database:
    """This class provides helper functions to communicate with the sqlite database."""

    def __init__(self, dbname='db/chatlog.sqlite'):
        """Creates database connection."""
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)

    def setup(self):
        """Creates new table and column."""
        stmt = 'CREATE TABLE IF NOT EXISTS chatlog (messages text)'
        self.conn.execute(stmt)
        self.conn.commit()

    def add_item(self, item_text):
        """Inserts item into table."""
        stmt = 'INSERT INTO chatlog (messages) VALUES (?)'
        args = (item_text, )
        self.conn.execute(stmt, args)
        self.conn.commit()

    def delete_item(self, item_text):
        """Deletes item from table."""
        stmt = 'DELETE FROM chatlog WHERE messages = (?)'
        args = (item_text, )
        self.conn.execute(stmt, args)
        self.conn.commit()

    def get_items(self):
        """Gets all items from table."""
        stmt = 'SELECT messages FROM chatlog'
        return [x[0] for x in self.conn.execute(stmt)]
