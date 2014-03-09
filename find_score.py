import os

if os.path.exists("./scorekeeping/scoreboard.txt"):
	scoreboard = open("./scorekeeping/scoreboard.txt")
	problems = {}
	for line in scoreboard:
		problems[ line.split()[0] ] = 0
		if not "INCORRECT" in line:
			problems[ line.split()[0] ] = 60
	scoreboard = open("./scorekeeping/scoreboard.txt")
	for line in scoreboard:
		if "INCORRECT" in line:
			problems[ line.split()[0] ] -= 5
	s = 0
	print "%-21s%-21s%-5s" % ("Problem Name", "Status", "Score")
	for key in sorted(problems.keys()):
		status = "CORRECT" if problems[key] > 0 else "INCORRECT" 
		s = s+problems[key] if problems[key] > 0 else s
		print "%-20s %-20s %-5d" % (key, status, problems[key] if status == "CORRECT" else 0)
	
	print "%-42s%-d" % ("TOTAL",s)
else:
	print 0
