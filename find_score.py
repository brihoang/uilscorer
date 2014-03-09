import os

if os.path.exists("./scorekeeping/scoreboard.txt"):
	scoreboard = open("./scorekeeping/scoreboard.txt")
	problems = {}
	for line in scoreboard:
		problems[ line.split()[0] ] = 60
	scoreboard = open("./scorekeeping/scoreboard.txt")
	for line in scoreboard:
		if "INCORRECT" in line:
			problems[ line.split()[0] ] -= 5
	s = 0
	for key in problems.keys():
		s += problems[key]
	
	print s
