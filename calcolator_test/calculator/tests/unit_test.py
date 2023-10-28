import sys

sys.path.append("calcolator_test/calculator")
sys.path.append("../")

from functions.sum import suma
from calculator.functions.prod import producto
from calculator.functions.div import division
import pytest

def obtener_datos_test_suma():
        return [("-2","3.5", 1.5), ("4","7", 11), ("-1","3.5", 2.5)]

@pytest.mark.parametrize('a, b, esperado', obtener_datos_test_suma())
def test_sum_parametrize(a, b, esperado):
        assert suma(a,b) == esperado

def obtener_datos_test_prod():
        return [("-2","3", -6), ("4","7", 28), ("-1","3", -3)]

@pytest.mark.parametrize('a, b, esperado', obtener_datos_test_prod())
def test_sum_parametrize(a, b, esperado):
        assert producto(a,b) == esperado

def obtener_datos_test_div():
        return [("-6","3", -2), ("4","2", 2), ("10","2", 5)]

@pytest.mark.parametrize('a, b, esperado', obtener_datos_test_div())
def test_sum_parametrize(a, b, esperado):
        assert division(a,b) == esperado