# Visitor Create GUI
# by jem -_-

import tkinter as tk
from tkinter import messagebox
from databases import VisitorsCRUD as VC


class VisitorWindow(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.configure(width=980, height=720, bg='#EAC4A3')
        self.grid_propagate(False)
        self.grid(row=0, column=1)

        self.back_pic = tk.PhotoImage(file='graphics/back_buttons.png')
        self.back_pic2 = self.back_pic.subsample(5, 5)

        self.backButton = tk.Button(self, image=self.back_pic2, command=self.back, bg='#EAC4A3', activebackground='#EAC4A3', bd=0)
        self.backButton.grid(row=0, column=0, sticky='nw')

        # Frame
        self.frame = tk.Frame(self, bg='#EAC4A3')
        self.frame.grid(row=1, column=0, padx=125, pady=10)
        
        self.home_photo = tk.PhotoImage(file='graphics/home_logo.png')
        self.home_photo2 = self.home_photo.subsample(10, 10)
        
        # Setting Frame names
        self.frame_name = tk.LabelFrame(self.frame, text="Visitor Info", bg='#EAC4A3')
        self.frame_name.grid(row=0, column=0, padx=20, pady=20)
        
        self.frame_name2 = tk.LabelFrame(self.frame, text="Privacy Act", bg='#EAC4A3')
        self.frame_name2.grid(row=2, column=0, padx=20, pady=20)
        
        # PRIVACY ACT
        self.check = tk.Label(self.frame_name2, text="""I understand and agree that by pressing "Register" button of this form 
        I am allowing the T.A.P.S.I.Log System from the Technological Institute of the Philippines - Quezon City to collect,
        use, share, and disclose my personal information for activity evaluation purposes and to store it as long as necessary 
        for the fulfillment of the stated purpose and in accordance with applicable law, including the Data Privacy Act of 2012 
        and its implementing Rules and Regulations, and the T.I.P. Privacy Policy. The purpose and extent of the collection, 
        use, sharing, disclosure, this form is collecting email addresses. Change settings and storage of my personal information
        was explained to me.""", bg='#EAC4A3')
        self.check.grid(row=0, column=0)

        # Name
        self.name_label = tk.Label(self.frame_name, text="Name:", bg='#EAC4A3')
        self.name_label.grid(row=0, column=0)

        # Name Entry
        self.name_entry = tk.Entry(self.frame_name)
        self.name_entry.grid(row=0, column=1, columnspan=1)

        # Vehicle
        self.vehicle_label = tk.Label(self.frame_name, text='Vehicle:', bg='#EAC4A3')
        self.vehicle_label.grid(row=1, column=0)
        
        # Vehicle Entry Frame
        self.vehicle_frame = tk.Frame(self.frame_name, bg='#EAC4A3')
        self.vehicle_frame.grid(row=1, column=1)
        
        self.entryval = tk.IntVar()
        # Vehicle Entry 1
        self.vehicle_entry1 = tk.Radiobutton(self.vehicle_frame, variable=self.entryval, text='Yes', bg="#EAC4A3", value=1, activebackground='#EAC4A3')
        self.vehicle_entry1.grid(row=0, column=0)

        # Vehicle Entry 2
        self.vehicle_entry2 = tk.Radiobutton(self.vehicle_frame, variable=self.entryval, text='No', bg='#EAC4A3', value=0, activebackground='#EAC4A3')
        self.vehicle_entry2.grid(row=0, column=1)
        
        # Purpose Label
        self.purpose_label = tk.Label(self.frame_name, text="Purpose of Visit:", bg='#EAC4A3')
        self.purpose_label.grid(row=2, column=0)

        # Purpose Entry
        self.selection = tk.StringVar()
        self.options = ["Transportation", "Delivery Service", "Homeowner Visit", "Official Housing Business", "Maintenance of Commodities", "Housing Development", 'Others']
        self.purpose_entry = tk.OptionMenu(self.frame_name, self.selection, *self.options)
        self.purpose_entry.grid(row=2, column=1)

        # Contact No.
        self.contact_label = tk.Label(self.frame_name, text="Contact:", bg='#EAC4A3')
        self.contact_label.grid(row=0, column=2)

        # Contact Entry
        self.contact_entry = tk.Entry(self.frame_name)
        self.contact_entry.grid(row=0, column=3)

        # Plate Number
        self.plate_label = tk.Label(self.frame_name, text="Plate Number:", bg='#EAC4A3')
        self.plate_label.grid(row=1, column=2)

        # Plate Number Entry
        self.plate_entry= tk.Entry(self.frame_name)
        self.plate_entry.grid(row=1, column=3)

        # Formatting all the widgets
        for widgets in self.frame_name.winfo_children():
            widgets.grid_configure(padx=15, pady=15)

        self.vis_but = tk.PhotoImage(file='graphics/visitor_but.png')
        self.vis_but2 = self.vis_but.subsample(2, 2)

        # Register Button
        self.check_button = tk.Button(self.frame, image=self.vis_but2, command=self.register_clicked, bd=0, bg='#EAC4A3', activebackground='#EAC4A3')
        self.check_button.grid(row=1, column=0)
    
    def register_clicked(self):
        # Data from Entries
        name = self.name_entry.get()
        vehicle = self.entryval.get()
        contact = self.contact_entry.get()
        purpose = self.selection.get()
        if name == '' or vehicle == '' or contact == '' or purpose == '':
            messagebox.showerror(title='Not all have input', message="All entries requires input")
        else:
            if vehicle == 0:
                plate_number = None
            else:
                plate_number = self.plate_entry.get()
            # Create new Visitor
            new = VC.Visitor(name, vehicle, plate_number, contact, purpose)
            vdb = VC.VisitorDB()
            vdb.create_visitor(new)
            messagebox.showinfo(title="SUCCESSFUL", message="Your data has been Registered!")
            self.destroy()
    def back(self):
        self.destroy()

        

