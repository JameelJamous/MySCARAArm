#include "IKSolver.h"

IKSolver::IKSolver(){ /* Do Nothing */ }

IKSolver::IKSolver(const IKSolver& aCopy) { *this = aCopy; }

IKSolver::IKSolver(std::vector<Joint> someJoints, Point theTarget) {
	joints = someJoints;
	this->theTarget = theTarget;
}

IKSolver::~IKSolver(){ /* Do Nothing */ }

IKSolver& IKSolver::operator=(const IKSolver& aCopy) {
	joints = aCopy.joints;
	theTarget = aCopy.theTarget;
	theSolution = aCopy.theSolution;
	return *this;
}

size_t IKSolver::numOfJoints() { return joints.size(); }

void IKSolver::addJoint(const Joint& aJoint) { joints.push_back(aJoint); }

void IKSolver::setTarget(Point aTarget) { theTarget = aTarget; }

Solutions IKSolver::getSolutions() { return theSolution; }

bool IKSolver::setupWorkSpace() {

	//iterate through each joint "joints must be in order from x, y, z
	/*Point maxLen;
	for (auto item : joints) {
		if (item.getType() == "prismatic") {
			
		}
		else { // is revolute
			maxLen += Point(item.getParam(0));
		}
		limitations.push_back(Point(item.getParam(0))); // distance to next joint 
		limitations.push_back(Point(item.getParam(1))); // max distance
		limitations.push_back(Point(item.getParam(2))); // min distance
	}

	*/

	return false;
}

 

bool IKSolver::solve() { //using analytical approach

	

	return false;
}	

/*
	We have angles from MCU
	
	- jacobian changes with number of links

	param = (pow(target_x,2) + pow(target_y,2) - pow(L1,2) - pow(L2,2))/2*L1*L2;
	theta2 = acos(param);

	param = (target_y*(L1+L2*cos(theta2))-target_x*L2*sin(theta2))/(target_x*(L1+L2*cos(theta2))+target_y*L2*sin(theta2))
	theta1 = atan(param);


	WHEN inputting angles 

	1. calculate the angle offset from home position of each joint and override to that pos


	For solving 2D IK for N Links:

	https://opentextbooks.clemson.edu/wangrobotics/chapter/inverse-kinematics/


*/