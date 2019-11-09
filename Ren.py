#a~z 
n=int(input('请输入偏移的数量：'))
dic={}
p=1
for i in range(26):
    p=i+n+97
    if p>122:
        p-=26
    dic.update({chr(i+ord('a')):chr(p)} )  #ord :ASCII 
x=[]
x=input("Please input you password as MingWen:")
miwen=''
for i in x:
    miwen+=dic[i]
print("You password changed into MiWen:",miwen)