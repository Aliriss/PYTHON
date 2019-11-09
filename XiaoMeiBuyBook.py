ditGoods={'1012':['写作不求人',43.00,5],'1014':['数学实验班',15.70,5],'1015':['英语天天练',21.50,5],'1018':['时事大百科',16.80,5]}
Book={'1012':['写作不求人',43.00,0],'1014':['数学实验班',15.70,0],'1015':['英语天天练',21.50,0],'1018':['时事大百科',16.80,0]}
bookCode=['1012','1014','1015','1018']
TotalPrice=Money=Balance=0
print('All books are there:')
print('商品编号          名称            单价            库存')
for i in range(len(bookCode)):
    print(bookCode[i],'          ',ditGoods[bookCode[i]][0],'      ',ditGoods[bookCode[i]][1],'           ',ditGoods[bookCode[i]][2])
Money=float(input('Please check you money to ensure you have enough money to buy!'))
i=c=1
while i==1:
    k=1
    book=str(input('Please input book\'s code:'))
    if book in bookCode:
        amounts=int(input('Please input book\'s amounts:'))
        if Book[book][2]+amounts>5:
            print('Please check you amount and re-input.')
        else:
            if (TotalPrice+Book[book][1]*Book[book][2])<=Money:
                Book[book][2]+=amounts
                ditGoods[book][2]-=amounts
                TotalPrice+=Book[book][2]*Book[book][1]
            else:
                print('You don\'t have enough money to afford these, please check you shopping trolley!')
    else:
        print('Please check you book\'s code and make sure it is right')
    while k==1:
        print('Do you want to buy another?(Y/N)')
        print('You can check you books and amounts by inputing \'c\'!')
        jud=input()
        if jud=='N' or jud=='n':
            k=0
            break
        elif jud=='Y' or jud=='y':
            k=1
            break
        elif jud=='c':
            print('商品编号          名称            单价            数量')
            for i in range(len(bookCode)):
                if Book[bookCode[i]][2]!=0:
                    print(bookCode[i],'          ',Book[bookCode[i]][0],'      ',Book[bookCode[i]][1],'           ',Book[bookCode[i]][2])
            print('You balance is:',Price-TotalPrice)
            k=1
        else:
            print('I don\'t know, please scan the tip again!')
    if k==0:
        break

print('\n\nThese are your books, balance and receipt.\nHere you are!\nWelcome to come again!\n')
print('商品编号          名称            单价            数量')
for i in range(len(bookCode)):
    if Book[bookCode[i]][2]!=0:
        print(bookCode[i],'          ',Book[bookCode[i]][0],'      ',Book[bookCode[i]][1],'           ',Book[bookCode[i]][2])
print('You balance is:',Money-TotalPrice)
