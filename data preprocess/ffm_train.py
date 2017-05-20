#!/usr/bin/python

import os
import time

ffm_train="~/Documents/657A/project/ffm/ffm-train "

fields=[5,6,9,13,16,19,21,22]

fn={}
for i in fields:
    fn[i]="../dataset/subset{0}.ffm.norm ".format(i)
print(fn)

for f in fields:
    time_start = time.time()
    #print(ffm_train + fn[f] + "../output/m"+str(f) + " > ../output/o"+str(f))
    os.system(ffm_train + " -k 8 " + fn[f] + "../output/mk8_"+str(f) + " > ../output/ok8_"+str(f))
    time_end = time.time()

    #print('echo ' + str(time_end - time_start) + ">>o16")
    os.system('echo ' + str(time_end - time_start) + " >>../output/ok8_"+str(f))


