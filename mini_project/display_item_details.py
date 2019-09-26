from tkinter import *
from tkinter import messagebox
import mysql.connector
from fpdf import FPDF
import random
import datetime
from mini_project import database_connection, working_with_mongo

class DisplayItemDetails:
    def __init__(self):
        self.db = database_connection.Database()
        self.window = Tk()
        self.window.title('Purchase Items')
        self.window.geometry('700x900')

    def submit_cart_items_clicked(self):
        total_cart_amount = 0
        global print_items_list
        print_items_list = [['Item Name', 'Item Price', 'Item Quantity', 'Item Total Amount']]
        if len(self.items_quantity_cart) < 1:
            messagebox.showerror('Submit Cart', 'Empty Cart Could not be processed')
            return
        else:
            for key in self.items_quantity_cart.keys():
                temp = []
                total_cart_amount += (int(self.items_quantity_cart[key]) * int(self.items_prices[key]))
                temp.append(key)
                temp.append(self.items_prices[key])
                temp.append(self.items_quantity_cart[key])
                temp.append(str(int(self.items_quantity_cart[key]) * int(self.items_prices[key])))
                print_items_list.append(temp)
        global total_payable_amount
        total_payable_amount = total_cart_amount

        self.total_cart_amount_label = Label(self.window,
                                        text='Your Cart Amount is :₹ {}'.format(total_cart_amount),
                                        font=('Arial bold', 20))
        self.total_cart_amount_label.grid(row=35, column=3)
        self.print_bt = Button(self.window, text='Print', bg='orange', fg='white',
                          font=('Arial bold', 10),
                          command=self.print_clicked)
        self.print_bt.grid(row=37, column=3)


    def add_to_cart_clicked(self):
        try:
            item_name_txt = self.item_name.get()
            item_quantity_txt = self.item_quantity.get()
            if len(item_name_txt) < 1:
                messagebox.showwarning('Add To Cart', 'Item Name Should Not be Empty')
            elif item_name_txt not in self.items_prices:
                messagebox.showerror('Add To Cart',
                                     'Currently the Item is not availble, Please check later')
            elif len(item_quantity_txt) < 1:
                messagebox.showwarning('Add To Cart', 'Item Quantity Should Not be Empty')
            elif int(item_quantity_txt) < 1:
                messagebox.showwarning('Add To Cart', 'Item Quantity Should not be 0 or less')
            else:
                self.items_quantity_cart[item_name_txt] = item_quantity_txt
                messagebox.showinfo('Add To Cart', 'Item Added to Cart Successfully...')
        except ValueError as e:
            messagebox.showerror('Add To Cart', 'Item Quantity should be in Number format only')
            print(e)
        except Exception as e:
            messagebox.showerror('Add To Cart', 'Something wnt wrong, Please try again later')
            print(e)

    def save_customer_transaction_to_db(self,transaction_id, transaction_amount, transaction_date):
        try:
            query = "INSERT INTO user_transaction (transaction_id, transaction_amount, transaction_date) VALUES ('{}','{}','{}')".format(
                transaction_id, transaction_amount, transaction_date)
            self.db.insert_or_update_query(query)
            return transaction_id
        except Exception as e:
            print(e)
            self.generate_transaction_id()

    def save_selected_items_to_mongo(self, transaction_id):
        try:
            mongo_ref = working_with_mongo.MongoOperations()
            mongo_data_list = []
            for item in print_items_list:
                if item[0] == 'Item Name' or item[1] == 'Item Price' or item[2] == 'Item Quantity' or item[3] == 'Item Total Amount':
                    continue
                else:
                    local_dict={}
                    local_dict['transaction_id']=transaction_id
                    local_dict['item_name']=item[0]
                    local_dict['item_price']=item[1]
                    local_dict['item_quantity']=item[2]
                    local_dict['item_total_amount']=item[3]
                    mongo_data_list.append(local_dict)
            if len(mongo_data_list)<1:
                messagebox.showerror('Mongo Error', 'No Transaction data is there to save')
            elif len(mongo_data_list)>1:
                mongo_ref.insert_many_records_into_collection(mongo_data_list)
            else:
                mongo_ref.insert_one_record_into_collection(mongo_data_list[0])
        except Exception as e:
            print(e)


    def generate_transaction_id(self):
        try:
            global transaction_id
            transaction_id=''
            for num in range(0, 10):
                transaction_id += str(random.randint(0, 9))
            self.save_customer_transaction_to_db(transaction_id, total_payable_amount,
                                            datetime.datetime.now().strftime("%Y-%m-%d"))
            self.save_selected_items_to_mongo(transaction_id)
        except Exception as e:
            print(e)


    def generate_pdf(self, spacing, transaction_id):
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
            file_name = 'pdf_files/'\
                        +datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S_')\
                        +transaction_id+'.pdf'
            pdf.output(file_name)
            messagebox.showinfo('PDF Generation', 'PDF Generated Successfully...')
            messagebox.showinfo('Transaction',
                                'Your Transaction is Successful with transation number : {}, Thanks for Shopping, Please Visit Again'.format(
                                    transaction_id))
        except Exception as e:
            messagebox.showerror('PDF Generation', 'Print Generation Failed Please Try again...')
            print(e)

    def print_clicked(self):
        self.generate_transaction_id()
        self.generate_pdf(1, transaction_id)

    def read_items_details(self):
        try:
            self.db.connect_db()
            query = "SELECT a.item_name,a.item_amount FROM add_item as a LEFT JOIN shop_registration as r ON a.shop_id=r.shop_id WHERE r.shop_name ='V.L Super Market'"
            db_data = self.db.get_data_for_query(query)
            self.items_prices = dict(db_data)
            i = 0

            for data in db_data:
                lb2 = Label(self.window, text='{}  ₹ {}/Kg'.format(data[0], data[1]), font=('bold', 9))
                lb2.grid(row=i, column=1)
                i += 1
            i += 3
            self.item_name_lbl = Label(self.window, text='Enter Item name and Quantity')
            self.item_name_lbl.grid(row=i, column=1)
            self.item_name = Entry(self.window, text='')
            self.item_name.grid(row=i, column=2)
            self.item_quantity = Entry(self.window, text='')
            self.item_quantity.grid(row=i, column=3)
            self.add_to_cart_bt = Button(self.window, text='Add To Cart', bg='orange', fg='white', font=('Arial bold', 10),
                                    command=self.add_to_cart_clicked)
            i += 3
            self.add_to_cart_bt.grid(row=i, column=1)
            self.submit_cart_item_bt = Button(self.window, text='Submit Cart Items', bg='orange', fg='white',
                                         font=('Arial bold', 10),
                                         command=self.submit_cart_items_clicked)
            self.submit_cart_item_bt.grid(row=i, column=3)
        except Exception as e:
            print(e)

    def display_details(self):
        try:
            self.items_prices = dict()
            self.items_quantity_cart = dict()
            self.read_items_details()
            self.window.mainloop()
        except Exception as e:
            print(e)