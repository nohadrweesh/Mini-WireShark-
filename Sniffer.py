from threading import Thread
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5 import QtCore
from scapy.all import *
import time


class Sniffer (QObject, Thread):
    show_packets_data = pyqtSignal('PyQt_PyObject')
    show_packets_data_after_filtering = pyqtSignal('PyQt_PyObject',int)

    def __init__(self,parent=None):
        super(Sniffer, self).__init__(parent)
        self.filter = ''
        self.timeToStop = False
        self.sniffed_packets_from_thread = PacketList()
        self.offline = None
        self.save_for_filtering = False
        self.interface = conf.iface

    def filter_captured_packets(self ):
        # self.offline = str(int(time.time()))+'.pcap'
        # wrpcap(self.offline, self.sniffed_packets_from_thread)
        # #self.start_sniffing_from_thread()
        # sniff(filter=self.filter, prn=self.gui_callback, store=0, offline=self.offline)
        self.timeToStop = True
        time.sleep(2)

        for index, p in enumerate(self.sniffed_packets_from_thread):
            protocol = p[1].get_field('proto')
            field = protocol.i2s[p[1].proto]
            print("show_filered_item from thread " + field)
            print("show_filer from thread " + self.filter)
            if field == self.filter:
                print("field = " + field)
                print("filter = " + self.filter)
                self.show_packets_data_after_filtering.emit(p, index)

        self.timeToStop = False
        #self.start_sniffing_from_thread()

    def run(self):
        print("running")

        #sniff(filter=self.filter, prn=self.gui_callback,)
        #while 1:
            #if self.timeToStop == False:
        self.start_sniffing_from_thread()

    def stop(self):
        print("Sniffer stoping...")
        self.timeToStop = True

    def stopFilter(self,x):
        return self.timeToStop

    def start_sniffing_from_thread(self):
        print("Sniffer started...")
        sniff( prn=self.gui_callback, store=0, stop_filter = self.stopFilter, offline=self.offline,iface=self.interface)
        print("start_sniffing_from_thread :len of niffed_packets_from_thread", len(self.sniffed_packets_from_thread))

    def show_read_packets(self):
        pckts=rdpcap(self.offline)
        sniff(prn=self.gui_callback, store=0,  offline=pckts, iface=self.interface)


    def gui_callback(self, data):
        print("Sending data to GUI..."+str(self.offline))

        self.sniffed_packets_from_thread.append(data)
        time.sleep(2)
        self.show_packets_data.emit(data)



