# 1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
# третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке
# (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов.
# При его нарушении выводить соответствующее сообщение и завершать скрипт.

#решение №1:
from time import sleep


class TrafficLight:
    __color = "nocolor"

    def running(self):
        while True:
            print('Red')
            sleep(7)
            print('Yellow')
            sleep(2)
            print('Green')
            sleep(7)
            print('Yellow')
            sleep(2)


trafficlight = TrafficLight()
trafficlight.running()

#решение №2

import time
import itertools


class TraficLight:
    __color = [['Red', [7, 31]], ['Yellow', [2, 33]], ['Green', [7, 32]], ['Yellow', [2, 33]]]

    def running(self):
        for light in itertools.cycle(self.__color):
            print(f"\r\033[{light[1][1]}m\033[1m{light[0]}\033[0m", end="")  #\r-переводит каретку в началу строчки
            time.sleep(light[1][0])


trf = TraficLight()
trf.running()

# 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.


class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_full_profit(self):
        return f"{self._length} м * {self._width} м * 25 кг * 5 см = {(self._length * self._width * 25 * 5) / 1000} т"


road_1 = Road(5000, 20)
print(road_1.get_full_profit())

# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'profit': wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_full_profit(self):
        return f"{sum(self._income.values())}"


manager = Position("Sam", 'Worker', "CEO", 500000, 125000)
print(manager.get_full_name())
print(manager.position)
print(manager.get_full_profit())

# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.


class Car:

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f"New car: {self.name} (color {self.color}) police car - {self.is_police}")

    def go(self):
        print(f"{self.name}: Car started")

    def stop(self):
        print(f"{self.name}: Car stoped")

    def turn(self, direction):
        print (f"{self.name}: Car turned {'to the left' if direction == 0 else 'to the right'}")

    def show_speed(self):
        print(f"{self.name}: Car speed -  {self.speed}")


class WorkCar(Car):

    def show_speed(self):
        return f"{self.name}: Car speed - {self.speed} - the speed is overhead!!"\
          if self.speed > 40 else f"{self.name}: Car speed - {self.speed}"


class SportCar(Car):
    def show_speed(self):
        print(f"{self.name}: Car speed -  {self.speed}")


class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


police_car = PoliceCar('COP', 'White', 80)
police_car.go()

# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationary:

    def __init__(self, title="something that can draw"):
        self.title = title

    def draw(self):
        print(f'Just start drawing! {self.title}')


class Pen(Stationary):
    def draw(self):
        print(f'Just strt drawing with Pen! {self.title}')


class Pencil(Stationary):
    def draw(self):
        print(f'Just start drawing with Pencil! {self.title}')


class Marker(Stationary):
    def draw(self):
        print(f'Just start drawing with Marker! {self.title}')


start = Stationary()
start.draw()

mark = Marker()
pen = Pencil()

mark.draw()
pen.draw()