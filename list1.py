a=[1,1,1,1]
k=0
j=0
#The first, but error
for i in a:
    if int(i)==1:
        a.remove(i)
    else:
        continue
#The second is success
for i in range(0,len(a)):
    a.remove(1)
#The third is right
for i in a[::]:
    if i==1:
        a.remove(i)

print (a)