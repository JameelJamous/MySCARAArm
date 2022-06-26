# Remote Software

This is software that is designed to be ran on a remote device not contiguous to the arm. This software must be capable of reading raw sensor data from the arm and process the data to extract: angles, orientation, object proximity, etc. The remote software must also send joint angles either from user input or from an Inverse Kinematics solver. Might be a reach but the software must also be able to follow user defined paths. The remote software must be able to save paths and load paths. 

### Navigate:

`FileManager` : [Link](FileManager/README.md) - saves and load data to and from memory 

`IKSolver` : [Link](IKSolver/README.md) - solves the inverse kinematics with the current angles 

`Utils` : [Link](Utils/README.md) - utility classes/files 

`UML Diagrams` : [Link](Utils/README.md) - diagrams to show class relationships using VSCode extension: `Draw.io Integration`