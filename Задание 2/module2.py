with open('travels.txt','r') as f:
    sum1=0
    sum2=0
    sum3=0
    for i in f:
        s=i[-4:]
        a=int(s)
        l=i.split()
        chislo=int(l[0])
        massa=int(l[6])
        if  chislo==1:
            sum1=sum1+massa

        elif  chislo==2:
            sum2=sum2+massa

        elif chislo==3:
            sum3=sum3+massa
print(sum1,sum2,sum3)





