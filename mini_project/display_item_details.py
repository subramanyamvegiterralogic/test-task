from tkinter import *
from tkinter import messagebox
import mysql.connector
from fpdf import FPDF
import random
import datetime, threading
from mini_project import database_connection, working_with_mongo,send_email, error_logger
import functools


def display_item_details():
    emails_list = [#'v.subramanyam586@gmail.com',
                   'subramanyam.cse.86@gmail.com',
                   # 'vegisubramanyam@gmail.com',
                   # 'subramanyam.hyd.act@gmail.com',
                   'subramanyam.vegi@terralogic.com',
                   'python.developer.subramanyam@gmail.com']
    db = database_connection.Database()
    window = Tk()
    window.title('Purchase Items')
    window.geometry('900x900')
    error_log = error_logger.ReportError()

    def customer_details_required(func):
        def inner_validate():
            global customer_name, customer_email
            customer_name = customer_name_entry.get()
            customer_email = customer_email_entry.get()
            if re.fullmatch(r'\w+', customer_name) == None:
                messagebox.showwarning('Customer Validation', 'Please Enter Valid Customer Name')
            elif re.fullmatch(r'^[a-zA-Z0-9._]+\@[a-zA-Z0-9.]+\.[a-z]{2,3}$', customer_email) == None:
                messagebox.showwarning('Customer Validation', 'Please Enter Valid Customer Email')
            else:
                func()

        return inner_validate

    @customer_details_required
    def submit_cart_items_clicked():
        total_cart_amount = 0
        global print_items_list
        print_items_list = [['Item Name', 'Item Price', 'Item Quantity', 'Item Total Amount']]
        if len(items_quantity_cart) < 1:
            messagebox.showerror('Submit Cart', 'Empty Cart Could not be processed')
            return
        else:
            for key in items_quantity_cart.keys():
                temp = []
                total_cart_amount += (eval(items_quantity_cart[key]) * eval(items_prices[key]))
                temp.append(key)
                temp.append(items_prices[key])
                temp.append(items_quantity_cart[key])
                temp.append(str(eval(items_quantity_cart[key]) * eval(items_prices[key])))
                print_items_list.append(temp)
        global total_payable_amount
        total_payable_amount = total_cart_amount

        total_cart_amount_label = Label(window,
                                        text='Your Cart Amount is :₹ {}'.format(total_cart_amount),
                                        font=('Arial bold', 20))
        total_cart_amount_label.grid(row=25, column=3)
        print_bt = Button(window, text='Print', bg='orange', fg='white',
                          font=('Arial bold', 10),
                          command=print_clicked)
        print_bt.grid(row=26, column=3)


    @customer_details_required
    def add_to_cart_clicked():
        try:
            item_name_txt = item_name.get()
            item_quantity_txt = item_quantity.get()
            if len(item_name_txt) < 1:
                messagebox.showwarning('Add To Cart', 'Item Name Should Not be Empty')
                assert len(item_name_txt)<1, 'Item Name Should not be empty'
            elif item_name_txt not in items_prices:
                messagebox.showerror('Add To Cart',
                                     'Currently the Item is not availble, Please check later')
            elif len(item_quantity_txt) < 1:
                messagebox.showwarning('Add To Cart', 'Item Quantity Should Not be Empty')
                assert len(item_quantity_txt)<1, 'Item entity Should not be empty'
            elif int(item_quantity_txt) < 1:
                messagebox.showwarning('Add To Cart', 'Item Quantity Should not be 0 or less')
            else:
                items_quantity_cart[item_name_txt] = item_quantity_txt
                messagebox.showinfo('Add To Cart', 'Item Added to Cart Successfully...')
        except ValueError as e:
            messagebox.showerror('Add To Cart', 'Item Quantity should be in Number format only')
            error_log.report_error_log(__file__, e.__str__())
        except Exception as e:
            messagebox.showerror('Add To Cart', 'Something wnt wrong, Please try again later')
            error_log.report_error_log(__file__, e.__str__())

    def save_customer_transaction_to_db(transaction_id, transaction_amount, transaction_date):
        try:
            query = "INSERT INTO user_transaction (transaction_id, transaction_amount, transaction_date) VALUES ('{}','{}','{}')".format(
                transaction_id, transaction_amount, transaction_date)
            db.insert_or_update_query(query)
            return transaction_id
        except Exception as e:
            error_log.report_error_log(__file__, e.__str__())
            generate_transaction_id()

    def save_selected_items_to_mongo(transaction_id):
        try:
            mongo_ref = working_with_mongo.MongoOperations()
            mongo_data_list = []
            for item in print_items_list:
                if item[0] == 'Item Name' or item[1] == 'Item Price' or item[2] == 'Item Quantity' or item[
                    3] == 'Item Total Amount':
                    continue
                else:
                    local_dict = {}
                    local_dict['transaction_id'] = transaction_id
                    local_dict['item_name'] = item[0]
                    local_dict['item_price'] = item[1]
                    local_dict['item_quantity'] = item[2]
                    local_dict['item_total_amount'] = item[3]
                    mongo_data_list.append(local_dict)
            if len(mongo_data_list) < 1:
                messagebox.showerror('Mongo Error', 'No Transaction data is there to save')
            elif len(mongo_data_list) > 1:
                mongo_ref.insert_many_records_into_collection(mongo_data_list)
            else:
                mongo_ref.insert_one_record_into_collection(mongo_data_list[0])
        except Exception as e:
            error_log.report_error_log(__file__, e.__str__())

    def generate_transaction_id():
        try:
            global transaction_id
            transaction_id = ''
            for num in range(0, 10):
                transaction_id += str(random.randint(0, 9))
            # save_customer_transaction_to_db(transaction_id, total_payable_amount,
            #                                                              datetime.datetime.now().strftime("%Y-%m-%d"))
            threading.Thread(target=save_customer_transaction_to_db, args=(transaction_id, total_payable_amount,
                                                                           datetime.datetime.now().strftime(
                                                                               "%Y-%m-%d"),),
                             name='my_sql_thread').start()
            # save_selected_items_to_mongo(transaction_id)
            threading.Thread(target=save_selected_items_to_mongo, args=(transaction_id,),
                             name='mongo_db_thread').start()
        except Exception as e:
            error_log.report_error_log(__file__, e.__str__())

    def generate_pdf(spacing, transaction_id):
        try:
            pdf = FPDF()
            pdf.set_font('Arial', size=12)
            pdf.add_page()
            col_width = pdf.w / 4.5
            row_height = pdf.font_size
            pdf.cell(200, 5, 'V.L Super Market', ln=1, align='C')
            pdf.cell(200, 5, 'Thanks for Shopping', ln=2, align='C')
            pdf.cell(200, 5, 'Your Bill Details', ln=3, align='C')
            pdf.cell(200, 5, 'Total Amount : ' + str(total_payable_amount), ln=4, align='C')
            pdf.cell(200, 5, 'Transaction ID : ' + str(transaction_id), ln=5, align='C')
            for row in print_items_list:
                for item in row:
                    pdf.cell(col_width, row_height * spacing, txt=item, border=1, align='C')
                pdf.ln(row_height * spacing)
            file_name = 'pdf_files/' \
                        + datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S_') \
                        + transaction_id + '.pdf'
            pdf.output(file_name)
            messagebox.showinfo('PDF Generation', 'PDF Generated Successfully...')
            messagebox.showinfo('Transaction Successful',
                                'Your Transaction is Successful with transation number : {}, Thanks for Shopping, Please Visit Again'.format(
                                    transaction_id))
            mail = send_email.Transaction_email()
            mail.send_mail(customer_email,file_name, customer_name, transaction_id)
            # for to_email in emails_list:
            #     try:
            #         threading.Thread(target=mail.send_mail, args=(to_email, file_name),
            #                          name='sending_to_{}'.format(to_email)).start()
            #         print(threading.current_thread().getName())
            #         print(threading.enumerate())
            #     except Exception as e:
            #         error_log.report_error_log(__file__, e.__str__())
            #         continue
        except Exception as e:
            messagebox.showerror('PDF Generation', 'Print Generation Failed Please Try again...')
            error_log.report_error_log(__file__, e.__str__())

    def print_clicked():
        generate_transaction_id()
        generate_pdf(1, transaction_id)

    def read_items_details():
        try:
            db.connect_db()
            query = "SELECT a.item_name,a.item_amount FROM add_item as a LEFT JOIN shop_registration as r ON a.shop_id=r.shop_id WHERE r.shop_name ='V.L Super Market'"
            db_data = db.get_data_for_query(query)
            global items_prices
            items_prices = dict(db_data)
            i = 3

            for data in db_data:
                lb2 = Label(window, text='{}  ₹ {}/Kg'.format(data[0], data[1]), font=('bold', 9))
                lb2.grid(row=i, column=1)
                i += 1
            i += 3
            global item_name, item_quantity
            item_name_lbl = Label(window, text='Enter Item name and Quantity')
            item_name_lbl.grid(row=i, column=1)
            item_name = Entry(window, text='')
            item_name.grid(row=i, column=2)
            item_quantity = Entry(window, text='')
            item_quantity.grid(row=i, column=3)
            add_to_cart_bt = Button(window, text='Add To Cart', bg='orange', fg='white', font=('Arial bold', 10),
                                    command=add_to_cart_clicked)
            i += 3
            add_to_cart_bt.grid(row=i, column=1)
            submit_cart_item_bt = Button(window, text='Submit Cart Items', bg='orange', fg='white',
                                         font=('Arial bold', 10),
                                         command=submit_cart_items_clicked)
            submit_cart_item_bt.grid(row=i, column=3)
        except Exception as e:
            error_log.report_error_log(__file__, e.__str__())

    global items_quantity_cart
    items_quantity_cart = dict()
    customer_name_lbl = Label(window, text='Enter Customer Name ')
    customer_name_lbl.grid(row=0, column=1)
    customer_name_entry = Entry(window, text='')
    customer_name_entry.grid(row=0, column=2)
    customer_email_lbl = Label(window, text='Enter Customer Email')
    customer_email_lbl.grid(row=1, column=1)
    customer_email_entry = Entry(window, text='')
    customer_email_entry.grid(row=1, column=2)
    items_in_store_lbl = Label(window, text='Items Available in Store ', font=('bold', 15))
    items_in_store_lbl.grid(row=2, column=2)
    read_items_details()
    window.mainloop()