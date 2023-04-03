import mysql.connector
import Table_Classes

class MySQLDatabase:
    def __init__(self):
        self.db = mysql.connector.connect(host="localhost", user="root", passwd="guest", database="photoShare")
        self.cursor = self.db.cursor()


    #insert functions
    def insert_user(self, userID, albumID, fname, lname, email, DOB, gender, homeTown, PW):
        query = "INSERT INTO users (userID, albumID, fname, lname, email, DOB, gender, homeTown, PW) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (userID, albumID, fname, lname, email, DOB, gender, homeTown, PW)
        self.cursor.execute(query, values)
        self.db.commit()

    def insert_friend(self, FriendID, FriendShipDate):
        query = "INSERT INTO friends (FriendID, FriendShipDate) VALUES (%s, %s)"
        values = (FriendID, FriendShipDate)
        self.cursor.execute(query, values)
        self.db.commit()

    def insert_Uer_Friend(self,  userID, friendID):
        query = "INSERT INTO userfriends (UserID, FriendID ) VALUES( %s, %s)"
        values = (userID, friendID)
        self.cursor.execute(query, values)
        self.db.commit()

    def insert_album(self, albumID, userID, photoID, albumName, dateCreated):
        query = "INSERT INTO albums (AlbumID, UserID, PhotoID, AlbumName, DateCreated) VALUES (%s, %s, %s, %s, %s)"
        values = (albumID, userID, photoID, albumName, dateCreated)
        self.cursor.execute(query, values)
        self.db.commit()

    def insert_comment(self, commentID, photoID, userID, text, date):
        query = "INSERT INTO comments (CommentID, PhotoID, UserID, text, date) VALUES (%s, %s, %s, %s, %s)"
        values =(commentID, photoID, userID, text, date)
        self.cursor.execute(query, values)
        self.db.commit()

    def insert_like(self, userID, photoID):
        query = "INSERT INTO likes (userID, photoID) VALUES (%s, %s)"
        values = (userID, photoID)
        self.cursor.execute(query, values)
        self.db.commit()

    def insert_photo(self, photoID, albumID, commentID, tagID, caption, DATa):
        query = "INSERT INTO photo (PhotoID, AlbumID, CommentID, TagID, Caption, Caption, data) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (photoID, albumID, commentID, tagID, caption, DATa)
        self.cursor.execute(query, values)
        self.db.commit()


    def insert_tag(self, tagID, photoID, tagname):
        query = "INSERT INTO tags (TagID, PhotoID, TagName) VALUES (%s, %s, %s)"
        values = (tagID, photoID, tagname)
        self.cursor.execute(query, values)
        self.db.commit()




    def select_user_by_email(self, email):
        sql = "SELECT email, PW FROM Users WHERE email = %s"
        val = (email,)
        self.cursor.execute(sql, val)
        result = self.cursor.fetchone()
        return result

    def __del__(self):
        self.cursor.close()
        self.db.close()

