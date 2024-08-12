import pytest

from class_data import Bank, MIN_CAPITAL


class TestBank:

    def test_bank_creation_too_low_capital(self):
        with pytest.raises(ValueError):
            Bank(name='645456', stakeholders=[], capital=MIN_CAPITAL - 1)

    def test_bank_add_one_stakeholder(self, bank):
        # bank = Bank(name='Poly', stakeholders=['Vinnyk'], capital=MIN_CAPITAL)
        assert len(bank.stakeholders) == 1

        bank.add_stakeholder('Potap', 1000)

        assert len(bank.stakeholders) == 2
        assert bank.capital == MIN_CAPITAL + 1000

    def test_bank_creation_name(self, bank):
        # bank = Bank(name='Poly', stakeholders=['Vinnyk'], capital=MIN_CAPITAL)
        assert bank.name == 'VAT POLY'


class TestAccount:
    def test_new_account(self, account1):
        assert account1.balance == 0

    def test_add_money(self, account1):
        account1.put_money(2000)
        assert account1.balance == 2000

    def test_withdraw_money(self, account1):
        account1.withdraw_money(2000)
        assert account1.balance == 0


class TestAccountTransfer:
    def test_transfer1(self, account1, account2):
        account1.transfer_money(account2, 300)
        assert account2.balance == 300
        assert account1.balance == -300

    def test_transfer2(self, account1, account2):
        account1.transfer_money(account2, 200)
        assert account2.balance == 500
        assert account1.balance == -500
