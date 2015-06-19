import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class CropWindow(QMainWindow):
    """this class creates a main window to observe the growth of a crop"""

    #constructor
    def __init__(self):
        super().__init__() #call super class constructor
        self.setWindowTitle("Crop Simulator") # set window title

def main():
    crop_simulation = QApplication(sys.argv) #create new application
    crop_window = CropWindow() #create new instance of main window
    crop_window.show() # make instance visible
    crop_window.raise_() # raises instance to top of window stack
    crop_simulation.exec_() # monitor application for events

if __name__ == "__main__":
    main()
