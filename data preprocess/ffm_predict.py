#!/usr/bin/python

import os
import time

ffm_predict="~/Documents/657A/project/ffm/ffm-predict "

fields=[5,6,9,13,16,19,21,22]

fn={}
for i in fields:
    fn[i]="../output/mk8_{0} ".format(i)
print(fn)

for f in fields:
    time_start = time.time()
    print(ffm_predict + "../dataset/subset99.ffm.norm " + fn[f]  + " ../output/o_predict_"+str(f))
    os.system(ffm_predict + "../dataset/subset99.ffm.norm " + fn[f]  + " ../output/o_predict_k8_"+str(f))
    time_end = time.time()

    #print('echo ' + str(time_end - time_start) + ">>o16")
    #os.system('echo ' + str(time_end - time_start) + " >>../output/o_vk8"+str(f))
