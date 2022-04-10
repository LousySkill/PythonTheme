import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 18, 6) == 3

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 10, 5) == 5

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 25, 25) == 50

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 10, 10) == 100

