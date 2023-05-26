# Visitor Update GUI
# by jem -_-

import tkinter as tk
from tkinter import messagebox
from databases import VisitorsCRUD as VC

class VisitorWindow3(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.configure(width=980, height=720, bg='#EAC4A3')
        self.grid_propagate(False)
        self.grid(row=0, column=1)

        self.back_pic = tk.PhotoImage(file='graphics/back_buttons.png')
        self.back_pic2 = self.back_pic.subsample(5, 5)

        self.backButton = tk.Button(self, image=self.back_pic2, bg='#EAC4A3',
                                    activebackground='#EAC4A3', bd=0, command=self.back)
        self.backButton.grid(row=0, column=0, sticky='nw')

        # Frame
        self.frame = tk.Frame(self, bg='#EAC4A3')
        self.frame.grid(row=1, column=0, padx=200, pady=10)
        
        self.home_photo = tk.PhotoImage(file='graphics/home_logo.png')
        self.home_photo2 = self.home_photo.subsample(10, 10)
        
        # Setting Frame names
        self.frame_name = tk.LabelFrame(self.frame, text="Visitor ID", bg='#EAC4A3')
        self.frame_name.grid(row=0, column=0, padx=20, pady=20)
        
        self.frame_name2 = tk.LabelFrame(self.frame, text="Update Details", bg='#EAC4A3')
        self.frame_name2.grid(row=1, column=0, padx=20, pady=20)
        
        # Visitor ID Selection
        self.v_id_label = tk.Label(self.frame_name, text="Visitor ID:", bg="#EAC4A3")
        self.v_id_label.grid(row=0, column=0)
        
        self.v_id = tk.IntVar()
        self.v_id_entry = tk.Spinbox(self.frame_name, from_=0, to=99999999999999, textvariable=self.v_id, width=4)
        self.v_id_entry.grid(row=0, column=1)
        
        # Name
        self.name_label = tk.Label(self.frame_name2, text="Name:", bg='#EAC4A3')
        self.name_label.grid(row=0, column=0)

        # Name Entry
        self.name_entry = tk.Entry(self.frame_name2)
        self.name_entry.grid(row=0, column=1, columnspan=1)

        # Vehicle
        self.vehicle_label = tk.Label(self.frame_name2, text='Vehicle:', bg='#EAC4A3')
        self.vehicle_label.grid(row=1, column=0)
        
        #Vehicle Entry Frame
        self.vehicle_frame = tk.Frame(self.frame_name2, bg='#EAC4A3')
        self.vehicle_frame.grid(row=1, column=1)
        
        self.entryval = tk.IntVar()
        # Vehicle Entry 1
        self.vehicle_entry1 = tk.Radiobutton(self.vehicle_frame, variable=self.entryval, text='Yes', bg="#EAC4A3", value=1)
        self.vehicle_entry1.grid(row=0, column=0)

        # Vehicle Entry 2
        self.vehicle_entry2 = tk.Radiobutton(self.vehicle_frame, variable=self.entryval, text='No', bg='#EAC4A3',value=0)
        self.vehicle_entry2.grid(row=0, column=1)
        
        # Purpose Label
        self.purpose_label = tk.Label(self.frame_name2, text="Purpose of Visit:", bg='#EAC4A3')
        self.purpose_label.grid(row=2, column=0)

        # Purpose Entry
        self.selection = tk.StringVar()
        self.options = ["", "Transportation", "Delivery Service", "Homeowner Visit", "Official Housing Business", "Maintenance of Commodities", "Housing Development", 'Others']
        self.purpose_entry = tk.OptionMenu(self.frame_name2, self.selection,*self.options)
        self.purpose_entry.grid(row=2, column=1)

        # Contact No.
        self.contact_label = tk.Label(self.frame_name2, text="Contact:", bg='#EAC4A3')
        self.contact_label.grid(row=0, column=2)

        # Contact Entry
        self.contact_entry = tk.Entry(self.frame_name2)
        self.contact_entry.grid(row=0, column=3)

        # Plate Number
        self.plate_label = tk.Label(self.frame_name2, text="Plate Number:", bg='#EAC4A3')
        self.plate_label.grid(row=1, column=2)

        # Plate Number Entry
        self.plate_entry= tk.Entry(self.frame_name2)
        self.plate_entry.grid(row=1, column=3)

        # Formatting all the widgets
        for widgets in self.frame_name.winfo_children():
            widgets.grid_configure(padx=15, pady=15)
            
        for widgets in self.frame_name2.winfo_children():
            widgets.grid_configure(padx=15, pady=15)

        self.pic = tk.PhotoImage(file='graphics/update_btn.png')
        self.pic2 = self.pic.subsample(2, 2)
        # Register Button
        self.check_button = tk.Button(self.frame, image=self.pic2, command=self.register_clicked, bd=0, activebackground='#EAC4A3',  bg='#EAC4A3')
        self.check_button.grid(row=2, column=0)

        self.pic21 = tk.PhotoImage(file='graphics/delete_btn.png')
        self.pic22 = self.pic21.subsample(2, 2)
        # Register Button
        self.check_button1 = tk.Button(self.frame, image=self.pic22, command=self.delete_visitor, bd=0,
                                      activebackground='#EAC4A3', bg='#EAC4A3')
        self.check_button1.grid(row=3, column=0)
    
    def register_clicked(self):
        try:
            vid = self.v_id.get()
            vdb = VC.VisitorDB()
            vstr = vdb.get_visitors("Visitor ID", vid)

            if self.name_entry.get() == "":
                name = vstr[0][0]
            else:
                name = self.name_entry.get()
            vehicle = self.entryval.get()
            if vehicle == 0:
                plate_number = None
            else:
                if self.plate_entry.get() == "":
                    plate_number = vstr[0][2]
                else:
                    plate_number = self.plate_entry.get()
            if self.contact_entry.get() == "":
                contact = vstr[0][3]
            else:
                contact = self.contact_entry.get()
            if self.selection.get() == "":
                purpose = vstr[0][4]
            else:
                purpose = self.selection.get()
            new = VC.Visitor(name, vehicle, plate_number, contact, purpose, visitor_id=vid)
            vdb.update_visitor(new)
            messagebox.showinfo(title='Successfully Updated', message=f"The visitor id {vid} is successfully updated")
            self.destroy()
        except TypeError:
            messagebox.showerror(title='OUT OF RANGE', message="This Visitor ID is out of reach")
        except IndexError:
            messagebox.showerror(title='OUT OF RANGE', message="This Visitor ID is out of reach")

    def back(self):
        self.destroy()

    def delete_visitor(self):
        try:
            vdb = VC.VisitorDB()
            if self.v_id.get() < 1:
                messagebox.showerror(title='ID MISSING', message="Homeowner Id should not be blank!")
            else:
                if messagebox.askyesno(title='Are you sure?', message=f"Are you sure you want to delete id# {self.v_id.get()}?"):
                    vdb.delete_visitor(self.v_id.get())
                    messagebox.showinfo(title="SUCCESSFULY DELETED", message=f"The Homeowner ID{self.v_id.get()} is successfully deleted")
                    self.destroy()
        except sqlite3.OperationalError:
            messagebox.showerror(title='ID MISSING', message="Homeowner Id should not be blank!")

