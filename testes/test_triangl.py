from src.triangulopast.triangulo import Triangulo

def test_string1():
    t = Triangulo()
    assert t.verificar(0, 0, 0) == False
    
def test_string2():
    t = Triangulo()
    assert t.verificar(5, 0, 7) == False
    
def test_string3():
    t = Triangulo()
    assert t.verificar(30, 40, 50) == True
    
def test_string4():
    t = Triangulo()
    assert t.verificar(4, 6, 10) == False
    
def test_string5():
    t = Triangulo()
    assert t.verificar(5, 6, 8) == True

def test_string6():
    t = Triangulo()
    assert t.verificar(9, 8, 16) == True
