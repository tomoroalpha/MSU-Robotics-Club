# About this repository

The purpose of this repository is to keep track of the current working robotics experiments and ARGoS configurations of the MSU-Robotics Club. 
It also serves as a collaboration homebase for the software and hardware teams as projects expand beyond simulation. 
 
## NASA TODOs before December 13th

    - GPR Plugin Design + Implementation
    - Preliminary Rover Design
    - Figure out object importing workflow in ARGoS 
    - Create ARGoS Prototype Rover Entity
    - Simple solidworks model exported into ARGoS framework (perhaps a cube?)
    - Simplistic swarm control behavior (3-4 robots working together to map an area)
    - Output Data Processing Workflow
    - Data Output Sample
    - Preliminary Design Document 
    
## Quick Start with ARGoS 

The following steps assume that you have already installed ARGoS on your system as described here:
https://www.argos-sim.info/core.php

Note: If you are booting from the Live USB that you got from the club meeting, you do not need to install ARGoS! It comes pre-loaded on the USB. Follow the steps below to get the examples running on the Live USB stick. 

1. Download the repository and unpack it in a memorable directory. 

2. Navigate to the directory you unpacked the repository in: 

    $ cd /PATH/MSU-Robotics-Club

    (remember that "PATH" denotes the upper path of the file's location....dont actually type "PATH")

3. Create a new directory and name it "build"

    $ mkdir build

4.  Navigate to the new directory: 

    $ cd build

5. Call cmake to get the files ready for compilation. You have 2 options:

    $ cmake -DCMAKE_BUILD_TYPE=Release ..  

    or

    $ cmake -DCMAKE_BUILD_TYPE=Debug ..

6. Make the configuration:

    $ make

7. If you get no errors then you can navigate back up to the MSU-Robotics-Club directory to launch ARGoS.
    
    If you want to launch ARGoS with the Lua editor you can type:

    $ argos3 -c lua-only/expSetup.argos

    If you want to lanch an experiment on its own without the editor, you can type:

    $ argos3 -c experiments/diffusion_1.argos
    
    Note that "diffusion_1.argos" can be replaced with any .argos file that has been included and compiled in the directory. 


