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
    def recommend_friends(self, user_id):
        query = """
        SELECT
            PotentialFriends.UserID,
            PotentialFriends.Fname,
            PotentialFriends.Lname,
            COUNT(*) AS CommonFriendsCount
        FROM
            UserFriends AS User_Friends
        JOIN
            UserFriends AS Friends_Friends ON User_Friends.FriendID = Friends_Friends.UserID
        JOIN
            Users AS PotentialFriends ON Friends_Friends.FriendID = PotentialFriends.UserID
        WHERE
            User_Friends.UserID = %s
            AND PotentialFriends.UserID != %s
            AND PotentialFriends.UserID NOT IN (
                SELECT FriendID
                FROM UserFriends
                WHERE UserID = %s
            )
        GROUP BY
            PotentialFriends.UserID, PotentialFriends.Fname, PotentialFriends.Lname
        ORDER BY
            CommonFriendsCount DESC;
        """
        # Pass the user_id variable as a tuple to the execute() method
        self.cursor.execute(query, (user_id, user_id, user_id))
        result = self.cursor.fetchall()
        return result

    def select_user_by_ID(self, userID):
        query = "select * from users where userID = %s"
        val = (userID, )
        self.cursor.execute(query, val)
        result = self.cursor.fetchone()
        return result

    def select_photo_by_tagName(self, tagName):
        query = """
            SELECT Photo.PhotoID, Photo.Caption, Photo.img
            FROM Photo
            JOIN PhotoTags ON Photo.PhotoID = PhotoTags.PhotoID
            JOIN Tags ON PhotoTags.TagID = Tags.TagID
            WHERE Tags.TagName = %s;
        """
        val = (tagName, )
        self.cursor.execute(query, val)
        result = self.cursor.fetchall()
        return result

    def select_photo_by_tag_and_userId(self, tagName, userID):
        query = """
                SELECT Photo.PhotoID, Photo.Caption, Photo.img
                FROM Photo
                JOIN PhotoTags ON Photo.PhotoID = PhotoTags.PhotoID
                JOIN Tags ON PhotoTags.TagID = Tags.TagID
                JOIN Albums ON Photo.AlbumID = Albums.AlbumID
                JOIN Users ON Albums.UserID = Users.UserID
                WHERE Tags.TagName = %s
                AND Users.UserID = %s;
                """
        vals = (tagName, userID)
        self.cursor.execute(query, vals)
        result = self.cursor.fetchall()
        return result

    def find_most_popular_tags(self):
        query = """
                SELECT Tags.TagName, COUNT(PhotoTags.PhotoID) AS TagCount
                FROM Tags
                JOIN PhotoTags ON Tags.TagID = PhotoTags.TagID
                GROUP BY Tags.TagID, Tags.TagName
                ORDER BY TagCount DESC
                LIMIT 10;
        """
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    # returns false if email is not in use
    def check_if_email_in_users(self, email):
        emails = self.select_user_by_email(email)
        return not(emails is None)


    def search_by_comment(self, com):
        query = """
        SELECT Users.UserID, Users.Fname, Users.Lname, COUNT(Comments.CommentID) AS MatchingCommentCount
        FROM Users
        JOIN Comments ON Users.UserID = Comments.UserID
        WHERE Comments.text LIKE %s
        GROUP BY Users.UserID, Users.Fname, Users.Lname
        HAVING COUNT(Comments.CommentID) > 0
        ORDER BY MatchingCommentCount DESC;
        """
        search_term = f"%{com}%"
        val = (search_term, )
        self.cursor.execute(query, val)
        result = self.cursor.fetchall()
        return result

    def get_top_five_tags(self, user_id):
        query = """
        SELECT Tags.TagID, Tags.TagName, COUNT(*) AS TagCount
        FROM PhotoTags
        JOIN Tags ON PhotoTags.tagID = Tags.TagID
        JOIN Photo ON PhotoTags.photoID = Photo.PhotoID
        JOIN Albums ON Photo.AlbumID = Albums.AlbumID
        WHERE Albums.UserID = %s
        GROUP BY Tags.TagID, Tags.TagName
        ORDER BY TagCount DESC
        LIMIT 5;
        """
        self.cursor.execute(query, (user_id,))
        result = self.cursor.fetchall()
        return result

    def recommend_photos(self, user_id):
        top_five_tags = self.get_top_five_tags(self, user_id)
        tag_ids = [tag[0] for tag in top_five_tags]

        query = """
        SELECT Photo.PhotoID, COUNT(PhotoTags.tagID) AS MatchedTags, COUNT(DISTINCT pt_all.tagID) AS TotalTags
        FROM Photo
        LEFT JOIN PhotoTags ON Photo.PhotoID = PhotoTags.photoID
        LEFT JOIN PhotoTags AS pt_all ON Photo.PhotoID = pt_all.photoID
        WHERE PhotoTags.tagID IN (%s, %s, %s, %s, %s)
        GROUP BY Photo.PhotoID
        ORDER BY MatchedTags DESC, TotalTags ASC;
        """
        self.cursor.execute(query, tuple(tag_ids))
        result = self.cursor.fetchall()
        return result
        
   
    def select_max_userID(self):
        query = "SELECT MAX(UserID) FROM Users"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        largest_user_id = result[0]
        return largest_user_id

    def select_max_albumID(self):
        query = "SELECT MAX(albumID) FROM Albums"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        largest = result[0]
        return largest

    def select_max_photoID(self):
        query = "SELECT MAX(photoID) FROM photo"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        largest = result[0]
        return largest

    def select_max_commentID(self):
        query = "SELECT MAX(commentID) FROM comments"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        largest = result[0]
        return largest

    def select_max_tagID(self):
        query = "SELECT MAX(tagID) FROM tags"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        largest = result[0]
        return largest
        
        
    # destructer
    def __del__(self):
        self.cursor.close()
        self.db.close()




