import re

class Packet:

    def __init__(self, src=None,dst=None,type=None,length=None,
                 nb_segs=None,rss_hash=None,rss_queue=None,
                 hw_ptype=None,sw_ptype=None,l2_len=None,
                 inner_l2_len=None,l3_len=None,inner_l3_len=None,
                 l4_len=None,receive_queue=None, ol_flags=None):
        self.src = src
        self.dst = dst
        self.type = type
        self.length = length
        self.nb_segs = nb_segs
        self.rss_hash = rss_hash
        self.rss_queue = rss_queue
        self.hw_ptype = hw_ptype
        self.sw_ptype = sw_ptype
        self.l2_len = l2_len
        self.inner_l2_len = inner_l2_len
        self.l3_len = l3_len
        self.inner_l3_len = inner_l3_len
        self.l4_len = l4_len
        self.receive_queue = receive_queue
        self.ol_flags = ol_flags


# open packets file
with open('packets.txt') as packets_file:
    packets_file_content = packets_file.read() # Get the contents of the file

packets_info = []
# Seperate the contents of the file based on the keyword 'port' as Each packet is received on one of two ports
packets = packets_file_content.split('port ')
packets.pop(0) # remove the first element of the list since it doesn't contain anything
print("The number of packets : ", len(packets)) # print the number of the packets

search_pattern = "src=(?P<src>[\w:]*) [\S]* dst=(?P<dst>[\w:]*) [\S]* type=(?P<type>[\w]*) [\S]* length=(?P<length>[\w]*) [\S]* nb_segs=(?P<nb_segs>[\w]*) [\S]* RSS hash=(?P<rss_hash>[\w]*) [\S]* RSS queue=(?P<rss_queue>[\w]*) [[\S]* hw ptype: (?P<hw_ptype>[\w ]*)]* [[\S]* sw ptype: (?P<sw_ptype>[\w ]*) [\S]*]*[ \- ]* l2_len=(?P<l2_len>[\w]*)([ \- ]* inner_l2_len=(?P<inner_l2_len>[\w]*))*([ \- ]* l3_len=(?P<l3_len>[\w]*))*([ \- ]* inner_l3_len=(?P<inner_l3_len>[\w]*))*([ \- ]* l4_len=(?P<l4_len>[\w]*))*[ \- ]*Receive queue=(?P<receive_queue>[\w]*)[[\n ]*ol_flags: (?P<ol_flags>[\w ]*)]*"
for packet in packets:
    
    packet_analysis = re.search(search_pattern, packet)
    if(packet_analysis != None):
        packet_h = Packet(src = packet_analysis.group('src'),
                          dst = packet_analysis.group('dst'),
                          type = packet_analysis.group('type'),
                          length = packet_analysis.group('length'),
                          nb_segs = packet_analysis.group('nb_segs'),
                          rss_hash = packet_analysis.group('rss_hash'),
                          rss_queue = packet_analysis.group('rss_queue'),
                          hw_ptype = packet_analysis.group('hw_ptype').split(' ') ,
                          sw_ptype = packet_analysis.group('sw_ptype').split(' ') ,
                          l2_len = packet_analysis.group('l2_len'),
                          inner_l2_len = packet_analysis.group('inner_l2_len') ,
                          l3_len=packet_analysis.group('l3_len'),
                          inner_l3_len=packet_analysis.group('inner_l3_len'),
                          l4_len=packet_analysis.group('l4_len'),
                          receive_queue=packet_analysis.group('receive_queue'),
                          ol_flags=packet_analysis.group('ol_flags').split(' '))
                          


    # append the packet into the list
    packets_info.append(packet_h)
# printing the data in formatted way
for packet in packets_info:
    print("The src of the packet :", packet.src, " , The dst : ", packet.dst)
    print("The type : ", packet.type, ", the length : ", packet.length)
    print("the nb_segs : ",packet.nb_segs, " ,The rss hash : ", packet.rss_hash, ",The rss queue : ", packet.rss_queue)
    print("The hw ptype : ", packet.hw_ptype," , The sw ptype : ", packet.sw_ptype)
    print("l2_len : ", packet.l2_len, " , inner l2_len : ", packet.inner_l2_len)
    print("l3_len : ", packet.l3_len, " , inner l3_len : ", packet.inner_l3_len)
    print("l4_len : ", packet.l4_len, " , Receive queue : ", packet.receive_queue)
    print("ol_flags : ", packet.ol_flags)
    print("============================================================")
