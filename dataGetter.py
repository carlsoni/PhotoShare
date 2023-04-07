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

    # selects users email and password by email
    def select_user_by_email(self, email):
        sql = "SELECT email, PW FROM Users WHERE email = %s"
        val = (email,)
        self.cursor.execute(sql, val)
        result = self.cursor.fetchone()
        return result

    def select_photo_by_id(self, photoID):
        query = "SELECT img FROM photo WHERE photoID = %s"
        val = (photoID, )
        self.cursor.execute(query, val)
        result = self.cursor.fetchall()
        return result

    def select_album_by_userID(self, userID):
        query = "select * from albums WHERE userID = %s"
        val = (userID, )
        self.cursor.execute(query, val)
        result = self.cursor.fetchall()
        return result

    def delete_photo(self, photoID):
        val = (photoID,)

        query1 = "delete from phototags where photoID = %s"
        self.cursor.execute(query1, val)
        self.db.commit()

        query2 = "delete from likes where photoID = %s"
        self.cursor.execute(query2, val)
        self.db.commit()

        query3 = "delete from comments where photoID = %s"
        self.cursor.execute(query3, val)
        self.db.commit()

        query = "delete from photo where PhotoID = %s"
        self.cursor.execute(query, val)
        self.db.commit()

    def delete_album(self, albumID):
        photos = self.selct_photos_by_albumID(albumID)
        for row in photos:
            self.delete_photo(row[0])
        query = "delete from albums where albumID = %s"
        val = (albumID,)
        self.cursor.execute(query, val)
        self.db.commit()

    def selct_photos_by_albumID(self, albumID):
        query = "select * from photo WHERE AlbumID = %s"
        val = (albumID, )
        self.cursor.execute(query, val)
        result = self.cursor.fetchall()
        return result


    #friends of friends
    def select_friends_of_friends(self, userId):
        query = """
            SELECT f2.FriendID, COUNT(*) AS MutualFriends
            FROM Friends f1
            JOIN UserFriends uf1 ON f1.FriendID = uf1.FriendID
            JOIN UserFriends uf2 ON uf1.UserID = uf2.FriendID
            JOIN Friends f2 ON uf2.FriendID = f2.FriendID
            WHERE uf1.UserID = %s AND f2.FriendID <> uf1.UserID
            GROUP BY f2.FriendID
            ORDER BY MutualFriends DESC;
        """
        val = (userId, )
        self.cursor.execute(query, val)
        result = self.cursor.fetchall()
        for row in result:
            result1 = result1 + (self.select_user_by_ID(row[0]), )
        return result1

    def select_user_by_ID(self, userID):
        query = "select * from users where userID = %s"
        val = (userID, )
        self.cursor.execute(query, val)
        result = self.cursor.fetchone()
        return result

    # returns false if email is not in use
    def check_if_email_in_users(self, email):
        emails = self.select_user_by_email(email)
        return not(emails is None)





    # destructer
    def __del__(self):
        self.cursor.close()
        self.db.close()



