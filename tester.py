from dataGetter import MySQLDatabase
import Table_Classes


db = MySQLDatabase()
                    #userID ,albumID,  fname , lname, email,                        DOB,        gender, homeTown, PW
#new_user = Table_Classes.User(2, 3 ,1, "Ian" , "Carlson", "iancarlson0599@gmail.com", "2000-05-03", "M", "Parker","password" )

#db.insert_user(new_user.userID, new_user.albumID, new_user.fname, new_user.lname, new_user.email, new_user.DOB, new_user.gender, new_user.homeTown, new_user.PW)
result = db.select_user_by_email("johndoe@example.com")
print(result)

del db
