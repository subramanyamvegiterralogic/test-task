from tkinter import *
from tkinter import messagebox
import mysql.connector

try:
    items_prices = dict()
    items_quantity_cart = dict()
    window = Tk()
    window.title('Purchase Items')
    window.geometry('1000x1000')
    def read_items_details():
        try:
            my_connect = mysql.connector.connect(host='localhost', database='mini_project', user='root', password='')
            cursor = my_connect.cursor()
            query = "SELECT a.item_name,a.item_amount FROM add_item as a LEFT JOIN shop_registration as r ON a.shop_id=r.shop_id WHERE r.shop_name ='V.L Super Market'"
            cursor.execute(query)
            db_data = cursor.fetchall()
            items_prices = dict(db_data)
            i=0

            def add_to_cart_clicked():
                try:
                    item_name_txt = item_name.get()
                    item_quantity_txt = item_quantity.get()
                    if len(item_name_txt)<1:
                        messagebox.showwarning('Add To Cart','Item Name Should Not be Empty')
                    elif item_name_txt not in items_prices:
                        messagebox.showerror('Add To Cart', 'Currently the Item is not availble, Please check later')
                    elif len(item_quantity_txt)<1:
                        messagebox.showwarning('Add To Cart', 'Item Quantity Should Not be Empty')
                    elif int(item_quantity_txt)<1:
                        messagebox.showwarning('Add To Cart', 'Item Quantity Should not be 0 or less')
                    else:
                        items_quantity_cart[item_name_txt]=item_quantity_txt
                        messagebox.showinfo('Add To Cart','Item Added to Cart Successfully...')
                except ValueError as e:
                    messagebox.showerror('Add To Cart', 'Item Quantity should be in Number format only')
                    print(e)
                except Exception as e:
                    messagebox.showerror('Add To Cart', 'Something wnt wrong, Please try again later')
                    print(e)

            def print_clicked():
                pass

            def submit_cart_items_clicked():
                total_cart_amount = 0
                if len(items_quantity_cart)<1:
                    messagebox.showerror('Submit Cart','Empty Cart Could not be processed')
                    return
                else:
                    for key in items_quantity_cart.keys():
                        total_cart_amount += (int(items_quantity_cart[key]) * int(items_prices[key]))
                total_cart_amount_label = Label(window,text='Your Cart Amount is :₹ {}'.format(total_cart_amount),font=('Arial bold', 20))
                total_cart_amount_label.grid(row=35, column=3)
                print_bt = Button(window, text='Print', bg='black', fg='white',
                                             font=('Arial bold', 10),
                                             command=print_clicked)
                print_bt.grid(row=37, column=3)

            for data in db_data:
                lb2 = Label(window, text='{}  ₹ {}/Kg'.format(data[0],data[1]), font=('bold', 9))
                lb2.grid(row=i, column=1)
                i += 1
            i +=3
            item_name_lbl = Label(window,text='Enter Item name and Quantity')
            item_name_lbl.grid(row=i,column=1)
            item_name = Entry(window, text='')
            item_name.grid(row=i, column=2)
            item_quantity = Entry(window, text='')
            item_quantity.grid(row=i, column=3)
            add_to_cart_bt = Button(window, text='Add To Cart', bg='black', fg='white', font=('Arial bold', 10),
                         command=add_to_cart_clicked)
            i += 3
            add_to_cart_bt.grid(row=i, column=1)
            submit_cart_item_bt = Button(window, text='Submit Cart Items', bg='black', fg='white', font=('Arial bold', 10),
                                    command=submit_cart_items_clicked)
            submit_cart_item_bt.grid(row=i, column=3)
        except Exception as e:
            print(e)
    read_items_details()

        # print(shop_name_i.get())
    window.mainloop()
except Exception as e:
    print(e)