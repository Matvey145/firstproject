S=0
a=0
def decor(uskorenie):
    def rastoanie(a,u1,u2,t):
        uskorenie(a,u1,u2,t)
        S=(u1*t)+((a*t*t)/2)
        print('Расстояние:',S)
    return rastoanie

def uskorenie(a,v0,v1,t):
    a=(u2-u1)/t
    print('Ускорение:',a)

try:
    u1=float(input('Введите начальную скорость: '))
    u2=float(input('Введите конечную скорость: '))
    t=float(input('Введите время: '))
    uskorenie=decor(uskorenie)
    uskorenie(a,u1,u2,t)


except ZeroDivisionError:
    print('Введите правильное время(время не может быть=0)')
except ValueError:
    print('Введите правильный тип данных(число)')
