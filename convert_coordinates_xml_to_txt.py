import os
import cv2

DIRECTORY = "kaggle_images/annotations"

annotations = ""

for file in os.listdir(DIRECTORY):
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
    
    x_min = -1
    y_min = -1
    x_max = -1
    y_max = -1
    for boundbox in o.split("<bndbox>"):
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
      boxes.append([x_min, y_min, x_max, y_max, classNumber])   
  
  boxCoordinates = ""
  for box in boxes:
    for coordinate in box:
      boxCoordinates += str(coordinate) + ","
    boxCoordinates = boxCoordinates[0:-1]
    boxCoordinates += " "
  boxCoordinates = boxCoordinates[0:-1]
  annotations += "kaggle_images/images/" + imageName + " " + boxCoordinates + "\n"

annotationsFile = open("kaggle_images/annotations.txt", "w")
annotationsFile.write(annotations)
annotationsFile.close()

    #for coordinate in box:
    #  boxCoordinates += str(coordinate) + ","
    #boxCoordinates = boxCoordinates[0:-1]
  #annotations += imageName + " " + boxCoordinates

  #print(boxCoordinates)
   # if(classNumber >= 0):
   #   print(className + "\t" + str(classNumber))


'''
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
    xml = [line for line in open(DIRECTORY + "/" + file, "r")]
    image_name = DIRECTORY + "/" + file[:-4]
    save_txt = open((image_name + ".txt"), "w")
    for line_index in range(len(xml)):
      if("xmin" in xml[line_index]):
        x_min = xml[line_index    ][9:-8]
        y_min = xml[line_index + 1][9:-8]
        x_max = xml[line_index + 2][9:-8]
        y_max = xml[line_index + 3][9:-8]
        new_coordinates = convert(image_name, [float(x_min), float(y_min), float(x_max), float(y_max)])
        save_txt.write(str(new_coordinates[0]) + " "  + str(new_coordinates[1]) + " " + str(new_coordinates[2]) + " " + str(new_coordinates[3]) + "0 ")
    save_txt.close()
'''