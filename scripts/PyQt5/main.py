import sys
from PyQt5 import QtWidgets

## pyuic5 -x INPUT.ui -o OUTPUT.py
## super(MyWindow, self).__init__()

#label = None
text = "You pressed button {} times"
count = 0

def onClick(label):
    global count
    count += 1

    #label.setText(str(count)) # if global, without lambda expression
    
    label.setText(text.format(count))
    label.adjustSize()

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    window.setGeometry(200, 200, 300, 300)
    window.setWindowTitle("PyQt5 Window")

    #global label
    label = QtWidgets.QLabel(window)
    label.setText("It's just a text")
    label.move(50, 50)

    button = QtWidgets.QPushButton(window)
    button.setText("Click me!")
    button.clicked.connect(lambda: onClick(label))

    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
