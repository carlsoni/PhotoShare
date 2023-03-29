from tkinter import *

def login():
    # Check if the username and password are correct
    if username_entry.get() == "admin" and password_entry.get() == "password":
        # Destroy the login window and create the main application window
        login_window.destroy()
        app_window = Tk()
        app_window.title("My Application")
        # Add widgets to the main window
        Label(app_window, text="Welcome, admin!").pack()
        app_window.mainloop()
    else:
        # Display an error message if the username or password is incorrect
        error_label.config(text="Incorrect username or password")

# Create the login window
login_window = Tk()
login_window.title("PhotoShare Login")
login_window.geometry("2000x1000")

# Center the window on the screen
login_window.eval('tk::PlaceWindow %s center' % login_window.winfo_toplevel())

# Add widgets to the login window
Label(login_window, text="Username").pack(pady=10)
username_entry = Entry(login_window)
username_entry.pack(pady=10)

Label(login_window, text="Password").pack(pady=10)
password_entry = Entry(login_window, show="*")
password_entry.pack(pady=10)

login_button = Button(login_window, text="Login", command=login)
login_button.pack(pady=10)

error_label = Label(login_window, fg="red")
error_label.pack(pady=10)

login_window.mainloop()


