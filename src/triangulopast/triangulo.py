class Triangulo:

    #Nenhum lado pode ter comprimento zero
    def __lado_Coprimento_0(self, a, b, c):
        if (a != b != c != 0):
            return True 
            
    #Cada lado deve ser menor que a soma de todos os lados dividida por 2;
    def __ladoMenor_SomadosLados_Div2(self, a, b, c):
        soma_lados = a + b + c 
        if a <  b <  c < ( soma_lados / 2 ):
            return True 
           
    #Um lado é igual à soma do outro
    def __ladoIgualSomadoOutro(self, a, b, c):
        if (a < b + c and b < a + c and c < a + b):
            return True
    
    def verificar(self, a, b, c):
        if (self.__ladoMenor_SomadosLados_Div2(a, b, c)  and self.__ladoIgualSomadoOutro(a, b, c) and self.__lado_Coprimento_0(a, b, c)):
            return True
        return False