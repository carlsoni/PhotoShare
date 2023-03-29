import mysql.connector

class User:
    def __init__(self, userID ,albumID, fname , lname, email, DOB, gender, homeTown,PW ):
        self.userID = userID
        self.albumID = albumID
        self.fname = fname
        self.lname = lname
        self.email = email
        self.DOB = DOB
        self.gender = gender
        self.homeTown = homeTown
        self.PW = PW
        db = mysql.connector.connect(host="localhost", user="root", passwd="guest", database="photoShare")

        self.mycursor = db.cursor()

    def insert(self):
        sql = 'INSERT INTO users (userID, albumID, fname, lname, email, DOB, gender, homeTown, PW) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
        values = (self.userID, self.albumID, self.fname, self.lname, self.email, self.DOB, self.gender, self.homeTown, self.PW)
        self.cursor.execute(sql, values)
        self.conn.commit()

    @staticmethod
    def get_name_pw_and_email_by_email(email):
        conn = mysql.connector.connect(db=mysql.connector.connect(host="localhost", user="root", passwd="guest", database="photoShare"))
        cursor = conn.cursor()
        sql = 'SELECT fname, lname, email, PW FROM users WHERE email=%s'
        values = (email,)
        cursor.execute(sql, values)
        row = cursor.fetchone()
        if row:
            return User(*row)
        else:
            return None





class Friend:
    def __int__(self, friendID, friendshipDate):
        self.friendID = friendID
        self.friendshipDate = friendshipDate


class UserFriend:
    def __int__(self, userID, friendID):
        self.userID = userID
        self.friendID = friendID


class ALbum:
    def __int__(self, albumID, userID, photoID, albumName, dateCreated):
        self.albumID = albumID
        self.userID = userID
        self.photoID = photoID
        self.albuName = albumName
        self.dateCreated = dateCreated


class Like:
    def __int__(self, userID, photoID):
        self.userID = userID
        self.photoID = photoID


class Photo:
    def __int__(self, photoID, albumID, commentID, tagID, caption, DATA):
        self.photoID = photoID
        self.albumID = albumID
        self.commentID = commentID
        self.tagID = tagID
        self.caption = caption
        self.DATA = DATA


class Comment:
    def __int__(self, commentID, photoID, userID, text, date):
        self.commentID = commentID
        self.photoID = photoID
        self.userID = userID
        self.text = text
        self.date = date


class Tag:
    def __int__(self, tagID, photoID, tagName):
        self.tagID = tagID
        self.tagName = tagName
        self.photoID = photoID
