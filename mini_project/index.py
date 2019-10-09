from tkinter import *
from tkinter import messagebox
from mini_project import statisticks, shop_registration, display_item_details, error_logger, search_error_logs
from mini_project.items_upload import FileItemsUpload, item_upload_process
from threading import *
import os,time
from datetime import datetime,date,timedelta

class Index:

    def wait_for_tomorrow(self):
        tomorrow = datetime.replace(datetime.now()+timedelta(days=1), hour=15, minute=11, second=0)
        delta = tomorrow-datetime.now()
        return delta.seconds

    def return_pattern(self, pattern):
        return re.compile(pattern)

    def read_files_from_input_dir(self):
        try:
            cwd = os.getcwd()
            files_dir = str(cwd)+'/input_files'
            while True:
                if os.path.exists(files_dir):
                    files_list = os.listdir(files_dir)
                    pattern = r'^{}.*(.xls|.csv)'.format(datetime.now().strftime('%Y-%m-%d'))
                    regex_pattern = self.return_pattern(pattern)
                    required_files_list = list(filter(regex_pattern.match, files_list))
                    upload = FileItemsUpload()
                    for file in required_files_list:
                        if (re.fullmatch(r'^.*.csv$', file)) != None:
                            Thread(target=upload.read_csv_file_data, args=(file,), name='CSV Thread').start()
                        elif (re.fullmatch(r'^.*.xls$', file)) != None:
                            Thread(target=upload.read_excel_file_data, args=(file,), name='XLS Thread').start()
                else:
                    print('Not Found')
                time.sleep(12*60*60)
        except Exception as e:
            print(e)

    def delete_old_files_from_input_dir(self):
        cwd = os.getcwd()
        files_dir = str(cwd)+'/input_files/'
        while True:
            if os.path.exists(files_dir):
                files_list = os.listdir(files_dir)
                for file in files_list:
                    if re.match('^(?!{}).*'.format(datetime.now().strftime('%Y-%m-%d')),file):
                        file_full_name = str(files_dir+file)
                        os.remove(file_full_name)
                        # print('Deleted File Name : ',file_full_name)
            else:
                print('DIR Does niot exist')
            time.sleep(self.wait_for_tomorrow())

    def delete_old_logs(self):
        cwd = os.getcwd()
        log_dir = str(cwd)+'/error_logs'
        while True:
            one_week_older = datetime.today()-timedelta(days=7)
            if os.path.exists(log_dir):
                files_list = os.listdir(log_dir)
                for item in files_list:
                    date_obj = datetime.strptime(item.split('_')[0],'%Y-%m-%d')
                    if date_obj < one_week_older:
                        file_name = log_dir+'/'+item
                        if os.path.exists(file_name):
                            os.remove(file_name)
                            print('File Removed : ',file_name)
                    else:
                        pass
            else:
                print("Dir Doesn't Exist")
            time.sleep(self.wait_for_tomorrow())

    def delete_sent_pdfs(self):
        cwd = os.getcwd()
        pdf_files_dir = str(cwd)+'/pdf_files'
        while True:
            if os.path.exists(pdf_files_dir):
                file_list = os.listdir(pdf_files_dir)
                pattern = r'\d{4}-\d{2}-\d{2}.*$'
                regex_pattern = re.compile(pattern)
                updated_list = list(filter(regex_pattern.match, file_list))
                for item in updated_list:
                    if item.startswith(str(current_date)):
                        pass
                    else:
                        file_name = pdf_files_dir + '/' + item
                        if os.path.exists(file_name):
                            os.remove(file_name)
                            print('File Removed : ',file_name)
            else:
                print("Dir Doesn't Exist")
            time.sleep(self.wait_for_tomorrow())

    def __init__(self):
        global current_date
        current_date = date.today()
        self.window = Tk()
        self.window.title('Shop Index Page')
        self.window.geometry('800x250')
        self.error_log = error_logger.ReportError()
        Thread(target=self.delete_old_logs, name='delete_old_logs').start()
        Thread(target=self.delete_sent_pdfs, name='delete_sent_pdfs').start()
        Thread(target=self.delete_old_files_from_input_dir, name='delete_old_files_from_input_dir').start()
        Thread(target=self.read_files_from_input_dir, name='read_files_from_input_dir').start()

    def register_clicked(self):
        try:
            self.window.quit()
            register = shop_registration.ShopRegistration()
            register.create_ui()
            self.window.quit()
        except Exception as e:
            self.error_log.report_error_log(__file__, e.__str__())

    def items_upload_clicked(self):
        try:

            # upload.read_csv_file_data()
            # upload.read_excel_file_data()
            item_upload_process()
            self.window.quit()
        except Exception as e:
            self.error_log.report_error_log(__file__, e.__str__())


    def display_item_details_clicked(self):
        try:
            display_item_details.display_item_details()
            self.window.quit()
        except Exception as e:
            self.error_log.report_error_log(__file__, e.__str__())

    def stitisticks_clicked(self):
        try:
            data_statisticks = statisticks.GraphicalRepresentation()
            # data_statisticks.bar_chart_representation()
            Thread(target=data_statisticks.bar_chart_representation, name='bar_thread').start()
            Thread(target=data_statisticks.statistic_line_representation, name='line_thread').start()
            Thread(target=data_statisticks.statistic_pie_chart_representation, name='pie_chart_thread').start()
            # Thread(target=data_statisticks.statistic_tree_map(), name='tree_thread').start()
            # self.window.quit()
        except Exception as e:
            self.error_log.report_error_log(__file__, e.__str__())
    def error_logs_clicked(self):
        try:
            search_error = search_error_logs.SearchErrorLogs()
            search_error.create_ui()
            self.window.quit()
        except Exception as e:
            self.error_log.report_error_log(__file__, e.__str__())

    def create_ui(self):
        try:
            register_btn = Button(self.window, text='Registration', bg='black', fg='white',font=('Arial Bold',15), command=self.register_clicked)
            register_btn.grid(row=0 ,column=0)
            items_upload_btn = Button(self.window, text='Items Upload', bg='green', fg='white',font=('Arial Bold',15), command=self.items_upload_clicked)
            items_upload_btn.grid(row=1 ,column=2)
            display_item_details_btn = Button(self.window, text='Items in Store', bg='orange', fg='white',font=('Arial Bold',15), command=self.display_item_details_clicked)
            display_item_details_btn.grid(row=2 ,column=3)
            statistics_btn = Button(self.window, text='Recent Statisticks', bg='pink', fg='white',font=('Arial Bold',15), command=self.stitisticks_clicked)
            statistics_btn.grid(row=3 ,column=4)
            statistics_btn = Button(self.window, text='Error Logs', bg='dark red', fg='white', font=('Arial Bold', 15), command=self.error_logs_clicked)
            statistics_btn.grid(row=4, column=5)
            self.window.mainloop()
        except Exception as e:
            self.error_log.report_error_log(__file__, e.__str__())
i = Index()
i.create_ui()
