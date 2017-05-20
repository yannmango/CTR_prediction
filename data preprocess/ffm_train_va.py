#!/usr/bin/python

import os
import time

ffm_train="~/Documents/657A/project/ffm/ffm-train "
testfile="~/Documents/657A/project/dataset/test.ffm "

fields=[5,6,9,13,16,19,21,22]

fn={}
for i in fields:
    fn[i]="../dataset/subset{0}.ffm.norm ".format(i)
print(fn)

for f in fields:
    time_start = time.time()
    cmd=ffm_train + " -p "+testfile + fn[f] + "../output/m_v"+str(f) + " > ../output/o_vk8"+str(f)
    print(cmd)
    os.system(cmd)
    time_end = time.time()

    #print('echo ' + str(time_end - time_start) + ">>o16")
    os.system('echo ' + str(time_end - time_start) + " >>../output/o_v"+str(f))


