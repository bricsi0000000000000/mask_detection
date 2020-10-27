import os
import cv2

DIRECTORY = "archive/annotations/images"
IMAGE_EXTENSION = ".png"

annotations = ""

def convert(filename_str, coords):
  image = cv2.imread(filename_str + IMAGE_EXTENSION)
  coords[2] -= coords[0]
  coords[3] -= coords[1]
  x_diff = int(coords[2]/2)
  y_diff = int(coords[3]/2)
  coords[0] = coords[0]+x_diff
  coords[1] = coords[1]+y_diff
  coords[0] /= int(image.shape[1])
  coords[1] /= int(image.shape[0])
  coords[2] /= int(image.shape[1])
  coords[3] /= int(image.shape[0])
  return coords

for file in os.listdir(DIRECTORY):
  if(file.endswith(".xml")):
    fileContent = open(DIRECTORY + "/" +file, "r").read()
    imageName = fileContent.split("<filename>")[1].split("</filename>")[0]
    boxes = []
    for o in fileContent.split("<object>"):
      className = ""
      classNumber = -1
      for a in o.split("<name>"):
        className = a.split("</name>")[0]
        if className == "with_mask":
          classNumber = 0
        elif className == "without_mask":
          classNumber = 1
        elif className == "mask_weared_incorrect":
          classNumber = 2
      if(classNumber > -1):
        x_min = -1
        y_min = -1
        x_max = -1
        y_max = -1
        for boundbox in o.split("<bndbox>"):
          annotations = ""
          for row in boundbox.split("<xmin>"):
            value = row.split("</xmin>")[0]
            try:
              x_min = int(value)
            except:
              pass
          for row in boundbox.split("<ymin>"):
            value = row.split("</ymin>")[0]
            try:
              y_min = int(value)
            except:
              pass
          for row in boundbox.split("<xmax>"):
            value = row.split("</xmax>")[0]
            try:
              x_max = int(value)
            except:
              pass
          for row in boundbox.split("<ymax>"):
            value = row.split("</ymax>")[0]
            try:
              y_max = int(value)
            except:
              pass

        if(x_min >= 0 and y_min >= 0 and x_max >= 0 and y_max >= 0):
          coordinates = convert(file, [x_min, y_max, x_max, y_max])
          annotations = str(classNumber) + " " + str(x_min) + " " + str(x_max) + " " + str(y_min) + " " + str(y_max) + " " + "\n"
          annotationsFile = open("archive/annotations/" + imageName[0:-4] + ".txt", "a")
          annotationsFile.write(annotations)
          annotationsFile.close()

