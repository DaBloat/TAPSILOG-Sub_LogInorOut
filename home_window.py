import tkinter as tk
from tkinter import messagebox
import login_window as lw
from main_frames import main_home, main_reg, main_find, main_update, main_log, main_gen


class ControlFrame(tk.LabelFrame):
    def __init__(self, main_frame, name):
        super().__init__(main_frame, bg='#F4E8E2', width=300, height=720)
        self.name = name
        self.main_frame = main_frame
        self.grid_propagate(False)
        self.pack_propagate(False)
        self.grid(row=0, column=0)

        self.side_logo = tk.Frame(self, bg='#EDD8D0')
        self.side_logo.grid(row=0, column=0, padx=50, pady=20)

        self.photo = tk.PhotoImage(file='graphics/Logo-cut.png')
        self.photo2 = self.photo.subsample(5, 5)
        self.logo_at_side = tk.Label(self.side_logo, image=self.photo2, bg='#EDD8D0', text='T.A.P.S.I.Log',
                                     font=("Arial Black", 20), compound='top')
        self.logo_at_side.grid(row=0, column=0)

        self.label_at_side = tk.Label(self.side_logo, text=
        """
Total Activity Processed
through a Strictly Implemented 
Log System 
        """, font=('', 8), bg='#EDD8D0')
        self.label_at_side.grid(row=2, column=0)

        self.side_buttons = tk.Frame(self, bg='#F4E8E2')
        self.side_buttons.grid(row=1, column=0, padx=50, pady=20)

        self.btn_variable = tk.IntVar()

        # Home Logo
        self.home_photo = tk.PhotoImage(file='graphics/home_logo.png')
        self.home_photo2 = self.home_photo.subsample(20, 20)

        # Home Button
        self.home_button = tk.Button(self.side_buttons, text='Home', bg='#EAC4A3', bd=0, font=("Arial Black", 15),
                                     command=self.run_home, image=self.home_photo2, compound='none')
        self.home_button.grid(row=0, column=0)

        # Register Logo
        self.reg_photo = tk.PhotoImage(file='graphics/reg_logo.png')
        self.reg_photo2 = self.reg_photo.subsample(15, 15)

        # Register Button
        self.reg_button = tk.Button(self.side_buttons, text='Register', bg='#F4E8E2', bd=0, font=("Arial Black", 15),
                                    command=self.run_reg, image=self.reg_photo2, compound='left')
        self.reg_button.grid(row=1, column=0)

        # Find Logo
        self.find_photo = tk.PhotoImage(file='graphics/find_logo.png')
        self.find_photo2 = self.find_photo.subsample(15, 15)

        # Find Button
        self.find_button = tk.Button(self.side_buttons, text='Find', bg='#F4E8E2', bd=0, font=("Arial Black", 15),
                                     command=self.run_find, image=self.find_photo2, compound='left')
        self.find_button.grid(row=2, column=0)

        #  Update Logo
        self.update_photo = tk.PhotoImage(file='graphics/update_logo.png')
        self.update_photo2 = self.update_photo.subsample(15, 15)

        # Update Button
        self.update_button = tk.Button(self.side_buttons, text='Update', bg='#F4E8E2', bd=0, font=("Arial Black", 15),
                                       command=self.run_update, image=self.update_photo2, compound='left')
        self.update_button.grid(row=3, column=0)

        #  Log Logo
        self.log_photo = tk.PhotoImage(file='graphics/log_logo.png')
        self.log_photo2 = self.log_photo.subsample(15, 15)

        # Log Button
        self.log_button = tk.Button(self.side_buttons, text='Log', bg='#F4E8E2', bd=0, font=("Arial Black", 15),
                                    command=self.run_log, image=self.log_photo2, compound='left')
        self.log_button.grid(row=4, column=0)

        #  Generate Logo
        self.generate_photo = tk.PhotoImage(file='graphics/generate_logo.png')
        self.generate_photo2 = self.generate_photo.subsample(15, 15)

        # Generate Button
        self.generate_button = tk.Button(self.side_buttons, text='Generate', bg='#F4E8E2', bd=0,
                                         font=("Arial Black", 15), command=self.run_generate, image=self.generate_photo2, compound='left')
        self.generate_button.grid(row=5, column=0)

        # Exit Logo
        self.exit_photo = tk.PhotoImage(file='graphics/exit_logo.png')
        self.exit_photo2 = self.exit_photo.subsample(15, 15)

        # Exit Button
        self.exit_button = tk.Button(self.side_buttons, text='Exit', bg='#F4E8E2', bd=0, font=("Arial Black", 15),
                                     command=self.exit_app,  image=self.exit_photo2, compound='left')
        self.exit_button.grid(row=6, column=0)

        for widgets in self.side_buttons.winfo_children():
            widgets.grid_configure(padx=15, pady=12)

        self.frames = {5: main_gen.MainGenerate(self.main_frame),
                       4: main_log.MainLog(self.main_frame),
                       3: main_update.MainUpdate(self.main_frame),
                       2: main_find.MainFind(self.main_frame),
                       1: main_reg.MainRegister(self.main_frame),
                       0: main_home.MainHome(self.main_frame, self.name)}

    def run_home(self):
        self.refresh_indicator()
        self.home_button.config(compound='none', bg='#EAC4A3')
        self.btn_variable = 0
        self.switch_frame()

    def run_reg(self):
        self.refresh_indicator()
        self.reg_button.config(compound='none', bg='#EAC4A3')
        self.btn_variable = 1
        self.switch_frame()

    def run_find(self):
        self.refresh_indicator()
        self.find_button.config(compound='none', bg='#EAC4A3')
        self.btn_variable = 2
        self.switch_frame()

    def run_update(self):
        self.refresh_indicator()
        self.update_button.config(compound='none', bg='#EAC4A3')
        self.btn_variable = 3
        self.switch_frame()

    def run_log(self):
        self.refresh_indicator()
        self.log_button.config(compound='none', bg='#EAC4A3')
        self.btn_variable = 4
        self.switch_frame()

    def run_generate(self):
        self.refresh_indicator()
        self.generate_button.config(compound='none', bg='#EAC4A3')
        self.btn_variable = 5
        self.switch_frame()

    def switch_frame(self):
        frame = self.frames[self.btn_variable]
        frame.tkraise()

    def refresh_indicator(self):
        self.home_button.config(compound='left', bg='#F4E8E2')
        self.reg_button.config(compound='left', bg='#F4E8E2')
        self.find_button.config(compound='left', bg='#F4E8E2')
        self.update_button.config(compound='left', bg='#F4E8E2')
        self.log_button.config(compound='left', bg='#F4E8E2')
        self.generate_button.config(compound='left', bg='#F4E8E2')

    def exit_app(self):
        if messagebox.askyesno(title='Are you sure', message="Are you sure to exit the program?"):
            self.main_frame.destroy()

class HomeWindow(tk.Tk):
    def __init__(self, name):
        super().__init__()
        self.name = name
        # Main GUI
        self.title('T.A.P.S.I.Log')
        self.cx = (int(self.winfo_screenwidth() / 2)) - int(1280 / 2)
        self.geometry("{}x{}+{}+{}".format(1280, 720, self.cx, 50))
        self.resizable(False, False)
        self.side_frame = ControlFrame(self, self.name)
        self.protocol("WM_DELETE_WINDOW", self.side_frame.exit_app)
        self.mainloop()


#display = HomeWindow('Kyna')
