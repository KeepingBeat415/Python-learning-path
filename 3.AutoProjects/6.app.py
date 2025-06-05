from PyQt6.QtWidgets import QApplication,QWidget, QVBoxLayout, QHBoxLayout, QFileDialog
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit, QComboBox
from PyQt6.QtCore import Qt
from pathlib import Path

# ---- Make Sentence ----

def make_sentence():
    input_text = text.text()
    output_label.setText(input_text.capitalize() + '.')

app = QApplication([]) # instance
window = QWidget() # window
window.setWindowTitle('Sentence Maker') # window title

layout = QVBoxLayout() # layout inside of window
text = QLineEdit() # input line
layout.addWidget(text) # attach widget to layout

btn = QPushButton('Make')
layout.addWidget(btn)
btn.clicked.connect(make_sentence)

output_label = QLabel('')
layout.addWidget(output_label)

window.setLayout(layout) # attach layout into window
window.show()
app.exec()

# ---- Currency Converter ----
for bs4 import BeautifulSoup
import requests

def get_currency(in_currency, out_currency):
    url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1"
    content = requests.get(url).text 
    soup = BeautifulSoup(content, 'html.parser')
    rate = soup.find("span", class_="ccOutputRslt").get_text()
    rate = float(rate[:-4])
    
    return rate

def show_currency():
    input_text = float(text.text())
    in_cur = in_combo.currentText()
    target_cur = target_combo.currentText()
    rate = get_currency(in_cur, target_cur)
    output = input_text * rate
    output_label.setText(str(output))

app = QApplication([]) # instance
window = QWidget() # window
window.setWindowTitle('Currency Converter') # window title

layout = QVBoxLayout() # layout inside of window

layout_1 = QHBoxLayout()
layout.addLayout(layout_1) # add sub layout into main layout

output_label = QLabel('')
layout.addWidget(output_label) # add sub layout into main layout

layout_2 = QVBoxLayout() 
layout_1.addLayout(layout_2) # add nest layout

layout_3 = QVBoxLayout() 
layout_1.addLayout(layout_2) # add nest layout

in_combo = QComboBox()
in_combo.addItems(['USD','EUR','INR'])
layout_2.addWidget(in_combo) # add widget into layout

target_combo = QComboBox()
target_combo.addItems(['USD','EUR','INR'])
layout_2.addWidget(target_combo) # add widget into layout

text = QLineEdit() # input line
layout_3.addWidget(text) # attach widget to layout

btn = QPushButton('Convert')
layout_3.addWidget(btn, alignment=Qt.AlignmentFlag.AlignBottom)
btn.clicked.connect(show_currency)

window.setLayout(layout) # attach layout into window
window.show()
app.exec()

# # ---- File Destroyer ----
def open_files():
    filenames, _ = QFileDialog.getOpenFileName(window, 'Select Files') # return selected file list (file path)
    #print(filenames)
    message.setText('\n'.join(filenames))


def destroy_files():
    for filename in filenames:
        path = Path(filename)
        with open(path, 'wb') as file: # overwrite current file content
            file.write(b'')
        path.unlink()
    message.setText('Destruction Successful!')

filenames = []

app = QApplication([]) # instance
window = QWidget() # window
window.setWindowTitle('File Destroyer') # window title

layout = QVBoxLayout() # layout inside of window

description = QLabel('Select the files you want to destroy. The files will be <front color="red">permanently</front> deleted.')

layout.addWidget(description)

open_btn = QPushButton('Open Files')
open_btn.setToolTip('Open File') # pop info when mouse close it
open_btn.setFixedWidth(100)
layout.addWidget(open_btn, alignment=Qt.AlignmentFlag.AlignCenter)
open_btn.clicked.connect(open_files)

destroy_btn = QPushButton('Destroy Files')
destroy_btn.setFixedWidth(100)
layout.addWidget(destroy_btn, alignment=Qt.AlignmentFlag.AlignCenter)
destroy_btn.clicked.connect(destroy_files)

message = QLabel('')
layout.addWidget(message)

window.setLayout(layout) # attach layout into window
window.show()
app.exec()