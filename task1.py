money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

mounth = 0
while money_capital + salary >= spend:
    rashod = spend - salary
    money_capital -= rashod
    spend = spend * (1 + increase)
    mounth += 1

print("Количество месяцев, которое можно протянуть без долгов:", mounth)
