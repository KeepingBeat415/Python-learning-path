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