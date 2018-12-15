import sqlite3


class SQLiteDB:
    DB_NAME = 'users.db'

    def __init__(self):
        self.conn = None
        try:
            open(SQLiteDB.DB_NAME, 'r').close()
        except FileNotFoundError:
            self._create_db()
        self.connect()

    def connect(self):
        self.conn = sqlite3.connect(SQLiteDB.DB_NAME, check_same_thread=False)

    @staticmethod
    def _create_db():
        conn = sqlite3.connect(SQLiteDB.DB_NAME)
        c = conn.cursor()
        c.execute('''
            CREATE TABLE Messages(timestamp int, chat_id int, msg_id int, data varchar)
        ''')
        conn.commit()
        conn.close()

    def alter_entry(self, chat_id, message_id, new_data):
        c = self.conn.cursor()
        c.execute('''
            UPDATE Messages SET data=? WHERE chat_id=? AND msg_id=?
        ''', (new_data, chat_id, message_id))
        self.conn.commit()

    def add_entry(self, timestamp, chat_id, message_id, data):
        c = self.conn.cursor()
        c.execute('''
            INSERT INTO Messages(timestamp, chat_id, msg_id, data) VALUES(?, ?)
        ''', (timestamp, chat_id, message_id, data))
        self.conn.commit()

    def remove_old(self, timestamp_ref):
        c = self.conn.cursor()
        c.execute('''
            DELETE FROM Messages WHERE timestamp <= ?
        ''', (timestamp_ref))

    def get_all(self):
        c = self.conn.cursor()
        c.execute('''
            SELECT * FROM Messages
        ''')
        f = c.fetchall()
        if f:
            return f

