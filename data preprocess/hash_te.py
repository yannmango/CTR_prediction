#!/usr/bin/python

import hashlib
import time

# fields=[5,6,7,9,13,14,16,19,21,22]
# fname=["subset","subtest"]
#
# fn={}
# for i in range(0,20):
#     for m in fname:
#         fn["{0}{1}".format(m,i)]="../dataset/{0}{1}".format(m,i)
#
#
# print(fn)
def myhash(s):
    ss = hashlib.md5(s.encode()).hexdigest()
    h=int(ss,16)%1000000
    return str(h);

# fields=[5,6,9,13,14,16,19,21,22]
fname=["test","_hashed"]

text=[5,6,7,8,9,10,11,12,13]
num=[0,1,2,3,4,14,15,16,17,18,19,20,21,22]

# fn={}
# for i in fields:
#     fn[i]="../dataset/{0}{1}".format(fname[0],i)
# print(fn)

fo=open("../dataset/test","r")
fow=open("../dataset/test_hased","w")

line=fo.readline()
row=0
for line in fo:
    s=line.split(",")
    #print(len(s))
    #print(s)
    ss=[s[0],"1"]+s[1:23]
    #print(ss)
    #time.sleep(1)
    for m in text:
        ss[m] = myhash(ss[m])
    fow.write(','.join(ss))
    row+=1
    if row %10000 ==0:
        print(row)

fow.close()
fo.close()
# for j in fields:
#     fo = open(fn[j],"r")
#     fow = open(fn[j]+"_hased","w")
#
#     print("Writing ", fn[j]+"_hased" )
#     for line in fo:
#         s = line.split(",")
#         for m in text:
#             s[m] = myhash(s[m])
#
#         fow.write(','.join(s))
#     fow.close()
#     fo.close()
#     print("Writing ", fn[j] + "_hased" , " Done")

print("All Done")
