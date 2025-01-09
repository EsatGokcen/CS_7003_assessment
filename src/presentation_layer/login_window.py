import tkinter


class LoginWindow:

    def __init__(self, master, controller):
        self.master = master
        self.controller = controller
        self.master.title("Login")
        self.master.geometry("600x400")