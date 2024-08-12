from typing import Self

from faker import Faker

fake = Faker()

MIN_CAPITAL = 50_000_000


class Bank:

    def __init__(self, name: str, stakeholders: list['Person'], capital: int):
        if capital < MIN_CAPITAL:
            raise ValueError('Too low capital amount')
        self.name = f'VAT {name.upper()}'
        self.stakeholders = stakeholders
        self.capital = capital
        self.accounts = []

    def add_stakeholder(self, stakeholder, capital):
        self.stakeholders.append(stakeholder)
        self.capital += capital

    def open_account(self, person: 'Person'):
        account = Account(self, person)
        self.accounts.append(account)
        person.accounts.append(account)
        return account

    def __str__(self):
        return f'<Bank  {self.name}>'


class Account:
    def __init__(self, bank: 'Bank', person: 'Person'):
        self.bank = bank
        self.balance = 0
        self.iban = fake.iban()
        self.person = person

    def put_money(self, amount: int):
        self.balance += amount

    def withdraw_money(self, amount: int):
        self.balance -= amount

    def transfer_money(self, another_account: Self, amount: int):
        self.balance -= amount
        another_account.balance += amount

    def __str__(self):
        return f'<Account {self.iban} belongs to {self.person}>'

    __repr__ = __str__


class Person:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address
        self.accounts = []

    def __str__(self):
        return f'<Person {self.name}>'

    @property
    def number_of_accounts(self):
        return len(self.accounts)

    __repr__ = __str__


person = Person('Potap', 'Lviv')
person2 = Person('Potap222', 'Lviv18')
bank = Bank('Finance and credit', [person], 67797797789)

bank.open_account(person)
bank.open_account(person)
bank.open_account(person2)

print(bank.accounts)
print(person.accounts)
