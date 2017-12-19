#import psutil
import sys
import time


from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import pyqtSignal

class MainUIClass(QtWidgets.QMainWindow):
     def __init__(self,parent=None):
          super(MainUIClass, self).__init__(parent)

          self.ui = Ui_Wireshark()
          self.ui.setupUi(self)

          self.threadclass = ThreadClass()
          self.threadclass.start()
          self.threadclass.update_progressbar.connect(self.update_progressbar)

     def update_progressbar(self,val):
          self.ui.progressBar.setValue(val)
class Ui_Wireshark(object):
    def setupUi(self, Wireshark):
        Wireshark.setObjectName("Test")
        Wireshark.resize(1260, 693)
        self.centralwidget = QtWidgets.QWidget(Wireshark)
        self.centralwidget.setObjectName("centralwidget")
        self.progressBar=QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20,10, 600, 40))
        self.progressBar.setObjectName("progressBar")
        Wireshark.setCentralWidget(self.centralwidget)
        self.retranslateUi(Wireshark)
        QtCore.QMetaObject.connectSlotsByName(Wireshark)

    def retranslateUi(self, Wireshark):
        _translate = QtCore.QCoreApplication.translate
        Wireshark.setWindowTitle(_translate("Wireshark", "MainWindow"))



class ThreadClass(QtCore.QThread):
     update_progressbar = pyqtSignal(float)

     def __init__(self, parent=None):
         super(ThreadClass,self).__init__(parent)

     def run(self):
         val=0
         while True:
               #val = psutil.cpu_percent()
               val+=1
               time.sleep(2)
               self.update_progressbar.emit(val)


if __name__ == "__main__":
    a = QtWidgets.QApplication(sys.argv)
    app = MainUIClass()
    app.show()
    sys.exit(a.exec_())
