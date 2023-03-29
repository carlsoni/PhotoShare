import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", passwd="guest", database="photoShare")

mycursor = db.cursor()

# SQL query to insert a new record into the Users table
#sql = "INSERT INTO Users (UserID, FriendID, AlbumID, Fname, Lname, email, DOB, Gender, HomeTown, PW) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
#val = (1, 2, 3, "John", "Doe", "johndoe@example.com", "1990-01-01", "Male", "New York", "password123")

# Execute the query with values
#mycursor.execute(sql, val)

# Commit the changes to the database
#db.commit()

# Print the number of rows that were inserted
#print(mycursor.rowcount, "record inserted.")

sql = "SELECT Fname FROM Users WHERE UserID = %s"
val = (1,)

# Execute the query with values
mycursor.execute(sql, val)

# Fetch the result
result = mycursor.fetchone()

print(result[0])


