#include "Joint.h"

Joint::Joint(float distanceToNext, float maxAngle,
	float minAngle, std::string jointType, ChainType chainType) {
	jointParams.push_back(distanceToNext);
	jointParams.push_back(maxAngle);
	jointParams.push_back(minAngle);
	type = jointType;
	posInChain = chainType;
}

Joint::Joint(const Joint& aCopy) { *this = aCopy; }

Joint& Joint::operator=(const Joint& aCopy) {
	jointParams = aCopy.jointParams;
	type = aCopy.type;
	return *this;
}

Joint::~Joint(){ /* Do Nothing */ }

float Joint::getParam(size_t paramNo) { return jointParams[paramNo]; }

std::string Joint::getJointType() { return type; }

ChainType Joint::getPositionInChain() { return posInChain; }

void Joint::defineJointType(std::string aType){ type = aType; }

void Joint::defineAngles(float maxAngle, float minAngle){ 
	jointParams[1] = maxAngle; jointParams[2] = minAngle;
}

void Joint::defineDistance(float distanceToNext){ jointParams[0] = distanceToNext; }

void Joint::defineChainType(ChainType aType){ posInChain = aType; }

std::string Joint::save() const {
	std::string outStr;
	outStr += std::to_string(jointParams[0]) + "," + std::to_string(jointParams[1]) +
		"," + std::to_string(jointParams[2]) + "," + type + "," + "\n";

	return outStr;
}

void Joint::load(std::string theData) {

	auto ret = splitCSV(theData);
	if (!ret.has_value())
		return;

	std::list<std::string> dataList = ret.value();

	for (int i = 0; i < 3; i++) {
		jointParams[i] = std::stof(dataList.front());
		dataList.pop_front();
	}
	type = dataList.front(); 
}

listOpt Joint::splitCSV(std::string theData) {
	std::list<std::string> theList;
	std::string content = "";
	for (auto aChar : theData) {
		if (aChar == ',') {
			theList.push_back(content); //FIX: exception thrown here // cant write to optional 
			content = "";
		}
		else
		{
			content.push_back(aChar);
		}
	}
	
	if (!theList.empty())
		return theList;

	return std::nullopt;
}