import tkinter as tk

def sign_up():
    name = name_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    print("Name:", name)
    print("Email:", email)
    print("Password:", password)

root = tk.Tk()
root.title("Sign Up Page")

name_label = tk.Label(root, text="Name:")
email_label = tk.Label(root, text="Email:")
password_label = tk.Label(root, text="Password:")

name_entry = tk.Entry(root)
email_entry = tk.Entry(root)
password_entry = tk.Entry(root, show="*")

sign_up_button = tk.Button(root, text="Sign Up Now", command=sign_up)

name_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
name_entry.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)
email_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
email_entry.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)
password_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)
password_entry.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)
sign_up_button.grid(row=3, columnspan=2, padx=10, pady=10)

root.mainloop()
