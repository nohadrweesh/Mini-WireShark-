from threading import Thread
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5 import QtCore
from scapy.all import *
class Sniffer(QObject,Thread):
    def __init__(self):
        Thread.__init__(self)
        self.filter = ''


    def run(self):
        print("Sniffer started...")
        sniff(filter=self.filter, prn=self.gui_callback)

    def stop(self):
        print("Sniffer stoping...")




    def gui_callback(self, data):
        print("Sending data to GUI...")
        # What am i supposed to put in here??
        packetSend = pyqtSignal('PyQt_PyObject')
        #self.packetSend.connect(self.handle_trigger)

        # Emit the signal.
        packetSend.emit(data)

        #window.emit(QtCore.SIGNAL('packetReceived(PyQt_PyObject)'), data)


