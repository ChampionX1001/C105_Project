import os
import cv2


path = "ProjectImages\Images"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)

frame=cv2.imread(images[0])

height, width, channels = frame.shape
size = (width, height)        

print(len(images))
count = len(images)

out = cv2.VideoWriter('project.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 12, size)

for i in range(0, count-1, 1):
    frame=cv2.imread(images[i])
    out.write(frame)

out.release()