##Call from the root of the installer
import hashlib
import os
import sys
import split

#Get the MD5 of a file using chunk size 4k
def md5(fname):
  hash_md5 = hashlib.md5()
  with open(fname, "rb") as f:
    for chunk in iter(lambda: f.read(4096), b""):
        hash_md5.update(chunk)
  return hash_md5.hexdigest()
  
if __name__ == '__main__':
    #Make sure that the MD5 file doesn't exist
    try:
        os.remove("MD5.txt")
    except OSError:
        pass
    #Walk through all files and split those over 2gb
    for root, dirs, files in os.walk("."):
        for name in files:
            file=os.path.join(root, name)
            if (os.path.getsize(file) > 2147483648): #hardcode 2gb
                #create a directory of the same name as the file for the splitfiles, fail if it exists (something is wrong)
                dirSplit=file.split(".")
                dirName="."+dirSplit[1]
                os.makedirs(dirName) #it will split the first period (cwd)
                #Call split.py on the file and put it in the created directory    
                split.split(file, dirName, 1000000000)
                os.remove(file)
    
    MD5File=open("MD5.txt", 'w+')
    #Walk through all the files in CWD and get the MD5s
    for root, dirs, files in os.walk("."):
        for name in files:
            file=os.path.join(root, name)
            MD5Sum=md5(file)
            unsplitLine=file+"="+MD5Sum
            splitLine=""
            addSpace=False
            #Add spaces every 2 characters like certutil does
            for charIndex in range(unsplitLine.index("=")+1,len(unsplitLine)):
                splitLine+=unsplitLine[charIndex]
                if addSpace: splitLine+=" "
                addSpace=not addSpace
            MD5File.write(file +"="+splitLine.strip()+"\n")