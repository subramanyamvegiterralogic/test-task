from tkinter import *
import mysql.connector
from tkinter import messagebox
import csv


def save_file_items_details_to_db(shop_id_txt, item_name_txt, item_amount_txt):
    try:
        my_connect = mysql.connector.connect(host= 'localhost', user='root', password='', database='mini_project')
        data_cursor = my_connect.cursor()
        query = "SELECT * FROM add_item WHERE shop_id='{}' and item_name='{}'".format(shop_id_txt,item_name_txt)
        data_cursor.execute(query)
        data = data_cursor.fetchall()
        try:
            if len(data)<1:
                query = "INSERT INTO add_item VALUES ('{}','{}','{}')".format(shop_id_txt, item_name_txt, item_amount_txt)
                print(query)
                data_cursor.execute(query)
            else:
                query = "UPDATE add_item SET item_name='{}', item_amount='{}' WHERE shop_id='{}'".format(item_name_txt, item_amount_txt,shop_id_txt)
                print(query)
                data_cursor.execute(query)
        except Exception as e:
            print(e)
        finally:
            my_connect.commit()
    except Exception as e:
        print(e)

def read_csv_file_data():
    try:
        with open('add_items.csv','r') as f:
            data = csv.reader(f)
            for row in data:
                try:
                    print(row)
                    save_file_items_details_to_db(row[0],row[1],row[2])
                except Exception as e:
                    print(e)
                    continue
    except FileNotFoundError as fne:
        print(fne)
    except FileExistsError as fee:
        print(fee)
    except Exception as e:
        print(e)
read_csv_file_data()

try:
    window = Tk()
    window.title('Add/Update Shop Items')
    window.geometry('600x500')
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
            res = messagebox.askyesno('Add Item','Do you want to add this item to DB?')
            print(res)
            if res == True:
                my_connect = mysql.connector.connect(host= 'localhost', user='root', password='', database='mini_project')
                data_cursor = my_connect.cursor()
                query = "SELECT * FROM add_item WHERE shop_id='{}' and item_name='{}'".format(shop_id_txt,item_name_txt)
                data_cursor.execute(query)
                data = data_cursor.fetchall()
                try:
                    if len(data)<1:
                        query = "INSERT INTO add_item VALUES ('{}','{}','{}')".format(shop_id_txt, item_name_txt.title(), item_amount_txt)
                        print(query)
                        data_cursor.execute(query)
                        messagebox.showinfo('Add Item', "Item Added Successfully...")
                    else:
                        query = "UPDATE add_item SET item_name='{}', item_amount='{}' WHERE shop_id='{}'".format(item_name_txt, item_amount_txt,shop_id_txt)
                        print(query)
                        data_cursor.execute(query)
                        messagebox.showinfo('Update Item','Item Data Updated Successfully...')
                except Exception as e:
                    print(e)
                finally:
                    my_connect.commit()
                    data_cursor.close()
                    my_connect.close()
            else:
                messagebox.showerror('Add Item', 'User Cancelled Adding Item')
        except Exception as e:
            print(e)
        pass


    def add_item_clicked():
        try:
            shop_id_txt = shop_id.get()
            item_name_txt = item_name.get()
            item_amount_txt = item_amount.get()
            if len(shop_id_txt)<1:
                show_custom_alert('Shop ID Should Not be Empty')
            elif len(item_name_txt)<1:
                show_custom_alert('Item Name Should Not be Empty')
            elif len(item_amount_txt) < 1:
                show_custom_alert('Item Amount Should Not be Empty')
            else:
                save_store_items_details_to_db(shop_id_txt, item_name_txt, item_amount_txt)
        except Exception as e:
            print(e)

    btn = Button(window, text='Add Item', bg='black', fg='white', font=('Arial bold', 15),
                 command=add_item_clicked)
    btn.grid(row=7, column=1)
    window.mainloop()
except Exception as e:
    print(e)

