import mysql.connector

class MySQLDatabase:
    def __init__(self):
        self.db = mysql.connector.connect(host="localhost", user="root", passwd="guest", database="photoShare")
        self.cursor = self.db.cursor()


    #insert functions
    def insert_user(self, userID, fname, lname, email, DOB, gender, homeTown, PW):
        query = "INSERT INTO users (userID, fname, lname, email, DOB, gender, homeTown, PW) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (userID, fname, lname, email, DOB, gender, homeTown, PW)
        self.cursor.execute(query, values)
        self.db.commit()

    def insert_friend(self, FriendID, FriendShipDate):
        query = "INSERT INTO friends (FriendID, FriendShipDate) VALUES (%s, %s)"
        values = (FriendID, FriendShipDate)
        self.cursor.execute(query, values)
        self.db.commit()

    def insert_User_Friend(self,  userID, friendID):
        query = "INSERT INTO userfriends (UserID, FriendID ) VALUES( %s, %s)"
        values = (userID, friendID)
        self.cursor.execute(query, values)
        self.db.commit()


    def insert_album(self, albumID, userID, albumName, dateCreated):
        query = "INSERT INTO albums (AlbumID, UserID, AlbumName, DateCreated) VALUES (%s, %s, %s, %s)"
        values = (albumID, userID, albumName, dateCreated)
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


    def insert_photo(self, photoID, albumID, caption, img1):
        query = "INSERT INTO photo (PhotoID, AlbumID, Caption, Caption, img) VALUES (%s, %s, %s, %s)"
        values = (photoID, albumID, caption, img1)
        self.cursor.execute(query, values)
        self.db.commit()



    def insert_tag(self, tagID, tagname):
        query = "INSERT INTO tags (TagID, PhotoID, TagName) VALUES (%s, %s)"
        values = (tagID, tagname)
        self.cursor.execute(query, values)
        self.db.commit()

    def insert_photo_tag(self, photoID, tagID):
        query = "INSERT INTO phototags (photoID, tagID) VALUES (%s, %s)"
        values = (photoID, tagID)
        self.cursor.execute(query, values)
        self.db.commit()

    #end of insert functions


    # selects all of a given users albums
    def select_albums_by_userID(self, userID):
        query = "SELECT Albums.* FROM Albums JOIN Users ON Albums.UserID = Users.UserID WHERE Users.UserID = %s"
        val = (userID, )
        self.cursor.execute(query, val)
        result = self.cursor.fetchall()
        return result

    # selects the number of friends from a given user
    def select_numFriends(self, userID):
        query = "SELECT COUNT(*) FROM userFriends WHERE userID = %s"
        val = (userID, )
        self.cursor.execute(query, val)
        result = self.cursor.fetchone()
        return result

    # searches for other users based on first name or last name
    def select_user_by_name(self, fname, lname):
        query = "SELECT * FROM Users WHERE Fname = %s OR Lname = %s"
        val = (fname, lname)
        self.cursor.execute(query, val)
        resut = self.cursor.fetchall()
        return resut


    # returns the 10 users with the most activity
    def select_most_active_user(self):
        query = """
            SELECT Users.UserID, Users.Fname, Users.Lname, 
                (SELECT COUNT(*) FROM Photo WHERE Photo.AlbumID IN (SELECT AlbumID FROM Albums WHERE Albums.UserID = Users.UserID)) AS NumPhotos,
                (SELECT COUNT(*) FROM Albums WHERE Albums.UserID = Users.UserID) AS NumAlbums,
                (SELECT COUNT(*) FROM Comments WHERE Comments.UserID = Users.UserID) AS NumComments,
                (SELECT COUNT(*) FROM Likes WHERE Likes.UserID = Users.UserID) AS NumLikes,
                (SELECT COUNT(*) FROM UserFriends WHERE UserFriends.UserID = Users.UserID OR UserFriends.FriendID = Users.UserID) AS NumFriends,
                FROM Users,
                ORDER BY (NumPhotos + NumAlbums + NumComments + NumLikes) DESC,
                LIMIT 10;
                """
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    # selects all of a users friends
    def select_users_friends(self, userid):
        query = """
        SELECT u2.Fname, u2.Lname
                FROM Users u1
                JOIN UserFriends uf ON u1.UserID = uf.UserID
                JOIN Users u2 ON uf.FriendID = u2.UserID
                WHERE u1.UserID = %s;
                """
        val = (userid,)
        self.cursor.execute(query, val)
        result = self.cursor.fetchall()
        return result

    # selects user by email
    def select_user_by_email(self, email):
        sql = "SELECT email, PW FROM Users WHERE email = %s"
        val = (email,)
        self.cursor.execute(sql, val)
        result = self.cursor.fetchone()
        return result
    def select_photo_by_id(self):
        query = "SELECT img FROM photo WHERE photoID = %s"
        val = (1, )
        self.cursor.execute(query, val)
        result = self.cursor.fetchone()
        print(result)

    # destructer
    def __del__(self):
        self.cursor.close()
        self.db.close()


