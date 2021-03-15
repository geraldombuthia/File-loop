import os

parent = "F:/"
entries = os.scandir(parent +"camera")
thislist = os.scandir(parent +"camera")
for entry in entries : 
    if entry.is_dir() or entry.is_file(): 
        print(entry.name) 
no = len(list(thislist))
print(no)