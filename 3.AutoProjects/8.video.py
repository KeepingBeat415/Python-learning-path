import cv2

video = cv2.VideoCapture("files/video.mp4")

width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
nr_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)

fps = video.get(cv2.CAP_PROP_FPS)

#print(width, height, nr_frames, fps)

count = 1
while count <= nr_frames * fps:
    # read() - read frame per call
    success, frame = video.read()
    cv2.imwrite(f'files/images/{count}.jpg', frame)
    count += 1

# remove all frames
from pathlib import Path
path = Path('files/images')

for file in path.glob('*.jpg'):
    file.unlink()

# ---- Extract Frame at Timestamp ----
timestamp = '00:00:02.75'
timestamp_list = timestamp.split(':')
timestamp_list_floats = [float(i) for i in timestamp_list]

hours, minutes, seconds = timestamp_list_floats

frame_nr = hours * 3600 * fps + minutes * 60 * fps + seconds * fps

video.set(1, frame_nr)
success, frame = video.read()

cv2.imwrite(f'Frame at {hours}:{minutes}:{seconds}.jpg', frame)

# ---- Faces in Video ----
import cv2

video = cv2.VideoCapture("video.mp4") # read original video
success, frame = video.read()

height = frame.shape[0] # capture picture size
width = frame.shape[1]

face_cascade = cv2.CascadeClassifier('faces.xml') # face cascade
output = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'DIVX'), 30, (width, height)) # output video

while success:
    faces = face_cascade.detectMultiScale(frame, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 255), 4) # draw rectangle in the face
    output.write(frame)
    success, frame = video.read()

output.release() # generate video


# ---- Faces Using Blurred Area ----
import cv2

video = cv2.VideoCapture("files/smile.mp4")

success, frame = video.read() # read frame

height = frame.shape[0]
width = frame.shape[1]

face_cascade = cv2.CascadeClassifier('faces.xml')

output = cv2.VideoWriter('blurred_smile.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 30, (width, height))

while success:
    faces = face_cascade.detectMultiScale(frame, 1.1, 4)

    for (x, y, w, h) in faces:
        frame[y:y+h, x:x+w] = cv2.blur(frame[y:y+h, x:x+w], (50, 50))

    output.write(frame)

    success, frame = video.read()

output.release()