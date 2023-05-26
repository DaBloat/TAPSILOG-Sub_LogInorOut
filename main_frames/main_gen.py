import tkinter as tk
from tkinter import ttk
from databases import HomeownersCRUD as home
from databases import VisitorsCRUD as visit
from qr_generate_scanner import qr_generator
from email_senders import admicode_email
import time
from tkinter import messagebox
import sys, os


class MainGenerate(tk.Frame):  # Main Frame
    def __init__(self, container):
        super().__init__(container, highlightbackground='black', highlightthickness=2)
        self.configure(width=980, height=720, bg='#EAC4A3')
        self.grid_propagate(False)
        self.grid(row=0, column=1)
        self.button = tk.Button(self, text='GEN')
        self.button.grid(row=0, column=0)
        self.hm = home.HomeownersDB()
        self.vt = visit.VisitorDB()

        # First Frame within the Frame - placeholder for next widgets
        self.frame = tk.Frame(self, bg='#EAC4A3')
        self.frame.grid(row=0, column=0, padx=10, pady=10)

        self.photo = tk.PhotoImage(file='graphics/generate_logo_circle.png')
        self.photo2 = self.photo.subsample(3, 3)
        self.logo_at_side = tk.Label(self.frame, image=self.photo2, bg='#EAC4A3')
        self.logo_at_side.grid(row=0, column=0)

        self.reg_label = tk.Label(self.frame, text="GENERATE A QR CODE", font=('Arial Black', 20),
                                  bg='#EAC4A3')
        self.reg_label.grid(row=0, column=1)

        self.frame2 = tk.Frame(self, bg='#EAC4A3')
        self.frame2.grid(row=1, column=0)

        self.button_home_image = tk.PhotoImage(file='graphics/send_qr_home.png')
        self.button_home_image2 = self.button_home_image.subsample(1, 1)
        self.button_homereg = tk.Button(self.frame2, image=self.button_home_image2, bg='#EAC4A3', bd=0,
                                        activebackground='#EAC4A3', command=self.generate_home)
        self.button_homereg.grid(row=0, column=0)

        self.button_image = tk.PhotoImage(file='graphics/send_qr_visitor.png')
        self.button_image2 = self.button_image.subsample(1, 1)
        self.button = tk.Button(self.frame2, image=self.button_image2, bg='#EAC4A3', bd=0, activebackground='#EAC4A3', command=self.generate_visit)
        self.button.grid(row=0, column=1)

        self.button_image3 = tk.PhotoImage(file='graphics/send_qr_user.png')
        self.button_image232 = self.button_image3.subsample(1, 1)
        self.button3 = tk.Button(self.frame2, image=self.button_image232, bg='#EAC4A3', bd=0, activebackground='#EAC4A3')
        self.button3.grid(row=0, column=2)

        for widget in self.frame2.winfo_children():
            widget.grid_configure(padx=0, pady=0)

    def generate_home(self):

        self.run = FrameLoading(self)
        self.run.progress(self.hm.all_homeowner())

    def generate_visit(self):
        self.frame3 = tk.Frame(self, bg='#EAC4A3', width=400, height=250, highlightthickness=2, highlightbackground='black')
        self.frame3.grid_propagate(False)
        self.frame3.grid(row=1, column=0)

        self.back_pic = tk.PhotoImage(file='graphics/back_buttons.png')
        self.back_pic2 = self.back_pic.subsample(5, 5)

        self.backButton = tk.Button(self.frame3, image=self.back_pic2, bg='#EAC4A3',
                                    activebackground='#EAC4A3', bd=0, command=self.back)
        self.backButton.grid(row=0, column=0, sticky='nw')

        self.entry_label = tk.Label(self.frame3, text="Input Visitor ID: ", bg='#EAC4A3')
        self.entry_label.grid(row=1, column=0, padx=30, pady=10)

        self.entry = tk.Entry(self.frame3)
        self.entry.grid(row=1, column=1, padx=30, pady=10)

        self.entry_label2 = tk.Label(self.frame3, text="Input Email: ", bg='#EAC4A3')
        self.entry_label2.grid(row=2, column=0, padx=30, pady=10)

        self.entry2 = tk.Entry(self.frame3)
        self.entry2.grid(row=2, column=1, padx=30, pady=10)

        self.pic = tk.PhotoImage(file='graphics/submit_btn.png')
        self.pic2 = self.pic.subsample(2, 2)

        self.btn = tk.Button(self.frame3, image=self.pic2, bd=0, bg='#EAC4A3', activebackground='#EAC4A3', command=self.submit)
        self.btn.grid(row=3, column=1, padx=30, pady=10)

    def back(self):
        self.frame3.destroy()

    def submit(self):
        if self.entry.get() == '' or self.entry2.get()=="":
            messagebox.showerror(title="NOT ALL HAVE INPUT", message="All inputs should be inputted")
        else:
            self.run = FrameLoading(self.frame3)
            self.run.progress2(self.entry.get(), self.entry2.get())


class FrameLoading(tk.Frame):
    def __init__(self, container):
        super().__init__(container, bg='#EAC4A3')
        self.container = container
        self.grid(row=1, column=0)

        self.text = tk.Label(self, text="SENDING EMAILS PLEASE WAIT", bg='#EAC4A3')
        self.text.grid(row=0, column=0)

        self.prog = ttk.Progressbar(self, orient='horizontal', length=300, mode='determinate', value=0)
        self.prog.grid(row=1, column=0)

        for widget in self.winfo_children():
            widget.grid_configure(pady=5, padx=50)

    def progress(self, piece):
        for i in range(6):
            #try:
                if self.prog['value'] < 100:
                    self.update_idletasks()
                    self.prog['value'] += 20
                    time.sleep(1)
                else:
                    self.gen = qr_generator.QRGenerate()
                    self.send = admicode_email.EmailSender()
                    for value in piece:
                        self.gen.genQrHome(value)
                        self.send.send_qrHome(value[1], value[6])
                    self.destroy()
            #except:
              ##  messagebox.showerror(title="Something Occured", message="There is an error, please try Again")
               # self.python = sys.executable
               # os.execl(self.python, self.python, *sys.argv)

    def progress2(self, visit1, email):
        for i in range(6):
            #try:
                if self.prog['value'] < 100:
                    self.update_idletasks()
                    self.prog['value'] += 20
                    time.sleep(1)
                else:
                    self.person = visit.VisitorDB()
                    self.visit_person = self.person.get_visitor(visit1)
                    self.qr = qr_generator.QRGenerate()
                    self.qr.genQrVisit(self.visit_person)
                    self.send = admicode_email.EmailSender()
                    self.send.send_qrVisit(self.visit_person[0], email)
                    self.destroy()
            #except:
               # messagebox.showerror(title="Something Occured", message="There is an error, please try Again")
               # self.python = sys.executable
               # os.execl(self.python, self.python, *sys.argv)


