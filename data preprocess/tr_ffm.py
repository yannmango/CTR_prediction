#!/usr/bin/python

fields=[5,6,9,13,14,16,19,21,22]
#fname=["subset5_hased"]


fn={}
for i in fields:

    fn[i]="../dataset/subset{0}_hased".format(i)
print(fn)

for j in fields:
    fo=open(fn[j],"r")
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
            # print(apps)
    fo.close()
    print("apps done for ",str(j))
    foo = open(fn[j], "r")
    fow = open(fn[j]+".ffm", "w")

    click_his = {}

    for line in foo:
        ss = line.split(",")
        s = [ss[1], ss[0]] + ss[2:30]
        s[-1] = s[-1].strip("\n")
        app_count = []
        # apps used for every user
        for x in set(apps[s[12]]):
            app_count.append(x + ":" + str(apps[s[12]].count(x)))
        # print(app_count)

        # click history for user
        ffm_line = s[0]
        for sub in range(1, len(s)):
            ffm_line += " " + str(sub) + ":" + str(sub) + ":" + s[sub]

        for a in app_count:
            ffm_line += " 24:" + a

        if s[12] in click_his:
            clk = click_his[s[12]]
            click_his[s[12]] += s[0]
            ffm_line += " 25:1:" + str(clk.count("1"))
            ffm_line += " 25:0:" + str(clk.count("0"))
        else:
            clk = ""
            click_his[s[12]] = s[0]
        ffm_line += "\n"
        fow.write(ffm_line)
    fow.close()
    foo.close()