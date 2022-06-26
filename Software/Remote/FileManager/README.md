# Filemanager and its usage

`FileManager` is a class that allows the storage of its visitors into a file with the `.rob` extension. When initializing a `FileManager`, it is best to specify a path to folder to create, save, and load files. 

The `<<` operator adds a visitor to the FileManager.`saveContents` goes through all the current visitors (in sequential order) and calls their `save` function to aquire the data to write to the file specified in the first parameter.
`loadContents` goes through all the current visitors(in sequential order) and reads the data specified in the file. It then stores the data the program memory for the visitor's to use. 

To allow this functionality to future classes make sure to inherit `Visitor.h` and override the definitions.

The contents of an example file with the `.rob` extension saving 5 visitors will look like this:

```
Visitor1DataMember1,
Visitor2DataMember1,Visitor2DataMember2,
Visitor3DataMember1,Visitor2DataMember2,Visitor2DataMember3
Visitor4DataMember1,
Visitor5DataMember1,Visitor5DataMember2
```

When implementing `save` on visitors make sure to export class data as a string using CSV in between the visitor's data. 

When implementing `load` use your favorite CSV decoding method as the `FileManager` will pass the corresponding line from the file to `load`.

# Navigate:

`Software` : [Link](Software/) - Regards Software design and source code
