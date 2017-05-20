#!/usr/bin/python

import os
import time

ffm_train="/Users/yananchen/Downloads/libffm-1.14/ffm-train "

fields=[5,6,9,13,16,19,21,22,99]

fn={}
for i in fields:
    fn[i]="../dataset/subset{0}.ffm.norm ".format(i)
print(fn)

for f in fields:
    time_start = time.time()
    print(ffm_train + fn[f] + "../output/m"+str(f) + " > ../output/o"+str(f))
    os.system(ffm_train + fn[f] + "../output/m"+str(f) + " > ../output/o"+str(f))
    time_end = time.time()

    #print('echo ' + str(time_end - time_start) + ">>o16")
    os.system('echo ' + str(time_end - time_start) + " >>../output/o"+str(f))


