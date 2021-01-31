with open('travels.txt','r') as f:
    sum1=0
    sum2=0
    sum3=0
    sumlipki=0
    sumS=0
    k=0
    for i in f:
        s=i[-4:]
        a=int(s)
        l=i.split()
        chislo=int(l[0])
        massa=int(l[6])
        if  chislo==1:
            sum1+=massa

        elif  chislo==2:
            sum2+=massa

        elif chislo==3:
            sum3+=massa

        if str(l[2])=="Липки":
            sumlipki+=massa

        if chislo==1:
            sumS+=int(l[4])


print('Сумма грузов 1 октября:',sum1)
print('Сумма грузов 2 октября:',sum2)
print('Сумма грузов 3 октября:',sum3)


if sum1>sum2 and sum1>sum3:
    print('1 октября перевезено больше всего грузов:',sum1)
elif sum2>sum1 and sum2>sum3:
    print('3 октября перевезено больше всего грузов:',sum2)
elif sum3>sum1 and sum3>sum2:
    print('2 октября перевезено больше всего грузов:',sum3)

print('Масса всех грузов,отправленных из Липков:',sumlipki)
print('Суммарное расстояние,которое проеахл транспорт за 1 октября:',sumS)









