from class_data import Bank, MIN_CAPITAL, Person, Account
import pytest


@pytest.fixture(scope='class')
def person() -> Person:
    person = Person('Vinnyk', 'Lviv')
    return person


@pytest.fixture(scope='class')
def person2() -> Person:
    person = Person('Potap222', 'Lviv18')
    return person


@pytest.fixture(scope='class')
def bank_creation_payload(person) -> dict:
    payload = {'name': 'Poly', 'stakeholders': [person.name], 'capital': MIN_CAPITAL}
    return payload


@pytest.fixture(scope='class')
def bank(bank_creation_payload) -> Bank:
    bank = Bank(
        name=bank_creation_payload['name'],
        stakeholders=bank_creation_payload['stakeholders'],
        capital=bank_creation_payload['capital'],
    )
    return bank


@pytest.fixture(scope='class')
def account1(bank, person) -> Account:
    print(11111111111)
    account = bank.open_account(person)
    return account


@pytest.fixture(scope='class')
def account2(bank, person2) -> Account:
    print(22222222222)
    account = bank.open_account(person2)
    return account
