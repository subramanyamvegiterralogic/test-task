import mysql.connector
from tkinter import *
from tkinter import messagebox
from mini_project import database_connection, error_logger
import re

class ShopRegistration:
    def __init__(self):
        self.db = database_connection.Database()
        self.window = Tk()
        self.window.title('Shop Registration')
        self.window.geometry('650x200')
        self.error_log = error_logger.ReportError()

    def save_store_details_to_db(self, shop_name_txt, shop_owner_name_txt, shop_id_txt, shop_gst_number_txt,
                                 shop_address_txt,  contact_number_txt):
        try:
            res = messagebox.askquestion('Registration', 'Do want to Register Store ?')
            if res == 'yes':
                self.db.connect_db()
                query = 'SELECT * FROM shop_registration WHERE shop_id="' + shop_id_txt + '"'
                row_data = self.db.get_data_for_query(query)
                if len(row_data) > 0:
                    messagebox.showwarning('Registration', 'User Already Registered')
                else:
                    try:
                        query = 'INSERT INTO shop_registration (shop_name,shop_owner_name,shop_id,gst_number,address,contact_number) VALUES ("{}","{}","{}","{}","{}","{}")'.format(
                            shop_name_txt, shop_owner_name_txt, shop_id_txt, shop_gst_number_txt,
                            shop_address_txt, contact_number_txt)
                        self.db.insert_or_update_query(query)
                        self.db.disconnect_db()
                        messagebox.showinfo('Registration', 'User Registered Successfully...!')
                    except Exception as e:
                        self.error_log.report_error_log(__file__, e.__str__())
            else:
                messagebox.showerror('Registration', 'Registration Cancelled by User')

        except Exception as e:
            messagebox.showerror('Registration', 'Registration Failed Please Try again later')
            self.error_log.report_error_log(__file__, e.__str__())

    def show_custom_alert(self,message_text):
        messagebox.showwarning('Registaration', message_text)

    def message_box_clicked(self):
        shop_name_txt = self.shop_name.get()
        shop_owner_name_txt = self.shop_owner_name.get()
        shop_id_txt = self.shop_id.get()
        shop_gst_number_txt = self.shop_gst_number.get()
        shop_address_txt = self.shop_address.get()
        contact_number_txt = self.contact_number.get()

        if len(shop_name_txt) < 1:
            self.show_custom_alert('Shop Name Should Not be Empty')
        elif len(shop_owner_name_txt) < 1:
            self.show_custom_alert('Shop Owner Name Should Not be Empty')
        elif len(shop_id_txt) < 1:
            self.show_custom_alert('Shop ID Should Not be Empty')
        elif re.fullmatch('\w{15}',shop_gst_number_txt) == None:#len(shop_gst_number_txt) < 1:
            self.show_custom_alert('Please Enter Valid Shop GST number')
        elif len(shop_address_txt) < 1:
            self.show_custom_alert('Shop Address Should Not be Empty')
        elif re.fullmatch('(0|91)?[6-9][0-9]{9}',contact_number_txt) == None:#len(contact_number_txt) < 1:
            self.show_custom_alert('Please Enter Valid Contact Number')
        else:
            self.save_store_details_to_db(shop_name_txt, shop_owner_name_txt, shop_id_txt, shop_gst_number_txt,
                                     shop_address_txt, contact_number_txt)

    def create_ui(self):
        try:
            self.shop_name_lbl = Label(self.window, text='Shop Name : ', font=('Arial bold', 10))
            self.shop_name_lbl.grid(row=0, column=0)
            self.shop_name = Entry(self.window, width=50)
            self.shop_name.grid(row=0, column=3)

            self.shop_owner_name_lbl = Label(self.window, text='Shop Owner Name : ', font=('Arial bold', 10))
            self.shop_owner_name_lbl.grid(row=1, column=0)
            self.shop_owner_name = Entry(self.window, width=50)
            self.shop_owner_name.grid(row=1, column=3)

            self.shop_id_lbl = Label(self.window, text='Shop ID : ', font=('Arial bold', 10))
            self.shop_id_lbl.grid(row=2, column=0)
            self.shop_id = Entry(self.window, width=50)
            self.shop_id.grid(row=2, column=3)

            self.shop_gst_number_lbl = Label(self.window, text='Shop GST Number : ', font=('Arial bold', 10))
            self.shop_gst_number_lbl.grid(row=3, column=0)
            self.shop_gst_number = Entry(self.window, width=50)
            self.shop_gst_number.grid(row=3, column=3)

            self.shop_address_lbl = Label(self.window, text='Shop Address : ', font=('Arial bold', 10))
            self.shop_address_lbl.grid(row=4, column=0)
            self.shop_address = Entry(self.window, width=50)
            self.shop_address.grid(row=4, column=3)

            self.contact_number_lbl = Label(self.window, text='Contact Number : ', font=('Arial bold', 10))
            self.contact_number_lbl.grid(row=5, column=0)
            self.contact_number = Entry(self.window, width=50)
            self.contact_number.grid(row=5, column=3)

            btn = Button(self.window, text='Register Store', bg='black', fg='white', font=('Arial bold', 15),
                         command=self.message_box_clicked)
            btn.grid(row=7, column=1)

            self.window.mainloop()
        except Exception as e:
            self.error_log.report_error_log(__file__, e.__str__())
# shop_register = ShopRegistration()
# shop_register.create_ui()