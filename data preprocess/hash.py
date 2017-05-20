#!/usr/bin/python

import hashlib

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

fields=[5,6,9,13,14,16,19,21,22]
fname=["subset","_addfea"]

text=[5,6,7,8,9,10,11,12,13]
num=[0,1,2,3,4,14,15,16,17,18,19,20,21,22]

fn={}
for i in fields:
    fn[i]="../dataset/{0}{1}".format(fname[0],i)
print(fn)

for j in fields:
    fo = open(fn[j],"r")
    fow = open(fn[j]+"_hased","w")
#fo = open("../dataset/subset13_addfea","r")
    print("Writing ", fn[j]+"_hased" )
    for line in fo:
        s = line.split(",")
        for m in text:
            s[m] = myhash(s[m])
        #print(s[m])
        #print(','.join(s))
        fow.write(','.join(s))
    fow.close()
    fo.close()
    print("Writing ", fn[j] + "_hased" , " Done")

# s="f0d41ff1|33c4eb7c|39947756|9a6fd16e|73206397|92f5800b"
#
# print(myhash(s))

print("All Done")
