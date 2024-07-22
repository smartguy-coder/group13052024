from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum, unique, auto
from random import randint

from typing import Self


# class D(Enum):
#     m = auto()
#     m3 = auto()
#     m4 = auto()
#
#
# print(D.m3.value)

@unique
class General(Enum):
    HEALTH = 100
    # HEALTH = 100
    # OTHER = 100


@dataclass(frozen=True)
class Params:
    DWARF_POWER = 45
    DWARF_ACCURACY = 29
    ELVES_POWER = 24
    ELVES_ACCURACY = 60


class Character(ABC):
    def __init__(self, name: str, power: int, accuracy: int):
        self.name = name
        self.health = General.HEALTH.value
        self.power = power
        self.accuracy = accuracy

    @property
    def is_alive(self):
        return self.health > 0
    #
    # def dance(self):
    #     raise NotImplementedError

    # def attack(self, other: Self):
    def attack(self, other: 'Character') -> bool:
        print('-' * 20)
        if not self.is_alive:
            print(f'{self} and I am dead already')
            return False

        our_try = randint(1, 101)
        if our_try <= self.accuracy:
            # win_method = getattr(self, 'dance', None)
            # if win_method:
            #     win_method()
            print(f'{other.name} was hit was hit by {self.name}')
            other.health -= self.power

            if not other.is_alive:
                return True
            else:
                return False

    def __repr__(self):
        return self.name

    @abstractmethod
    def __str__(self):
        return f'My name is {self.name}'


class Dwarf(Character):
    def __init__(self, name: str):
        power = Params.DWARF_POWER
        accuracy = Params.DWARF_ACCURACY
        super().__init__(name, power, accuracy)

    def __str__(self):
        return f'I an Dwarf. My name is {self.name}'

    def dance(self):
        print('I am dancing')


class Elves(Character):
    def __init__(self, name: str):
        power = Params.ELVES_POWER
        accuracy = Params.ELVES_ACCURACY
        super().__init__(name, power, accuracy)

    def __str__(self):
        return f'I am Elves. My name is {self.name}'


d = Dwarf('Dwarf')
d2 = Dwarf('Dwarf2')
e = Elves('Elves')
# print(d.health)
# # e = Elves('Elves')
#
# print()
# d.attack(d2)
#
#
#
# print(type(d))
# print(isinstance(d, Dwarf))
# print(isinstance(d, Character))
d.attack(d2)
d.attack(d2)
d.attack(d2)
d.attack(d2)
d.attack(d2)
d.attack(d2)
d.attack(d2)
d.attack(d2)
d.attack(d2)
d.attack(d2)
e.attack(d)
e.attack(d)
e.attack(d)
e.attack(d)
e.attack(d)
e.attack(d)
e.attack(d)
e.attack(d)
e.attack(d)
e.attack(d)
e.attack(d)
e.attack(d)
e.attack(d)
e.attack(d)

ch = [Dwarf(str(randint(1, 10*9))) for number in range(100)]
ch2 = [Elves(str(randint(1, 10*9))) for number2 in range(100)]
print(ch[0])
print(ch)
print(ch2)

print(type(ch[0]))
print(type(ch2[0]))
