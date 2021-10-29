#! /usr/bin/env python3

from pynput import keyboard

lst2 = []
def sort_key(key):
	try:
		print ("\n\nPressed Key {0}".format(key))
		print (str(key))
		lst = ['1','2','3','4']
		#if key in lst and key in lst2:
		#	lst2.remove(key)
		#	print ('found')
		#elif key in lst and key not in lst2:
		#	lst.2.append(key)
		##	print ('found')
		##!! this works
		if key.char in lst and key.char not in lst2:
			lst2.append(key.char)
			print(':+: '+str(key).strip("'") + ' Added')
		elif key.char in lst and key.char in lst2:
			lst2.remove(key.char)
			print(':-: '+str(key).strip("'") + ' Removed')
		# this dont work
		#if key == keyboard.Key.enter:
		#	print("retr0")
	# dis works
	except AttributeError:
		if key == keyboard.Key.enter:
			print(lst2)
		pass
	#	print ("Pressed Key {0}".format(key))

def __main__():
	#starts listening to the keyboard
	with keyboard.Listener(on_press=sort_key) as l:
		#with each key, 
		l.join()

if __name__=="__main__":
	__main__()