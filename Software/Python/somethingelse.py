import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


def return_pressed(event):
    print('Return key pressed.')


def log(event):
    print(event)


root = tk.Tk()

btn = ttk.Button(root, text='Save', command=lambda: filedialog.asksaveasfile())
btn.bind('<Return>', return_pressed)
btn.bind('<Return>', log, add='+')


btn.focus()
btn.pack(expand=True)

root.mainloop()