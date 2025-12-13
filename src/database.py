import sqlite3
import os

class Database:
    def __init__(self):
        # Connect to SQLite database file
        self.conn = sqlite3.connect("passwords.db")
        self.cursor = self.conn.cursor()

        # Create table if it doesn't exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS passwords (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                service TEXT NOT NULL,
                username TEXT NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def add_password(self, service, userid, encrypted_password):
        self.cursor.execute(
            "INSERT INTO passwords (service, username, password) VALUES (?, ?, ?)",
            (service, userid, encrypted_password)
        )
        self.conn.commit()

    def get_passwords(self):
        self.cursor.execute("SELECT service, username, password FROM passwords")
        results = self.cursor.fetchall()

        entries = []
        for row in results:
            entries.append({
                "service": row[0],
                "userid": row[1],
                "password": row[2]
            })
        return entries

    def delete_password(self, service, userid):
        self.cursor.execute(
            "DELETE FROM passwords WHERE service = ? AND username = ?",
            (service, userid)
        )
        self.conn.commit()

    def update_password(self, service, userid, new_enc_passwd):
        self.cursor.execute(
            "UPDATE passwords SET password = ? WHERE service = ? AND username = ?",
            (new_enc_passwd, service, userid)
        )
        self.conn.commit()

    def close(self):
        self.conn.close()
