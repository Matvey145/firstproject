with open('travels.txt','r') as f:
    sum=0
    for i in f:
        s=i[-4:]
        a=int(s)
    for i in range(1,27):
        sum=sum+a
print(sum)