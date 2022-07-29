import tkinter as tk
from tkinter.ttk import Label
from turtle import left

root = tk.Tk()
root.geometry('1024x768')
root.title('Label Widget Demo')

# create labels
text_str = 'Forward Kinematics'
section_label = Label(root, text=text_str, font=("Helvitica", 12))
space_label = Label(root, text='\t\t\t\t\t\t\t\t\t\t\t\t')
endfx_label = Label(root, text='0.0', font=("Helvitica", 9))

# place on window
section_label.grid(column=1, row=0)
space_label.grid(column=0, row=0)
endfx_label.grid(column=1,row=1)

root.mainloop()