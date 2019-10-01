op=['+','-','*','/']
s=input()
s2=list(s)
flag=0
number1=number2=0.0
for i in range(0,len(s2)):
    if s[i] in op and i!=0:
        op_num=i
        if s[0]=='-':
            number1=-float((s[1:i]).strip())
        elif s[0:2] == '0x':
            number1=int(eval(s[:i].strip()))
        else:
            number1=float((s[:i]).strip())
        number2=float((s[i+1:]).strip())
if s[op_num]=='+':
    print("{:.2f}".format(number1+number2))
elif s[op_num]=='-':
    print("{:.2f}".format(number1-number2))
elif s[op_num]=='*':
    print("{:.2f}".format(number1*number2))
elif s[op_num]=='/':
    print("{:.2f}".format(number1/number2))
else:
    pass


'''
number1=number2=0.0
s2=''
for i,s2 in enumerate(s):
    if s2 in op and i!=0:
        if s[0]=='-':
            number1=-float((s[1:i]).strip())
        elif s[0:2] == '0x':
            number1=int(eval(s[:i].strip()))
        else:
            number1=float((s[:i]).strip())
        number2=float((s[i+1:]).strip())
    
    if s2=='+':
        print("{:.2f}".format(number1+number2))
    elif s2=='-' and s[0]!='-':
        print("{:.2f}".format(number1-number2))
    elif s2=='*':
        print("{:.2f}".format(number1*number2))
    elif s2=='/':
        print("{:.2f}".format(number1/number2))
    else:
        pass
'''