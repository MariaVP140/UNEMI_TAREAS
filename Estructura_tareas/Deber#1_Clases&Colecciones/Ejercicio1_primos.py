class NumeroPrimo:
    def __init__(self):
        self.historial = []
        

    def es_primo(self,num):
        self.historial.append(num)
        primo = True
        if num < 2 :
            primo = False
        else : 
            for i in range(2,num):
                if num % i :
                    primo = False 
                    break

        return primo 

    def primos_en_rango(self, *args):
        primos = []
        for i in args :
            if self.es_primo(i):
                primos.append(i)

        return primos


primos1 = NumeroPrimo

print(primos1.es_primo(9))
print(primos1.primos_en_rango(5,7,6,9,10))
print(primos1.historial)