import random
playerSymbol = '@'  # Символ персонажа
groundSymbol = '_'  # Символ пола
playerCoords = [0, 0]   # Координаты персонажа
mapSize = (2, 2)   # Размер карты
treasureCoords = [random.randint(0,mapSize[0]-1), random.randint(0,mapSize[1]-1)]   # создаем клад в случайной точке на карте

def drawMap():  # Создание карты
    for y in range(mapSize[1]):
        for x in range(mapSize[0]):
            if x == playerCoords[0] and y == playerCoords[1]:   # Размещение персонажа либо пола
                print(playerSymbol, end='')
            else:
                print(groundSymbol, end='')
        print()

drawMap()
while True:
    inputKey = input('Куда вы хотите двигаться (wasd) или копать клад (f): ')     # wasd символы для движения, f для копания
    if inputKey == 'w' and playerCoords[1] > 0:    # проверям хочет ли игрок идти наверх и не выйдет ли он за поле
        playerCoords[1] -= 1
    elif inputKey == 's' and playerCoords[1] < mapSize[1] - 1:
        playerCoords[1] += 1
    elif inputKey == 'a' and playerCoords[0] > 0:
        playerCoords[0] -= 1
    elif inputKey == 'd' and playerCoords[0] < mapSize[0] - 1:
        playerCoords[0] += 1
    elif inputKey == 'f':   # копание клада
        if playerCoords[0] == treasureCoords[0] and playerCoords[1] == treasureCoords[1]:   # проверка стоит ли персонаж на кладе
            print('Вы откопали клад!')
            treasureCoords = [random.randint(0, mapSize[0] - 1), random.randint(0, mapSize[1] - 1)]     # создаем новый клад в новом месте
        else:
            print('Тут ничего нет')
    print('------------------------------------------------------------')
    drawMap()   # отрисовываем карту

    
