import tkinter as tk

def login():
    username = username_entry.get()
    password = password_entry.get()
    print("Username:", username)
    print("Password:", password)

root = tk.Tk()
root.title("Login Page")

username_label = tk.Label(root, text="Username:")
password_label = tk.Label(root, text="Password:")

username_entry = tk.Entry(root)
password_entry = tk.Entry(root, show="*")

login_button = tk.Button(root, text="Login", command=login)

username_label.place(x=30, y=50)
password_label.place(x=30, y=80)

username_entry.place(x=120, y=50)
password_entry.place(x=120, y=80)

login_button.place(x=80, y=120)

root.mainloop()
