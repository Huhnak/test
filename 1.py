import random
names = ['Степан', 'Елисей', 'Константин', 'Платон', 'Артур', 'Иван']
firstName = ['Пирожков', 'Иванов', 'Петров', 'Ломаносов', 'Пушкин', 'Степанов']
number = random.randint(0,100000)
clients = []
money = 0
for i in range(number):
    clients.append(names[random.randint(0,len(names)-1)]+' '+firstName[random.randint(0,len(firstName)-1)])
for i in range(number):
    c = clients.pop(0)
    spend = random.randint(0, 1000)
    money += spend
    print(f'Мы обслужили клиента {c} он потратил {spend}')
print(f'За сегодня мы заработали {money}')
