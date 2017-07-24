import sqlite3


__author__ = 'anaeanet'


class DBHelper:
    """
    Data Access Module (DAM) providing an interface
    to separate bot implementation from specific database implementation.
    """

    def __init__(self, db_name):
        self.__conn = sqlite3.connect(db_name)
        self.setup()

    def setup(self):

        # create required tables
        tbl_statements = [
              "CREATE TABLE IF NOT EXISTS user (user_id INTEGER NOT NULL PRIMARY KEY"
                                                + ", user_name TEXT NOT NULL"
                                                + ", user_state INTEGER NOT NULL"
                                                + ", message_id INTEGER"
                                                + ", post_id INTEGER)"
        ]

        for stmt in tbl_statements:
            self.__conn.execute(stmt)

        # create some indexes
        idx_statements = [
              "CREATE INDEX IF NOT EXISTS user_id ON user (user_id ASC)"
        ]
        for stmt in idx_statements:
            self.__conn.execute(stmt)

        # make sure foreign keys are enforced
        fk_stmt = "PRAGMA foreign_keys = ON"
        self.__conn.execute(fk_stmt)

        self.__conn.commit()

    # -------------------------------------------------- user ----------------------------------------------------------

    def get_users(self, **filters):
        stmt = "SELECT * FROM user"
        args = []

        if filters:
            stmt += " WHERE " + " = ? AND ".join(filters.keys()) + " = ?"
            for key, value in filters.items():
                args.append(value)

        return [[x[0], x[1], x[2], x[3], x[4]] for x in self.__conn.execute(stmt, tuple(args))]

    def get_user(self, user_id):
        user = None

        users = self.get_users(**{"user_id": user_id})
        if len(users) == 1:
            user = users[0]

        return user

    def add_user(self, user_id, user_name, user_state, message_id=None, post_id=None):
        param_dict = dict({key: value for key, value in locals().items() if key != "self"})

        stmt = "INSERT INTO user (" + ",".join(param_dict.keys()) + ") " \
               + "VALUES (" + ",".join(["?" for x in param_dict.keys()]) + ")"
        args = []

        for key, value in param_dict.items():
            args.append(value)

        cursor = self.__conn.cursor()
        cursor.execute(stmt, tuple(args))
        self.__conn.commit()

        return cursor.lastrowid

    def update_user(self, user_id, user_name, user_state, message_id=None, post_id=None):
        param_dict = dict({key: value for key, value in locals().items() if key != "self"})

        stmt = "UPDATE user SET " + " = ?, ".join(param_dict.keys()) + " = ? WHERE user_id = ?"
        args = []

        for key, value in param_dict.items():
            args.append(value)
        args.append(user_id)

        cursor = self.__conn.cursor()
        cursor.execute(stmt, tuple(args))
        self.__conn.commit()

        return cursor.rowcount > 0

    def delete_user(self, user_id):
        user = self.get_user(user_id)
        cursor = self.__conn.cursor()

        if user is not None:
            # TODO delete user's posts

            stmt = "DELETE FROM user WHERE user_id = ?"
            args = [user_id]
            cursor.execute(stmt, tuple(args))
            self.__conn.commit()

        return user and cursor.rowcount > 0
