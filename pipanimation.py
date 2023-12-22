import os, time #get required modules

frames=["—", chr(92), "|", "/"] #list of frames used
framelen=len(frames) #length of the list of frames

def clear():
	os.system("cls" if os.name=="nt" else "clear") #clears screen, gotta admit got from Stack Overflow.

def timer():
	i=0
	for i in range(framelen):
		clear()
		print("LOADING ANIMATION: "+frames[i]) #prints the value of i in loop
		time.sleep(0.35) #2.857142857 fps, amazing
	timer() #uses recursion to reset the timer to run infinitely

timer() #begins the timer