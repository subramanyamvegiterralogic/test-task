from tkinter import *
from tkinter import messagebox
import csv, os
from mini_project import database_connection,my_logger
import pandas as pd

db = database_connection.Database()
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
                    db.insert_or_update_query(query)
            except Exception as e:
                my_logger.logging_operation(e.__str__())
        except Exception as e:
            my_logger.logging_operation( e.__str__())
        # finally:
        #     db.disconnect_db()

    def read_csv_file_data(self,file_name):
        try:
            file_name = 'input_files/'+file_name
            with open(str(file_name), 'r') as f:
                data = csv.reader(f)
                for row in data:
                    try:
                        self.save_file_items_details_to_db(row[0], row[1], row[2])
                    except Exception as e:
                        my_logger.logging_operation( e.__str__())
                        continue
                    # print(current_thread().getName())
                    # time.sleep(2)
        except FileNotFoundError as fne:
            print(fne)
            my_logger.logging_operation( fne.__str__())
        except FileExistsError as fee:
            print(fee)
            my_logger.logging_operation( fee.__str__())
        except Exception as e:
            my_logger.logging_operation( e.__str__())

    def read_excel_file_data(self, file_name):
        try:
            file_name = 'input_files/'+file_name
            data = pd.read_excel(os.path.abspath(file_name), sheet_name='Sheet1')
            shop_id = data['shop_id']
            item_name = data['item_name']
            item_amount = data['item_amount']
            for s_id, name, amount in zip(shop_id, item_name, item_amount):
                try:
                    id_flag, name_flag, amount_flag = False, False, False
                    if ((len(s_id.strip())>0 and s_id is not None)):
                        id_flag = True
                    if (len(name.strip())>0 and name is not None):
                        name_flag = True
                    if (str(amount).lower() !='nan'):
                        amount_flag = True
                    if (id_flag and name_flag and amount_flag):
                        self.save_file_items_details_to_db(s_id, name, amount)
                        # print(current_thread().getName())
                    else:
                        continue
                except Exception as e:
                    # print(e)
                    my_logger.logging_operation( e.__str__())
                    continue
                # time.sleep(2)
        except FileNotFoundError as fne:
            print(fne)
            my_logger.logging_operation( fne.__str__())
        except FileExistsError as fee:
            print(fee)
            my_logger.logging_operation( fee.__str__())
        except Exception as e:
            print(e)
            my_logger.logging_operation( e.__str__())

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
                        my_logger.logging_operation( e.__str__())
                else:
                    messagebox.showerror('Add Item', 'User Cancelled Adding Item')
            except Exception as e:
                my_logger.logging_operation( e.__str__())

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
                my_logger.logging_operation( e.__str__())

        btn = Button(window, text='Add Item', bg='green', fg='white', font=('Arial bold', 15),
                     command=add_item_clicked)
        btn.grid(row=7, column=1)
        window.mainloop()
    except Exception as e:
        my_logger.logging_operation( e.__str__())

# upload = FileItemsUpload()
# upload.read_csv_file_data()
# item_upload_process()