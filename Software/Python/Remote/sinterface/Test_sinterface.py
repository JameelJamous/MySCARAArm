from importlib.resources import path
from sinterface import IKSolver
from utils import Joint
import numpy as np

jointLists = [Joint(1.0,180.0,0.0), Joint(1.0,180.0,0.0)]

theSolver = IKSolver(jointLists, [0.5,0.5])

theSolver.max_iter = 2000
theSolver.error_margin = 1e-2
if(theSolver.solve()):
    print("The Solutions: ", theSolver.getSolutions())
    print("The Solutions will produce an end-effctor position of: ",theSolver.verifySolutions())
else:
    print("No solution can be found within an error margin of ", theSolver.error_margin, " and a max iteration of ", theSolver.max_iter)

aPath = []

point = [0.55, 0.55]
point2 = [0.66, 0.66]
point3 = [0.77, 0.77]

aPath.append(point)
aPath.append(point2)
aPath.append(point3)

print("-----------------------------")

if(theSolver.solvePath(aPath)):
    print("The solutions for this path: ", theSolver.getPathSol())
    print("The Solutions will produce the following end-effector positions: ", theSolver.verifyPathSol())
else:
    print("No solution can be found within an error margin of ", theSolver.error_margin, " and a max iteration of ", theSolver.max_iter)