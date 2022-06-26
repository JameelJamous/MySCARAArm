#include "FileManager.h"


//--------------------------------------------
// Public Methods
//--------------------------------------------

FileManager::FileManager(){ /* Do Nothing*/ }

FileManager::FileManager(const FileManager& aCopy) { *this = aCopy; }

FileManager::FileManager(std::string aPath) { theFolderPath = aPath; }

FileManager::FileManager(const char* aPath) { theFolderPath = aPath; }

FileManager& FileManager::operator=(const FileManager& aCopy) {
    theFolderPath = aCopy.theFolderPath; theData = aCopy.theData;
	return *this;
}

FileManager::~FileManager() { /* Do Nothing */ }

void FileManager::clearVisitors() { theVisitorList.clear(); }

void  FileManager::specifyFolderPath(std::string aPath) { theFolderPath = aPath; }

FileManager& FileManager::operator<<(Visitor* aVisitor) {
    theVisitorList.push_back(aVisitor);
    return *this;
}

bool FileManager::saveContents(std::string aFileName, bool overwrite) {
    std::string theCompletePath = theFolderPath + "\\" + aFileName;
    if (!theCompletePath.ends_with(".rob"))
        theCompletePath.append(".rob");

    for (auto& item : theVisitorList) {
        addDataFrom(item);
    }

    return insertToFile(theCompletePath, overwrite);
}

bool FileManager::loadContents(std::string aFileName) {
    std::string theCompletePath = theFolderPath + "\\" + aFileName;
    if (!theCompletePath.ends_with(".rob"))
        theCompletePath.append(".rob");
    /* each new line is a new visitor's data */
    extractFromFile(theCompletePath);
    int i = 0;
    for (auto& item : theVisitorList) {
        loadInto(item, fileLines[i]);
        i++;
    }

    return true;
}

//------------------------------------------------
// Private Members
//------------------------------------------------

void FileManager::addDataFrom(Visitor* aVisitor) { theData.append(aVisitor->save()); }

void FileManager::loadInto(Visitor* aVisitor, std::string extracted) { aVisitor->load(extracted); }

bool FileManager::insertToFile(std::string aPath, bool overwrite) {

    std::ofstream outFile(aPath,
        (overwrite) ? std::ios_base::out : std::ios_base::app);

    if (!(outFile << theData << "\n")) {
        std::cerr << "Failed to write to file" << std::endl;
        outFile.close();
        return false;
    }

    outFile.close();
    return true;
}

bool FileManager::extractFromFile(std::string aPath) {
    std::ifstream aFileStream;
    aFileStream.open(aPath);
    if (aFileStream.is_open()) {
        std::string content = "";
        while (!aFileStream.eof()) {
            aFileStream >> content;
            fileLines.push_back(content);
        }

        fileLines.pop_back();
        aFileStream.close();
        return true;
    }
    aFileStream.close();
    return false;
}
