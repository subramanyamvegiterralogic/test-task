from tkinter import *
from tkinter import messagebox
from mini_project import statisticks, shop_registration, display_item_details
from mini_project.items_upload import FileItemsUpload, item_upload_process

class Index:
    def __init__(self):
        self.window = Tk()
        self.window.title('Shop Index Page')
        self.window.geometry('650x200')

    def register_clicked(self):
        self.window.quit()
        register = shop_registration.ShopRegistration()
        register.create_ui()

    def items_upload_clicked(self):
        upload = FileItemsUpload()
        upload.read_csv_file_data()
        item_upload_process()

    def display_item_details_clicked(self):
        display = display_item_details.DisplayItemDetails()
        display.display_details()
        self.window.quit()

    def stitisticks_clicked(self):
        data_statisticks = statisticks.GraphicalRepresentation()
        data_statisticks.bar_chart_representation()

    def create_ui(self):
        register_btn = Button(self.window, text='Registration', bg='black', fg='white',font=('Arial Bold',15), command=self.register_clicked)
        register_btn.grid(row=0 ,column=0)
        items_upload_btn = Button(self.window, text='Items Upload', bg='green', fg='white',font=('Arial Bold',15), command=self.items_upload_clicked)
        items_upload_btn.grid(row=1 ,column=2)
        display_item_details_btn = Button(self.window, text='Items in Store', bg='orange', fg='white',font=('Arial Bold',15), command=self.display_item_details_clicked)
        display_item_details_btn.grid(row=2 ,column=3)
        statistics_btn = Button(self.window, text='Recent Statisticks', bg='red', fg='white',font=('Arial Bold',15), command=self.stitisticks_clicked)
        statistics_btn.grid(row=3 ,column=4)
        self.window.mainloop()
i = Index()
i.create_ui()
