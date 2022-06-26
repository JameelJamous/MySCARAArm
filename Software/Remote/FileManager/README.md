#Filemanager and its usage

`FileManager` is a class that allows the storage of its visitors into a file with the `.rob` extension. When initializing a `FileManager`, it is best to specify a path to folder to create, save, and load files. 

The `<<` operator adds a visitor to the FileManager.
The `saveContents` goes through all the current visitors (in sequential order) and calls their `save` function to aquire the data to write to the file specified in the first parameter.
The `loadContents` goes through all the current visitors(in sequential order) and reads the data specified in the file. It then stores the data the program memory for the visitor's to use. 

To allow this functionality to future classes make sure to inherit `Visitor.h` and override the definitions 