import serial as ser
from time import sleep
from utils import NewtonRaph
import math
import numpy as np
import random as rand
"""
Handles Serial Communication between SCARA arm and this remote software
"""
class Communications():
    
    __comms = None
    __port_name = None
    __baud_rate = None
    
    
    """
    Store information for communication, must call setup to start connection
    """
    def __init__(self, port_name, baud_rate):
        self.__port_name = port_name
        self.__baud_rate = baud_rate
        
    """
    Sets up the Serial 
    """
    def setup(self):
        self.__comms=ser.Serial(self.__port_name, self.__baud_rate)
    
    """
    Close the Serial Connection allow 0.5s for commands to finish executing
    """
    def close(self):
        sleep(0.5)
        self.__comms.close()
    
    """
    Sends Message to MCU
    """    
    def send_message(self, message):
        if(message[-1]!='\n'):
            message=message+'\n'
        self.__comms.write(message.encode('utf-8'))    

    """
    Recieves Message from MCU
    """
    def recieve_message(self, num_bytes=50):
        if(self.__comms.in_waiting>0):
            return self.__ser.readline(num_bytes).decode('utf-8')
        else:
            return None

"""
Inverse Kinematics Solver
"""        
class IKSolver():
    
    __theSolution=[]
    __pathSol = []
    __joints=[]
    __invJac_CB = None
    __F_CB = None
    
    theTarget=[]
    max_iter = 1000
    error_margin = 1e-2
    
    
    def __init__(self, Joints, Target, invJac_CB=None, F_CB=None):
        self.__joints=Joints
        self.theTarget=Target
        if(invJac_CB == None or F_CB == None):
            self.__invJac_CB = self.invJac
            self.__F_CB = self.F

    def __makeGuess(self):
        return np.vstack((math.pi*rand.uniform(0,2), math.pi*rand.uniform(0,2)))
    
    def invJac(self,x):
        #print("length: ", self.__joints)
        #print("x: ", x)
        
        row1 = [(-self.__joints[0].lengthTo*math.sin(x[0])-self.__joints[1].lengthTo*math.sin(x[0]+x[1])),(-self.__joints[1].lengthTo*math.sin(x[0]+x[1]))]
        
        row2 = [(self.__joints[0].lengthTo*math.cos(x[0])+self.__joints[1].lengthTo*math.cos(x[0]+x[1])),(self.__joints[1].lengthTo*math.cos(x[0]+x[1]))]
        ret = np.array(row1)
        ret1 = row2
        theResult = np.vstack((ret, ret1))
    
        try:
            np.linalg.inv(theResult)
        except np.linalg.LinAlgError:
            print("Divided by 0, makeing newGuess")
            guess = self.__makeGuess()
            return self.invJac(guess)
        
        return np.linalg.inv(theResult)    
    
    """
    To make this and invJac more versitile allow these as class parameters so we can use them as user defined callbacks 
    """
    def F(self, x):     

        row1 = abs(self.__joints[0].lengthTo*math.cos(x[0])+self.__joints[1].lengthTo*math.cos(x[0]+x[1]))
        row2 = abs(self.__joints[0].lengthTo*math.sin(x[0])+self.__joints[0].lengthTo*math.sin(x[0]+x[1]))
        return [row1, row2]  

    def getSolutions(self):
        return self.__theSolution
        
    def solve(self):
        if(self.__invJac_CB == None or self.__F_CB == None): 
            self.__invJac_CB = self.invJac
            self.__F_CB = self.F
        theNewtRaph = NewtonRaph([self.__invJac_CB, self.__F_CB], self.__makeGuess(),self.error_margin,self.theTarget,self.max_iter)
        if(theNewtRaph.solve()):
            self.__theSolution=theNewtRaph.getSolution()
            return True
        else:
            return False
        
    def verifySolutions(self):
        return self.__F_CB(self.__theSolution)
    
    def verifyPathSol(self):
        i = 0
        endEffPath = []
        while(i != len(self.__pathSol)):
            endEffPath.append(self.__F_CB(self.__pathSol[i]))
            i = i + 1
        return endEffPath
            

    #path is a list of points [[x1,x2],[x3,x4],[x5,x6], etc], a point is a list [x1, x2]
    def solvePath(self, path):
        i = 0
        pathSol = []
        while(i != len(path)): 
            self.theTarget = path[i]
            try: 
                if(self.solve()):
                    pathSol.append(self.getSolutions().tolist())
                else:
                    print("There is no solution for this point: ", path[i])
                    return False
            except:
                return False
            i = i+1
        self.__pathSol = pathSol
        return True
    
    def getPathSol(self):
        return self.__pathSol
    
"""
Forward Kinematics Solver
"""
class FKSolver():
    def __init__():
        return True

"""
We need some way to extract way from MCU in a format where this code can easily read/manipulate/etc. 

Another way to run program ("move end effector in a predetermined paths as well as grasp control ")

verify angles here or on MCU?

"""

    