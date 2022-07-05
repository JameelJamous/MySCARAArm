import matplotlib.pyplot as plt
import math
import numpy as np
import random as rand

# FWD kinematic equations
def F_x(theta, links): 
    row1 = abs(links[0]*math.cos(theta[0])+links[1]*math.cos(theta[0]+theta[1]))
    row2 = abs(links[0]*math.sin(theta[0])+links[1]*math.sin(theta[0]+theta[1]))
    print(theta, links)
    return np.array([row1, row2])   

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
    #print("F_x: ", F_x(x,links), "Inv: ", invJacobian(x,links))
    return  np.subtract(x,np.subtract(np.matmul(desired,invJacobian(x,links)),np.matmul(F_x(x, links),invJacobian(x, links))))

def currentRelativeError(x_new, x):
    return np.absolute((x_new-x)/(x_new))

def getRefAngle(x):
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
            return getRefAngle(x_new), i, x_new
        else:
            guess = x_new
            i = i + 1 
            if i > max_iter:
                return "Not found", i

def analApproach(desired, links):
    num = (math.pow(desired[0],2)+math.pow(desired[1],2)-math.pow(links[0],2)-math.pow(links[1],2))
    denom = (2*links[0]*links[1])
    theta2 = math.acos(num/denom)
    num = (desired[1]*(links[0]+links[1]*math.cos(theta2)))-desired[0]*links[1]*math.sin(theta2)
    denom = (desired[0]*(links[0]+links[1]*math.cos(theta2))+desired[1]*links[1]*math.sin(theta2))
    theta1 = math.atan(num/denom)
    return theta1, theta2


def main():
    theta = [math.pi/3, math.pi/2]
    links = [1.0, 1.0]
    desired = [0.75, 0.5]

    row1 = [math.pi/2]
    row2 = [math.pi/3]  


    maxIter = 1000
    errMax = np.array(np.vstack((0.0000001, 0.0000001)))

    print("starting newtonRaph method")
    reached, i, unprocessed = newtonRaph(theta, errMax, desired, maxIter, links)
    print("-----------------------")
    print("newtonRaph Angles(processed):", reached)
    print("newtonRaph Angles(unprocessed): ", unprocessed)
    print("iterations: ", i)

    print("Fwd Kinematics with newtonRaph angles(processed): ", F_x(reached,links))
    print("Fwd Kinematics with newtonRaph angles(unprocessed): ", F_x(unprocessed,links))

    print("Desired: ", desired)
    
    ################################# Anaylitical method

    t1, t2 = analApproach(desired, links)
    theArray = np.array(np.vstack((t1,t2)))
    print("-----------------------------------")
    print("Analytical Approach: ", np.rad2deg(theArray))

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