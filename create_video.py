import os
import cv2

path = "C:/Users/kalya/Downloads/Project 117 - Video Album/Images"

images= []
extensions = ['.gif', '.png', '.jpg', '.jpeg', 'jfif']

for file in os.listdir(path):
    name,ext = os.path.splitext(file)
    
    if ext in extensions:
        file_name = path+'/'+file

        print(file_name)
        images.append(file_name)

print(len(images))
count = len(images)

frame = cv2.imread(images[0])
height, width, channels = frame.shape
size = (width, height)
print(size)

out = cv2.VideoWriter('project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

for i in range(0, count-1):
    image_read = cv2.imread(images[i])
    out.write(image_read)

print("Done")
