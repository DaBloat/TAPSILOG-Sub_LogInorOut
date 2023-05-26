# CODE AUTHOR: KYNA

import _tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from databases import admin_database as admin
import support_admin as ad
import register_admin as adreg
import home_window as main

global cnt, cnt2
cnt = 1
cnt2 = 1


class LogInWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        # Main GUI
        self.title('T.A.P.S.I.Log')
        self.cx = (int(self.winfo_screenwidth() / 2)) - int(600 / 2)
        self.cy = (int(self.winfo_screenheight() / 2)) - int(600 / 2)
        self.geometry("{}x{}+{}+{}".format(600, 600, self.cx, self.cy))
        self.resizable(False, False)
        self.cant_sign_run = False
        self.reg_run = False
        self.protocol("WM_DELETE_WINDOW", self.close_all)
        self.from_db = admin.AdminDatabase()

        # Background setting
        self.bg_model = tk.Label(self, bg='#EAC4A3')
        self.bg_model.place(x=0, y=0, relwidth=1, relheight=1)

        # Entry Photo
        self.entry = tk.PhotoImage(file='graphics/entry.png')

        # Picture-In-Windows
        self.photo = tk.PhotoImage(file='graphics/Logo.png')
        self.photo2 = self.photo.subsample(2, 2)
        self.photo_image = tk.Label(self, image=self.photo2, text='Welcome to T.A.P.S.I.Log', font=("Pricedown", 42),
                                    compound='top', bg='#EAC4A3')
        self.photo_image.pack()

        # Setting Frame
        self.sign = tk.Frame(self, bg='#EAC4A3')
        self.sign.pack(padx=50, pady=50, fill='x', expand=True)

        # Setting Variables
        self.username = tk.StringVar()
        self.password = tk.StringVar()

        # Label for Username
        self.username_label = tk.Label(self.sign, text="Username:", font=('Comic Sans', 12, 'bold'), bg='#EAC4A3')
        self.username_label.pack(fill='x')

        # Enter for Username
        self.username_entry = ttk.Entry(self.sign, textvariable=self.username, width=50)
        self.username_entry.pack(expand=True)
        self.username_entry.focus()

        # Label For password
        self.password_label = tk.Label(self.sign, text="Password:", font=('Comic Sans', 12, 'bold'), bg='#EAC4A3')
        self.password_label.pack(fill='x', expand=True)

        # Enter for Password
        self.password_entry = ttk.Entry(self.sign, textvariable=self.password, show="*", width=50)
        self.password_entry.pack(expand=True)

        self.login_pic = tk.PhotoImage(file='graphics/login_button.png')
        self.login_pic2 = self.login_pic.subsample(2, 2)

        # Button
        self.login_button = tk.Button(self.sign, image=self.login_pic2, command=self.login_clicked, bd=0, activebackground='#EAC4A3', bg='#EAC4A3')
        self.login_button.pack()

        # Frame 2
        self.frameTwo = tk.Frame(self, bg='#EAC4A3')
        self.frameTwo.pack(fill='x', expand=True)

        # Why can't sign in
        self.cant_sign_button = tk.Button(self.frameTwo, text="Can't Sign In?", font=("Comic Sans", 8, 'underline'),
                                          bg='#EAC4A3', bd=0, command=self.cant_clicked)
        self.cant_sign_button.pack(anchor='center')


        #  Register an admin Button
        self.register_add_button = tk.Button(self.frameTwo, text="Register a new Admin",
                                             font=("Comic Sans", 8, 'underline'), bg='#EAC4A3', bd=0,
                                             command=self.register_clicked)
        self.register_add_button.pack(anchor='center')

    def login_clicked(self):
        try:
            # Open the Main Window if correct
            if self.username.get() == ((self.from_db.search_admin(self.username.get()))[0]) and self.password.get() == (
            (self.from_db.search_admin(self.username.get()))[1]):
                self.close_all()
                self.run_main = main.HomeWindow(((self.from_db.search_admin(self.username.get()))[2]))
            else:
                messagebox.showerror(title="Incorrect Input", message="Incorrect Username or Password")
        except TypeError:
            if self.username.get() == '' or self.password.get() == '':
                messagebox.showinfo(title='Not all have input', message="All entries requires input")
            else:
                messagebox.showerror(title="Incorrect Input", message="Incorrect Username or Password")

    def cant_clicked(self):
        self.cant_sign_run = True
        global cnt

        if cnt < 2:
            self.can_sign = ad.AdminSupp()
            cnt += 1
            self.can_sign.protocol("WM_DELETE_WINDOW", self.refresh)
        else:
            messagebox.showerror(title='Limited Number of Tabs', message='The Windows is already opened')

    def register_clicked(self):
        self.reg_run = True
        global cnt2

        if cnt2 < 2:
            self.reg = adreg.AdminReg()
            cnt2 += 1
            self.reg.protocol("WM_DELETE_WINDOW", self.refresh2)
        else:
            messagebox.showerror(title='Limited Number of Tabs', message='The Windows is already opened')

    def refresh(self):
        global cnt
        self.can_sign.destroy()
        cnt -= 1

    def refresh2(self):
        global cnt2
        self.reg.destroy()
        cnt2 -= 1

    def close_all(self):
        try:
            self.destroy()
            if self.cant_sign_run:
                self.can_sign.destroy()
            if self.reg_run:
                self.reg.destroy()
        except _tkinter.TclError:
            pass



