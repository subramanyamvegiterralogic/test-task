import datetime
from mini_project import error_logger
import os, re
from tkinter import *
from mini_project import error_logger
from tkinter import messagebox

class SearchErrorLogs:
    def __init__(self):
        self.window = Tk()
        self.window.title('Exceptions From The File')
        self.window.geometry('1300x600')
        self.error_log = error_logger.ReportError()

    def create_ui(self):
        try:
            # self.get_error_from_file()
            self.date_lbl = Label(self.window, text='Date To Search : ', font=('Arial bold', 10))
            self.date_lbl.grid(row=0, column=0)
            self.date_entry = Entry(self.window, width=50)
            self.date_entry.grid(row=0, column=3)

            self.time_lbl = Label(self.window, text='Time To Search : ', font=('Arial bold', 10))
            self.time_lbl.grid(row=1, column=0)
            self.time_entry = Entry(self.window, width=50)
            self.time_entry.grid(row=1, column=3)

            search_btn = Button(self.window, text='Search Error Logs', bg='Dark Red', fg='white', font=('Arial bold', 15),
                         command=self.get_error_from_log_file)
            search_btn.grid(row=2, column=1)

            self.window.mainloop()
        except Exception as e:
            self.error_log.report_error_log(__file__, e.__str__())

    def get_error_from_file(self):
        try:
            # search_date = input('Enter Date To Search \t:\t')
            # hour_of_the_day = input('Enter On which Hour You Want See Exceptions  : ')
            search_date = '2019-09-27'
            hour_of_the_day = '2019-09-27 10'
            end_time = '2019-09-27 11'
            error_dir_name = 'error_logs/'
            error_file_name = error_dir_name + search_date + "_log.txt"
            buffer = []
            with open(os.path.abspath(error_file_name), 'r') as read_f:
                for line in read_f:
                    if line.startswith(hour_of_the_day):
                        buffer.append(line)
                    elif line.startswith(end_time):
                        pass
            print(buffer)
            print(len(buffer))
        except Exception as e:
            print(e)

    def get_error_from_log_file(self):
        try:
            # search_date = input('Enter Date To Search \t:\t')
            # hour_of_the_day = input('Enter On which Hour You Want See Exceptions  : ')
            search_date = self.date_entry.get()
            hour_of_the_day = self.time_entry.get()
            if self.check_validation(search_date,hour_of_the_day):
                error_dir_name = 'error_logs/'
                error_file_name = error_dir_name + search_date + "_log.txt"
                with open(os.path.abspath(error_file_name), 'r') as read_f:
                    file_data = read_f.readlines()
                    re_genre = r'{} {}.*$'.format(search_date, hour_of_the_day)
                    regex_pattern = re.compile(re_genre)
                    new_list = list(filter(regex_pattern.match, file_data))
                    print(new_list)
                    i = 4
                    for item in new_list:
                        self.data_label = Label(self.window, text = item.replace('\n',''))
                        self.data_label.grid(row=i, column=0)
                        i += 1
        except Exception as e:
            print(e)
            self.data_label = Label(self.window, text='No File / Data Found')
            self.data_label.grid(row=4, column=0)
            messagebox.showinfo("No Data Found", 'File / Data Not Available')
            self.error_log.report_error_log(__file__, e.__str__())

    def check_validation(self, date , hour):
        if re.fullmatch(r'\d{4}-\d{1,2}-\d{1,3}',date) == None:
            messagebox.showwarning('Validation', 'Date format should be YYYY-MM-DD ex:2000-12-31')
            return False
        elif re.fullmatch(r'\d{2}', hour) == None:
            messagebox.showwarning('Validation', 'Time Should Enter in Hours and 24 hours format only Ex: 17')
            return False
        else:
            return True