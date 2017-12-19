
class Packet():
    def __init__(self,num,tm,src,dist,protocol,length,info=''):
        self.num=num
        self.tm=tm
        self.src=src
        self.dist=dist
        self.protocol=protocol
        self.length=length
        self.info=info

    def show_packet(self):
        print(self.num+'==='+
        self.tm+'==='+
        self.src+'==='+
        self.dist+'==='+
        self.protocol+'==='+
        self.length+'==='+
        self.info+'===\n')
from scapy.all import *
interface_name=''
filter=''
pakets_list = []
num_of_pckts=1
# def extract_info(pckt):
#     new_pckt=Packet(num_of_pckts,pckt.time,pckt.src,pckt.dst,,pckt.len,)
#     ret_pckt=[str(num_of_pckts),pck]


pkts_sniffed = sniff(count=10,filter=filter)


# for i in range(10):
#     pkt = sniff(count=1,filter=filter)
#     print(pkt.summary())
#     print(pkt.show())
#     pakets_list.append(pkt)

