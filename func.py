a=eval(raw_input("Enter 1st value: "))
b=eval(raw_input("Enter 1st value: "))
op=raw_input("Enter an operator: ")
def calc():
    if op=="+":
        return a+b
    elif op=="-":
        return a-b
    elif op=="*":
        return a*b
    elif op=="/":
        return a/b
    else:
        return "Enter an proper value"
print "Answer: ",calc()
