import os
for file in os.listdir():
	path=os.path.abspath(file)
	filesize = os.path.getsize(file)
	if (filesize <2000) & (os.path.splitext(path)[1]!=".txt"):
		os.remove(file)
