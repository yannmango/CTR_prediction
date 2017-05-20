#!/usr/bin/python

import os
import subprocess

filename="../dataset/test_hased.data"
fields=[5,6,9,13,16,19,21,22]

fn={}
for i in fields:
    fn[i]="../dataset/subset{0}_hased".format(i)
print(fn)

for f in fields:
    print(fn[f])
    foo=open(fn[f],"r")
    last=subprocess.check_output("wc "+fn[f], shell=True)
    last_line=int(last.split(" ")[2])
    #print(last_line)
    line_num=0
    for line in foo:
        s = line.split(",")
        if s[2] == "14103000":
            os.system("tail -n "+str(last_line-line_num)+" "+fn[f]+" >>"+filename)
            foo.close()
            break

        line_num += 1
