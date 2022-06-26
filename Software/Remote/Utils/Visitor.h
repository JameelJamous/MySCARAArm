#pragma once
#include <string>

class Visitor {
public:
	virtual void load(std::string theData) = 0;
	virtual std::string save() const = 0;
};