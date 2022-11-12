#В наследниках класса из предыдущего урока переопределить методы из класса родителя, а также добавить не менее трёх значений по умолчанию.
class Animal:
    def __init__(self, clas = 'лучепёрые рыбы', vid = 'скумбрия', age = '1 год'):
        self.clas = clas
        self.vid = vid
        self.age = age

    def info(self):
        print('Класс:', self.clas, ',', 'Вид: ', self.vid, ',', 'Возраст: ', self.age)

class Podrobnosti1(Animal):
    def __init__(self, age, population = '3 особи'):
        self.age = age
        self.population = population
    def info(self):
        print('Возраст: ', self.age, 'Популяция в мире составляет: ', self.population)
animal = Podrobnosti1('10 лет', '600 особей')
animal1 = Animal('млекопитающее', 'Амурский тигр', '10 лет')
animal.info()
animal1.info()