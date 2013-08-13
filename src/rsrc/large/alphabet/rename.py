import os
for f in os.listdir('.'):
	if not f.startswith('.'):
		if f != "rename.py":
			import string
			if f[-5] in string.uppercase:
				os.rename(f, "U_"+str(f[-5])+".png")
			else: os.rename(f, "L_"+str(f[-5])+".png")