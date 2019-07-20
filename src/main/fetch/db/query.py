from .connect import Connect


class Query:

    def __init__(self):
        self.myConnect = Connect()
        self.myDb = self.myConnect.connect_to_db()
        self.myCursor = self.myDb.cursor()


    def addOne(self, title, newsLink, imageLink, postDateTime, catalogue, organization):
        sql = "INSERT INTO news (title, newsLink, imageLink, postDateTime, catalogue, organization) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (title, newsLink, imageLink, postDateTime, catalogue, organization)
        
        self.myCursor.execute(sql, val)
        self.myDb.commit()
        return self.myCursor.lastrowid

    def addAll(self, valList):
        sql = "INSERT INTO news (title, newsLink, imageLink, postDateTime, catalogue, organization) VALUES (%s, %s, %s, %s, %s, %s)"
        self.myCursor.executemany(sql, valList)
        self.myDb.commit()
        return True
        
    
    def findByTitle(self, title):
        sql = "SELECT * FROM news WHERE title = %s"
        title = (title, )
        self.myCursor.execute(sql, title)
        return self.myCursor.fetchall()


    def close(self):
        self.myDb.close()