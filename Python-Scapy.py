from scapy import all*

pkt = rdpcap("CaptureFile.cap")
print(type(pkt))    # -> <class 'scapy.plist.PacketList'> 

#First Question
pkt_first = pkt[0]
print(type(pkt_first))  #what is the first place in pkt ? which type?
print(len(pkt_first))         #what is the length of the pkt file in byte?

#Second Question
counters={
    'google':0,
    'ynet':0,
    'SuperPhramLogo.gif':0,
    'HelloWorld':0
}

for packt in pkt:
    for key in counters.keys():
        counters[key]+=0 if str(packt).count(key)==0 else 1

print(counters)                     # -> {'google': 265, 'ynet': 318, 'SuperPhramLogo.gif': 0, 'HelloWorld': 0}

#Third Question
print(pkt)                      # -> <CaptureFile.cap: TCP:998 UDP:112 ICMP:0 Other:5>
print(len(pkt))                 # ->  1115  

#Four Question

pkt_len,pkt_indx=max([(len(packets[i]),i+1) for i in range(len(packets))])
print("pkt_len=",pkt_len,"pkt_indx=",pkt_indx)  # -> pkt_len= 1514 pkt_indx= 1053

#Five Question
pkt_len,pkt_indx=min([(len(packets[i]),i+1) for i in range(len(packets))])
print("pkt_len=",pkt_len,"pkt_indx=",pkt_indx)  # -> pkt_len= 42 pkt_indx= 471

#Six Question
get_packets=[str(p).split("Host: ")[1].split("\\r\\n")[0]   #when i use split it cuts the string until this 
for p in packets if str(p).count("GET")>0]
print(get_packets)


#Explain
a="208.20.00 HTTP/1.1\r\nHost: www.ynet.co.il\r\nConnection: keep-"
b=a.split("Host: ")
print(b)
c=b[1].split("\r\n")
print(c)