# MCU Software

This software must tell the MCU to send and recieve command from the remote device. It must be able to report sensor data and current angles of each position as well as the time the data and angles were sampled. The MCU must send just raw data and the computing will be done remotely. 


We need a way to track the angles of the arms so we use accelermoters 
when recieving angles into MCU: base calculate the delta angle from the home position() and subsequent links calculates angle from the previous 
so the accelerometers measure the angle between previous link axis and current link axis 

### Navigate:

`Software` : [Link](https://github.com/JameelJamous/MySCARAArm/tree/main/Software) - Regards Software design and source code
