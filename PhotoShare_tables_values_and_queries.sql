
CREATE DATABASE PhotoShare;

CREATE TABLE Users (
UserID INT PRIMARY KEY,
Fname VARCHAR(50),
Lname VARCHAR(50),
email VARCHAR(50),
DOB DATE,
Gender VARCHAR(10),
HomeTown VARCHAR(50),
PW VARCHAR(50),
);

CREATE TABLE ALbums(
AlbumID INT PRIMARY KEY,
UserID INT,
AlbumName VARCHAR(50),
DateCreated DATE,
FOREIGN KEY (UserID) REFERENCES Users(UserID),
);

CREATE TABLE Photo(
PhotoID INT PRIMARY KEY ,
AlbumID INT,
Caption VARCHAR(100),
img BLOB,
FOREIGN KEY (AlbumID) REFERENCES ALbums(AlbumID),
);

CREATE TABLE Friends(
FriendID INT PRIMARY KEY,
FriendShipDate DATE
);


CREATE TABLE Likes (
userID INT,
photoID INT,
PRIMARY KEY (userID, photoID),
FOREIGN KEY (userID) REFERENCES Users(UserID),
FOREIGN KEY (photoID) REFERENCES Photo(PhotoID)
);


CREATE TABLE Comments(
CommentID INT PRIMARY KEY,
PhotoID INT,
UserID INT,
text VARCHAR(80),
date DATE,
FOREIGN KEY (PhotoID) REFERENCES Photo(PhotoID),
FOREIGN KEY (UserID) REFERENCES Users(UserID)
);

CREATE TABLE Tags(
TagID INT PRIMARY KEY,
TagName VARCHAR(50),
);


CREATE TABLE UserFriends (
UserID INT,
FriendID INT,
PRIMARY KEY (UserID, FriendID),
FOREIGN KEY (UserID) REFERENCES Users(UserID),
FOREIGN KEY (FriendID) REFERENCES Friends(FriendID)
);

CREATE TABLE photoTags (
  photoID INT,
  tagID INT,
  PRIMARY KEY (photoID, tagID),
  FOREIGN KEY (photoID) REFERENCES Photo(photoid),
  FOREIGN KEY (tagID) REFERENCES tags(tagID)
);
--inserting values


