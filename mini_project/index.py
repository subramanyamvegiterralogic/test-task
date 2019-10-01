from tkinter import *
from tkinter import messagebox
from mini_project import statisticks, shop_registration, display_item_details, error_logger, search_error_logs
from mini_project.items_upload import FileItemsUpload, item_upload_process
from threading import *
from datetime import datetime

class Index:
    def __init__(self):
        self.window = Tk()
        self.window.title('Shop Index Page')
        self.window.geometry('800x250')
        self.error_log = error_logger.ReportError()

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
            upload = FileItemsUpload()
            print('Before Calling CSV : ',datetime.now())
            Thread(target=upload.read_csv_file_data, name='CSV Thread').start()
            # upload.read_csv_file_data()
            print('After Calling CSV and Before Calling Excel : ',datetime.now())
            # upload.read_excel_file_data()
            Thread(target=upload.read_excel_file_data, name='XLS Thread').start()
            print('After Calling Excel : ',datetime.now())
            item_upload_process()
            self.window.quit()
        except Exception as e:
            self.error_log.report_error_log(__file__, e.__str__())


    def display_item_details_clicked(self):
        try:
            display = display_item_details.DisplayItemDetails()
            display.display_details()
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
