salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен
need_money = 0  # количество денег, чтобы прожить 10 месяцев

for current_month in range(months):
    if current_month == 0:
        delta = spend - salary
        need_money += delta
    else:
        spend = spend + spend * increase
        need_money += spend - salary
print(round(need_money))
