#В классе из предыдущего урока приведите пример инкапсуляции.
class Animal:
    def __init__(self, clas, vid, age):
        self.clas = clas
        self.vid = vid
        self.age = age

    def __name(self):
        print('Класс:', self.clas, ',', 'Вид: ', self.vid, ',', 'Возраст: ', self.age)

class Podrobnosti1(Animal):
    def __init__(self, clas, vid, age, population):
        super().__init__(clas, vid, age)
        self.population = population
    def _pop(self):
        print('Популяция в мире составляет: ', self.population)

class Podrobnosti2(Animal):
    def __init__(self, clas, vid, age, rare):
        super().__init__(clas, vid, age)
        self.rare = rare
    def _rar(self):
        print('Редкость: ', self.rare)
class Podrobnosti3(Animal):
    def __init__(self, clas, vid, age, gender):
        super().__init__(clas, vid, age)
        self.gender = gender
    def _sex(self):
        print('Пол: ', self.gender)
animal = Animal('млекопитающее', 'Амурский тигр', '10 лет')
animal1_1 = Podrobnosti1('млекопитающее', 'Амурский тигр', '10 лет', '600 особей')
animal1_2 = Podrobnosti2('млекопитающее', 'Амурский тигр', '10 лет', 'внесен в Красную Книгу РФ')
animal1_3 = Podrobnosti3('млекопитающее', 'Амурский тигр', '10 лет', 'мужской')
animal1_1._Animal__name()
animal1_1._pop()
animal1_2._rar()
animal1_3._sex()

