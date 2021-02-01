def uskorenie():
    a=(u2-u1)/t
    print(a)

def decor(uskorenie):
    def rastoynie():
      def uskorenie():
        s=(u1*t)+((a*(t*t))/2)
    return rastoynie





try:
    u1=float(input('Введите начальную скорость:'))
    u2=float(input('Введите конечную скорость:'))
    t=float(input('Введите время:'))
    uskorenie(u1,u2,t)


except TypeError:
        print('Ошибка.Введи число,а не что попало.')
except ZeroDivisionError:
        print('Ошибка.Где время не пиши 0.')

