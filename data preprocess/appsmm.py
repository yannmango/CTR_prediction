
fields=[5,6,9,13,16,19,21,22]

fn={}
for i in fields:

    fn[i]="../dataset/subset{0}.ffm".format(i)
print(fn)

appsmax={}
appsmin={}

click=[0,0]
fo=open("../dataset/test.ffm")

for line in fo:
    #print(line)
    s=line[line.find("24:"):-1]
    ss=s.rstrip().split(" ")
    #print(s)
    #print(ss)
    for i in ss:
        if i.startswith("24:"):
            app = i.replace("24:","",1).split(":")
            #print(app)
            if app[0] in appsmax:
                appsmax[app[0]] = max(appsmax[app[0]], int(app[1]))
            else:
                appsmax[app[0]] = int(app[1])

            if app[0] in appsmin:
                appsmin[app[0]] = min(appsmin[app[0]], int(app[1]))
            else:
                appsmin[app[0]] = int(app[1])

    click_start=line.rfind("25:1:")
    if click_start !=-1:
        c=line[click_start:-1].split(" ")
        #print(c)
        click[0]=max(click[0],int(c[1].split(":")[2]))
        click[1]=max(click[1],int(c[0].split(":")[2]))
        #print(click)

fo.close()
print("max:",appsmax)
print("min:",appsmin)
print(click)

for f in fields:
    foo=open(fn[f],"r")
    print(fn[f])
    for line in foo:
        #print(line)
        s = line[line.find("24:"):-1]
        ss = s.rstrip().split(" ")
        # print(s)
        # print(ss)
        for i in ss:
            if i.startswith("24:"):
                app = i.replace("24:", "", 1).split(":")
                #print(app)
                if app[0] in appsmax:
                    appsmax[app[0]] = max(appsmax[app[0]], int(app[1]))
                else:
                    appsmax[app[0]] = int(app[1])

                if app[0] in appsmin:
                    appsmin[app[0]] = min(appsmin[app[0]], int(app[1]))
                else:
                    appsmin[app[0]] = int(app[1])

        click_start = line.rfind("25:1:")
        if click_start != -1:
            c = line[click_start:-1].split(" ")
            #print(c)
            click[0] = max(click[0], int(c[1].split(":")[2]))
            click[1] = max(click[1], int(c[0].split(":")[2]))
    foo.close()

    print("max:",appsmax)
    print("min:",appsmin)
    print(click)