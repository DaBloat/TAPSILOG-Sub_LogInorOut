# -*- coding: utf-8 -*-
"""
Created on Wed May  3 20:43:30 2023

@author: SLYWDYNSTY
"""
import sqlite3
#jem'd gui homeowners

import tkinter as tk
from databases import HomeownersCRUD as fs
from tkinter import messagebox


class MainWinUpd(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.configure(width=980, height=720, bg="#eac4a3")
        self.grid_propagate(False)
        self.grid(row=0, column=1)

        self.back_pic = tk.PhotoImage(file='graphics/back_buttons.png')
        self.back_pic2 = self.back_pic.subsample(5, 5)

        self.backButton = tk.Button(self, image=self.back_pic2, bg='#EAC4A3',
                                    activebackground='#EAC4A3', bd=0, command=self.back)
        self.backButton.grid(row=0, column=0, sticky='nw')

        self.mew_frame = tk.Frame(self, bg ='#eac4a3')
        self.mew_frame.grid(row=1, column=0, padx=130, pady=10)

# Frame
        self.group = tk.LabelFrame(self.mew_frame, text='Update Homeowner Database', bg='#eac4a3', padx=20, pady=20)
        self.group.grid()

# Labels + entry fields
#id_num
        self.idnum_entry = tk.Entry(self.group)
        self.idnum_entry.grid(row=0, column=3, columnspan=2)
        self.idnum_label = tk.Label(self.group, text="ID Number:", bg='#eac4a3')
        self.idnum_label.grid(row=0, column=2, padx=5, pady=5, sticky="E")
#name
        self.name_entry = tk.Entry(self.group)
        self.name_entry.grid(row=1, column=1)
        self.name_label = tk.Label(self.group, text="Name:", bg='#eac4a3')
        self.name_label.grid(row=1, column=0, padx=5, pady=5, sticky="E")
#contact no.
        self.contc_entry = tk.Entry(self.group)
        self.contc_entry.grid(row=1, column=3, columnspan=2)
        self.contc_label = tk.Label(self.group, text="Contact Number:", bg='#eac4a3')
        self.contc_label.grid(row=1, column=2, padx=5, pady=5, sticky="E")
#email
        self.email_entry = tk.Entry(self.group)
        self.email_entry.grid(row=1, column=6)
        self.email_label = tk.Label(self.group, text="Email:", bg='#eac4a3')
        self.email_label.grid(row=1, column=5, padx=5, pady=7, sticky="E")
#block num
        self.blkno_entry = tk.Entry(self.group)
        self.blkno_entry.grid(row=3, column=1)
        self.blkno_label = tk.Label(self.group, text="Block Number:", bg='#eac4a3')
        self.blkno_label.grid(row=3, column=0, padx=5, pady=5, sticky="E")
#lot num
        self.lotno_entry = tk.Entry(self.group)
        self.lotno_entry.grid(row=3, column=3, columnspan=2)
        self.lotno_label = tk.Label(self.group, text="Lot Number:", bg='#eac4a3')
        self.lotno_label.grid(row=3, column=2, padx=5, pady=5, sticky="E")
#plate num
        self.pltno_entry = tk.Entry(self.group)
        self.pltno_entry.grid(row=3, column=6)
        self.pltno_label = tk.Label(self.group, text="Plate Number:", bg='#eac4a3')
        self.pltno_label.grid(row=3, column=5, padx=5, pady=5, sticky="E")
        
#yesnt radiobutt
        self.ynval = tk.IntVar()
        self.yesno = tk.Label(self.group, text="Vehicle: ", bg="#EAC4A3")
        self.yesno.grid(row=4, column=2, columnspan=2)
        self.yesnt = tk.Radiobutton(self.group, text='Yes', value=1, bg="#EAC4A3", variable=self.ynval, command=self.pltopen)
        self.yesnt.grid(row=4, column=3)
        self.nont = tk.Radiobutton(self.group, text='No', value=0, bg="#EAC4A3", variable=self.ynval, command=self.pltclose)
        self.nont.grid(row=4, column=4)

    
#Idhuh?    
        self.group_2 = tk.LabelFrame(self.mew_frame, text="What is my ID number?", bg='#EAC4A3')

        self.group_2.grid(row=2, column=0, columnspan=8)

        self.check = tk.Label(self.group_2, text="""Not sure about your Homeowner ID number?\n head on to the Find tab to view your information""", bg='#EAC4A3')
        self.check.grid(column=1, padx=50, pady=10)
    
    
#privact
        self.pic = tk.PhotoImage(file='graphics/update_btn.png')
        self.pic2 = self.pic.subsample(2, 2)
        # Register Button
        self.check_button = tk.Button(self.mew_frame, image=self.pic2, command=self.upd_howner, bd=0,
                                      activebackground='#EAC4A3', bg='#EAC4A3')
        self.check_button.grid(row=3, column=0)

        self.pic21 = tk.PhotoImage(file='graphics/delete_btn.png')
        self.pic22 = self.pic21.subsample(2, 2)
        # Register Button
        self.check_button1 = tk.Button(self.mew_frame, image=self.pic22, command=self.delete_home, bd=0,
                                       activebackground='#EAC4A3', bg='#EAC4A3')
        self.check_button1.grid(row=4, column=0)


#plateno yeno definer
    def pltclose(self):
        self.pltno_entry.config(state="disabled")
            
    def pltopen(self):
        self.pltno_entry.config(state="normal")

# Function to be called when the button is clicked
    def upd_howner(self):
        try:
            db = fs.HomeownersDB()
            self.past = db.get_hmowner(self.idnum_entry.get())

            if self.name_entry.get() == '':
                self.name = self.past[1]
            else:
                self.name = self.name_entry.get()

            if self.blkno_entry.get() == '':
                self.blk = self.past[2]
            else:
                self.blk = self.blkno_entry.get()

            if self.lotno_entry.get() == '':
                self.lot = self.past[3]
            else:
                self.lot = self.lotno_entry.get()

            if self.pltno_entry.get() == '':
                self.plt = self.past[4]
            else:
                self.plt = self.pltno_entry.get()

            if self.contc_entry.get() == '':
                self.contc = self.past[5]
            else:
                self.contc = self.contc_entry.get()

            if self.email_entry.get() == '':
                self.email = self.past[6]
            else:
                self.email = self.email_entry.get()

            if self.ynval.get() == '':
                self.yn = self.past[7]
            else:
                self.yn = self.ynval.get()

            self.person = fs.Homeowner(self.name, self.blk, self.lot, self.plt, self.contc, self.email, self.yn)

            if self.yn == 0:
                self.plt = None
            db.upd_hmowner(self.person, self.idnum_entry.get())
            messagebox.showinfo(title='SUCCESSFULLY UPDATED', message=f'Homeowner ID {self.idnum_entry.get()} is successfully updated')
            self.destroy()
        except sqlite3.OperationalError:
            messagebox.showerror(title='ID MISSING', message="Homeowner Id should not be blank!")

    def delete_home(self):
        try:
            if self.idnum_entry.get() == '':
                messagebox.showerror(title='ID MISSING', message="Homeowner Id should not be blank!")
            else:
                db = fs.HomeownersDB()
                if messagebox.askyesno(title='Are you sure?', message=f"Are you sure you want to delete id# {self.idnum_entry.get()}?"):
                    db.del_hmowner(self.idnum_entry.get())
                    messagebox.showinfo(title="SUCCESSFULY DELETED", message=f"The Homeowner ID{self.idnum_entry.get()} is successfully deleted")
                    self.destroy()
        except sqlite3.OperationalError:
            messagebox.showerror(title='ID MISSING', message="Homeowner Id should not be blank!")

    def back(self):
        self.destroy()