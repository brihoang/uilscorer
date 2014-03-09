import os  #allows for automated compilation 
import sys #allows for use of command line arguments 
from datetime import datetime

def create_scoreboard():
	if not os.path.isdir("./scorekeeping"):
		os.system("mkdir scorekeeping")
		os.system("touch ./scorekeeping/scoreboard.txt")

def already_correct(problem_name):
	scoreboard = open("./scorekeeping/scoreboard.txt")
	for line in scoreboard:
		if line == problem_name + " CORRECT":
			return True
	return False

def correct(problem_name):
	create_scoreboard()
	if not already_correct(problem_name):
		board = open("./scorekeeping/scoreboard.txt", "a")
		board.write(problem_name + " CORRECT\n")
		board.close()


def incorrect(problem_name):
	create_scoreboard()
	if not already_correct(problem_name):
		board = open("./scorekeeping/scoreboard.txt", "a")
		board.write(problem_name + " INCORRECT\n")
		board.close()

java_file_name = str(sys.argv[1]) #ony file name since other things are similarly named. 
judge_file_out = open("./judge_files/" +(sys.argv[3]))

if os.path.exists("./judge_files/" + sys.argv[2]):
	os.system("cp ./judge_files/" + sys.argv[2] + " .")
os.system("javac "+java_file_name+".java") #compile submission 
os.system("java "+ java_file_name+" > test_output.out") #store submission output 
if os.path.exists("./"+sys.argv[2]):
	os.system("rm " + sys.argv[2])

submit = open("test_output.out")

#create an archive if there is not already one, date stamp the current file and copy it to the archive 
if not os.path.isdir("./archive"):
	os.system("mkdir archive")

now = datetime.now()
os.system("cp " + java_file_name + ".java ./archive/" + java_file_name +"_"+ str(now.hour) + "_" + str(now.minute) + "_"+ str(int(now.second))+".java")
correct_output = []
submit_output = []

#trim outputs
for line in judge_file_out:
	correct_output.append(line.strip())

for line in submit:
	submit_output.append(line.strip())

while submit_output[-1].isspace() or submit_output[-1] == '':
	submit_output.pop()

while correct_output[-1].isspace() or correct_output[-1] == '':
	correct_output.pop()

#check if outut is correct.
if submit_output == correct_output:
	correct(java_file_name)
	print "correct"
else:
	max_size = max(len(submit_output), len(correct_output))
	for x in range(max_size):
		if x < len(submit_output) and x < len(correct_output):
			print '%-20s%-20s' % (submit_output[x], correct_output[x])
		elif x < len(submit_output):
			print ('%-20s'%submit_output[x]) +(' '*20 )
		else:
			print (' '*20)+('%-20s'%correct_output[x])
	is_correct = raw_input("is the program correct[y/n]: ")
	if is_correct.lower() == "y":
		correct(java_file_name)
	else:
		incorrect(java_file_name)

os.system("rm test_output.out")
os.system("rm " + java_file_name + ".class")
