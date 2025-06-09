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