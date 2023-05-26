import tkinter as tk
from tkinter import ttk
import VisitorsUpdateGUI as visitup
import UpdtfromDB as homeup


class MainUpdate(tk.Frame):
    def __init__(self, container):
        super().__init__(container, highlightbackground='black', highlightthickness=2)
        self.container = container
        self.configure(width=980, height=720, bg='#EAC4A3')
        self.grid_propagate(False)
        self.grid(row=0, column=1)
        self.button = tk.Button(self, text='BAD')
        self.button.grid(row=0, column=0)

        self.frame = tk.Frame(self, bg='#EAC4A3')
        self.frame.grid(row=0, column=0, padx=10, pady=10)

        self.photo = tk.PhotoImage(file='graphics/update_logo_circle.png')
        self.photo2 = self.photo.subsample(3, 3)
        self.logo_at_side = tk.Label(self.frame, image=self.photo2, bg='#EAC4A3')
        self.logo_at_side.grid(row=0, column=0)

        self.update_label = tk.Label(self.frame, text="UPDATE DETAILS OF A HOMEOWNER OR A VISITOR", font=('Arial Black', 20),
                                  bg='#EAC4A3')
        self.update_label.grid(row=0, column=1)

        self.frame2 = tk.Frame(self, bg='#EAC4A3')
        self.frame2.grid(row=1, column=0, padx=10, pady=10)

        self.button_home_image = tk.PhotoImage(file='graphics/update_button_home.png')
        self.button_home_image2 = self.button_home_image.subsample(1, 1)
        self.button_homereg = tk.Button(self.frame2, image=self.button_home_image2, bg='#EAC4A3', bd=0,
                                        activebackground='#EAC4A3', command=self.run_find_home)
        self.button_homereg.grid(row=0, column=0, padx=0, pady=0)

        self.button_image = tk.PhotoImage(file='graphics/update_button_visit.png')
        self.button_image2 = self.button_image.subsample(1, 1)
        self.button = tk.Button(self.frame2, image=self.button_image2, bg='#EAC4A3', bd=0, activebackground='#EAC4A3', command=self.run_find_visit)
        self.button.grid(row=1, column=0, padx=0, pady=0)

        for widget in self.frame2.winfo_children():
            widget.grid_configure(padx=10, pady=10)


    def run_find_visit(self):
        self.run = visitup.VisitorWindow3(self.container)

    def run_find_home(self):
        self.run = homeup.MainWinUpd(self.container)
