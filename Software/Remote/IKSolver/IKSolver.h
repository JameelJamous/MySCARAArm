/*!
 *  @file IKSolver.hpp
 *
 * 	File Manager 
 * 
 *  Written by Jameel Jamous. 
 * 
 *  Permission is hereby granted, free of charge, to any person obtaining a copy
 *  of this software and associated documentation files (the "Software"), to
 *  deal in the Software without restriction, including without limitation the
 *  rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
 *  sell copies of the Software, and to permit persons to whom the Software is
 *  furnished to do so, subject to the following conditions:
 *
 *  The above copyright notice and this permission notice shall be included in
 *  all copies or substantial portions of the Software.
 *
 *  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 *  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 *  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 *  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 *  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 *  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
 *  IN THE SOFTWARE.
 */



#include "Point.h"
#include "Joint.h"

using Solution = std::vector<float>;
using Solutions = std::pair<Solution, Solution>; //<elbow-up, elbow-down>

class IKSolver {
public:

	IKSolver();
	IKSolver(std::vector<Joint> someJoints, Point theTarget = (0.0f, 0.0f, 0.0f));
	IKSolver(const IKSolver& aCopy);
	~IKSolver();
	IKSolver& operator=(const IKSolver& aCopy);

	size_t numOfJoints();
	void addJoint(const Joint& aJoint); 

   /*!
    *  @brief  Sets the desired end-effector target
    */
	void setTarget(Point aTarget);

	/*!
    *  @brief  Returns a Pair of Solution (elbow-up & elbow-down)
    *  @return this->theSolution
    */
	Solutions getSolutions();
	
	/*!
    *  @brief  Determines the limitations of the chain of joints)
    *  @return Success or Failure
    */
	bool setupWorkSpace();
	
	/*!
    *  @brief  Solves the Inverse Kinematic equation with the current parameters
    *  @return True if there is AT LEAST ONE solution, False if no solution
    */
	bool solve();

private:

	std::vector<Joint> joints;
	Point theTarget;
	Solutions theSolution; 
	std::vector<Point> limitations;

};