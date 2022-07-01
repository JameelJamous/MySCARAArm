/*!
 *  @file Joint.hpp
 *
 * 	Joint
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


#pragma once

#include "Visitor.h"
#include <string>
#include <optional>
#include <list>
#include <vector>

enum class ChainType{
	null, base, link, end
};


using listOpt = std::optional<std::list<std::string>> ;
class Joint : public Visitor {
public:
	Joint(float distanceToNext=0, float maxAngle=0, float minAngle=0, 
		std::string jointType="", ChainType chainType=ChainType::null);

	Joint(const Joint& aCopy);
	Joint& operator=(const Joint& aCopy);
	~Joint();

	void defineJointType(std::string aType);
	void defineAngles(float maxAngle = 0, float minAngle = 0);
	void defineDistance(float distanceToNext = 0);
	void defineChainType(ChainType aType);

	/*!
    *  @brief  Returns the parameter denoted by paramNo
    *  @return jointParams[paramNo]
    */
	float getParam(size_t paramNo);

	ChainType Joint::getPositionInChain();
	std::string getJointType();
 
	std::string save() const override;
	void load(std::string theData) override;

public:

	float curAngle;

private:

	listOpt splitCSV(std::string theData);

private:

	std::vector<float> jointParams; //1st - distanceToNext, 2nd - maxAngle, 3rd - minAngle
	std::string type;
	ChainType posInChain;


};