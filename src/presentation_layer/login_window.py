import tkinter as tk


class LoginWindow:

    def __init__(self, master, controller):
        self.master = master
        self.controller = controller
        self.master.title("Login")
        self.master.geometry("600x400")

        # Username Label and Entry
        tk.Label(master, text="Username:").pack(pady=5)
        self.username_entry = tk.Entry(master)
        self.username_entry.pack(pady=5)

        # Password Label and Entry
        tk.Label(master, text="Password:").pack(pady=5)
        self.password_entry = tk.Entry(master, show="*")
        self.password_entry.pack(pady=5)

        # Login Button
        tk.Button(master, text="Login", command=self.login).pack(pady=10)

    def login(self):
        pass