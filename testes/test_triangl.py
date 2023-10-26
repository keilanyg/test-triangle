from src.triangulopast.triangulo import Triangulo


def test_all_values_zero():
    t = Triangulo()
    assert t.verificar(0, 0, 0) == False
    
def test_one_value_zero():
    t = Triangulo()
    assert t.verificar(5, 0, 7) == False
    
def test_sum_of_two_values_equal_to_the_third():
    t = Triangulo()
    assert t.verificar(4, 6, 10) == False

def test_valid_triangle():
    t = Triangulo()
    assert t.verificar(5, 6, 8) == True
