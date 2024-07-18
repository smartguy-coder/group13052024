import datetime
from typing import Self


class Person:
    INITIAL_MONEY: int = 50_000
    XYZ = 'xyz-yyy-xxx'
    CLASS_NAME = 'Mammals'

    population = []

    @staticmethod
    def get_planet_positions():
        return 'Venus - in the sky'

    @classmethod
    def write_person_life(cls, person: Self, action: str):
        with open('life.csv', mode='a', encoding='utf-8') as file:
            file.write(f'{id(person)},{person.name},{action},{cls.INITIAL_MONEY},{len(cls.population)}\n')

    def __init__(self, name: str, weight: float = 0, birthday: datetime.datetime = None):
        self.name = name.title()
        self.__person_birth_weight = weight
        self.birthday = birthday or datetime.datetime.now()
        self.__money = self.INITIAL_MONEY
        self.population.append(self)
        self.write_person_life(self, 'was born')


    def run(self):
        print(f'{self.name} is running...')

    # def get_age(self) -> int:
    #     now = datetime.datetime.now()
    #     return (now - self.birthday).days // 365

    @property
    def person_birth_weight(self) -> float:
        return self.__person_birth_weight

    @person_birth_weight.setter
    def person_birth_weight(self, value):
        login = input('Enter login >> ')
        if login == '123':
            self.__person_birth_weight = value

    @property
    def age(self) -> int:
        now = datetime.datetime.now()
        return (now - self.birthday).days // 365

    @property
    def money(self) -> int:
        return self.__money

    def __str__(self) -> str:
        return f'<Person {self.name}, {self.age} years old>'

    # def __repr__(self) -> str:
    #     return f'<Person {self.name}, {self.age} years old>'
    __repr__ = __str__

    def transfer_money_to_another_person(self, other: Self, summa: int):
        if self.__money >= summa:
            self.__money = self.__money - summa
            other.__money += summa

    def __eq__(self, other: Self) -> bool:
        return self.__money == other.__money

    def __ge__(self, other):
        return self.__money >= other.__money

    def __del__(self):
        print(f'Deleting {self}')
        len([])
        self.write_person_life(self, 'deleted')


print(Person.INITIAL_MONEY)

person1 = Person(name='alex', weight=37.600, birthday=datetime.datetime(year=2001, month=4, day=9))
person2 = Person(name='Donald', weight=4.2)

# person1.__del__()
# del Person.population[0]
# del person1
#
# Person.write_person_life(person1, 'custom')
# person1.write_person_life(person1, 'another')

Person.run(person1)
person1.run()

# print(id(person1))

# del person1

# print(id(Person.population[0]))

print(person1.INITIAL_MONEY)
person1.INITIAL_MONEY = 66600
print(person1.INITIAL_MONEY)
print(Person.INITIAL_MONEY)
Person.INITIAL_MONEY = 889999
person3 = Person(name='Donald', weight=4.2)

print(Person.population)
print(22, person1.population)

print(person1 == person2)
# print(person1.money == person2.money)
# print(person1.__eq__(person2))
#
# print(person1.__dict__)
# person1.hobbies = ['tennis']
# person1.name = 'Bill'
# # print(person1._Person__person_birth_weight)
# # print(person1.__person_birth_weight)
# print(person1.person_birth_weight)
#
# person2.transfer_money_to_another_person(person1, 1000)
#
# # person1.person_birth_weight = 4
# print(person1.__dict__)

# age_person_1 = person1.get_age()
age_person_1 = person1.age
print(age_person_1)

# print(person1.name)
# person2.run()
# person1.run()
# print(person1.birthday)
# print(person2.birthday)
#
print(person1)
print(person2)
print(person1 == person2)
print(person1 == person1)

tour_enrollment_list = [person1, person2]
print(tour_enrollment_list)

del Person.population[0]
del person1

print(person2.__dict__)
