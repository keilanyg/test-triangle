from src.indentifier.validar_string import verificar_string
def test_string1():
    teste = "S2"
    assert verificar_string(teste) == True

def test_string2():
    teste = "progr4m"
    assert verificar_string(teste) == False

def test_string3():
    teste = "20rk13"
    assert verificar_string(teste) == False

def test_string4():
    teste = "Rt7ek"
    assert verificar_string(teste) == True
    
def test_string5():
    teste = "system"
    assert verificar_string(teste) == True

def test_string6():
    teste = "Sdr89@"
    assert verificar_string(teste) == False

def test_string7():
    teste = "Line35"
    assert verificar_string(teste) == True