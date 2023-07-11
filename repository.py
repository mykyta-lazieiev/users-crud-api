from flask import g

from config import config
import sqlite3
import hashlib


class UsersRepository:
    def __init__(self):
        conn = sqlite3.connect(config['DB_PATH'], check_same_thread=False)
        conn.row_factory = sqlite3.Row
        self.db = conn

    def execute(self, command, params=None):
        if params is None:
            params = []

        result = self.db.execute(command, params)
        self.db.commit()

        return result

    def hash_password(self, value):
        res = hashlib.md5(value.encode())
        return res.hexdigest()

    def fetch_all(self):
        return self.execute("SELECT name, email FROM Users").fetchall()

    def get_user(self, id):
        return self.execute("SELECT name, email FROM Users WHERE id = ?", [id]).fetchone()

    def create_user(self, data):
        query = 'INSERT INTO Users (name, email, password) VALUES(?, ?, ?)'
        password = self.hash_password(data['password'])
        params = (
            data['name'],
            data['email'],
            password
        )

        return self.execute(query, params).lastrowid

    def edit_user(self, id, data):
        query = "UPDATE Users SET name = ? AND email = ? AND password = ? WHERE id = ?"
        password = self.hash_password(data['password'])

        params = (
            data['name'],
            data['email'],
            password,
            id
        )

        return self.execute(query, params)

    def delete_user(self, id):
        return self.execute("DELETE FROM Users WHERE id = ?", [id])
