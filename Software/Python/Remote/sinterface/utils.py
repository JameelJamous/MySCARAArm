from enum import Enum
import matplotlib.pyplot as plt
import math
import numpy as np
import random as rand

class Joint():
    lengthTo = 0.0
    maxAng = 0.0
    minAng = 0.0
    jointType = ""

    def __init__(self, len, maxAng, minAng, jointType=""):
        self.lengthTo = len
        self.maxAng = maxAng
        self.minAng = minAng
        self.jointType = jointType
        
class NewtonRaph():
    callbacks = []
    initGuess = []
    error_margin = []
    desired = []
    max_iter = 0
    solution = []
    
    def __init__(self, callbacks, guess, error_margin, desired, max_iter):
        self.callbacks=callbacks
        self.initGuess=guess
        self.error_margin=error_margin
        self.desired=desired
        self.max_iter=max_iter
        
    
    def __makeGuess(self):
        return np.vstack((math.pi*rand.uniform(0,2), math.pi*rand.uniform(0,2)))
    
    def solve(self):
        guess = self.initGuess
        x_new = 0
        i = 0
        while 1:
            #print(guess, i, x_new)
            #input()
            x_new = self.__findNext(guess)
            if(np.less_equal(self.__currentRelativeError(x_new, guess), np.array(np.hstack((self.error_margin, self.error_margin)))).all()):
                _ , processed = self.__determineQuadrant(x_new)
                
                if(np.less_equal(self.__currentRelativeError(self.callbacks[1](processed), self.desired), np.array(np.hstack((self.error_margin, self.error_margin)))).all()):
                    self.solution = processed
                    return True
                else:
                    guess = self.__makeGuess()
                    i = 0
                    continue      
            else:
                guess = x_new
                i = i + 1 
                if i > self.max_iter:
                    return False
                
    def getSolution(self):
        return self.solution
    
    def __findNext(self, x_old):
        #print (self.callbacks[0](x), self.callbacks[1](x))
        #rn callback [0] is inverse and callback[1] is F
        #inverse, F, inverse
        #print("find next result: ", np.subtract(x,np.subtract(np.matmul(self.desired,self.callbacks[0](x)),np.matmul(self.callbacks[1](x),self.callbacks[0](x)))))
        x = np.hstack(x_old)
        #print("x: ", x)
        
        #print("desired*invJacob: ",np.matmul(self.desired,self.callbacks[0](x)),"\n")
        #print("F*invJacob: ", np.matmul(self.callbacks[1](x),self.callbacks[0](x)),"\n")
        #print("(des*invJac-F*invJacob): ",np.subtract(np.matmul(self.desired,self.callbacks[0](x)),np.matmul(self.callbacks[1](x),self.callbacks[0](x))),"\n")
        #print("Find Next: ", np.subtract(x,np.subtract(np.matmul(self.desired,self.callbacks[0](x)),np.matmul(self.callbacks[1](x),self.callbacks[0](x)))), "\n")
        return  np.subtract(x,np.subtract(np.matmul(self.desired,self.callbacks[0](x)),np.matmul(self.callbacks[1](x),self.callbacks[0](x))))
        
    def __currentRelativeError(self, x_new_o, x_o):
        x_new = np.array(x_new_o)
        x = np.array(x_o)
        return np.absolute((x_new-x)/(x_new))
    
    def __determineQuadrant(self, x_og):
        
        x = x_og # copy
        while(not(np.less_equal(x,2*math.pi).all() and np.greater_equal(x,0).all())):
            #print(x)
            #print(np.less_equal(x,2*math.pi).all(), np.greater_equal(x,0).all())
            #print(not(np.less_equal(x,2*math.pi).all(), np.greater_equal(x,0).all()))
            for i in range(len(x)):
                if(x[i] < 0.0):  
                    if(not(x[i] <= 2*math.pi and x[i] >= 0)): 
                        x[i] = x[i] + 2*math.pi
                else:
                    if(not(x[i] <= 2*math.pi and x[i] >= 0)):
                        x[i] = x[i] - 2*math.pi
        #print(x)
        #input()
                
    #input()
    #print(x)
        div = np.divide(x,math.pi/2)
        mod_trunc = np.trunc(div)
    #print(mod_trunc)
    #input()
        return [Quadrants(mod_trunc[0]), Quadrants(mod_trunc[1])], x

class Quadrants(Enum):
    One = 0
    Two = 1
    Three = 2
    Four = 3