import tkinter as tk
from tkinter import *
from tkinter.tix import LabelEntry

from pyparsing import col


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('SCARA Viewer')
        self.geometry('1024x768')
        
class CanvasFrame(Frame):
    def __init__(self, container):
        super().__init__(container)
        
        #canvas
        self.canvas = Canvas(self, width=450, highlightbackground='black',highlightthickness=1)
        self.canvas.bind('<B1-Motion>',self.draw_line)
        self.canvas.bind('<Button-3>', self.clear_canvas)
        self.canvas.bind('<Motion>',self.update_coordsLabel)
        self.canvas.grid(column=0,row=0)
        
        #Preset Paths
        self.LineButton = Button(self, text="Add Line", width=10)
        self.LineButton.grid(row=1,column=0,pady=1)
        self.grid(row=0,column=0)
        
        self.labelFrames = Frame(self)
        
        self.xCoordLabel = LabelFrame(self.labelFrames, 'X')
        self.xCoordLabel.grid(row=0, column=0)
        self.yCoordLabel = LabelFrame(self.labelFrames, 'Y')
        self.yCoordLabel.grid(row=0,column=1)
        
        self.labelFrames.grid(row=2, column=0)
        
        
    def update_coordsLabel(self,event):
        self.xCoordLabel.label2.config(text=str(event.x))
        self.yCoordLabel.label2.config(text=str(event.y))
             
    # Define a function to draw the line between two points
    def draw_line(self, event, listener=None):
        x1=event.x
        y1=event.y
        x2=event.x
        y2=event.y
        print("x1: ", x1, "y1: ", y1, "x2: ", x2, "y2:" ,y2)
        # Draw an oval in the given co-ordinates
        self.canvas.create_polygon(x1,y1,x2,y2, outline='#f11', fill="black", width=3)
    
    def clear_canvas(self, event):
        self.canvas.delete('all')
        
    def add_line(self,event):
        if(str(event.type) == 'Hover'):
            self.canvas.old_coords = event.x, event.y
        elif(str(event.type) == 'ButtonRelease'):
            x, y = event.x, event.y
            x1, y1 = self.canvas.old_coords
            self.canvas.create_line(x,y,x1,y1)
            
class DiagFrame(Frame):
    def __init__(self,container):
        super().__init__(container,width=50, highlightbackground='red',highlightthickness=3)

        self.currentAngle1 = LabelFrame(self, 'End-x', '0.0')
        self.currentAngle2 = LabelFrame(self, 'End-y', '0.0')
        self.currentAngle3 = LabelFrame(self, 'End-z', '0.0')

        self.alpha = LabelFrame(self, 'Alpha', '0.0')
        self.beta = LabelFrame(self, 'Beta', '0.0')
        self.gamma = LabelFrame(self, 'Gamma', '0.0')

                
        self.currentAngle1.grid(row=1, column=0, padx=5, pady=5, ipadx=5, ipady=5)
        self.currentAngle2.grid(row=1, column=1, padx=5, pady=5, ipadx=5, ipady=5)
        self.currentAngle3.grid(row=1, column=2, padx=5, pady=5, ipadx=5, ipady=5)
        
        self.alpha.grid(row=2, column=0, padx=5, pady=5, ipadx=5, ipady=5)
        self.beta.grid(row=2, column=1, padx=5, pady=5, ipadx=5, ipady=5)
        self.gamma.grid(row=2, column=2, padx=5, pady=5, ipadx=5, ipady=5)

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
    label1 = None
    label2 = None
    
    def __init__(self,container, label1_text, label2_text='0.0'):
        super().__init__(container)

        self.label1 = Label(self,text=label1_text+':',justify='left')
        self.label2 = Label(self,text=label2_text)
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
            self.entry1 = EntryFrame(self,'Target-Alpha')
            self.entry2 = EntryFrame(self,'Target-Beta')
            self.entry3 = EntryFrame(self,'Target-Gamma')

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
        
        self.IKFrame        = KinematicFrame(self,'Inverse Kinematics')
        self.FKFrame        = KinematicFrame(self,'Forward Kinematics')
        self.DiagFrame      = DiagFrame(self)
        self.CanvasFrame    = CanvasFrame(self)

        self.IKFrame.grid(row=0, column=0)
        self.FKFrame.grid(row=1,column=0)
        self.DiagFrame.grid(row=2,column=0,pady=10)
        self.CanvasFrame.grid(row=0, column=1, pady=10)

        self.grid(row=0,column=0)

if __name__ == "__main__":
    app = App()
    frame = MainFrame(app)
    app.mainloop()