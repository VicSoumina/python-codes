number_tickets = int(input("Введите количество билетов: "))
price_tickets = 0

for i in range(number_tickets):
    age = int(input("Введите ваш возраст: "))
    i += 1
    if age < 18:
        print("Бесплатно!")
    elif 18 <= age < 25:
        price_tickets += 990
        print('Билет стоит 990 рублей')
    else:
        price_tickets += 1390
        print("Билет стоит 1390 рублей")
if number_tickets > 3:
    price_tickets = price_tickets*0.9
    print("Стоимость билетов с 10% скидкой для 3+ человек: ", price_tickets)
else:
    print("Общая сумма к оплате", price_tickets)
    