from enum import Enum
import matplotlib.pyplot as plt
import math
import numpy as np
import random as rand


class Quadrants(Enum):
    One = 0
    Two = 1
    Three = 2
    Four = 3
    
"""
callbacks need F which is a nd vector containing equations for each dimenstion
"""



# FWD kinematic equations
def F_x(theta, links): 
    row1 = abs(links[0]*math.cos(theta[0])+links[1]*math.cos(theta[0]+theta[1]))
    row2 = abs(links[0]*math.sin(theta[0])+links[1]*math.sin(theta[0]+theta[1]))
    #print(theta, links)
    return np.array([row1, row2])   

x = F_x
print(x)
# returns inverse jacobian
def invJacobian(theta, links):
    row1 = [(-links[0]*math.sin(theta[0])-links[1]*math.sin(theta[0]+theta[1])),(-links[1]*math.sin(theta[0]+theta[1]))]
    row2 = [(links[0]*math.cos(theta[0])+links[1]*math.cos(theta[0]+theta[1])),(links[1]*math.cos(theta[0]+theta[1]))]
    ret = np.array(row1)
    ret1 = row2
    theResult = np.vstack((ret, ret1))
    
    try:
        np.linalg.inv(theResult)
    except np.linalg.LinAlgError:
        print("Divided by 0, makeing newGuess")
        guess = newGuess()
        return invJacobian(guess,links)

    return np.linalg.inv(theResult)

def newGuess():
    return np.vstack((math.pi*rand.uniform(0,2), math.pi*rand.uniform(0,2)))

def findNext(x, links, desired):
    print("F_x: ", F_x(x,links), "Inv: ", invJacobian(x,links))
    print("Find Next: ", np.subtract(x,np.subtract(np.matmul(desired,invJacobian(x,links)),np.matmul(F_x(x, links),invJacobian(x, links)))))
    return  np.subtract(x,np.subtract(np.matmul(desired,invJacobian(x,links)),np.matmul(F_x(x, links),invJacobian(x, links))))

def currentRelativeError(x_new, x):
    return np.absolute((x_new-x)/(x_new))

def determineQuadrant(x_og):
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

def getRefAngle(x):
    
    #determineQuadrant(x)
    angle = np.mod(x,math.pi)
    while np.greater(angle,math.pi/2).all():
        angle = np.subtract(math.pi,angle)
    
    return angle

# newton raph method(what we are working on ) # we did it but now we need to convert th angles into fundamental angles
def newtonRaph(guess, error, desired, max_iter, links):
    # guess of x
    i = 0
    while 1:
        #print(guess, i)
        x_new = findNext(guess, links, desired)
        if(np.less_equal(currentRelativeError(x_new, guess), error).all()):
            _ , processed = determineQuadrant(x_new)
            return processed, i, x_new
        else:
            guess = x_new
            i = i + 1 
            if i > max_iter:
                return "Not found", i, "Not found"

def analApproach(desired, links):
    num = (math.pow(desired[0],2)+math.pow(desired[1],2)-math.pow(links[0],2)-math.pow(links[1],2))
    denom = (2*links[0]*links[1])
    theta2 = math.acos(num/denom)
    num = (desired[1]*(links[0]+links[1]*math.cos(theta2)))-desired[0]*links[1]*math.sin(theta2)
    denom = (desired[0]*(links[0]+links[1]*math.cos(theta2))+desired[1]*links[1]*math.sin(theta2))
    theta1 = math.atan(num/denom)
    return theta1, theta2


def main():
    
    theta = [math.pi/2, math.pi/2]
    links = [1.0, 1.0]
    desired = [0.5, 0.5]

    row1 = [math.pi/2]
    row2 = [math.pi/3]  


    maxIter = 1000
    errMax = np.array(np.vstack((0.0001, 0.0001)))

    print("starting newtonRaph method")
    reached, i, unprocessed = newtonRaph(theta, errMax, desired, maxIter, links)
    print("-----------------------")
    print("newtonRaph Angles(processed):", reached)
    print("newtonRaph Angles(unprocessed): ", unprocessed)
    #print(determineQuadrant(unprocessed))
    #print(determineQuadrant(reached))
    print("iterations: ", i)
    

    print("Fwd Kinematics with newtonRaph angles(processed): ", F_x(reached,links))
    print("Fwd Kinematics with newtonRaph angles(unprocessed): ", F_x(unprocessed,links))

    print("Desired: ", desired)
    
    ################################# Anaylitical method

    t1, t2 = analApproach(desired, links)
    theArray = np.array(np.vstack((t1,t2)))
    print("-----------------------------------")
    _, x = determineQuadrant(theArray)
    print("Analytical Approach: ", x)

    print("Fwd Kinematics with Analytic angles: ", F_x(theArray, links))

    print("Desired: ", desired)
    

if __name__ == "__main__":
    main()
    """
    
    import math

angle = float (input("Enter angle(deg) to calculate reference angle for : "))
angle = angle%2*math.pi
print("modulus: ", angle)
if angle > math.pi/2 :
    angle = math.pi - angle
print("Reference Angle = ",angle)

print(1.0*math.cos(18.3343055))
print(1.0*math.sin(18.3343055), "\n")

print(1.0*math.cos(18.3343055+96.45428598))
print(1.0*math.sin(18.3343055+96.45428598), "\n")

print(1.0*math.cos(18.3343055)+1.0*math.cos(18.3343055+96.45428598))
print(1.0*math.sin(18.3343055)+1.0*math.sin(18.3343055+96.45428598), "\n")

print("------------------------\n")
print(1.0*math.cos(0.51525042))
print(1.0*math.sin(0.51525042), "\n")

print(1.0*math.cos(0.51525042+0.93508628))
print(1.0*math.sin(0.51525042+0.93508628), "\n")

print(1.0*math.cos(0.51525042)+1.0*math.cos(0.51525042+0.93508628))
print(1.0*math.sin(0.51525042)+1.0*math.sin(0.51525042+0.93508628))
    """