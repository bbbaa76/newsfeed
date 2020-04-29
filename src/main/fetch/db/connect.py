import mysql.connector


class Connect:

    def __init__(self):
        self.host = "localhost"
        self.user = "anthony"
        self.password = "lglin"
        self.database = "newsfeed"

    def connect_to_db(self):
        mydb = mysql.connector.connect(
            host=self.host,
            user=self.user,
            passwd=self.password,
            database=self.database
        )
        return mydb
