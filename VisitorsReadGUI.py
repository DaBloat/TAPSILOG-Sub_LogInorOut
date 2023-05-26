# Visitor Read GUI
# by jem -_-

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from databases import VisitorsCRUD as VC


class VisitorWindow2(tk.Frame):
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
        self.frame.grid(row=1, column=0, padx=30, pady=10)
        
        #self.home_photo = tk.PhotoImage(file='graphics/home_logo.png')
        #self.home_photo2 = self.home_photo.subsample(10, 10)
        
        # Setting Frame names
        self.frame_name = tk.LabelFrame(self.frame, text="Visitor Info", bg='#EAC4A3', width=500)
        self.frame_name.grid(row=0, column=0, padx=40, pady=10)
        
        self.frame_name2 = tk.LabelFrame(self.frame, bg='#EAC4A3')
        self.frame_name2.grid(row=2, column=0, padx=40, pady=10)
        
        # Category
        self.category = tk.Label(self.frame_name, text="Category", bg='#EAC4A3')
        self.category.grid(row=0, column=0)
        
        # Category Drop Box
        self.detail = tk.StringVar()
        self.category_entry = ttk.Combobox(self.frame_name, width = 15, textvariable=self.detail)
        self.category_entry['values'] = ('All', 'Visitor ID', 'Name', 'Vehicle', 'Plate Number', 'Contact Number', 'Purpose')
        self.category_entry.grid(row=0, column=1)
        self.category_entry.current(0)
        
        # Value
        self.val_label = tk.Label(self.frame_name, text="Value:", bg='#EAC4A3')
        self.val_label.grid(row=1, column=0)

        # Value Entry
        self.value = tk.StringVar()
        self.val_entry = tk.Entry(self.frame_name, width=18, textvariable=self.value)
        self.val_entry.grid(row=1, column=1)
        
        # Formatting all the widgets
        for widgets in self.frame_name.winfo_children():
            widgets.grid_configure(padx=35, pady=10)

        self.find_pic = tk.PhotoImage(file='graphics/find_btn.png')
        self.find_pic2 = self.find_pic.subsample(2, 2)
        # Register Button
        self.check_button = tk.Button(self.frame, image=self.find_pic2, command=self.register_clicked, bd=0, bg='#EAC4A3', activebackground='#EAC4A3')
        self.check_button.grid(row=1, column=0)
        
        # Treeview Table
        self.table = ttk.Treeview(self.frame_name2, columns=('Visitor ID','Name', 'Vehicle', 'Plate Number', 'Contact Number', 'Purpose'), show='headings', height=15)
        self.table.column("# 1", anchor='center', width=125)
        self.table.column("# 2", anchor='center', width=125)
        self.table.column("# 3", anchor='center', width=125)
        self.table.column("# 4", anchor='center', width=125)
        self.table.column("# 5", anchor='center', width=125)
        self.table.column("# 6", anchor='center', width=125)
        self.table.heading('Visitor ID', text='Visitor ID')
        self.table.heading('Name', text='Name')
        self.table.heading('Vehicle', text='Vehicle')
        self.table.heading('Plate Number', text='Plate Number')
        self.table.heading('Contact Number', text='Contact Number')
        self.table.heading('Purpose', text='Purpose')
        self.table.grid(row=0, column=0, padx=25, pady=10)

        self.scroll = ttk.Scrollbar(self.frame_name2, orient=tk.VERTICAL, command=self.table.yview)
        self.table.configure(yscroll=self.scroll.set)
        self.scroll.grid(row=0, column=1, sticky='ns')
        
    def register_clicked(self):
        for content in self.table.get_children():
            self.table.delete(content)
        
        # Data from Entries
        detail = self.detail.get()
        value = self.value.get()
        
        vdb = VC.VisitorDB()
        visitors = vdb.get_visitors(detail, value)
        if len(visitors) == 0:
            messagebox.showinfo(title='No data for this category', message="This category is empty")
        else:
            for visitor in visitors:
                self.table.insert(parent='', index='end', values=(visitor[5], visitor[0], visitor[1], visitor[2], visitor[3], visitor[4]))

    def back(self):
        self.destroy()
    
