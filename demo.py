# from scapy.all import *
# def show_pack(item):
#     item.show()
#
# sniff(count=0, prn=show_pack)
#


#
# from PyQt4 import QtCore, QtGui
#
#
# class Ui_GuiForm(object):
#     def setupUi(self, GuiForm):
#         GuiForm.setObjectName("GuiForm")
#         GuiForm.resize(381, 324)
#         self.centralwidget = QtGui.QWidget(GuiForm)
#         self.centralwidget.setObjectName("centralwidget")
#         self.gridLayout = QtGui.QGridLayout(self.centralwidget)
#         self.gridLayout.setObjectName("gridLayout")
#         self.textedit = QtGui.QTextEdit(self.centralwidget)
#         self.textedit.setReadOnly(True)
#         self.textedit.setObjectName("textedit")
#         self.gridLayout.addWidget(self.textedit, 0, 0, 1, 1)
#         GuiForm.setCentralWidget(self.centralwidget)
#         self.retranslateUi(GuiForm)
#         QtCore.QMetaObject.connectSlotsByName(GuiForm)
#
#     def retranslateUi(self, GuiForm):
#         GuiForm.setWindowTitle(QtGui.QApplication.translate("GuiForm", "myGUI", None, QtGui.QApplication.UnicodeUTF8))

import sys
from threading import Thread
from scapy.all import sniff
from PyQt4 import QtCore, QtGui
from testgui_ui import Ui_GuiForm


class SnifferThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.filter = "tcp port 80"
        self.timeToStop = False
        self.havegui = False

    def HaveGui(self):
        self.havegui = True

    def run(self):
        print
        "Sniffer started..."
        sniff(filter=self.filter, prn=self.pkt_callback, stopperTimeout=0.1, stopper=self.timeToStopChecker, store=0)

    def stop(self):
        print
        "Sniffer stoping..."
        self.timeToStop = True

    def timeToStopChecker(self):
        return self.timeToStop

    def gui_callback(self, data):
        print
        "Sending data to GUI..."
        # What am i supposed to put in here??

    def pkt_callback(self, pkt):
        data = pkt.sprintf('%IP.src% > %IP.dst%')
        print
        data
        if self.havegui: self.gui_callback(data)


class GuiForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_GuiForm()
        self.ui.setupUi(self)

    def callbackSetText(self, data):
        # Receiving data from sniffer thread
        # and puting them in a textedit widget
        self.ui.textedit.setText(data)


def terminateSnifferThread():
    sniffer.stop()
    sniffer.join()


if __name__ == '__main__':
    sniffer = SnifferThread()
    sniffer.start()

    if not "--nogui" in sys.argv[1:]:
        app = QtGui.QApplication([])
        window = GuiForm()
        window.show()
        sniffer.HaveGui()
        app.exec_()
        terminateSnifferThread()
    try:
        while (sniffer.timeToStop != True): pass
    except KeyboardInterrupt:
        terminateSnifferThread()