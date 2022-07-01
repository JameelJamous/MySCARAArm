/*!
 *  @file FileManager.hpp
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






#pragma once
#include <sstream>
#include <string>
#include <fstream>
#include <iostream>
#include <list>
#include <vector>
#include <optional>
#include "Visitor.h"

/*!
 *  @brief  Class that stores states of visitors and contains functions for interacting with
 *  external files with the extension ".rob"
 */
class FileManager {

public:
	
	FileManager();
	FileManager(const FileManager& aCopy);
	FileManager(std::string aPath);
	FileManager(const char* aPath);
	FileManager& operator=(const FileManager& aCopy);
	~FileManager();

	void clearVisitors();

   /*!
    *  @brief sets the path to the folder to save and load files from
    */
	void specifyFolderPath(std::string aPath);
   
   /*!
    *  @brief  Saves the current state of all the visitors
    *  @return Success or Failure
    */
	bool saveContents(std::string aFileName, bool overwrite = false);

   /*!
    *  @brief  Loads the state in aFileName into the each current visitor
    *  @return Success or Failure
    */
	bool loadContents(std::string aFileName);

   /*!
    *  @brief  Adds a visitor to FileManager
    *  @return Reference to this
    */
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