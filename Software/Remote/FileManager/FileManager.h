#pragma once
#include <sstream>
#include <string>
#include <fstream>
#include <iostream>
#include <list>
#include <vector>
#include <optional>
#include "Visitor.h"

class FileManager {

public:
	
	FileManager();
	FileManager(const FileManager& aCopy);
	FileManager(std::string aPath);
	FileManager(const char* aPath);
	FileManager& operator=(const FileManager& aCopy);
	~FileManager();

	void clearVisitors();
	void specifyFolderPath(std::string aPath);
	bool saveContents(std::string aFileName, bool overwrite = false);
	bool loadContents(std::string aFileName);
	FileManager& operator<<(Visitor* aVisitor);

private:

	void loadInto(Visitor* aVisitor, std::string extracted);
	void addDataFrom(Visitor* aVisitor);
	bool insertToFile(std::string aPath, bool overwrite = false);
	bool extractFromFile(std::string aPath);

private:

	std::string theFolderPath;
	std::string theData;
	std::vector<std::string> fileLines;
	std::vector<Visitor*> theVisitorList;
};