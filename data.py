noSub=int(raw_input("Enter number of subjects: "))
details={}
names=[]
for no in range(0,noSub):
    name=raw_input("Enter subject name: ")
    marks=eval(raw_input("Enter marks: "))
    details[name]=marks
    names.append(name)
print "No of subjects: ",details[name]
print "Name of subjects: ",names
print "Total marks: ",sum(details.values())
