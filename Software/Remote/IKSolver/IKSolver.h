#include "Point.h"
#include "Joint.h"

using Solutions = std::pair<std::vector<float>, std::vector<float>>; //elbow-up, elbow-down

class IKSolver {
public:

	IKSolver();
	IKSolver(std::vector<Joint> someJoints, Point theTarget = (0.0f, 0.0f, 0.0f));
	IKSolver(const IKSolver& aCopy);
	~IKSolver();
	IKSolver& operator=(const IKSolver& aCopy);

	size_t numOfJoints();
	void addJoint(const Joint& aJoint);
	void setTarget(Point aTarget);
	Solutions getSolutions();
	bool setupWorkSpace();
	bool solve();
	
	//void addConstraint(Constraint)

private:

	std::vector<Joint> joints;
	Point theTarget;
	Solutions theSolution; 

};