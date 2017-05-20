#!/usr/bin/python

from sklearn.metrics import f1_score
import os

#os.system("ls ../output")
y_true = [0]*39320
y_pred = [0]*39320


fo=open("../dataset/subset99.ffm.norm","r")

for i in range (0,39320):
    line=fo.readline()
    #print(line)
    s=line.split(" ")
    #print(s[0])
    if s[0] =="1":
        y_true[i] = 1

fo.close()
print("sum true: ")
print(sum(y_true))

fields=[5,6,9,13,16,19,21,22]

fn={}
for i in fields:
    fn[i]="../output/o_predict_k8_{0}".format(i)
print(fn)
for f in fields:
    print( fn[f])
    y_pred = [0] * 39320
    foo=open(fn[f],"r")
    line_num=0
    for line in foo:
        l = float(line)
        if l >= 0.5:
            y_pred[line_num] = 1
        line_num +=1


    print("sum: ", sum(y_pred))


    print(f1_score(y_true, y_pred, average='binary'))