INSERT INTO Users (UserID, Fname, Lname, email, DOB, Gender,
HomeTown, PW)
VALUES
(1, 'John', 'Doe', 'johndoe@example.com', '1990-01-01', 'Male', 'New
York', 'password123'),
(2, 'Jane', 'Doe', 'janedoe@example.com', '1992-02-02', 'Female', 'Los
Angeles', 'secret321'),
(3, 'Bob', 'Smith', 'bobsmith@example.com', '1985-03-03', 'Male',
'Chicago', 'qwerty'),
(4,  'Sarah', 'Johnson', 'sarahjohnson@example.com', '1995-04-04',
'Female', 'Houston', 'letmein'),
(5, 'Mike', 'Brown', 'mikebrown@example.com', '1998-05-05', 'Male', 'San
Francisco', 'password'),
(6, 'Emily', 'Taylor', 'emilytaylor@example.com', '1989-06-06', 'Female',
'Boston', '123456'),
(7, 'David', 'Lee', 'davidlee@example.com', '1993-07-07', 'Male',
'Seattle', 'pass123'),
(8, 'Jessica', 'Garcia', 'jessicagarcia@example.com', '1987-08-08',
'Female', 'Miami', 'password321'),
(9, 'Chris', 'Nguyen', 'chrisnguyen@example.com', '1996-09-09', 'Male',
'Dallas', 'abc123'),
(10, 'Stephanie', 'Chen', 'stephaniechen@example.com', '1991-10-10',
'Female', 'Phoenix', 'mypassword');


INSERT INTO Friends (FriendID, FriendShipDate)
VALUES
(1, '2022-01-01'),
(2, '2022-01-02'),
(3, '2022-01-03'),
(4, '2022-01-04'),
(5, '2022-01-05'),
(6, '2022-01-06'),
(7, '2022-01-07'),
(8, '2022-01-08'),
(9, '2022-01-09'),
(10, '2022-01-10');


INSERT INTO UserFriends (UserID, FriendID)
VALUES
(1, 2),
(2, 1),
(3, 4),
(4, 3),
(5, 6),
(6, 5),
(7, 8),
(8, 7),
(9, 10),
(10, 9);


INSERT INTO Albums (AlbumID, UserID, AlbumName, DateCreated)
VALUES
(1, 1, 'Vacation Photos', '2022-01-01'),
(2, 3, 'Family Photos', '2022-01-02'),
(3, 5,'Wedding Photos', '2022-01-03'),
(4, 7,'Graduation Photos', '2022-01-04'),
(5, 9,'Pet Photos', '2022-01-05'),
(6, 2, 'Travel Photos', '2022-01-06'),
(7, 4, 'Baby Photos', '2022-01-07'),
(8, 6, 'Nature Photos', '2022-01-08'),
(9, 8, 'Sports Photos', '2022-01-09'),
(10, 10, 'Food Photos', '2022-01-10');


INSERT INTO Photo (PhotoID, AlbumID, Caption, img)
VALUES
(1, 1, 'I am at the beach, its hotter then my nutsack', load_file('C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\photoSharePhotos\\beach.jpg'))
(2, 6, 'In front of the Eiffel Tower', load_file('C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\photoSharePhotos\\eiffle_tower.jpg')),
(3, 2,  'Family reunion', load_file('C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\photoSharePhotos\\family.jpg')),
(4, 7,  'Newborn baby', load_file('C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\photoSharePhotos\\baby.jpg')),
(5, 3,  'Bride and groom', load_file('C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\photoSharePhotos\\wedding.jpg')),
(6, 8,  'Beautiful sunset', load_file('C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\photoSharePhotos\\sunset.jpg')),
(7, 4,  'College graduation', load_file('C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\photoSharePhotos\\grad.jpg')),
(8, 9,  'Soccer game', load_file('C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\photoSharePhotos\\soccer.jpg')),
(9, 5,  'First dog', load_file('C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\photoSharePhotos\\puppy.jpg')),
(10, 10, 'Gourmet meal', load_file('C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\photoSharePhotos\\food.jpg'));


INSERT INTO Comments (CommentID, PhotoID, UserID, text, date)
VALUES
(1, 1, 2, 'Looks like a great day!', '2022-01-01'),
(2, 6, 5, 'Wow, what a view!', '2022-01-02'),
(3, 2, 1, 'Missing Paris!', '2022-01-03'),
(4, 7, 4, 'Congratulations!', '2022-01-04'),
(5, 3, 3, 'So happy to see everyone!', '2022-01-05'),
(6, 8, 8, 'Great shot!', '2022-01-06'),
(7, 4, 6, 'Adorable baby!', '2022-01-07'),
(8, 9, 9, 'Go team!', '2022-01-08'),
(9, 5, 10, 'Beautiful couple!', '2022-01-09'),
(10, 10, 7, 'Looks delicious!', '2022-01-10');


INSERT INTO Tags(TagID, TagName)
VALUES
(1, 'beach'),
(2, 'mountain'),
(3, 'hiking'),
(4, 'cityscape'),
(5, 'food'),
(6, 'restaurant'),
(7, 'sunset'),
(8, 'skyline'),
(9, 'landscape'),
(10, 'ocean');


INSERT INTO Likes (userID, photoID)
VALUES
(1, 2),
(2, 1),
(3, 4),
(4, 3),
(5, 6),
(6, 5),
(7, 8),
(8, 7),
(9, 10),
(10, 9);

INSERT INTO photoTags(photoID, tagID)
    values
        (1, 10),
        (2, 9),
        (3, 8),
        (4, 7),
        (5, 6),
        (6, 5),
        (7, 4),
        (8, 3),
        (9, 2),
        (10, 1);
