# ---- scan/detect QR code ----
import cv2

image = cv2.imread('qr.png')

detector = cv2.QRCodeDetector()

url, coords, pixels = detector.detectAndDecode(image)

print(url, coords, pixels)

webbrowser.open(url)

# ---- caputre from webcarm ----
import cv2 

video = cv2.VideoCapture(1)
success, frame = video.read()

detector = cv2.QRCodeDetector()

while success:
    url, coords, pixels = detector.detectAndDecode(image)

    cv2.imshow('frame', frame)

    if url:
        webbrowser.open(url)
        break

    # press q key to exit 
    if cv2.waitKey(1) == ord('q'):
        break
    success, frame = video.read()

video.release()
cv2.destoryAllWindows()

# ---- generate QR Code ----
import qrcode 

img = qrcode.make('https://google.com')
img.save('qr1.png')