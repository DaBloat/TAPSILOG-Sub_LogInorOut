import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time
from email_senders import admicode_email as send
import os, sys
from databases import admin_database as admin


class AdminReg(tk.Toplevel):
    def __init__(self):
        super().__init__()
        # Main GUI
        self.geometry('750x700+10+10')
        self.title('Admin Registration')
        self.bg = tk.Label(self, bg='#EAC4A3')
        self.bg.place(x=0, y=0, relwidth=1, relheight=1)
        self.run = FrameOne(self)


class FrameOne(tk.Frame):
    def __init__(self, container):
        super().__init__(container, bg='#EAC4A3')
        self.container = container
        self.pack()

        self.title = tk.Label(self, text="""NOTE: Register with the right and correct Information only! 
        Double check before pressing continue
        -love, Kyna""", bg='#EAC4A3', font=('Arial Black', 10))
        self.title.grid(row=2, column=0, padx=20, pady=20)

        self.frame_name = tk.LabelFrame(self, text="Admin Info", bg='#EAC4A3', font=('Arial Black', 10))
        self.frame_name.grid(row=1, column=0, padx=20, pady=20)

        # Name
        self.name_label = tk.Label(self.frame_name, text="Name:", bg='#EAC4A3', font=('Arial Black', 10))
        self.name_label.grid(row=0, column=0)

        # Name Entry
        self.name_entry = tk.Entry(self.frame_name)
        self.name_entry.grid(row=0, column=1)

        # Email
        self.email_label = tk.Label(self.frame_name, text='Email:', bg='#EAC4A3', font=('Arial Black', 10))
        self.email_label.grid(row=1, column=0)

        # Email Entry
        self.email_entry = tk.Entry(self.frame_name)
        self.email_entry.grid(row=1, column=1)

        # Username
        self.username_label = tk.Label(self.frame_name, text="Username:", bg='#EAC4A3', font=('Arial Black', 10))
        self.username_label.grid(row=2, column=0)

        # Username Entry
        self.username_entry = tk.Entry(self.frame_name)
        self.username_entry.grid(row=2, column=1)

        # Password
        self.password_label = tk.Label(self.frame_name, text="Password:", bg='#EAC4A3', font=('Arial Black', 10))
        self.password_label.grid(row=3, column=0)

        # Password Entry
        self.password_entry = tk.Entry(self.frame_name, show='*')
        self.password_entry.grid(row=3, column=1)

        # Reenter-Password
        self.password_relabel = tk.Label(self.frame_name, text="Reenter Password:", bg='#EAC4A3',
                                         font=('Arial Black', 10))
        self.password_relabel.grid(row=4, column=0)

        # Reenter-Password Entry
        self.password_reentry = tk.Entry(self.frame_name, show='*')
        self.password_reentry.grid(row=4, column=1)

        # Formatting all the widgets
        for widgets in self.frame_name.winfo_children():
            widgets.grid_configure(padx=10, pady=10)

        self.btn = tk.PhotoImage(file='graphics/visitor_but.png')
        self.btn2 = self.btn.subsample(2, 2)

        # Register
        self.check_button = tk.Button(self, image=self.btn2, bg='#EAC4A3', bd=0, activebackground='#EAC4A3',
                                      command=self.register_clicked)
        self.check_button.grid(row=3, column=0)

        self.logo = tk.PhotoImage(file='graphics/Logo-cut.png')
        self.logo2 = self.logo.subsample(2, 2)

        self.logo = tk.Button(self, image=self.logo2, bg='#EAC4A3', bd=0, activebackground='#EAC4A3')
        self.logo.grid(row=0, column=0)

    def register_clicked(self):
        self.get_name = self.name_entry.get()
        self.get_email = self.email_entry.get()
        self.get_username = self.username_entry.get()
        self.get_pass = self.password_entry.get()
        self.get_passre = self.password_reentry.get()
        self.person = admin.RegistrationAdmin(self.get_username, self.get_pass, self.get_name, self.get_email)
        self.db = admin.AdminDatabase()

        try:
            if self.get_username == self.db.search_admin(self.get_username)[0]:
                messagebox.showerror(title='Already in the database',
                                     message="Username is already connected to other admin account")
        except TypeError:
            try:
                if self.get_email == self.db.search_admin_email(self.get_email)[3]:
                    messagebox.showerror(title='Already in the database',
                                         message="Email is already connected to other admin account")
            except TypeError:
                if self.get_username == '' or self.get_email == '' or self.get_name == '' or self.get_pass == '' or self.get_passre == '':
                    messagebox.showinfo(title='Not all have input', message="All entries requires input")
                elif self.get_pass == self.get_passre:
                    if messagebox.askyesno(title='Please Confirm', message="Do you want to proceed?"):
                        self.destroy()
                        self.run = FrameTwo(self.container, self.person)

                else:
                    messagebox.showerror(title="Password doesn't match", message="Your Inputted password is not match")


