# Clase Calificador que: (1) tenga método validar_nota(nota) que retorne True si 0 ≤ nota ≤
# 100, False en caso contrario; (2) tenga método cargar_notas(*args) que reciba múltiples notas, 
# las valide, agregue solo las válidas a una lista interna, y retorne esa lista; (3) tenga método 
# promedio() que retorne el promedio de notas almacenadas.

class Calificador():
    def __init__(self):
        self.nota = []

    def validar_nota(self,nota):
        valida = False
        if 0 <= nota <= 100 :
            valida = True

        return valida
    
    def cargar_notas(self,*args):
        lista_validada = []

        for num in args:
            if self.validar_nota(num):
                lista_validada.append(num)
                self.nota.append(num)

        return lista_validada

    def promedio(self):
        return sum(self.nota) / len(self.nota)


calificacion1= Calificador()

print(calificacion1.cargar_notas(85,92,110,78,-5,88))
print(calificacion1.promedio())