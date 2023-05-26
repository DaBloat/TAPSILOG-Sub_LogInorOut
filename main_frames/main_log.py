import tkinter as tk
from tkinter import ttk
import tkcalendar as cal
from tkinter import messagebox
from qr_generate_scanner import scanner
from databases import logs_database as ldb
import time


class MainLog(tk.Frame):
    def __init__(self, container):
        super().__init__(container, highlightbackground='black', highlightthickness=2)
        self.cnt = 1
        self.rundb = ldb.Logs()
        self.configure(width=980, height=720, bg='#EAC4A3')
        self.grid_propagate(False)
        self.grid(row=0, column=1)
        self.button = tk.Button(self, text='LOG')
        self.button.grid(row=0, column=0)

        self.frame = tk.Frame(self, bg='#EAC4A3')
        self.frame.grid(row=0, column=0, padx=10, pady=10)

        self.photo = tk.PhotoImage(file='graphics/log_logo_circle.png')
        self.photo2 = self.photo.subsample(3, 3)
        self.logo_at_side = tk.Label(self.frame, image=self.photo2, bg='#EAC4A3')
        self.logo_at_side.grid(row=0, column=0)

        self.reg_label = tk.Label(self.frame, text="LOG OF ENTRY & EXIT", font=('Arial Black', 20),
                                  bg='#EAC4A3')
        self.reg_label.grid(row=0, column=1)

        self.frame2 = tk.Frame(self, bg='#EAC4A3')
        self.frame2.grid(row=1, column=0)

        self.text_label = tk.Label(self.frame2, text='Scan for: ', font=('Arial Black', 15), bg='#EAC4A3')
        self.text_label.grid(row=0, column=0)

        self.entrance_pic = tk.PhotoImage(file='graphics/record_entry.png')
        self.entrance_pic2 = self.entrance_pic.subsample(3, 3)
        self.entrance = tk.Button(self.frame2, image=self.entrance_pic2, bg='#EAC4A3', bd=0, activebackground='#EAC4A3', command=self.scan_entry)
        self.entrance.grid(row=0, column=1)

        self.exit_pic = tk.PhotoImage(file='graphics/record_exit.png')
        self.exit_pic2 = self.exit_pic.subsample(3, 3)
        self.exit = tk.Button(self.frame2, image=self.exit_pic2, bg='#EAC4A3', bd=0, activebackground='#EAC4A3', command=self.scan_exit)
        self.exit.grid(row=0, column=2)

        for widgets in self.frame2.winfo_children():
            widgets.grid_configure(padx=10, pady=10)

        self.frame3 = tk.LabelFrame(self, bg='#EAC4A3', text='Log Enter/Exit')
        self.frame3.grid(row=2, column=0)

        self.table = ttk.Treeview(self.frame3, columns=('Name', 'Contact No', 'Date', 'In', 'Out', 'Type'), show='headings', height=15)
        self.table.column("# 1", anchor='center', width=100)
        self.table.column("# 2", anchor='center', width=100)
        self.table.column("# 3", anchor='center', width=200)
        self.table.column("# 4", anchor='center', width=200)
        self.table.column("# 5", anchor='center', width=200)
        self.table.column("# 6", anchor='center', width=100)
        self.table.heading('Name', text='Name')
        self.table.heading('Contact No', text='Contact No')
        self.table.heading('Date', text='Date')
        self.table.heading('In', text='In')
        self.table.heading('Out', text='Out')
        self.table.heading('Type', text='Type')
        self.table.grid(row=0, column=0, padx=5, pady=5)

        self.scroll = ttk.Scrollbar(self.frame3, orient=tk.VERTICAL, command=self.table.yview)
        self.table.configure(yscroll=self.scroll.set)
        self.scroll.grid(row=0, column=1, sticky='ns')

        self.frame4 = tk.Frame(self, bg='#EAC4A3')
        self.frame4.grid(row=3, column=0)

        self.save_pic = tk.PhotoImage(file='graphics/save_button.png')
        self.save_pic2 = self.save_pic.subsample(2, 2)

        self.save_button = tk.Button(self.frame4, image=self.save_pic2, bd=0, background='#EAC4A3', activebackground='#EAC4A3', command=self.save_logs)
        self.save_button.grid(row=1, column=0)

        self.print_pic0 = tk.PhotoImage(file='graphics/print_button.png')
        self.print_pic02 = self.print_pic0.subsample(2, 2)

        self.print_button = tk.Button(self.frame4, image=self.print_pic02, bd=0, background='#EAC4A3', activebackground='#EAC4A3', command=self.print_logs)
        self.print_button.grid(row=1, column=1)

    def scan_entry(self):
        try:
            self.run = scanner.QrScanner()
            self.run.run_scan()
            self.run.release_cam()
            self.today_date = time.strftime("%m-%d-%Y")

            if int(self.run.get_value_list()[0]) == 0:
                if self.today_date == self.run.get_value_list()[6]:
                    messagebox.showinfo(title='Done', message=f"The user {self.run.get_value_list()[1]} is now registered to the log as a {self.run.get_value_list()[7]}!")
                    self.table.insert(parent='', index='end', values=(self.run.get_value_list()[1], self.run.get_value_list()[4], self.run.get_value_list()[6], self.run.get_value_list()[8], '', self.run.get_value_list()[7]))
                    self.table.grid()
                else:
                    messagebox.showerror(title='QR_ expired', message=f'This QR is expired in the day {self.run.get_value_list()[6]}')

            elif int(self.run.get_value_list()[0]) == 1:
                if self.today_date == self.run.get_value_list()[8]:
                    messagebox.showinfo(title='Done',
                                    message=f"The user {self.run.get_value_list()[1]} is now registered to the log as a {self.run.get_value_list()[9]}!")
                    self.table.insert(parent='', index='end', values=(
                    self.run.get_value_list()[1], self.run.get_value_list()[5], self.run.get_value_list()[8],
                    self.run.get_value_list()[10], '', self.run.get_value_list()[9]))
                    self.table.grid()
                else:
                    messagebox.showerror(title='QR_ expired', message=f'This QR is expired in the day {self.run.get_value_list()[8]}')

        except AttributeError:
            pass

        except ValueError:
            messagebox.showerror(title='Invalid Qr',
                                 message="You're Scanned QR is not generated by the T.A.P.S.I.Log System")
        except IndexError:
            messagebox.showerror(title='Invalid Qr', message="You're Scanned QR is not generated by the T.A.P.S.I.Log System")

    def scan_exit(self):
        try:
            self.selected = self.table.focus()
            self.past = self.table.item(self.selected, 'values')
            self.run = scanner.QrScanner()
            self.run.run_scan()
            self.run.release_cam()

            if int(self.run.get_value_list()[0]) == 0:
                if self.past[0] == self.run.get_value_list()[1]:
                    self.table.item(self.selected, values=(self.run.get_value_list()[1], self.run.get_value_list()[4], self.run.get_value_list()[6], self.past[3], self.run.get_value_list()[8], self.run.get_value_list()[7]))
                else:
                    messagebox.showerror(title='Error', message=f"Name {self.run.get_value_list()[0]} doesn't match!")

            elif int(self.run.get_value_list()[0]) == 1:
                if self.past[0] == self.run.get_value_list()[1]:
                    self.table.item(self.selected, values=(
                    self.run.get_value_list()[1], self.run.get_value_list()[5], self.run.get_value_list()[8],
                    self.past[3], self.run.get_value_list()[10], self.run.get_value_list()[9]))
                else:
                    messagebox.showerror(title='Error', message=f"Name {self.run.get_value_list()[1]} doesn't match!")

        except AttributeError:
            pass
        except IndexError:
            messagebox.showerror(title='Somethings wrong!', message=f"Please check if the user {self.run.get_value_list()[1]} is successfully selected")


    def save_logs(self):
        for items in self.table.get_children():
            self.values = self.table.item(items, 'values')
            if self.values[4] == '':
                messagebox.showerror(title="Can't be saved", message=f"User {self.values[0]} values needs to be complete to be saved")
            else:
                self.rundb.add_log(self.values[0], self.values[1], self.values[2], self.values[3], self.values[4], self.values[5])
                messagebox.showinfo(title='SUCCESSFUL', message=f'The user {self.values[0]} is Successfully Saved!')
                self.table.delete(items)

    def merge_logs(self):
        pass

    def print_logs(self):
        if self.cnt < 2:
            self.cnt = +1
            self.frameTOP = tk.Toplevel()

            self.bg_model = tk.Label(self.frameTOP, bg='#EAC4A3')
            self.bg_model.place(x=0, y=0, relwidth=1, relheight=1)

            self.frame_in_TOP = tk.Frame(self.frameTOP, bg='#EAC4A3', highlightbackground='black', highlightthickness=2)
            self.frame_in_TOP.grid(row=0, column=0)

            self.control_frames = CalendarFrame(self.frame_in_TOP)

            self.frame_in_label = tk.LabelFrame(self.frameTOP, text='Log of Entry/Exit', bg='#EAC4A3')
            self.frame_in_label.grid(row=0, column=1)

            self.tablePrint = ttk.Treeview(self.frame_in_label, columns=('Name', 'Contact No', 'Date', 'In', 'Out', 'Type'),
                                      show='headings', height=10)
            self.tablePrint.column("# 1", anchor='center', width=100)
            self.tablePrint.column("# 2", anchor='center', width=100)
            self.tablePrint.column("# 3", anchor='center', width=200)
            self.tablePrint.column("# 4", anchor='center', width=200)
            self.tablePrint.column("# 5", anchor='center', width=200)
            self.tablePrint.column("# 6", anchor='center', width=100)
            self.tablePrint.heading('Name', text='Name')
            self.tablePrint.heading('Contact No', text='Contact No')
            self.tablePrint.heading('Date', text='Date')
            self.tablePrint.heading('In', text='In')
            self.tablePrint.heading('Out', text='Out')
            self.tablePrint.heading('Type', text='Type')
            self.tablePrint.grid(row=0, column=0, padx=5, pady=5)

            self.scroll = ttk.Scrollbar(self.frame_in_label, orient=tk.VERTICAL, command=self.tablePrint.yview)
            self.tablePrint.configure(yscroll=self.scroll.set)
            self.scroll.grid(row=0, column=1, sticky='ns')

            self.get_datapic = tk.PhotoImage(file='graphics/get_data_button.png')
            self.get_datapic2 = self.get_datapic.subsample(2, 2)

            self.get_data_button = tk.Button(self.control_frames, image=self.get_datapic2, bg='#EAC4A3', bd=0, activebackground='#EAC4A3',
                                             command=self.get_data)
            self.get_data_button.grid(row=2, column=0)

            self.print_pic = tk.PhotoImage(file='graphics/print_pdf_button.png')
            self.print_pic2 = self.print_pic.subsample(2, 2)

            self.print_btn = tk.Button(self.control_frames, image=self.print_pic2, bg='#EAC4A3', bd=0, activebackground='#EAC4A3', command=self.print_all)
            self.print_btn.grid(row=3, column=0)

            self.frameTOP.mainloop()

        else:
            messagebox.showerror(title='Limited Number of Tabs', message='The Windows is already opened')

    def get_data(self):
        self.del_all()
        self.date_Una = self.control_frames.calendar.get_date()
        if len(self.rundb.show_all_by_dates(self.date_Una)) > 0:
            for values in self.rundb.show_all_by_dates(self.date_Una):
                self.tablePrint.insert(parent='', index='end',
                                       values=(values[0], values[1], values[2], values[3], values[4], values[5]))
                self.tablePrint.grid()
        else:
            messagebox.showinfo(title="No log records", message=f'{self.date_Una} has no log records')
            self.frameTOP.destroy()


    def print_all(self):
            pass

    def del_all(self):
        for values in self.tablePrint.get_children():
            self.tablePrint.delete(values)



class CalendarFrame(tk.LabelFrame):
    def __init__(self, main_frame):
        super().__init__(main_frame, bg='#EAC4A3', width=280, height=300)
        self.main_frame = main_frame
        self.grid_propagate(False)
        self.pack_propagate(False)
        self.grid(row=0, column=0)

        self.text_label = tk.Label(self, text='Select the date here:', font=('Comic Sans', 10, 'bold'), bg='#EAC4A3')
        self.text_label.grid(row=0, column=0, padx=60, sticky='nw')

        self.calendar = cal.Calendar(self, selectmode='day', date_pattern="mm-dd-y", year=int(time.strftime('%Y')),
                                     month=int(time.strftime('%m')), day=int(time.strftime('%d')))
        self.calendar.grid(row=1, column=0, sticky='nw', padx=10)











