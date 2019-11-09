import random
n=int(input('题目数量：'))
m=int(input('数字范围：'))
i=1
list_right=[]
list_wrong=[]
while i<=n:
    a=random.randint(0,m+1)
    b=random.randint(0,m+1)
    d=random.randint(0,3)
    if d==0:
        print(str(i)+'> '+str(a)+'+'+str(b)+'=',end='')
        d0=int(input())
        if d0==a+b:
            list_right.append(i)
        else:
            list_wrong.append(i)
        i+=1
    if d==1 and a>=b:
        print(str(i)+'> '+str(a)+'-'+str(b)+'=',end='')
        d1=int(input())
        if d1==a-b:
            list_right.append(i)
        else:
            list_wrong.append(i)
        i+=1
    if d==2 :
        print(str(i)+'> '+str(a)+'*'+str(b)+'=',end='')
        d2=int(input())
        if d2==a*b:
            list_right.append(i)
        else:
            list_wrong.append(i)
        i+=1
    if d==3 and a>=b and b!=0 and a%b==0:
        print(str(i)+'> '+str(a)+'/'+str(b)+'=',end='')
        d3=int(input())
        if d3==a/b:
            list_right.append(i)
        else:
            list_wrong.append(i)
        i+=1
           
print('您总共答对了',len(list_right),'题')
print('您总共答错了',len(list_wrong),'题')
print('Right:',list_right)
print('Wrong:',list_wrong)