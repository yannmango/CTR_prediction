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

fields=[5,6,9,13,14,16,19,21,22]
fname=["subset"]


fn={}
for i in fields:
    for m in fname:
        fn["{0}{1}".format(m,i)]="../dataset/{0}{1}".format(m,i)
print(fn)
for k in fn:

    fo = open(fn[k],"r")
    apps={}
    click={}
    for line in fo:
        s=line.split(",")
        if s[12] in apps:
            #print(dict[s[12]])
            apps[s[12]].add(s[8])
        else:
            apps[s[12]]=set()
            apps[s[12]].add(s[8])

        if s[12] in click:
            click[s[12]]+=s[1]
        else:
            click[s[12]] =s[1]

    fo.close()
    print(fn[k])

    foo = open(fn[k], "r")
    fow = fo = open(fn[k]+"_addfea","w")
    print("Writing in "+fn[k]+"_addfea")
    for line in foo:
        s = line.split(",")
        fow.write(line.strip('\n')+","+"|".join(apps[s[12]])+","+click[s[12]]+'\n')

    print("Writing in "+fn[k]+"_addfea"+"Done")
    fow.close()
    foo.close()
    print("======\n")
print("All Done")
