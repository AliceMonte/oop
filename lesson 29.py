#Создайте класс на тему животных.
#В классе должен присутствовать конструктор не менее трёх методов.
class Animal:
    def __init__(self, clas, vid, age, population, rare):
        self.clas = clas
        self.vid = vid
        self.age = age
        self.population = population
        self.rare = rare
    def name(self):
        print('Класс:', self.clas, ',', 'Вид: ', self.vid, ',', 'Возраст: ', self.age)
    def pop(self):
        print('Популяция в мире составляет: ', self.population)
    def rar(self):
        print('Редкость: ', self.rare)
animal1 = Animal('млекопитающее', 'Амурский тигр', '10 лет', '600 особей', 'внесен в Красную Книгу РФ')
animal2 = Animal('птицы', 'Бразильский крохаль', '1 год', '250 особей', 'на грани исчезновения')
animal3 = Animal('лучепёрые рыбы', 'скумбрия', '1 год', 'не установлено', 'часто')
animal1.name()
animal1.pop()
animal1.rar()
animal2.name()
animal2.pop()
animal2.rar()
animal3.name()
animal3.pop()
animal3.rar()