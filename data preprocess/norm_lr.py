feamax=[18446737290438444192, 1, 14103023, 1012, 7, 998911, 998079, 936908, 999774, 999645, 827266, 999999, 999999, 999460, 5, 5, 24052, 1024, 1024, 2758, 3, 1835, 100248, 255]
feamin=[1398958831653, 0, 14102100, 1001, 0, 745, 264, 1927, 163, 3118, 37161, 0, 0, 432, 0, 0, 375, 120, 20, 112, 0, 33, -1, 1]
appdiff={}


fields=[5,6,9,13,16,19,21,22,99]

fea=list(range(0,24))
fea.remove(1)
print(fea)
def mynorm(x,i):
    n=(x-feamin[i])/(feamax[i]-feamin[i])
    #print(i,"-",x,"-",n)
    return round(n,8)


fn={}
for i in fields:

    fn[i]="../dataset/subset{0}_hased".format(i)
print(fn)

for f in fields:
    fo = open(fn[f], "r")
    fow= open(fn[f]+".norm","w")
    print(fn[f])

    for line in fo:
        s=line.split(",")

        for i in fea:
            s[i]=str(mynorm(int(s[i]),i))

        norm_line=",".join(s)
        # print(len(s))
        # print(s)
        fow.write(norm_line+"\n")
    fow.close()
    fo.close()