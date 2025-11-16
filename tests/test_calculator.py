# Unit tests for calculator class

import pytest
from src.calculator import Calculator

class TestCalculator:
    def setup_method(self):
        self.calc = Calculator()
    
    def test_add_positive_numbers(self):
        assert self.calc.add(2, 3) == 5

    def test_add_negative_numbers(self):
        assert self.calc.add(-2, -3) == -5
    
    def test_add_mixed_numbers(self):
        assert self.calc.add(-2, 3) == 1
    
    def test_add_floats(self):
        assert self.calc.add(2.5, 3.5) == 6.0
    
    def test_add_invalid_first_input(self):
        with pytest.raises(TypeError):
            self.calc.add("2", 3)

    def test_add_invalid_second_input(self):
        with pytest.raises(TypeError):
            self.calc.add(2, "3")

    def test_subtract_positive_numbers(self):
        assert self.calc.subtract(5, 3) == 2

    def test_subtract_negative_result(self):
        assert self.calc.subtract(3, 5) == -2
    
    def test_subtract_floats(self):
        assert self.calc.subtract(5.5, 2.5) == 3.0
    
    def test_subtract_invalid_first_input(self):
        with pytest.raises(TypeError):
            self.calc.subtract("5", 3)
    
    def test_subtract_invalid_second_input(self):
        with pytest.raises(TypeError):
            self.calc.subtract(5, "3")
    
    def test_multiply_positive_numbers(self):
        assert self.calc.multiply(2, 3) == 6
    
    def test_multiply_negative_numbers(self):
        assert self.calc.multiply(-2, -3) == 6
    
    def test_multiply_mixed_numbers(self):
        assert self.calc.multiply(-2, 3) == -6
    
    def test_multiply_floats(self):
        assert self.calc.multiply(2.5, 4.0) == 10.0
    
    def test_multiply_invalid_first_input(self):
        with pytest.raises(TypeError):
            self.calc.multiply("2", 3)
    
    def test_multiply_invalid_second_input(self):
        with pytest.raises(TypeError):
            self.calc.multiply(2, "3")
    
    def test__multiply_by_zero(self):
        assert self.calc.multiply(5, 0) == 0
    
    def test_divide_positive_numbers(self):
        assert self.calc.divide(6, 3) == 2  

    def test_divide_negative_numbers(self):
        assert self.calc.divide(-6, -3) == 2
    
    def test_divide_mixed_numbers(self):
        assert self.calc.divide(-6, 3) == -2    
    
    def test_divide_floats(self):
        assert self.calc.divide(7.5, 2.5) == 3.0    
    
    def test_divide_by_zero(self):
        with pytest.raises(ValueError):
            self.calc.divide(5, 0)  
    
    def test_divide_invalid_first_input(self):
        with pytest.raises(TypeError):
            self.calc.divide("6", 3)
    
    def test_divide_invalid_second_input(self):
        with pytest.raises(TypeError):
            self.calc.divide(6, "3")
    
    def test_divide_resulting_in_float(self):
        assert self.calc.divide(7, 2) == 3.5
    
    def test_divide_negative_resulting_in_float(self):
        assert self.calc.divide(7, -2) == -3.5
    
    def test_divide_zero_numerator(self):
        assert self.calc.divide(0, 5) == 0
    
    
    

