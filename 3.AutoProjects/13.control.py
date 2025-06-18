import cv2
from flask import Flask, render_template, Response

# ---- live webcam streaming on the browser ----
video = cv2.VideoCapture(1)

def get_frame():
    while True:
        success, frame = video.read()
        sc, encoded_image cv2.imencode('.jpg', frame)

        frame = encoded_image.tobytes()

        yield(b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed_url')
def video_feed():
    return Response(get_frame(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ = "__main__":
    app.run(debug=True)

# ---- capture screenshot ----
from mss import mss

with mss() as screen:
    screen.shot(output='screen.jpd')

# ---- caputre partial screenshot ----
from mss import mss, tools

with mss() as screen:
    part = {'top':257,'left':900,'width':500,'height':400}
    image = screen.grab(part)
    tools.to_png(image.rgb, image.size, output='output.png')

# ---- Recording Audio ----
import sounddevice
from scipy.io.wavfile import write

seconds = 5
fps = 44100

# store as np array
myrecording = sounddevice.rec(frames=seconds * fps, samplerate=fps, channels=1)

sounddevice.wait()
write('output.mp3', fps, myrecording)

# ---- control mouse ----
import pyautogui

position = pyautogui.position() # get current mouse position

pyautogui.moveTo(139, 288, duration=1)
pyautogui.move(100, 0, duration=2)

pyautogui.click(clicks=2)
pyautogui.doubleClick()

pyautogui.click(139, 280, clicks=2) # left click
pyautogui.click(139, 280, button='right') # right click on WINDOWS

pyautogui.dragTo(139, 280, button='right') # right click on Mac

# ---- control keyboard ----

position = pyautogui.position()
print(position)

pyautogui.doubleclick(139, 280)
pyautogui.press('down')
pyautogui.write('Python is good too\n')

pyautogui.hotkey('control', 'a')
pyautogui.hotkey('control', 'c')
pyautogui.press(1*['down'])
pyautogui.hotkey('control', 'v')

# ---- Drawing with Python ----
import pyautogui
from mss import mss, tools

pyautogui.moveTo(1218, 355, duration=1)
pyautogui.click()

pyautogui.drag(0, 200, duration=0.3, button='left') #Down 200px
pyautogui.drag(600, 0, duration=0.3, button='left') #Down 200px
pyautogui.drag(0, -3, duration=0.3, button='left') #Down 200px
