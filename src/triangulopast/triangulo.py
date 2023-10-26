class Triangulo:

    #Nenhum lado pode ter comprimento zero
    def __lado_Coprimento_0(self, a, b, c):
        if (a != b != c != 0):
            return True 
        return False

    #Um lado é igual à soma do outro
    def __lado_menor_soma_dos_outros_lados(self, a, b, c):
        if a < b + c and b < a + c and c < a + b:
            return True
        return False
    
    def verificar(self, a, b, c):
        if self.__lado_menor_soma_dos_outros_lados(a, b, c) and self.__lado_Coprimento_0(a, b, c):
            return True
        return False