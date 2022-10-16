money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
needs = 0

month = 0  # количество месяцев, которое можно прожить

while True:
 needs = spend-salary
 money_capital -= needs
 if money_capital <= 0:
     break
 spend *= (1+increase)
 month += 1


print(month) # во время разбора этого задания на лекции вроде бы пришли к выводу что правильный ответ 5,так и не понял логику решения при котором ответ равен 3
