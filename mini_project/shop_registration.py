import mysql.connector
from tkinter import *
from tkinter import messagebox
from mini_project import database_connection

try:
    db = database_connection.Database()
    window = Tk()
    window.title('Shop Registration')
    window.geometry('600x500')

    shop_name_lbl = Label(window, text='Shop Name : ', font=('Arial bold',10))
    shop_name_lbl.grid(row=0, column=0)
    shop_name = Entry(window, width=50)
    shop_name.grid(row=0, column=3)

    shop_owner_name_lbl = Label(window, text='Shop Owner Name : ', font=('Arial bold',10))
    shop_owner_name_lbl.grid(row=1, column=0)
    shop_owner_name = Entry(window, width=50)
    shop_owner_name.grid(row=1, column=3)

    shop_id_lbl = Label(window, text='Shop ID : ', font=('Arial bold',10))
    shop_id_lbl.grid(row=2, column=0)
    shop_id = Entry(window, width=50)
    shop_id.grid(row=2, column=3)

    shop_gst_number_lbl = Label(window, text='Shop GST Number : ', font=('Arial bold',10))
    shop_gst_number_lbl.grid(row=3, column=0)
    shop_gst_number = Entry(window, width=50)
    shop_gst_number.grid(row=3, column=3)

    shop_address_lbl = Label(window, text='Shop Address : ', font=('Arial bold',10))
    shop_address_lbl.grid(row=4, column=0)
    shop_address = Entry(window, width=50)
    shop_address.grid(row=4, column=3)

    contact_number_lbl = Label(window, text='Contact Number : ', font=('Arial bold',10))
    contact_number_lbl.grid(row=5, column=0)
    contact_number = Entry(window, width=50)
    contact_number.grid(row=5, column=3)


    def save_store_details_to_db(shop_name_txt, shop_owner_name_txt, shop_id_txt, shop_gst_number_txt, shop_address_txt,
                                 contact_number_txt):
        try:
            res = messagebox.askquestion('Registration', 'Do want to Register Store ?')
            if res == 'yes':
                db.connect_db()
                query = 'SELECT * FROM shop_registration WHERE shop_id="' + shop_id_txt + '"'
                row_data = db.get_data_for_query(query)
                if len(row_data)>0:
                    messagebox.showwarning('Registration', 'User Already Registered')
                else:
                    try:
                        query = 'INSERT INTO shop_registration (shop_name,shop_owner_name,shop_id,gst_number,address,contact_number) VALUES ("{}","{}","{}","{}","{}","{}")'.format(shop_name_txt,shop_owner_name_txt,shop_id_txt,shop_gst_number_txt,shop_address_txt,contact_number_txt)
                        db.insert_or_update_query(query)
                        db.disconnect_db()
                        messagebox.showinfo('Registration','User Registered Successfully...!')
                    except Exception as e:
                        print(e)
            else:
                messagebox.showerror('Registration', 'Registration Cancelled by User')

        except Exception as e:
            messagebox.showerror('Registration','Registration Failed Please Try again later')
            print(e)


    def show_custom_alert(message_text):
        messagebox.showwarning('Registaration', message_text)
    def message_box_clicked():
        shop_name_txt = shop_name.get()
        shop_owner_name_txt = shop_owner_name.get()
        shop_id_txt = shop_id.get()
        shop_gst_number_txt = shop_gst_number.get()
        shop_address_txt = shop_address.get()
        contact_number_txt = contact_number.get()

        if len(shop_name_txt)<1:
            show_custom_alert('Shop Name Should Not be Empty')
        elif len(shop_owner_name_txt)<1:
            show_custom_alert('Shop Owner Name Should Not be Empty')
        elif len(shop_id_txt) < 1:
            show_custom_alert('Shop ID Should Not be Empty')
        elif len(shop_gst_number_txt)<1:
            show_custom_alert('Shop GST number Should Not be Empty')
        elif len(shop_address_txt)<1:
            show_custom_alert('Shop Address Should Not be Empty')
        elif len(contact_number_txt)<1:
            show_custom_alert('Contact Number Should Not be Empty')
        else:
            save_store_details_to_db(shop_name_txt, shop_owner_name_txt, shop_id_txt, shop_gst_number_txt, shop_address_txt, contact_number_txt)
    btn = Button(window, text='Register Store', bg='black',fg='white',font=('Arial bold',15), command=message_box_clicked)
    btn.grid(row=7, column=1)
    window.mainloop()
except Exception as e:
    print(e)