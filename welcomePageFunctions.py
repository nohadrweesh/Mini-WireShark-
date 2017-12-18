from scapy.all import *
from scapy import  arch

#print(get_windows_if_list())
def get_interfaces_list():
    lst = get_windows_if_list()
    interfaces_list=[ diction['netid'] for diction in lst]
    return  interfaces_list

print(get_interfaces_list())


if_s=[{'name': 'Bluetooth Device (Personal Area Network)',
  'win_index': '11', 'description': '', 'guid': '{54EFAB94-7612-4900-AAAA-B3384396D619}',
  'mac': 'BC:85:56:20:CC:26', 'netid': 'Bluetooth Network Connection'},

 {'name': 'Ralink RT3290 802.11bgn Wi-Fi Adapter', 'win_index': '13', 'description': '',
  'guid': '{BBA45C0B-A8E2-420F-B3BB-E56610879255}', 'mac': 'BC:85:56:20:CC:25', 'netid': 'Wireless Network Connection'},

 {'name': 'Realtek PCIe GBE Family Controller', 'win_index': '14', 'description': '', 'guid': '{D49EE2C8-84D7-4E68-889D-0E53226771DE}',
  'mac': 'B4:B5:2F:90:E1:93', 'netid': 'Local Area Connection'},

{'name': 'VirtualBox Host-Only Ethernet Adapter','win_index': '15', 'description': '', 'guid': '{DE8EE7DE-1275-40BC-BC61-09B3DFD22602}',
 'mac': '0A:00:27:00:00:0F','netid': 'Local Area Connection 2'},

{'name': 'Microsoft Virtual WiFi Miniport Adapter', 'win_index': '17', 'description': '',
'guid': '{366379CD-58EC-4EF9-9799-434E5A0CED17}', 'mac': 'BC:85:56:20:CC:24', 'netid': 'Wireless Network Connection 2'}]


print(arch.get_working_if())
#interfaces_list=arch.get_working_ifaces()
#print(interfaces_list)
#lsc()
