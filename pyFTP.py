#FTP post service

import ftplib
import getpass
import os

try:
	host=raw_input("Host: ")
	user=raw_input("Username: ")
	password=getpass.getpass("Password: ")

	ftp=ftplib.FTP(host,user,password)

	print(ftp.dir())

	location=raw_input("index: ")
	ftp.cwd(location)

#modified_local_file
	fileloc=raw_input("File Location: ")
        postf=raw_input("Modified File: ")
	gfile=open(fileloc,"wb")

	#modf=open(fileloc,"wb")
	
	#textw=raw_input("writing: ")
	#modf.write(textw)
	#modf.close()

	ftp.retrbinary("RETR "+postf,gfile.write)
	gfile.close()
	os.system("nano "+fileloc)
#---------------------------------
        gfile=open(fileloc,"rb")
#---------------------------------
#regex
	ftp.storbinary("STOR "+postf,gfile)
	gfile.close()
	ftp.quit()

	gfile=open(fileloc,"r")
	print(gfile.read())
	gfile.close()
except (TypeError,RuntimeError,NameError,ValueError):
	print("problem!")		

