## About
This is a grader/scorekeeper for Texas UIL CS competitions. It currently only scores for one team as it was made with intentions for one team practices. Capability for multiple teams may be looked at in the future. This assumes problems and problem names are in the UIL format.

## How to Use
Only one command is required. All the judging files should be in a directory called `judge_files`. Do not put the path of the file, just the name of the file. 

`$ python main.py [name of problem] [expected input file] [expected output file]`

This command will output if the program is correct, and a display of both files side by side if it is incorrect from automation. The judge can then manually judge if it is correct and then tell the program if it is correct or not. This command also adds a datestamp to the file name and places it in a directory called `./archive`. 

## Scoring
The `find_score.py`	program determines the score. Just give the command 

`python find_score.py` and it will determine the score.

If during judgement, an accidental incorrect judgement was given, you can manually go to the scorekeeping folder and delete the last line of the file. Tampering with this file too much may confuse the `find_score` program.


##Use
Currently, this program is only useable on Mac OS X/Linux
