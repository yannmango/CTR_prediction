#!/usr/bin/python
import time
fo = open("../dataset/test_hashed","r")

apps={}
for line in fo:
    s = line.split(",")
    if s[12] in apps:
        # print(dict[s[12]])
        apps[s[12]].append(s[8])
        #print(apps)
    else:
        apps[s[12]] = []
        apps[s[12]].append(s[8])
    #print(apps)
fo.close()

print("apps done")

foo = open("../dataset/test_hashed","r")
fow =open("../dataset/test.ffm","w")
click_his={}

for line in foo:
    ss=line.split(",")
    s=[ss[1],ss[0]]+ss[2:30]
    s[-1]=s[-1].strip("\n")
    app_count=[]
    # apps used for every user
    for x in set(apps[s[12]]):
        app_count.append(x+":"+str(apps[s[12]].count(x)))
    #print(app_count)

    # click history for user

    ffm_line=s[0]
    for sub in range(1,len(s)):
        ffm_line += " "+str(sub)+":"+str(sub)+":"+s[sub]

    for a in app_count:
        ffm_line += " 24:"+a

    if s[12] in click_his:
        clk=click_his[s[12]]
        click_his[s[12]] += s[0]
        ffm_line += " 25:1:"+str(clk.count("1"))
    else:
        clk=""
        click_his[s[12]] = s[0]
    ffm_line += "\n"
    fow.write(ffm_line)
fow.close()
foo.close()

# for k in fn:
#
#     fo = open(fn[k],"r")
#     apps={}
#     click={}
#     for line in fo:
#         s=line.split(",")
#         if s[12] in apps:
#             #print(dict[s[12]])
#             apps[s[12]].add(s[8])
#         else:
#             apps[s[12]]=set()
#             apps[s[12]].add(s[8])
#     fo.close()
#     print(fn[k])
#
#     foo = open(fn[k], "r")
#     fow = fo = open(fn[k]+"_addfea","w")
#     print("Writing in "+fn[k]+"_addfea")
#     for line in foo:
#         s = line.split(",")
#         fow.write(line.strip('\n')+","+"|".join(apps[s[12]])+","+click[s[12]]+'\n')
#
#     print("Writing in "+fn[k]+"_addfea"+"Done")
#     fow.close()
#     foo.close()
#     print("======\n")
print("All Done")
