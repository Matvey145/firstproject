with open('Perepis.txt','r') as f:
    k=0
    for i in f:
        s=i[-5:]
        a=int(s)
        l=i.split()
        if a<1978 :
            print(l[0])
            k+=1
print('Кол-во жителей:',k)







