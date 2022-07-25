import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from unicodedata import name

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('SCARA Viewer')
        self.geometry('1024x768')

class MainFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        options = {'padx': 5, 'pady': 5}

        self.configureGrid()
        
        # label
        self.label = ttk.Label(self, text='Hello, Tkinter!')
        self.label.grid(column=2, row=2, sticky=tk.E, **options)

        # button
        self.button = ttk.Button(self, text='Click Me')
        self.button['command'] = self.button_clicked
        self.button.grid(column=0, row=0, sticky=tk.W, **options)

        # show the frame on the container
        self.pack(**options)
        
        
    def button_clicked(self):
        showinfo(title='information',message='Hello, Tkinter!')
    
    def configureGrid(self):
        self.columnconfigure(2, weight=1)
        #self.columnconfigure(1, weight=3)

if __name__ == "__main__":
    app = App()
    frame = MainFrame(app)
    app.mainloop()