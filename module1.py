with open("mat_dv.txt", "r") as file:
    sum8=0
    sum9=0
    sum10=0
    sum11=0
    for i in file:
        l=i.split()
        print(l)
        clas=int(l[2])
        print(clas)
        bal1=int(l[3])
        bal2=int(l[4])
        if clas==8 :
            sum8=bal1+bal2
        if clas==9 :
            sum9=bal1+bal2
        if clas==10 :
            sum10=bal1+bal2
        if clas==11 :
            sum11=bal1+bal2
print(sum8,sum9,sum10,sum11)



