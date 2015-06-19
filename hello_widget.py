from PyQt4.QtGui import*
from PyQt4.QtCore import*

class HelloWidget(QWidget):

    BackEntered = pyqtSignal()
    
    def __init__(self):
        super().__init__()

        #components
        self.label = QLabel()
        self.back = QPushButton("Back")

        #create layout
        self.layout = QVBoxLayout()

        #add to layout
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.back)

        #set layout
        self.setLayout(self.layout)

        #connections
        self.back.clicked.connect(self.back_entered)

    def back_entered(self):
        self.BackEntered.emit()
