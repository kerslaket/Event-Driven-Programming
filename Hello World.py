from PyQt4.QtGui import*
from PyQt4.QtCore import*

import sys

from name_widget import*
from hello_widget import*

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello World")

        self.stack = QStackedLayout() #create stacked layout
        self.name = NameWidget() #create component
        self.hello = HelloWidget()
        self.stack.addWidget(self.name) #add to stack
        self.stack.addWidget(self.hello)

        self.widget = QWidget() #add layout to central widget
        self.widget.setLayout(self.stack)
        self.setCentralWidget(self.widget)

        #connections
        self.name.NameEntered.connect(self.name_entered)
        self.hello.BackEntered.connect(self.back_entered)

    def name_entered(self):
        print("Got Here")
        self.stack.setCurrentIndex(1)
        name = self.name.name.text()
        self.hello.label.setText("Hello {0}".format(name))

    def back_entered(self):
        self.stack.setCurrentIndex(0)
        self.name.name.clear()

        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    window.raise_()
    app.exec_()
