from tkinter import *
from tkinter import messagebox
import mysql.connector
from fpdf import FPDF
import random
import datetime
from mini_project import database_connection


db = database_connection.Database()
def generate_pdf(spacing):
    try:
        pdf = FPDF()
        pdf.set_font('Arial',size=12)
        pdf.add_page()
        col_width = pdf.w/4.5
        row_height = pdf.font_size
        pdf.cell(200, 5, 'V.L Super Market', ln=1, align='C')
        pdf.cell(200, 5, 'Thanks for Shopping', ln=2, align='C')
        pdf.cell(200, 5, 'Your Bill Details', ln=3, align='C')
        pdf.cell(200, 5, 'Total Amount : '+str(total_payable_amount), ln=4, align='C')
        for row in print_items_list:
            for item in row:
                pdf.cell(col_width,row_height*spacing, txt= item, border=1, align='C')
            pdf.ln(row_height*spacing)
        pdf.output('transaction.pdf')
        messagebox.showinfo('PDF Generation','PDF Generated Successfully...')
    except Exception as e:
        messagebox.showerror('PDF Generation','Print Generation Failed Please Try again...')
        print(e)
        # pass

try:
    items_prices = dict()
    items_quantity_cart = dict()
    window = Tk()
    window.title('Purchase Items')
    window.geometry('1000x1000')
    def read_items_details():
        try:
            db.connect_db()
            query = "SELECT a.item_name,a.item_amount FROM add_item as a LEFT JOIN shop_registration as r ON a.shop_id=r.shop_id WHERE r.shop_name ='V.L Super Market'"
            db_data = db.get_data_for_query(query)
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

            def save_customer_transaction_to_db(transaction_id, transaction_amount, transaction_date):
                try:
                    query = "INSERT INTO user_transaction (transaction_id, transaction_amount, transaction_date) VALUES ('{}','{}','{}')".format(transaction_id,transaction_amount,transaction_date)
                    db.insert_or_update_query(query)
                except Exception as e:
                    print(e)
                    generate_transaction_id()

            def generate_transaction_id():
                try:
                    transaction_id=''
                    for num in range(0,10):
                        transaction_id += str(random.randint(0,9))
                    print(transaction_id)
                    save_customer_transaction_to_db(transaction_id, total_payable_amount, datetime.datetime.now().strftime("%Y-%m-%d"))
                except Exception as e:
                    print(e)
            def print_clicked():
                generate_transaction_id()
                # generate_pdf(1)

            def submit_cart_items_clicked():
                total_cart_amount = 0
                global print_items_list
                print_items_list = [['Item Name', 'Item Price', 'Item Quantity', 'Amount']]
                if len(items_quantity_cart)<1:
                    messagebox.showerror('Submit Cart','Empty Cart Could not be processed')
                    return
                else:
                    for key in items_quantity_cart.keys():
                        temp = []
                        total_cart_amount += (int(items_quantity_cart[key]) * int(items_prices[key]))
                        temp.append(key)
                        temp.append(items_prices[key])
                        temp.append(items_quantity_cart[key])
                        temp.append(str(int(items_quantity_cart[key]) * int(items_prices[key])))
                        print_items_list.append(temp)
                global total_payable_amount
                total_payable_amount = total_cart_amount

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