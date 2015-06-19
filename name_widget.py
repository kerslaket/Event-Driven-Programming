from PyQt4.QtGui import*
from PyQt4.QtCore import*

class NameWidget(QWidget):

    NameEntered = pyqtSignal()

    
    def __init__(self):
        super().__init__()

        self.label = QLabel("Please enter your name")
        self.name = QLineEdit()
        self.submit = QPushButton("Submit")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.name)
        self.layout.addWidget(self.submit)

        self.setLayout(self.layout)

        self.submit.clicked.connect(self.name_entered)

    def name_entered(self):
        name = self.name.text()
        print(name)
        self.NameEntered.emit()
