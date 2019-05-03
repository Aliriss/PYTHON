import random
# Input 
n=int(input('Please input the amount of men:'))
m=int(input('Please input the amount of benches:'))
while n>m or (n==m and n==0):
    # ERROR and re-input
    print('ERROR!!!Amount1 > amount2!')
    n=int(input('Please re-input the amount of men:'))
    m=int(input('Please re-input the amount of benches:'))
# Init the sequence of benches
lst=[]   
for i in range(m):
    lst.append(0)
print('Benches are empty(No man sit on benches):',lst)
# The first man sit down.
lst[random.randint(0,m-1)]=1
print('No  ',1,' man:',lst)
#  head of son-sequence
first=head=0
# tail of son-sequence
last=tail=0
sums=0   # max sum of sequence
for b in range(2,n+1):
    zero=sums=first=last=0  # Init
    for i in range(0,m):
        zero+=1
        if lst[i]!=0 or i==m-1:
            if lst[i]==0:
                last=m
            else:
                last=i
        if zero>sums:   
            sums=last-first
            head=first
            tail=last
        if first!=last:
            first=last
            zero=0
    lst[(int)((head+tail)/2)]=b   # man sits
    print('No ','%2d'%(b),' man:',lst) # the sequence of benches 