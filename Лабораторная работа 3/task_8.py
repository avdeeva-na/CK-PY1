money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить
# TODO Оформить решение
month = 0
dif = salary - spend
while money_capital + dif >= 0:
    spend *= 1.05
    dif = salary - spend
    money_capital = money_capital + dif
    month += 1
print(month)
#Чтобы ответ получился 3
# money_capital = 10000
# salary = 5000
#spend = 6000
# sum1 = money_capital
# sum2 = spend
# months = 0
# while sum1 - sum2 + salary - spend * 1.05 > 0:
    # sum1 += salary
    # sum2 += spend * 1.05
    # months += 1
# print(months)