#Добавить абстрактный класс Animal и переопределить в нём все будущие абстрактные методы.
from abc import abstractmethod
class Animal:
    def __init__(self):
        pass
    @abstractmethod
    def clasvid(self):
        pass
    @abstractmethod
    def agepopulation(self):
        pass
    @abstractmethod
    def rar(self):
        pass
class Fish(Animal):
    def __init__(self, clas, vid, age, population, rare):
        self.clas = clas
        self.vid = vid
        self.age = age
        self.population = population
        self.rare = rare
    def clasvid(self):
        print('Класс:', self.clas, ',', 'Вид: ', self.vid)
    def agepopulation(self):
        print('Возраст: ', self.age,',', 'Популяция в мире составляет: ', self.population)
    def rar(self):
        print('Редкость: ', self.rare)

animal = Fish('лучепёрые рыбы', 'скумбрия', '1 год', 'не установлено', 'часто')
animal.clasvid()
animal.agepopulation()
animal.rar()