import mysql.connector
import Table_Classes

class MySQLDatabase:
    def __init__(self):
        self.db = mysql.connector.connect(host="localhost", user="root", passwd="guest", database="photoShare")
        self.cursor = self.db.cursor()

    def insert_user(self, userID, albumID, fname, lname, email, DOB, gender, homeTown, PW):
        query = "INSERT INTO users (userID, albumID, fname, lname, email, DOB, gender, homeTown, PW) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (userID, albumID, fname, lname, email, DOB, gender, homeTown, PW)
        self.cursor.execute(query, values)

    def select_user_by_email(self, email):
        sql = "SELECT email, PW FROM Users WHERE email = %s"
        val = (email,)
        self.cursor.execute(sql, val)
        result = self.cursor.fetchone()
        return result

    def __del__(self):
        self.cursor.close()
        self.db.close()
