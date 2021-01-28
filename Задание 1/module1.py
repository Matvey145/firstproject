with open('Perepis.txt','r') as f:
    k=0
    data1=int(input())
    data2=int(input())
    for i in f:
        s=i[-5:]
        a=int(s)
        l=i.split()
        if (data2<a<data1) or (data2>a>data1)  :
            print(l[0],l[1],l[2],l[3])
            k+=1
print('Кол-во этих жителей:',k)







