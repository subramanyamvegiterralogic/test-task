from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import ttk,filedialog, Menu
window = Tk()
window.title('GUI Example')
window.geometry('1000x700')

# Progress Bar
bar1 = Progressbar(window, length=780)
bar1['value'] = 100
bar1.grid(row=1, column=3)

style = ttk.Style()
style.theme_use('default')
style.configure('black.Horizontal.TProgressbar', background='black')
bar = Progressbar(window, length=200, style = 'black.Horizontal.TProgressbar')
bar['value']=70
bar.grid(row=2, column=2)

# File Dialogue
# file = filedialog.askopenfilename(filetypes=(("Text Files","*.txt"),("All Files","*.*")))

#Menu Bar
menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label = 'New')
new_item.add_separator()
new_item.add_command(label='Edit')
menu.add_cascade(label='File', menu=new_item)
window.config(menu=menu)
window.mainloop()