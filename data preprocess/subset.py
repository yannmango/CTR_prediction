#!/usr/bin/python

fields=[5,6,7,9,13,14,16,19,21,22]
values=['57ef2c87','968765cd','3e814130','b8d325c3','aad45b01','4','17653','2513','171','100076']

fo = open("../dataset/train", "r")
print(fo.name)

fn={}
for m in fields:
    fn["{0}".format(m)]="../dataset/subset{0}".format(m)

print(fn)

now=0
for line in fo:
    str_line=line.split(",")
    for i in fields:
        if str_line[i] == values[fields.index(i)]:
            fo=open(fn[str(i)],"a+")
            fo.write(line)
            fo.close()
    now+=1
    if now % 10000 ==0:
        print(now)



fo.close()