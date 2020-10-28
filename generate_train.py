import os

DIRECTORY = "data/obj"

fileNames = ""
for file in os.listdir(DIRECTORY):
  if(file.endswith(".png")):
      fileNames += DIRECTORY + "/" + file + "\n"

file = open("data/train.txt", "w")
file.write(fileNames)
file.close()