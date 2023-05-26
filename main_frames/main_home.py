import tkinter as tk
import time
from datetime import date
from databases import VisitorsCRUD as visit
from databases import HomeownersCRUD as home
import tkintermapview


class MainHome(tk.Frame):  # Main Frame Window
    def __init__(self, container, name):
        super().__init__(container, highlightbackground='black', highlightthickness=2)
        self.name = name
        self.home = home.HomeownersDB()
        self.visit = visit.VisitorDB()
        self.today = date.today()
        self.configure(width=980, height=720, bg='#EAC4A3')
        self.grid_propagate(False)
        self.grid(row=0, column=1)

        self.photo = tk.PhotoImage(file='graphics/Logo-cut.png')
        self.photo2 = self.photo.subsample(2, 2)
        self.logo_at_side = tk.Label(self, image=self.photo2, bg='#EAC4A3')
        self.logo_at_side.grid(row=0, column=0)

        self.welcome_label = tk.LabelFrame(self, font=('Arial Black', 15), bg='#EAC4A3')
        self.welcome_label.grid(row=1, column=0, padx=55, pady=10)


        """ Sets the window to greet the admin when ever it is morning, afternoon or evening
        note: base in the time presented by the host pc """
        if time.strftime('%p') == "AM":
            self.welcome_label.config(text=f"Good Morning, Admin {self.name}!")
        elif int(time.strftime('%I')) == 12 and time.strftime('%p') == 'PM':
            self.welcome_label.config(text=f"Good Afternoon, Admin {self.name}!")
        elif int(time.strftime('%I')) < 6 and time.strftime('%p') == 'PM':
            self.welcome_label.config(text=f"Good Afternoon, Admin {self.name}!")
        else:
            self.welcome_label.config(text=f"Good Evening, Admin {self.name}!")

        """The whole set of the widgets in the frames"""
        self.welcome_admin = tk.Label(self.welcome_label, text="WELCOME TO T.A.P.S.I.Log SYSTEM", font=('Arial Black', 30), bg='#EAC4A3')
        self.welcome_admin.grid(row=0, column=0, padx=30)

        # The clock that updates every 1 second
        self.clock = tk.Label(self, font=("Arial", 10), bg='#EAC4A3')
        self.clock.grid(row=2, column=0)
        self.get_time()

        # Center Frame
        self.new_frame = tk.Frame(self, bg='#EAC4A3')
        self.new_frame.grid(row=3, column=0, padx=50, pady=20, sticky='w')

        # Frames for both Counters
        self.new_new_frame = tk.Frame(self.new_frame, bg='#EAC4A3')
        self.new_new_frame.grid(row=0, column=0, padx=50, sticky='w')

        # Frame for Map
        self.new_new_new_frame = tk.Frame(self.new_frame, bg='#EAC4A3')
        self.new_new_new_frame.grid(row=0, column=1, padx=25)

        # Frame for Homeowner Counter
        self.label = tk.LabelFrame(self.new_new_frame, text='The Total Number of Registered Homeowners', font=("Arial Black", 10, 'bold'), bg='#EAC4A3')
        self.label.grid(row=0, column=0)

        self.count = tk.Label(self.label, text=f"{len(self.home.all_homeowner())}", font=("Arial Black", 30, 'bold'), bg='#EAC4A3')
        self.count.grid(row=0, column=0)

        # Frame for Visitor Counter
        self.label2 = tk.LabelFrame(self.new_new_frame, text='The Total Number of Registered Visitors',
                                   font=("Arial Black", 10, 'bold'), bg='#EAC4A3')
        self.label2.grid(row=1, column=0)

        # Counter of the visitors registered
        self.count2 = tk.Label(self.label2, text=f"{len(self.visit.all_visitor())}", font=("Arial Black", 30, 'bold'), bg='#EAC4A3')
        self.count2.grid(row=0, column=0)

        # Map sections
        self.label3 = tk.LabelFrame(self.new_new_new_frame, text='Map',
                                   font=("Arial Black", 10, 'bold'), bg='#EAC4A3')
        self.label3.grid(row=0, column=0)

        # Movable map
        self.map = tkintermapview.TkinterMapView(self.label3, width=425, height=350, corner_radius=0)
        self.map.grid(row=0, column=0)

        self.map.set_position(14.6258, 121.0617)

        for widgets in self.label.winfo_children():
            widgets.grid_configure(padx=150, pady=10)

        for widgets in self.label2.winfo_children():
            widgets.grid_configure(padx=150, pady=10)




    # Update the label time widget
    def get_time(self):
        self.today_date = self.today.strftime("%B %d, %Y")
        self.time = f"It is {time.strftime('%I:%M:%S %p')} of {self.today_date}"
        self.clock.config(text=self.time, font=("Arial Black", 10, 'bold'))
        self.clock.after(200, self.get_time)




