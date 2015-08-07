for mynum0 in[1,2,3,4,5]:
    print "hello", mynum0
for mynum1 in'meet':
    print mynum1
names = ['meet','hardik','bhavik']
for na in names:
    print na

a=float(raw_input("enter temp:"))
for temp in[a]:
    if temp>=31 and temp<=35:
        print "Sunny day"
    elif temp>=36 and temp<=40:
        print "Warm day"
    elif temp>=41 and temp<=50:
        print "High temprature"
    else:
        print "invalid"
        
for temp in range(0,50):
    if temp>=31 and temp<=35:
        print "Sunny day"
    elif temp>=36 and temp<=40:
        print "Warm day"
    elif temp>=41 and temp<=50:
        print "High temprature"
    else:
        print "invalid"

name=['meet','hardik']
print name
name.append('bhavik')
print name

age={} #dictionary,assosiative array
age['a']=20
age['b']=21
age['c']=22
age['d']=23
print age
