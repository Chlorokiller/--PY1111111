salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

for _ in range(months): # добавляем единицу, т.к. 10 не входит в данное множество
    capital = spend - salary # определяем дефицит бюджета
    spend *= 1 + increase
    need_money += capital

print(round(need_money))
