import time

while True:
    a = 0 # секунды
    b = 0 # минуты
    c = 0 # часы
    time_user = int(input("Введите количество секунд :"))
    for i in range(time_user):
        time.sleep(1)
        a += 1
        print("Прошло секунд :", a)
        if(b % 60) == 0:
            b += 1
            print("Прошло минут :", b)
        if (c % 3600) == 0:
            c += 1
            print("Прошло часов :", c)

    print("Время окончено!")


