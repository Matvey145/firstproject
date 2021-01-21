file=open('Perepis.txt','r+')
with open('Perepis.txt') as file:
    a=file.readlines()
    for i in range(1,len(a)):
        print(a[i])

