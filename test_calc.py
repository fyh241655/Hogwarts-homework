import pytest
from demo1.python_code import Calculator


class TestCalculator:
    def setup_class(self):
        self.calc = Calculator()
        print('开始计算')

    def teardown_class(self):
        print('结束计算')

    @pytest.mark.parametrize('a,b', [(0, 9), (10, 20), (0.5, 0.9), (1000, 2000)])
    def test_add(self, a, b):
        self.calc.add(a, b)

    @pytest.mark.parametrize('a,b', [(0, 9), (10, 0), (1.5, 0.3), (1000, 2000)])
    def test_sub(self, a, b):
        self.calc.sub(a, b)

    @pytest.mark.parametrize('a,b', [(0, 9), (20, 0), (2.5, 3.5), (1000, 2000)])
    def test_mul(self, a, b):
        self.calc.mul(a, b)

    @pytest.mark.parametrize('a,b', [(0, 9), (3, 0), (1.8, 0.2), (1000, 2000)])
    def test_div(self, a, b):
        self.calc.div(a, b)
