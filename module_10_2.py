import time
import threading

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name=name
        self.power=power

    def run(self):
        enemy=100
        dayWar=0
        print(f'{self.name}, на нас напали!')
        while enemy:
            enemy-=self.power
            time.sleep(1)
            dayWar+=1
            print(f'{self.name}, сражается {dayWar}, осталось {enemy} врагов')
        print(f'{self.name}, одержал победу спустя {dayWar} дней(дня)!')



# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()
# Вывод строки об окончании сражения