
from msilib.schema import SelfReg
import os,sys
import platform
import subprocess
from tkinter.filedialog import LoadFileDialog
from tkinter.ttk import Progressbar
from typing_extensions import Self
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from click import progressbar
# from COVIDET.index import verifier
from splash import Ui_SplashScreen
import time
counter = 0 
 


############SplashScreen#################################
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
#Frameless
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.Progress)
        # TIMER IN MILLISECONDS
        self.timer.start(70)
        self.show()
    def Progress(self):
        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        


        # INCREASE COUNTER
        counter += 1
        if counter == 101:
            time.sleep(0.5)
            #self.destroy()
            os.system(r"C:\Users\nimit\Desktop\File-Structure-Mini-Project-main\COVIDET\positive.txt")
            os.system(r"C:\Users\nimit\Desktop\File-Structure-Mini-Project-main\COVIDET\negative.txt")
             
           


            self.destroy()
            exit(0)
        
#class MainPage(QDialog):
    #def __init__(self):
        #super(QDialog,self).__init__()
        #LoadFileDialog(r"C:\Users\nimit\Desktop\File-Structure-Mini-Project-main\COVIDET\index.py",self)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    #window = QMainWindow() #=SplashScreen()
    sys.exit(app.exec_())
   

    

