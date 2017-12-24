from threading import Thread
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5 import QtCore
from scapy.all import *
import time


class Sniffer (QObject, Thread):
    show_packets_data = pyqtSignal('PyQt_PyObject',int)
    show_packets_data_after_filtering = pyqtSignal('PyQt_PyObject',int)

    def __init__(self,parent=None):
        super(Sniffer, self).__init__(parent)
        self.filter = ''
        self.prev_filter = ''
        self.timeToStop = False
        self.sniffed_packets_from_thread = PacketList()
        self.offline = None
        self.save_for_filtering = False
        self.interface = conf.iface
        self.flag = 0  # flag=0-->just sniff
        self.prev_flag = 0
        self.packet_numbers = 0

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
            # print("show_filered_item from thread " + field)
             #print("show_filer from thread " + self.filter)
            if field == self.filter:
                print("field = " + field)
                print("filter = " + self.filter)
                self.show_packets_data_after_filtering.emit(p, index)

        self.timeToStop = False
        #self.start_sniffing_from_thread()

    def run(self):
        print("running")


        #self.start_sniffing_from_thread()

        while 1:
            if self.flag == 0:
                sniff(count=1,prn=self.gui_callback, store=0,  iface=self.interface)
            elif self.flag==1:
                # stop capturing
                print("captured stop")
            elif self.flag == 2:
                # filtering either from [filter to '' ]or [from filter to filter ]or [from '' to filter]
                print("filtering")
                if self.filter == '' and self.prev_filter != '':
                    print("goes to filter")
                    self.capture_helper()
                elif self.filter ==self.prev_filter:
                    # do nothing same filter
                    print("do nothing same filter")

                else:
                    print("goes to capture")
                    self.filter_helper()
                self.flag = self.prev_flag #resume capturing
            elif self.flag == 3:
                print("restart capturing")
                self.flag = 0
                self.prev_flag = 0
                self.prev_filter = ''
                self.filter = ''
                self.packet_numbers = 0
                self.sniffed_packets_from_thread.clear()
            elif self.flag == 4:
                print("open file and show packets")
                #self.flag = 0
                self.prev_flag = 0
                self.prev_filter = ''
                self.filter = ''
                self.packet_numbers = 0
                self.sniffed_packets_from_thread.clear()
                self.show_read_packets()
                self.flag = 1

    def filter_helper(self):
        for index ,pkt in enumerate(self.sniffed_packets_from_thread):
            if self.test_data(pkt):
                # time.sleep(1)
                self.show_packets_data.emit(pkt, index)

    def capture_helper(self):
        for index, pkt in enumerate(self.sniffed_packets_from_thread):
            self.show_packets_data.emit(pkt, index)



    def stop(self):
        print("Sniffer stoping...")
        self.timeToStop = True

    def stopFilter(self, x):
        return self.timeToStop

    def start_sniffing_from_thread(self):
        print("Sniffer started...")
        sniff( prn=self.gui_callback, store=0, stop_filter = self.stopFilter, offline=self.offline,iface=self.interface)
        print("start_sniffing_from_thread :len of sniffed_packets_from_thread", len(self.sniffed_packets_from_thread))

    def show_read_packets(self):

        sniff(prn=self.gui_callback_after_filtering, store=0,  offline=self.offline)

    def test_data(self,data):
        try:
            protocol = data[1].get_field('proto')
            field = protocol.i2s[data[1].proto]

        except:  # for ipv6
            try:
                # print(item.show())
                field = data[1].nh

            except:
                print("error filtering with",data.show())
                field = ''

        if field == self.filter:
            # print("filter = OK")
            return True
        else:
            # print("filter = False")
            return False

    def gui_callback(self, data):
        # print("Sending data to GUI..."+str(self.offline))
        self.packet_numbers += 1
        self.sniffed_packets_from_thread.append(data)

        if self.filter != '':
            if self.test_data(data):
                self.show_packets_data.emit(data,self.packet_numbers)
                time.sleep(1)
        else:
            self.sniffed_packets_from_thread.append(data)
            self.show_packets_data.emit(data, self.packet_numbers)
            time.sleep(1)

    def gui_callback_after_filtering(self, data):
        # print("Sending data to GUI..."+str(self.offline))
        self.packet_numbers += 1
        self.sniffed_packets_from_thread.append(data)

        if self.filter != '':
            if self.test_data(data):
                self.show_packets_data.emit(data, self.packet_numbers)
                #time.sleep(1)
        else:
            self.sniffed_packets_from_thread.append(data)
            self.show_packets_data.emit(data, self.packet_numbers)
            #time.sleep(1)





