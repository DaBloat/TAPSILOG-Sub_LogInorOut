import tkinter as tk
from databases import HomeownersCRUD as fs
from tkinter import messagebox
import os, sys



class MainWin(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.configure(width=980, height=720, bg='#eac4a3')
        self.grid_propagate(False)
        self.grid(row=0, column=1)

        self.back_pic = tk.PhotoImage(file='graphics/back_buttons.png')
        self.back_pic2 = self.back_pic.subsample(5, 5)

        self.backButton = tk.Button(self, image=self.back_pic2, bg='#EAC4A3',
                                    activebackground='#EAC4A3', bd=0, command=self.back)
        self.backButton.grid(row=0, column=0, sticky='nw')

        # Frame
        self.frame = tk.Frame(self, bg='#EAC4A3')
        self.frame.grid(row=1, column=0, padx=125, pady=10)

        self.group = tk.LabelFrame(self.frame, text='Create New Homeowner', bg='#eac4a3', padx=20, pady=20)
        self.group.grid(row=0, column=0, padx=20, pady=20)

# Labels + entry fields

# name
        self.name_entry = tk.Entry(self.group)
        self.name_entry.grid(row=1, column=1)
        self.name_label = tk.Label(self.group, text="Name:", bg='#eac4a3')
        self.name_label.grid(row=1, column=0, padx=5, pady=5, sticky="E")

# contact no.
        self.contc_entry = tk.Entry(self.group)
        self.contc_entry.grid(row=1, column=3, columnspan=2)
        self.contc_label = tk.Label(self.group, text="Contact Number:", bg='#eac4a3')
        self.contc_label.grid(row=1, column=2, padx=5, pady=5, sticky="E")

# email
        self.email_entry = tk.Entry(self.group)
        self.email_entry.grid(row=1, column=6)
        self.email_label = tk.Label(self.group, text="Email:", bg='#eac4a3')
        self.email_label.grid(row=1, column=5, padx=5, pady=7, sticky="E")

# block num
        self.blkno_entry = tk.Entry(self.group)
        self.blkno_entry.grid(row=3, column=1)
        self.blkno_label = tk.Label(self.group, text="Block Number:", bg='#eac4a3')
        self.blkno_label.grid(row=3, column=0, padx=5, pady=5, sticky="E")

# lot num
        self.lotno_entry = tk.Entry(self.group)
        self.lotno_entry.grid(row=3, column=3, columnspan=2)
        self.lotno_label = tk.Label(self.group, text="Lot Number:", bg='#eac4a3')
        self.lotno_label.grid(row=3, column=2, padx=5, pady=5, sticky="E")

# plate num
        self.pltno_entry = tk.Entry(self.group)
        self.pltno_entry.grid(row=3, column=6)
        self.pltno_label = tk.Label(self.group, text="Plate Number:", bg='#eac4a3')
        self.pltno_label.grid(row=3, column=5, padx=5, pady=5, sticky="E")
        
# yesnt radiobutt
        self.ynval = tk.IntVar()
        self.yesno = tk.Label(self.group, text="Vehicle: ", bg="#EAC4A3")
        self.yesno.grid(row=4, column=2, columnspan=2)
        self.yesnt = tk.Radiobutton(self.group, text='Yes', value=1, bg="#EAC4A3", variable=self.ynval, command=self.pltopen, activebackground="#EAC4A3")
        self.yesnt.grid(row=4, column=3)
        self.nont = tk.Radiobutton(self.group, text='No', value=0, bg="#EAC4A3", variable=self.ynval, command=self.pltclose, activebackground="#EAC4A3")
        self.nont.grid(row=4, column=4)

        self.home_but = tk.PhotoImage(file='graphics/visitor_but.png')
        self.home_but2 = self.home_but.subsample(2, 2)

        # Register Button
        self.check_button = tk.Button(self.frame, image=self.home_but2, command=self.add_howner, bd=0, bg='#EAC4A3', activebackground='#EAC4A3')
        self.check_button.grid(row=1, column=0)

        self.group_2 = tk.LabelFrame(self, text="Privacy Act", bg='#EAC4A3')

        self.group_2.grid(row=3, column=0, columnspan=8)

        self.check = tk.Label(self.group_2, text="""I understand and agree that by pressing "Register" button of this form 
        I am allowing the T.A.P.S.I.Log System from the Technological Institute of the Philippines - Quezon City to collect,
        use, share, and disclose my personal information for activity evaluation purposes and to store it as long as necessary 
        for the fulfillment of the stated purpose and in accordance with applicable law, including the Data Privacy Act of 2012 
        and its implementing Rules and Regulations, and the T.I.P. Privacy Policy. The purpose and extent of the collection, 
        use, sharing, disclosure, this form is collecting email addresses. Change settings and storage of my personal information
        was explained to me.""", bg='#EAC4A3')
        self.check.grid(column=1, padx=10, pady=10)

# plateno yeno definer
    def pltclose(self):
        self.pltno_entry.config(state="disabled")
            
    def pltopen(self):
        self.pltno_entry.config(state="normal")

    def back(self):
        self.destroy()

# Function to be called when the button is clicked
    def add_howner(self):
        self.vehicle = self.ynval.get()

        pn = self.pltno_entry.get()

        if self.name_entry.get() =='' or self.blkno_entry.get() == '' or self.lotno_entry.get() == ''  or self.contc_entry.get() == '' or self.email_entry.get() == '':
            messagebox.showerror(title='Not all have input', message="All entries requires input")

            if self.vehicle == 0:
                pn = None

        else:
            self.person = fs.Homeowner(self.name_entry.get(), self.blkno_entry.get(), self.lotno_entry.get(),
                                           self.pltno_entry.get(), self.contc_entry.get(), self.email_entry.get(),
                                           self.vehicle)
            self.save = fs.HomeownersDB()
            self.save.create_hmowner(self.person)
            messagebox.showinfo(message='A Homeowner successfully registered')
            self.destroy()

