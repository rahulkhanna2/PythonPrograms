import os 

def rename_file():
	#gets file from the folder
	file_list  = os.listdir("C:\Downloads\Video")
	#print file_list
	saved_path = os.getcwd() #current working directory
	os.chdir(r"C:\Downloads\Video")

	#changes the file name in the folder
	for file_name in file_list:
		os.rename(file_name , file_name.translate(None , "'%20-'"))
	os.chdir(saved_path)
rename_file()

print "ALL DONE!!"
