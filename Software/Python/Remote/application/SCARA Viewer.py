from errno import ENOMSG
import tkinter as tk
from tkinter import *


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('SCARA Viewer')
        self.geometry('1024x768')

class DiagFrame(Frame):
    def __init__(self,container):
        super().__init__(container,width=50, highlightbackground='red',highlightthickness=3)

        self.currentAngle1 = LabelFrame(self, 'End-x', '0.0')
        self.currentAngle2 = LabelFrame(self, 'End-y', '0.0')
        self.currentAngle3 = LabelFrame(self, 'End-z', '0.0')

                self.currentAngle1 = LabelFrame(self, 'End-x', '0.0')
        self.currentAngle2 = LabelFrame(self, 'End-y', '0.0')
        self.currentAngle3 = LabelFrame(self, 'End-z', '0.0')

                
        self.currentAngle1.grid(row=1, column=0, padx=5, pady=5, ipadx=5, ipady=5)
        self.currentAngle2.grid(row=1, column=1, padx=5, pady=5, ipadx=5, ipady=5)
        self.currentAngle3.grid(row=1, column=2, padx=5, pady=5, ipadx=5, ipady=5)
        
        self.currentAngle1.grid(row=1, column=0, padx=5, pady=5, ipadx=5, ipady=5)
        self.currentAngle2.grid(row=1, column=1, padx=5, pady=5, ipadx=5, ipady=5)
        self.currentAngle3.grid(row=1, column=2, padx=5, pady=5, ipadx=5, ipady=5)

        self.grid(row=0, column=0)

class EntryFrame(Frame):
    def __init__(self,container,label_text):
        super().__init__(container)
    
        self.label = tk.Label(self, text=label_text+":")
        self.label.grid(row=0, column=0)
        self.grid(row=0, column=0)
                
        #textbox
        self.textbox = Entry(self, fg='black', font=(16), width=5)
        self.textbox.grid(row=0,column=1) 


class LabelFrame(Frame):
    def __init__(self,container, label1_text, label2_text):
        super().__init__(container)

        self.label1 = tk.Label(self,text=label1_text+':',justify='left')
        self.label2 = tk.Label(self,text=label2_text)
        self.label1.grid(row=0,column=0)
        self.label2.grid(row=0,column=1)
        self.grid(row=0, column=0)

class KinematicFrame(Frame):
    def __init__(self, container, label_text):
        super().__init__(container)

        self.label = tk.Label(self, text=label_text)
        if(label_text == 'Inverse Kinematics'):
            self.entry1 = EntryFrame(self,'Target-X')
            self.entry2 = EntryFrame(self,'Target-Y')
            self.entry3 = EntryFrame(self,'Target-Z')

            self.entry1.grid(row=1,column=0)
            self.entry2.grid(row=1,column=1)
            self.entry3.grid(row=1,column=2)
        else:
            self.entry1 = EntryFrame(self,'Alpha')
            self.entry2 = EntryFrame(self,'Beta')
            self.entry3 = EntryFrame(self,'Gamma')

            self.entry1.grid(row=1,column=0,ipadx=10)
            self.entry2.grid(row=1,column=1,ipadx=10)
            self.entry3.grid(row=1,column=2)

        self.setButton = tk.Button(self, width=10, text='Set')

        self.label.grid(row=0, column=1, padx=10, pady=10)


        self.setButton.grid(row=1,column=3, padx=10)
        self.grid(row=0, column=0)


class MainFrame(Frame):
    def __init__(self, container):
        super().__init__(container,highlightbackground='red',highlightthickness=3)
        
        self.IKFrame    = KinematicFrame(self,'Inverse Kinematics')
        self.FKFrame    = KinematicFrame(self,'Forward Kinematics')

        self.DiagFrame  = DiagFrame(self)

        self.IKFrame.grid(row=0, column=0)
        self.FKFrame.grid(row=1,column=0)
        self.DiagFrame.grid(row=2,column=0,pady=10)

        self.grid(row=0,column=0)

if __name__ == "__main__":
    app = App()
    frame = MainFrame(app)
    app.mainloop()