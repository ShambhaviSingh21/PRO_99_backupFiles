import os
import shutil
import time
import time

def main():

deletedFoldersCount = 0
deletedFilesCount = 0

days= 30
path = "C:\Users\DELL\Desktop\old folders"\

# converting days to seconds
# time.time() returns current time in seconds
seconds = time.time() - (days * 24 * 60 * 60)

# checking whether the file is present in path or not
if os.path.exists(path):
    for rootFolders, folders, files in os.walk(path):
        if seconds >= folderAge(rootFolders):
        # removing the folder
        removeFolder(rootFolders)
        # incrementing count
        deletedFoldersCount += 1
        
        break
    else: 
        for folder in folders:
        
            folderPath = os.path.join(rootFolders, folder)
            # comparing with the days
            if seconds >= folderAge(folderPath):
            
                removeFolder(folderPath)
                deletedFoldersCount +=1
                
        # checking the current directory files        
        for file in files:
            filePath = os.path.join(rootFolders, file)
            
            if seconds >= folderAge(filePath):
            
                removeFile(filePath)
                deletedFilesCount += 1
                
    else: 
    
        if  seconds >= folderAge(path):
            
            removeFile(path)
            deletedFilesCount += 1
            
    else:

       print('"{path}" is not found')
       deletedFilesCount +=1
       
      print("Total folders deleted: {deletedFoldersCount}")
	  print("Total files deleted: {deletedFilesCount}")
      
def removeFolder(path):

    if not shutil.rmtree(path):
       #removing the folder
		# success message
		print(f"{path} is removed successfully")

	else:

		# failure message
		print(f"Unable to delete the "+path)
            
def removeFile(path):

    if not os.remove(path):
    
        # success message
		print(f"{path} is removed successfully")

	else:

		# failure message
		print(f"Unable to delete the "+path)
        
def folderAge(path):

    ctime = os.stat()
    path.st_ctime
    
    return ctime