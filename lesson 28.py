#Создать класс и вызвать пять объектов этого класса.
class Character:
    def __init__(self, name, race, clas, gender, hair, spec):
        self.name = name
        self.race = race
        self.clas = clas
        self.gender = gender
        self.hair = hair
        self.spec = spec
    def char(self):
        print('Ваш персонаж:\n', 'Имя:', self.name, ',', 'Расса:', self.race, ',', 'Класс: ', self.clas, ',', 'Пол: ', self.gender, ',', 'Цвет волос: ', self.hair, ',', 'Спек: ', self.spec)
pers1 = Character('Ри', 'человек', 'прист', 'женский', 'блонд', 'холи')
pers2 = Character('Тикимикк', 'орк', 'воин', 'мужской', 'черный', 'армс')
pers3 = Character('Аюми', 'эльф крови', 'палладин', 'женский', 'рыжий', 'холи')
pers4 = Character('Дейлмар', 'троль', 'охотник', 'мужской', 'синий', 'мм')
pers5 = Character('Семотан', 'нежить', 'разбойник', 'мужской', 'фиолетовый', 'комбат')
pers1.char()
pers2.char()
pers3.char()
pers4.char()
pers5.char()