class FrameTwo(tk.Frame):
    def __init__(self, container, person):
        super().__init__(container, bg='#EAC4A3')
        self.container = container
        self.person = person
        self.pack()

        self.run = FrameLoading(self)
        self.run.progress(person)
        self.run_frame_two()

    def run_frame_two(self):
            self.back_pic = tk.PhotoImage(file='graphics/back_buttons.png')
            self.back_pic2 = self.back_pic.subsample(5, 5)

            self.backButton = tk.Button(self, image=self.back_pic2, bg='#EAC4A3',
                                        activebackground='#EAC4A3', bd=0, command=self.back)
            self.backButton.grid(row=0, column=0, sticky='nw')

            # Code
            self.frame_name4 = tk.LabelFrame(self, text='Summary', bg='#EAC4A3')
            self.frame_name4.grid(row=1, column=0, padx=20, pady=20)

            self.sum_name = tk.Label(self.frame_name4, text=f'Name: {self.person.name}', bg='#EAC4A3')
            self.sum_name.grid(row=0, column=0)

            self.sum_email = tk.Label(self.frame_name4, text=f'Email: {self.person.email}', bg='#EAC4A3')
            self.sum_email.grid(row=1, column=0)

            self.sum_username = tk.Label(self.frame_name4, text=f'Username: {self.person.username}', bg='#EAC4A3')
            self.sum_username.grid(row=2, column=0)

            self.sum_password = tk.Label(self.frame_name4, text=f'Password: {len(self.person.password)} digit pass', bg='#EAC4A3')
            self.sum_password.grid(row=3, column=0)

            # Setting Frame name 2
            self.frame_name2 = tk.LabelFrame(self, text="Registration", bg='#EAC4A3')
            self.frame_name2.grid(row=2, column=0, padx=20, pady=10)

            # Frame 2 Label
            self.title2 = tk.Label(self.frame_name2,
                                   text='PLEASE INPUT THE CODE Sent to this email (please save the code for update purposes): ',
                                   font=('Comic Sans', 12, 'bold'), bg='#EAC4A3')
            self.title2.grid(row=0, column=0)

            self.code = tk.Label(self.frame_name2, text=f'{self.person.email}', font=('Comic Sans', 15, 'bold'), bg='#EAC4A3')
            self.code.grid(row=1, column=0)

            self.code_label = tk.Label(self.frame_name2, text="Input the code here:", font=('Comic Sans', 10, 'bold'),
                                       bg='#EAC4A3')
            self.code_label.grid(row=2, column=0)

            self.code_entry = tk.Entry(self.frame_name2)
            self.code_entry.grid(row=3, column=0)

            for widgets in self.frame_name2.winfo_children():
                widgets.grid_configure(padx=10, pady=10)

            self.frame_name3 = tk.LabelFrame(self, text='Privacy Act', bg='#EAC4A3')
            self.frame_name3.grid(row=3, column=0, padx=20, pady=20)

            self.check = tk.Label(self.frame_name3, text="""PRIVACY CONSENT: I understand and agree that by pressing "Register" button of this form 
                    I am allowing the T.A.P.S.I.Log System from the Technological Institute of the Philippines - Quezon City to collect,
                    use, share, and disclose my personal information for activity evaluation purposes and to store it as long as necessary 
                    for the fulfillment of the stated purpose and in accordance with applicable law, including the Data Privacy Act of 2012 
                    and its implementing Rules and Regulations, and the T.I.P. Privacy Policy. The purpose and extent of the collection, 
                    use, sharing, disclosure, this form is collecting email addresses. Change settings and storage of my personal information
                    was explained to me.""", bg='#EAC4A3')
            self.check.grid(row=0, column=0)

            self.btn = tk.PhotoImage(file='graphics/visitor_but.png')
            self.btn2 = self.btn.subsample(2, 2)

            self.code_button = tk.Button(self.frame_name2, image=self.btn2, bd=0, activebackground='#EAC4A3',  bg='#EAC4A3', command=self.register_the_ad)
            self.code_button.grid(row=4, column=0)

    def register_the_ad(self):
        try:
            if int(self.code_entry.get()) == int(self.person.get_security_access()):
                if messagebox.askyesno(title="Are you sure",
                                       message="Pressing 'OK' will register you as the new admin"):
                    self.create = admin.AdminDatabase()
                    self.create.create_admin(self.person)
                    messagebox.showinfo(title="SUCCESSFUL", message="Your data has been Registered!")
                    self.python = sys.executable
                    os.execl(self.python, self.python, *sys.argv)
            else:
                messagebox.showerror(title='Code Not Match', message="Code not match please try again")
        except ValueError:
            messagebox.showinfo(title='Not all have input', message="All entries requires input")


    def back(self):
        self.destroy()
        self.run = FrameOne(self.container)


class FrameLoading(tk.Frame):
    def __init__(self, container):
        super().__init__(container, bg='#EAC4A3')
        self.grid(row=0, column=0, padx=50, pady=250)

        self.text = tk.Label(self, text="SENDING YOUR EMAIL PLEASE WAIT", bg='#EAC4A3')
        self.text.grid(row=0, column=0)

        self.prog = ttk.Progressbar(self, orient='horizontal', length=300, mode='determinate', value=0)
        self.prog.grid(row=1, column=0)

        for widget in self.winfo_children():
            widget.grid_configure(pady=5, padx=50)

    def progress(self, person):
        for i in range(6):
            try:
                if self.prog['value'] < 100:
                    self.update_idletasks()
                    self.prog['value'] += 20
                    time.sleep(1)
                else:
                    self.send = send.EmailSender()
                    self.send.send_code_email(person.name, person.security_access, person.email)
                    self.destroy()
            except:
                messagebox.showerror(title="Something Occured", message="There is an error, please try Again")
                self.python = sys.executable
                os.execl(self.python, self.python, *sys.argv)

