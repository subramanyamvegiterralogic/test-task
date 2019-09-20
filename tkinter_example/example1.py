from tkinter import *
from tkinter import scrolledtext,messagebox
from tkinter.ttk import Combobox

window = Tk()
window.title('Mini Project')
window.geometry('1000x1000')
lbl = Label(window, text='Stores Application', font=('Arial bold',15))
lbl.grid(row=0, column=0)

# Entry Text
shop_name = Entry(window, width=50)
shop_name.grid(row=1, column=1)

# def label_active():
#     registered_notification.pack()
# def label_inactive():
#     registered_notification.pack_forget()

def register_clicked():
    # Text Display
    registered_notification = Label(window, text='Registered Successfully', font=('Arial bold', 15))
    registered_notification.grid(row=3,column=1)

# Button
btn = Button(window, text='Register Store', bg='black',fg='white',font=('Arial bold',15), command=register_clicked)
btn.grid(row=2, column=1)

# Drop Down
combo = Combobox(window)
combo['values'] = (1,2,3,4,5,'Text')
combo.current(5)
combo.grid(row = 4, column= 0)

#Check Box
check_state = BooleanVar()
check_state.set(True)
chk = Checkbutton(window, text='Choose', var=check_state)
chk.grid(row=5, column= 0)

check_state2 = IntVar()
check_state2.set(0) #Un Check
# #chk_state.set(1) #check
che2 = Checkbutton(window, text='Int Var', var=check_state2)
che2.grid(row=5, column=1)

# Radio Button
selected = IntVar()
def radio_clicked():
    print(selected.get())
rad1 = Radiobutton(window, text='Sedots',value=1, variable=selected)
rad2 = Radiobutton(window, text='Act Fiber',value=2, variable=selected)
rad3 = Radiobutton(window, text='Terralogic',value=3, variable=selected)
btn2 = Button(window, text='Choose', command=radio_clicked)
rad1.grid(row=6, column=0)
rad2.grid(row=6, column=1)
rad3.grid(row=6, column=2)
btn2.grid(row=6, column=4)

# Scroll ed text
txt = scrolledtext.ScrolledText(window, width=40, height=10)
txt.grid(row=7,column=0)
txt.insert(INSERT,'Hello Subramanyam')
# txt.delete(1.0, END)

# Message Box
def message_box_clicked():
    messagebox.showinfo('Registration','User Registered Successfully...!')
    messagebox.showwarning('Registration','Please Cross Check Details')
    messagebox.showerror('Registration','Invalid User Details')
    messagebox.askquestion('Ask Question', 'Do needful')
    messagebox.askyesno('Ask Yes No','Do needful')
    messagebox.askyesnocancel('Ask Yes No Cancel','Do Needful')
    messagebox.askokcancel('Ask OK Cancel','Do needful')
    messagebox.askretrycancel('Ask RETRT Cancel','Do needful')
btn3 = Button(window, text='Register Store', bg='white', fg='black', font=('Arial bold', 15),
                 command=message_box_clicked)
btn3.grid(row=8, column=1)

# Spin Box
spin = Spinbox(window, from_=0, to=250, width=10)
spin.grid(row=9,column=1)
# Limited values in Spin Box
spin2 = Spinbox(window, values=(3,7,18), width=10)
spin2.grid(row=9,column=2)
# Default value for Spin box
var = IntVar()
var.set(36)
spin3 = Spinbox(window, from_=0, to=100, width=5, textvariable=var)
spin3.grid(row=9,column=3)
window.mainloop()
