import os

f = open("demo-file-handling.txt") #read
print(f.read())

with open("demo-file-handling.txt", "a") as f: #append
  f.write("Now the file has more content!")

with open("demofile.txt", "w") as f: #overwrite
  f.write("Woops! I have deleted the content!")

if os.path.exists("demo-file-handling.txt"): #delete if available
  os.remove("demo-file-handling.txt")
else:
  print("The file does not exist")