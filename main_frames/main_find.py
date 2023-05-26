import tkinter as tk
from tkinter import ttk
import VisitorsReadGUI as findvisit
import FindHMOwner as findhome


class MainFind(tk.Frame):
    def __init__(self, container):
        super().__init__(container, highlightbackground='black', highlightthickness=2)
        self.container = container
        self.configure(width=980, height=720, bg='#EAC4A3')
        self.grid_propagate(False)
        self.grid(row=0, column=1)
        self.button = tk.Button(self, text='SAD')
        self.button.grid(row=0, column=0)

        self.frame = tk.Frame(self, bg='#EAC4A3')
        self.frame.grid(row=0, column=0, padx=10, pady=10)

        self.photo = tk.PhotoImage(file='graphics/find_logo_circle.png')
        self.photo2 = self.photo.subsample(3, 3)
        self.logo_at_side = tk.Label(self.frame, image=self.photo2, bg='#EAC4A3')
        self.logo_at_side.grid(row=0, column=0)

        self.reg_label = tk.Label(self.frame, text="FIND EXISTING HOMEOWNER & EXISTING VISITOR", font=('Arial Black', 20),
                                  bg='#EAC4A3')
        self.reg_label.grid(row=0, column=1)

        self.frame2 = tk.Frame(self, bg='#EAC4A3')
        self.frame2.grid(row=1, column=0, padx=10, pady=10)

        self.button_home_image = tk.PhotoImage(file='graphics/find_button_homeowner.png')
        self.button_home_image2 = self.button_home_image.subsample(1, 1)
        self.button_homereg = tk.Button(self.frame2, image=self.button_home_image2, bg='#EAC4A3', bd=0,
                                        activebackground='#EAC4A3', command=self.home_btn)
        self.button_homereg.grid(row=0, column=0, padx=0, pady=0)

        self.button_image = tk.PhotoImage(file='graphics/find_button_visit.png')
        self.button_image2 = self.button_image.subsample(1, 1)
        self.button = tk.Button(self.frame2, image=self.button_image2, bg='#EAC4A3', bd=0, activebackground='#EAC4A3', command=self.visit_btn)
        self.button.grid(row=1, column=0, padx=0, pady=0)

        for widget in self.frame2.winfo_children():
            widget.grid_configure(padx=10, pady=10)


    def home_btn(self):
        self.run = findhome.HomeownerWindow2(self.container)

    def visit_btn(self):
        self.run = findvisit.VisitorWindow2(self.container)

