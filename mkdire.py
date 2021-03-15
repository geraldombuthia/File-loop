import os

directory = input("Enter name of your new directory")

parent = input("The file path to where to create the directory")
if bool(parent) == False:
  parent = "E:/systems"

path = os.path.join(parent, directory)
try:
 os.mkdir(path)
except OSError as error:
    pass

print("Directory created")

scanning = "F:/"
entries = os.scandir(scanning +"camera")
no = len(list(entries))
print(no)
for entry in entries : 
    if entry.is_dir() or entry.is_file(): 
        print(entry.name) 

