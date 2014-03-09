## About
This is a grader/scorekeeper for Texas UIL CS competitions. It currently only scores for one team as it was made with intentions for one team practices. Capability for multiple teams may be looked at in the future. This assumes problems and problem names are in the UIL format.

## How to Use
Only one command is required. 

`$ python main.py [name of problem] [expected output file]`

This command will output if the program is correct, and a display of both files side by side if it is incorrect from automation. The judge can then manually judge if it is correct and then tell the program if it is correct or not. This command also adds a datestamp to the file name and places it in a directory called `./archive`. The scoring system is currently not active yet, but it is in the works. The ability to remove an accidental incorrect judgement will come with the addition of the scoring system 

##Use
Currently, this program is only useable on Mac OS X/Linux
