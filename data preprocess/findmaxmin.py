

max=[-1000]*24
min=[10000000000000000000000000]*24
print(max[1].__class__)
print(min)


fields=[5,6,9,13,14,16,19,21,22]

fn={}
for i in fields:

    fn[i]="../dataset/subset{0}_hased".format(i)
print(fn)


for j in fields:

    fo=open("../dataset/train","r")
    fo = open(fn[j], "r")
    print(fn[j])
    line = fo.readline()
    for line in fo:
        s = line.split(",")
        for i in range(0, 24):
            #print(max[i])
            if int(s[i]) > max[i]:
                max[i] = int(s[i])
            if int(s[i]) < min[i]:
                min[i] = int(s[i])

    fo.close()

print(max)
print(min)