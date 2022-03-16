money = int(input('Сумма под проценты: '))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []
for key in per_cent:
    deposit.append(round(money * per_cent[key] / 100))
max_sum = max(deposit)
print(deposit)
print('Максимальная сумма, которую вы можете заработать: ', max_sum)
