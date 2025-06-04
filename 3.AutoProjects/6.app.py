from PyQt6.QtWidgets import QApplication,QWidget, QVBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit

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