import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import os, sys
import time
from databases import admin_database as admin
db = admin.AdminDatabase()


class AdminSupp(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.geometry('700x600+100+100')
        self.title('Admin Support')
        self.resizable(False, False)
        self.bg = tk.Label(self, bg='#EAC4A3')
        self.bg.place(x=0, y=0, relwidth=1, relheight=1)
        self.frame1 = FrameOne(self)


class FrameOne(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg='#EAC4A3')
        self.grid(row=0, column=0)

        self.parent = parent

        self.admin_selection = tk.LabelFrame(self, text='ADMIN SUPPORT', font=('Comic San', 20, 'bold'), bg='#EAC4A3')
        self.admin_selection.grid(row=1, column=0, padx=90, pady=20)

        self.admin_supp1 = tk.PhotoImage(file='graphics/admin_supp1.png')

        self.admin_edit = tk.Button(self.admin_selection, image=self.admin_supp1, bg='#EAC4A3', bd=0, activebackground='#EAC4A3', command=self.run_frame2)
        self.admin_edit.grid(row=0, column=0)

        self.admin_supp2 = tk.PhotoImage(file='graphics/admin_supp2.png')

        self.admin_pass = tk.Button(self.admin_selection, image=self.admin_supp2, bg='#EAC4A3', bd=0, activebackground='#EAC4A3', command=self.run_frame3)
        self.admin_pass.grid(row=1, column=0)

        self.admin_supp3 = tk.PhotoImage(file='graphics/admin_supp3.png')

        self.admin_contact = tk.Button(self.admin_selection, image=self.admin_supp3, bg='#EAC4A3', bd=0, activebackground='#EAC4A3', command=self.run_frame4)
        self.admin_contact.grid(row=2, column=0)

        self.admin_supp4 = tk.PhotoImage(file='graphics/admin_supp4.png')

        self.admin_show = tk.Button(self.admin_selection, image=self.admin_supp4, bg='#EAC4A3', bd=0, activebackground='#EAC4A3', command=self.run_frame5)
        self.admin_show.grid(row=3, column=0)

        self.logo = tk.PhotoImage(file='graphics/Logo-cut.png')
        self.logo2 = self.logo.subsample(2, 2)

        self.logo = tk.Button(self, image=self.logo2, bg='#EAC4A3', bd=0, activebackground='#EAC4A3')
        self.logo.grid(row=0, column=0)

    def run_frame2(self):
        self.destroy()
        self.run = FrameTwo(self.parent)

    def run_frame3(self):
        self.destroy()
        self.run = FrameThree(self.parent)

    def run_frame4(self):
        self.destroy()
        self.run = FrameFour(self.parent)

    def run_frame5(self):
        self.destroy()
        self.run = FrameFive(self.parent)


class FrameTwo(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg='#EAC4A3')
        self.grid(padx=10, pady=10)

        self.parent = parent

        self.back_pic = tk.PhotoImage(file='graphics/back_buttons.png')
        self.back_pic2 = self.back_pic.subsample(5, 5)

        self.backButton = tk.Button(self, image=self.back_pic2, bg='#EAC4A3',
                                    activebackground='#EAC4A3', bd=0, command=self.back)
        self.backButton.grid(row=0, column=0, sticky='nw')

        self.frame_name_two = tk.LabelFrame(self, text="Find Account", font=("Arial Black", 10, 'bold'),
                                            bg='#EAC4A3')
        self.frame_name_two.grid(row=1, column=0, padx=210)

        # Label
        self.title2 = tk.Label(self.frame_name_two,
                               text='PLEASE INPUT YOUR 5 DIGIT CODE: ',
                               font=("Arial Black", 10, 'bold'), bg='#EAC4A3')
        self.title2.grid(row=0, column=0)

        # Entry
        self.entry_code = tk.Entry(self.frame_name_two)
        self.entry_code.grid(row=1, column=0)

        self.find = tk.PhotoImage(file='graphics/find_btn.png')
        self.find2 = self.find.subsample(2, 2)

        self.button_code = tk.Button(self.frame_name_two, image=self.find2, bg='#EAC4A3',
                                    activebackground='#EAC4A3', bd=0, command=self.check_code)
        self.button_code.grid(row=2, column=0)

        self.frame_name_side = tk.LabelFrame(self, text="ACCOUNT DETAILS",
                                            font=("Arial Black", 10, 'bold'), bg='#EAC4A3')
        self.frame_name_side.grid(row=2, column=0)

        self.frame_label_name = tk.Label(self.frame_name_side,
                                         text=f'NAME: ',
                                         bg='#EAC4A3', font=("Arial Black", 10, 'bold'))
        self.frame_label_name.grid(row=0, column=0)

        self.frame_label_user = tk.Label(self.frame_name_side,
                                         text=f'Username: ',
                                         bg='#EAC4A3', font=("Arial Black", 10, 'bold'))
        self.frame_label_user.grid(row=0, column=1)

        self.frame_label_email = tk.Label(self.frame_name_side,
                                          text=f'Email: ',
                                          bg='#EAC4A3', font=("Arial Black", 10, 'bold'))
        self.frame_label_email.grid(row=1, column=0)

        self.frame_label_pass = tk.Label(self.frame_name_side,
                                         text=f'Password: * digit pass',
                                         bg='#EAC4A3', font=("Arial Black", 10, 'bold'))
        self.frame_label_pass.grid(row=1, column=1)

        for widgets in self.frame_name_side.winfo_children():
            widgets.grid_configure(padx=10, pady=10)

        for widgets in self.frame_name_two.winfo_children():
            widgets.grid_configure(padx=5, pady=5)


    def back(self):
        self.destroy()
        self.run = FrameOne(self.parent)

    def check_code(self):
        self.value = db.search_admin_sec(self.entry_code.get())
        try:
            self.frame_label_name.configure(text=f'NAME: {self.value[2]}')
            self.frame_label_user.configure(text=f'Username: {self.value[0]}')
            self.frame_label_email.configure(text=f'Email: {self.value[3]}')
            self.frame_label_pass.configure(text=f'Password: {len(self.value[1])} digit pass')
        except TypeError:
            messagebox.showinfo(title="Code not match", message='No code match to your inputted code')


class FrameThree(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.grid(padx=10, pady=10)

        self.back_pic = tk.PhotoImage(file='graphics/back_buttons.png')
        self.back_pic2 = self.back_pic.subsample(5, 5)

        self.backButton = tk.Button(self, image=self.back_pic2, bg='#EAC4A3',
                                    activebackground='#EAC4A3', bd=0, command=self.back)
        self.backButton.grid(row=0, column=0, sticky='nw')

    def back(self):
        self.destroy()
        self.run = FrameOne(self.parent)


class FrameFour(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg='#EAC4A3')
        self.grid(padx=10, pady=10)
        self.parent = parent

        self.back_pic = tk.PhotoImage(file='graphics/back_buttons.png')
        self.back_pic2 = self.back_pic.subsample(5, 5)

        self.backButton = tk.Button(self, image=self.back_pic2, bg='#EAC4A3',
                                    activebackground='#EAC4A3', bd=0, command=self.back)
        self.backButton.grid(row=0, column=0, sticky='nw')

        self.frame_name_two = tk.LabelFrame(self, text="Find Account", font=("Arial Black", 10, 'bold'),
                                            bg='#EAC4A3')
        self.frame_name_two.grid(row=1, column=0, padx=210)

        # Label
        self.title2 = tk.Label(self.frame_name_two,
                               text='PLEASE INPUT YOUR 5 DIGIT CODE: ',
                               font=("Arial Black", 10, 'bold'), bg='#EAC4A3')
        self.title2.grid(row=0, column=0)

        # Entry
        self.entry_code = tk.Entry(self.frame_name_two)
        self.entry_code.grid(row=1, column=0)

        self.find = tk.PhotoImage(file='graphics/find_btn.png')
        self.find2 = self.find.subsample(2, 2)

        self.button_code = tk.Button(self.frame_name_two, image=self.find2, bg='#EAC4A3',
                                     activebackground='#EAC4A3', bd=0, command=self.check_code)
        self.button_code.grid(row=2, column=0)

        self.frame_name_side = tk.LabelFrame(self, text="UPDATE ACCOUNT DETAILS",
                                             font=("Arial Black", 10, 'bold'), bg='#EAC4A3')
        self.frame_name_side.grid(row=2, column=0)

        self.frame_label_name = tk.Label(self.frame_name_side,
                                         text=f'NAME: ',
                                         bg='#EAC4A3', font=("Arial Black", 10, 'bold'))
        self.frame_label_name.grid(row=0, column=0)

        self.frame_name_entry = tk.Entry(self.frame_name_side)
        self.frame_name_entry.grid(row=0, column=1)

        self.frame_label_user = tk.Label(self.frame_name_side,
                                         text=f'Username: ',
                                         bg='#EAC4A3', font=("Arial Black", 10, 'bold'))
        self.frame_label_user.grid(row=0, column=2)

        self.frame_user_entry = tk.Entry(self.frame_name_side)
        self.frame_user_entry.grid(row=0, column=3)

        self.frame_label_email = tk.Label(self.frame_name_side,
                                          text=f'Email: ',
                                          bg='#EAC4A3', font=("Arial Black", 10, 'bold'))
        self.frame_label_email.grid(row=1, column=0)

        self.frame_email_entry = tk.Entry(self.frame_name_side)
        self.frame_email_entry.grid(row=1, column=1)

        self.frame_label_pass = tk.Label(self.frame_name_side,
                                         text=f'Password: ',
                                         bg='#EAC4A3', font=("Arial Black", 10, 'bold'))
        self.frame_label_pass.grid(row=1, column=2)

        self.frame_pass_entry = tk.Entry(self.frame_name_side, show='*')
        self.frame_pass_entry.grid(row=1, column=3)

        self.upd = tk.PhotoImage(file='graphics/update_btn.png')
        self.upd2 = self.upd.subsample(2, 2)

        self.up_btn = tk.Button(self, image=self.upd2, bd=0, activebackground='#EAC4A3', bg='#EAC4A3', command=self.update)
        self.up_btn.grid(row=3, column=0)

        self.del1 = tk.PhotoImage(file='graphics/delete_btn.png')
        self.del2 = self.del1.subsample(2, 2)

        self.del_btn = tk.Button(self, image=self.del2, bd=0, activebackground='#EAC4A3', bg='#EAC4A3',
                                command=self.delete)
        self.del_btn.grid(row=4, column=0)

        for widgets in self.frame_name_side.winfo_children():
            widgets.grid_configure(padx=10, pady=10)

        for widgets in self.frame_name_two.winfo_children():
            widgets.grid_configure(padx=5, pady=5)

        for widgets in self.winfo_children():
            widgets.grid_configure(pady=10)

    def back(self):
        self.destroy()
        self.run = FrameOne(self.parent)

    def check_code(self):
        self.value = db.search_admin_sec(self.entry_code.get())
        try:
            self.frame_name_entry.insert(0, self.value[2])
            self.frame_user_entry.insert(0, self.value[0])
            self.frame_email_entry.insert(0, self.value[3])
            self.frame_pass_entry.insert(0, self.value[1])

        except TypeError:
            messagebox.showinfo(title="Code not match", message='No code match to your inputted code')

    def update(self):
        if self.entry_code.get() == '':
            messagebox.showerror(title='NO CODE', message='No Security code registered to Update')
        else:
            if messagebox.askyesno(title='ARE YOU SURE?', message='Pressing yes will proceed to update'):
                self.person = admin.UpdateAdmin(self.frame_user_entry.get(), self.frame_pass_entry.get(), self.frame_name_entry.get(), self.frame_email_entry.get())
                self.update_all = db.update_admin(self.entry_code.get(), self.person)
                messagebox.showinfo(title="UPDATE SUCCESSFULLY", message='Updated Successfully! Program will restart')
                self.python = sys.executable
                os.execl(self.python, self.python, *sys.argv)

    def delete(self):
        if self.entry_code.get() == '':
            messagebox.showerror(title='NO CODE', message='No Security code registered to Update')
        else:
            if messagebox.askyesno(title='ARE YOU SURE?', message='Pressing yes will proceed to delete'):
                db.delete_admin(self.entry_code.get())
                messagebox.showinfo(title="DELETE SUCCESSFULLY", message='Updated Successfully! Program will restart')
                self.python = sys.executable
                os.execl(self.python, self.python, *sys.argv)


class FrameFive(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg='#EAC4A3')
        self.grid(padx=10, pady=10)

        self.parent = parent

        self.back_pic = tk.PhotoImage(file='graphics/back_buttons.png')
        self.back_pic2 = self.back_pic.subsample(5, 5)

        self.backButton = tk.Button(self, image=self.back_pic2, bg='#EAC4A3',
                                    activebackground='#EAC4A3', bd=0, command=self.back)
        self.backButton.grid(row=0, column=0, sticky='nw')

        self.frame_name_two = tk.LabelFrame(self, text="Verify", font=("Arial Black", 10, 'bold'),
                                            bg='#EAC4A3')
        self.frame_name_two.grid(row=1, column=0, padx=210)

        # Label
        self.title2 = tk.Label(self.frame_name_two,
                               text='PLEASE INPUT THE ADMIN PASSWORD: ',
                               font=("Arial Black", 10, 'bold'), bg='#EAC4A3')
        self.title2.grid(row=0, column=0)

        # Entry
        self.entry_code = tk.Entry(self.frame_name_two, show='*')
        self.entry_code.grid(row=1, column=0)

        self.submit = tk.PhotoImage(file='graphics/submit_btn.png')
        self.submit2 = self.submit.subsample(2, 2)

        self.submit_btn = tk.Button(self.frame_name_two, image=self.submit2, bg='#EAC4A3', bd=0, activebackground='#EAC4A3', command=self.run_table)
        self.submit_btn.grid(row=2, column=0)

        for widget in self.frame_name_two.winfo_children():
            widget.grid_configure(padx=10, pady=10)

        self.frame_name_all = tk.LabelFrame(self, text="ALL Account", font=("Comic Sans", 10, 'bold'),
                                            bg='#EAC4A3')
        self.frame_name_all.grid(row=2, column=0)

        self.entry_table = tk.Label(self.frame_name_all, text='THIS PORTION IS LOCKED AND ONLY AVAILABLE TO THE DEVELOPERS', font=("Arial Black", 10, 'bold'), bg="#EAC4A3")
        self.entry_table.grid(row=0, column=0, pady=10, padx=10)

    def run_table(self):
        if self.entry_code.get() == 'WTC91169420':
            for widget in self.frame_name_all.winfo_children():
                widget.destroy()

            self.run = FrameLoading(self.frame_name_all)

            self.run.progress()

            self.namelist = []
            self.un_list = []
            self.email_list = []

            for i in db.show_all_admin():
                self.namelist.append(i[2])
                self.un_list.append(i[0])
                self.email_list.append(i[3])

            self.table = ttk.Treeview(self.frame_name_all, columns=('Username', 'Name', 'Email'), show='headings')
            self.table.heading('Username', text='Username')
            self.table.heading('Name', text='Name')
            self.table.heading('Email', text='Email')
            for j in range(len(db.show_all_admin())):
                self.table.insert(parent='', index=0,
                                  values=((self.un_list)[j], (self.namelist)[j], (self.email_list)[j]))
            self.table.grid(row=1, column=0)

        else:
            messagebox.showerror(title='Wrong Code', message='Your code is invalid')

    def back(self):
        self.destroy()
        self.run = FrameOne(self.parent)


class FrameLoading(tk.Frame):
    def __init__(self, container):
        super().__init__(container, bg='#EAC4A3')
        self.grid(row=0, column=0, padx=10, pady=10)

        self.text = tk.Label(self, text="DEVELOPER CODE GRANTED- NOW LOADING", bg='#EAC4A3')
        self.text.grid(row=0, column=0)

        self.prog = ttk.Progressbar(self, orient='horizontal', length=300, mode='determinate', value=0)
        self.prog.grid(row=1, column=0)

        for widget in self.winfo_children():
            widget.grid_configure(pady=5, padx=50)

    def progress(self):
        for i in range(6):
            if self.prog['value'] < 100:
                self.update_idletasks()
                self.prog['value'] += 20
                time.sleep(1)
            else:
                self.destroy()







