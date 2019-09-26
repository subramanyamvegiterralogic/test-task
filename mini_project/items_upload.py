from tkinter import *
import mysql.connector
from tkinter import messagebox
import csv
from mini_project import database_connection, error_logger

db = database_connection.Database()
error_log = error_logger.ReportError()
class FileItemsUpload:
    def save_file_items_details_to_db(self,shop_id_txt, item_name_txt, item_amount_txt):
        try:
            db.connect_db()
            query = "SELECT * FROM add_item WHERE shop_id='{}' and item_name='{}'".format(shop_id_txt, item_name_txt)
            data = db.get_data_for_query(query)
            try:
                if len(data) < 1:
                    query = "INSERT INTO add_item VALUES ('{}','{}','{}')".format(shop_id_txt, item_name_txt,
                                                                                  item_amount_txt)
                    db.insert_or_update_query(query)
                else:
                    query = "UPDATE add_item SET item_name='{}', item_amount='{}' WHERE shop_id='{}'".format(
                        item_name_txt, item_amount_txt, shop_id_txt)
                    print(query)
                    db.insert_or_update_query(query)
            except Exception as e:
                error_log.report_error_log(__file__, e.__str__())
        except Exception as e:
            error_log.report_error_log(__file__, e.__str__())
        finally:
            db.disconnect_db()

    def read_csv_file_data(self):
        try:
            with open('add_items.csv', 'r') as f:
                data = csv.reader(f)
                for row in data:
                    try:
                        print(row)
                        self.save_file_items_details_to_db(row[0], row[1], row[2])
                    except Exception as e:
                        error_log.report_error_log(__file__, e.__str__())
                        continue
        except FileNotFoundError as fne:
            print(fne)
            error_log.report_error_log(__file__, fne.__str__())
        except FileExistsError as fee:
            print(fee)
            error_log.report_error_log(__file__, fee.__str__())
        except Exception as e:
            error_log.report_error_log(__file__, e.__str__())


def item_upload_process():
    try:
        window = Tk()
        window.title('Add/Update Shop Items')
        window.geometry('650x200')
        shop_id_lbl = Label(window, text='Shop ID : ', font=('Arial bold', 10))
        shop_id_lbl.grid(row=0, column=0)
        shop_id = Entry(window, width=50)
        shop_id.grid(row=0, column=3)

        item_name_lbl = Label(window, text='Item Name : ', font=('Arial bold', 10))
        item_name_lbl.grid(row=1, column=0)
        item_name = Entry(window, width=50)
        item_name.grid(row=1, column=3)

        item_amount_lbl = Label(window, text='Item Amount : ', font=('Arial bold', 10))
        item_amount_lbl.grid(row=2, column=0)
        item_amount = Entry(window, width=50)
        item_amount.grid(row=2, column=3)

        def show_custom_alert(message_text):
            messagebox.showwarning('Registaration', message_text)

        def save_store_items_details_to_db(shop_id_txt, item_name_txt, item_amount_txt):
            try:
                res = messagebox.askyesno('Add Item', 'Do you want to add this item to DB?')
                print(res)
                if res == True:
                    db.connect_db()
                    query = "SELECT * FROM add_item WHERE shop_id='{}' and item_name='{}'".format(shop_id_txt,
                                                                                                  item_name_txt)
                    data = db.get_data_for_query(query)
                    try:
                        if len(data) < 1:
                            query = "INSERT INTO add_item VALUES ('{}','{}','{}')".format(shop_id_txt,
                                                                                          item_name_txt.title(),
                                                                                          item_amount_txt)
                            db.insert_or_update_query(query)
                            messagebox.showinfo('Add Item', "Item Added Successfully...")
                        else:
                            query = "UPDATE add_item SET item_name='{}', item_amount='{}' WHERE shop_id='{}'".format(
                                item_name_txt, item_amount_txt, shop_id_txt)
                            db.insert_or_update_query(query)
                            messagebox.showinfo('Update Item', 'Item Data Updated Successfully...')
                    except Exception as e:
                        error_log.report_error_log(__file__, e.__str__())
                else:
                    messagebox.showerror('Add Item', 'User Cancelled Adding Item')
            except Exception as e:
                error_log.report_error_log(__file__, e.__str__())

        def add_item_clicked():
            try:
                shop_id_txt = shop_id.get()
                item_name_txt = item_name.get()
                item_amount_txt = item_amount.get()
                if len(shop_id_txt) < 1:
                    show_custom_alert('Shop ID Should Not be Empty')
                elif len(item_name_txt) < 1:
                    show_custom_alert('Item Name Should Not be Empty')
                elif len(item_amount_txt) < 1:
                    show_custom_alert('Item Amount Should Not be Empty')
                else:
                    save_store_items_details_to_db(shop_id_txt, item_name_txt, item_amount_txt)
            except Exception as e:
                error_log.report_error_log(__file__, e.__str__())

        btn = Button(window, text='Add Item', bg='green', fg='white', font=('Arial bold', 15),
                     command=add_item_clicked)
        btn.grid(row=7, column=1)
        window.mainloop()
    except Exception as e:
        error_log.report_error_log(__file__, e.__str__())

# upload = FileItemsUpload()
# upload.read_csv_file_data()
# item_upload_process()