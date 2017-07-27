import sqlite3


__author__ = 'anaeanet'


class DBHelper:

    def __init__(self, db_name):
        self.__conn = sqlite3.connect(db_name, check_same_thread=False)
        self.setup()

    def setup(self):

        # create required tables
        tbl_statements = [
            "CREATE TABLE IF NOT EXISTS user (user_id INTEGER NOT NULL PRIMARY KEY"
            + ", user_name TEXT NOT NULL"
            + ", user_state INTEGER"
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
        column_names = [x[1] for x in self.__conn.execute("PRAGMA table_info(user)")]

        stmt = "SELECT * FROM user"
        args = []

        if filters:
            stmt += " WHERE " + " = ? AND ".join(filters.keys()) + " = ?"
            for key, value in filters.items():
                args.append(value)

        user_data_list = []
        for record in [x for x in self.__conn.execute(stmt, tuple(args))]:
            user_data = dict()
            for column_index in range(len(column_names)):
                user_data[column_names[column_index]] = record[column_index]
            user_data_list.append(user_data)

        return user_data_list

    def get_user(self, user_id):
        user = {}

        users = self.get_users(user_id=user_id)
        if len(users) == 1:
            user = users[0]

        return user

    def add_user(self, user_id, user_name, **optional_params):
        column_names = [x[1] for x in self.__conn.execute("PRAGMA table_info(user)")
                        if x[1] not in ["user_id", "user_name"]]
        param_dict = dict({key: value for key, value in optional_params.items() if key in column_names})
        param_dict["user_id"] = user_id
        param_dict["user_name"] = user_name

        stmt = "INSERT INTO user (" + ",".join(param_dict.keys()) + ") " \
               + "VALUES (" + ",".join(["?" for x in param_dict.keys()]) + ")"
        args = []

        for key, value in param_dict.items():
            args.append(value)

        cursor = self.__conn.cursor()
        cursor.execute(stmt, tuple(args))
        self.__conn.commit()

        return cursor.lastrowid

    def update_user(self, user_id, **kwargs):
        column_names = [x[1] for x in self.__conn.execute("PRAGMA table_info(user)") if x[1] != "user_id"]
        param_dict = dict({key: value for key, value in kwargs.items() if key in column_names})
        param_dict["user_id"] = user_id

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
            stmt = "DELETE FROM user WHERE user_id = ?"
            args = [user_id]
            cursor.execute(stmt, tuple(args))
            self.__conn.commit()

        return user and cursor.rowcount > 0
