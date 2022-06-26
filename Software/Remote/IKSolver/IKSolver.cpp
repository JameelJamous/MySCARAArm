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
	for (auto item : joints) {
		if (item.getType() == "prismatic") {
			z_max = item.getParam(1);
			z_min = item.getParam(2);
		}
		else {
			
		}
	}


	return false;
}



bool IKSolver::solve() {




	return false;
}