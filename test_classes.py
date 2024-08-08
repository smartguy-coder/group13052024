import pytest

from class_data import Bank, MIN_CAPITAL


class TestBank:

    def test_bank_creation_too_low_capital(self):
        with pytest.raises(ValueError):
            Bank(name='645456', stakeholders=[], capital=MIN_CAPITAL - 1)

    def test_bank_add_one_stakeholder(self):
        bank = Bank(name='Poly', stakeholders=['Vinnyk'], capital=MIN_CAPITAL)
        assert len(bank.stakeholders) == 1

        bank.stakeholders.append('Potap')
        bank.capital += 1000

        assert len(bank.stakeholders) == 2
        assert bank.capital == MIN_CAPITAL + 1000

    def test_bank_creation_name(self):
        bank = Bank(name='Poly', stakeholders=['Vinnyk'], capital=MIN_CAPITAL)
        assert bank.name == 'VAT POLY'