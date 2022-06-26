#pragma once


#include <cmath>
#include <vector>
class Point {
public:
	float x_pos;
	float y_pos;
	float z_pos;

	Point(const float anX = 0, const float aY = 0, const float aZ = 0) {
		x_pos = anX;
		y_pos = aY;
		z_pos = aZ;
	}

	Point(const Point& aCopy) { *this = aCopy; }

	Point& operator=(const Point& aCopy) {
		x_pos = aCopy.x_pos;
		y_pos = aCopy.y_pos;
		z_pos = aCopy.z_pos;
		return *this;
	}

	Point& operator+(const Point& otherPoint) {
		x_pos = x_pos + otherPoint.x_pos;
		y_pos = y_pos + otherPoint.y_pos;
		z_pos = z_pos + otherPoint.z_pos;
		return *this;
	}

	Point& operator-(const Point& otherPoint) {
		x_pos = x_pos - otherPoint.x_pos;
		y_pos = y_pos - otherPoint.y_pos;
		z_pos = z_pos - otherPoint.z_pos;
		return *this;
	}

};
