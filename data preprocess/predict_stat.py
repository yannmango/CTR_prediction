#!/usr/bin/python

testfile="../dataset/subset99.ffm.norm"

fo=open(testfile,"r")

line_no=0
for line in fo:
    label=line.split(" ")[0]
    total_line += 1