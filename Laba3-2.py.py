while True:
    while True:
        try:
            x = float(input("введите числовое значение х: \n"))

            break
        except ValueError as e:
            print(e)

    while True:
        try:
            n = int(input("Введите числовое значение n:\n"))
            if n < 1:
                print("Ошибка.n<=1 Невохможно посчитать произведение.Пожалуйста введите число больше или равно 1")
                continue
            break
        except ValueError as e:
            print(e)

    p = 1
    for i in range (1, n+1):
        p = (x+i)/(i*i)*p

    print(p)
    z = input('продолжить вычисление? (y-да, другое-нет )\n')
    if z == "y":
        continue
    else:
        break
