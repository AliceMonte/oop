#В класс из предыдущего урока добавьте три класса-наследника на ваше усмотрение.
class Animal:
    def __init__(self, clas, vid, age):
        self.clas = clas
        self.vid = vid
        self.age = age

    def name(self):
        print('Класс:', self.clas, ',', 'Вид: ', self.vid, ',', 'Возраст: ', self.age)

class Podrobnosti1(Animal):
    def __init__(self, clas, vid, age, population):
        super().__init__(clas, vid, age)
        self.population = population
    def pop(self):
        print('Популяция в мире составляет: ', self.population)

class Podrobnosti2(Animal):
    def __init__(self, clas, vid, age, rare):
        super().__init__(clas, vid, age)
        self.rare = rare
    def rar(self):
        print('Редкость: ', self.rare)
class Podrobnosti3(Animal):
    def __init__(self, clas, vid, age, gender):
        super().__init__(clas, vid, age)
        self.gender = gender
    def sex(self):
        print('Пол: ', self.gender)
animal = Animal('млекопитающее', 'Амурский тигр', '10 лет')
animal1_1 = Podrobnosti1('млекопитающее', 'Амурский тигр', '10 лет', '600 особей')
animal1_2 = Podrobnosti2('млекопитающее', 'Амурский тигр', '10 лет', 'внесен в Красную Книгу РФ')
animal1_3 = Podrobnosti3('млекопитающее', 'Амурский тигр', '10 лет', 'мужской')
animal1_1.name()
animal1_1.pop()
animal1_2.rar()
animal1_3.sex()
