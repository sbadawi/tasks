import re

packets_file = open('packets.txt')
print(packets_file)
print("Name : ", packets_file.name)
# print("The content of the file is : ")
packets_file_content = packets_file.read()



packets = packets_file_content.split('port ')
packets.pop(0)
print("The number of packets : ", len(packets))

# print("the first packet : ", packets[0])
for packet in packets:
    # print("The current packet : port", packet)
    # test_str = re.search('src=[\w:]*', packet)
    # print("The output of the search : ", test_str)
    # print(" => first group : ", test_str.group(0))
    #str_= str(teest).split("src=")
    # print("Teses :", str_)
    
        #test_packet = re.search('src=[\w:]* [\S]* dst=[\w:]* [\S]*', packet)
        #print("The src in this packet : ", ) # .group(0).split('src=')[1])
        print(packet)
        # print("The dst in this packet : ", re.search('dst=[\w:]*', packet).group(0).split('dst=')[1])
        # print("The type in this packet : ", re.search('type=[\w]*', packet).group(0).split('type=')[1])
        # print("The length in this packet : ", re.search('length=[\w]*', packet).group(0).split('length=')[1])
        # print("The nb_segs in this packet : ", re.search('nb_segs=[\w]*', packet).group(0).split('nb_segs=')[1])
        # print("The RSS hash in this packet : ", re.search('RSS hash=[\w]*', packet).group(0).split('RSS hash=')[1])
        # print("The RSS queue in this packet : ", re.search('RSS queue=[\w]*', packet).group(0).split('RSS queue=')[1])#hw ptype
        # print("The hw pytpe in this packet : ", re.search('hw ptype: [\w ]*', packet).group(0).split('hw ptype: ')[1])
        # print("The sw ptype in this packet : ", re.search('sw ptype: [\w ]*', packet).group(0).split('sw ptype: ')[1])
        # print("The l2_len in this packet : ", re.search('l2_len=[\w]*', packet).group(0).split('l2_len=')[1])
        # print("The inner_l2_len in this packet : ", re.search('inner_l2_len=[\w]*', packet).group(0).split('inner_l2_len=')[1])
        # print("The l3_len in this packet : ", re.search('l3_len=[\w]*', packet).group(0).split('l3_len=')[1])#ol_flags
        # print("The inner_l3_len in this packet : ", re.search('inner_l3_len=[\w]*', packet).group(0).split('inner_l3_len=')[1])
        # print("The Receive queue in this packet : ", re.search('Receive queue=[\w]*', packet).group(0).split('Receive queue=')[1])#inner_l2_len
        # print("The ol_flags in this packet : ", re.search('ol_flags: [\w ]*', packet).group(0).split('ol_flags: ')[1])

        print("============================================================")

#print(packets_file_content.split('port '))