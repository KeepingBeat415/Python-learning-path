import cv2
import os

# ---- Read & Generate Image ----
color = cv2.imread('files\galaxy.jpeg', 0) # read image with gray scale

cv2.imwrite('files\galaxy-gray.jpeg', color) # output image

images = os.listdir('images')

for image in images:
    gray = cv2.imread('images/' + image, 0)
    cv2.imwrite(f'gray-{image}', gray)

image = cv2.imread('files\galaxy.jpeg')

# ---- Re-shape Image ----
print(image.shape)

def calculate_size(scale_percentage, width, height):
    new_width = int(width * scale_percentage / 100)
    
    new_height = int(height * scale_percentage / 100)
    return(new_width, new_height)

def resize(image_path, scale_percentage, resized_path):   
    image = cv2.imread(image_path)
    new_dim = calculate_size(scale_percentage, image.shape[1], image.shape[0])
    resized_image = cv2.resize(image, new_dim)
    cv2.imwrite(resized_path, resized_image)

resize('files/galaxy.jpeg', 10, 'files/reszied-galaxy.jpeg')

# ---- Detect Faces ----

image = cv2.imread('files/humans.jpeg', 1)

face_cascade = cv2.CascadeClassifier('faces.xml')

faces = face_cascade.detectMultiScale(image, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 255), 4)

cv2.imwrite('human_faces.jpeg', image)

# ---- Adding watermark to Image ----
image = cv2.imread('elfs.jpeg')
watermark = cv2.imread('watermark.png')

x = image.shape[1] - watermark.shape[1]
y = image.shape[0] - watermark.shape[0]

watermark_place = image[y:, x:] # extract replace image outs
cv2.imwrite('watermak_place.jpeg', watermark_place)

# create image with water marker
blend = cv2.addWeighted(watermake_place, 0.5, watermark, 0.5, 0)

image [y: , x: ] = blend
cv2.imwrite('elfs-watermarked.jpeg', image) # over-write the image with marker

# ---- Change Image Background ----
import numpy as np

foreground = cv2.imread("giraffe.jpeg")
background = cv2.imread("safari.jpeg")
width = foreground.shape[1]
height = foreground.shape[0]

resized_background = cv2.resize(background, (width, height))

for i in range(width):
    for j in range(height):
        pixel = foreground[j, i]
        if np.any(pixel == [28, 255, 76]):
            foreground[j, i] = resized_background[j, i]

cv2.imwrite('output.jpeg', foreground)


# ---- Collage Multiple Images ----
columns = 3
rows = 2

horizontal_margin = 40
vertical_margin = 20

images = os.listdir('images')
image_object = [cv2.imread(f'images/{filename}') for filename in images]

shape = cv2.imread('images/1.jpeg').shape

big_image = numpy.zeros((shape[0] * rows + horizontal_margin * (rows + 1), shape[1] * columns + vertical_margin * (columns + 1), shape[2]), numpy.uint8)

big_image.fill(255)

positions = [(x, y) for x in range(columns) for y in range(rows)]

for pos_x, pos_y in zip(positions, image_objects):
    x = pos_x * (shape[1] + vertical_margin) + vertical_margin
    y = pos_y * (shape[0] + horizontal_margin) + horizontal_margin
    big_image[y:y+shape[0], x:x+shape[1]] = image

cv2.imwrite('grid.jpeg', big_image)