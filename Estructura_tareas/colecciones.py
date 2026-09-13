# Ejercicios propuestos
# -----------------------------------------------------------------------------------------------------------------------------------
# RECORDEMOS EL METODO 
#  1 ENTENDER(E.P.S) -> 2 BOSQUEJO A MANO -> 3 DESCUBRIR EL PATRÓN
#  4 ESCRIBIR EL CÓDIGO -> 5 PRUEBA DE ESCRITORIO
# -----------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 1 _ Contar vocales en una cadena
    # Pide una frase al usuario y cuenta cuántas vocales (a, e, i, o, u) tiene. Ignora mayúsculas/minúsculas.
# ------------------------------------------------------------------------------------
# 1 ENTENDER EL PROBLEMA 

    # 1 ENTRADA _ qué me dan 
      # frase (str)

    # 2 PROCESO _ qué hago con eso
      # contar las vocales 

    # 3 SALIDA _ qué debo mostrar 
      # la cantidad de vocales que se encontro 
# ------------------------------------------------------------------------------------
# 2 BOSQUEJO A MANO 

  # frase = "hola como estas "
  # vocales = {a,e,i,o,u} 
  # pregunta = en la palabra frase se encuentra las siguientes vocales   
  # contador = 6 vocales
    
# ------------------------------------------------------------------------------------
# 3 DESCUBRIR EL PATRON 

  # convierte la cadena a minúsculas con .lower() y usa un set con las vocales 
  # para preguntar rápido si el carácter es vocal.
  
# ------------------------------------------------------------------------------------
#  4 ESCRIBIR EL CÓDIGO
frase = input("Ingrese una frase: ").lower()
vocales = {"a","e","i","o","u"}
contador= 0

for i in frase :
    if i in vocales:
        contador = contador + 1
print(f"{contador} vocales")
# ------------------------------------------------------------------------------------
# Ejercicio 2 _ Promedio y máximo de una lista de notas 
    # Dada una lista fija de notas [7, 8.5, 6, 9, 10, 5.5], calcula el promedio, la nota máxima y la mínima.
    # Imprime los tres valores con 2 decimales.
# ------------------------------------------------------------------------------------
# 1 ENTENDER EL PROBLEMA 

    # 1 ENTRADA _ qué me dan 
      # notas(list)

    # 2 PROCESO _ qué hago con eso
      # buscar el maximo el minimo y el promedio 

    # 3 SALIDA _ qué debo mostrar 
      # resulatados de la lista Max; Min;Promedio

# ------------------------------------------------------------------------------------
# 2 BOSQUEJO A MANO 

  # notas = [7, 8.5, 6, 9, 10, 5.5]
  # max = 10
  # min = 5.5
  # promedio = ( 7 + 8.5 + 6 + 9 + 10 + 5.5 )/6 = 7.66
# ------------------------------------------------------------------------------------
# 3 DESCUBRIR EL PATRON 

  # 
  # sum(notas)/len(notas), max(notas), min(notas).
  # 
# ------------------------------------------------------------------------------------
#  4 ESCRIBIR EL CÓDIGO
notas = [7, 8.5, 6, 9, 10, 5.5]
mayor = notas[0]
menor = notas[0]
suma= 0

for i in notas:
    suma = suma + i
    if i > mayor :   mayor = i 
    if i < menor: menor = i
    
promedio = suma / len(notas)
print(f"El promedio es {promedio:.2f}")
print(f"El mayor es {mayor:.2f}")
print(f"El menor es {menor:.2f}")

notas = [7, 8.5, 6, 9, 10, 5.5]
promedio = sum(notas) / len(notas)
print(f"Promedio: {promedio:.2f}")
print(f"Máximo:   {max(notas):.2f}")
print(f"Mínimo:   {min(notas):.2f}")

# ------------------------------------------------------------------------------------
# Ejercicio 2 _ Eliminar duplicados manteniendo el orden  
    # Dada la lista ["a", "b", "a", "c", "b", "d"], retorna una nueva lista sin duplicados 
    # respetando el orden de la primera aparición. (Con set se pierde el orden — hay que combinar set + list.)
# ------------------------------------------------------------------------------------
# 1 ENTENDER EL PROBLEMA 

    # 1 ENTRADA _ qué me dan 
      # lista(list)

    # 2 PROCESO _ qué hago con eso
      # nueva_lista sin duplicados  y con el mismo orden 

    # 3 SALIDA _ qué debo mostrar 
      # retornar la nueva lista
# ------------------------------------------------------------------------------------
# 2 BOSQUEJO A MANO 

  # lista = ["a", "b", "a", "c", "b", "d"]
  # nueva_lista = ["a","b","c","d"]

# ------------------------------------------------------------------------------------
# 3 DESCUBRIR EL PATRON 

  #  recorre la lista original y ve armando la nueva; usa un set auxiliar de «ya vistos»
  #  para chequear rápido.
  
# ------------------------------------------------------------------------------------
#  4 ESCRIBIR EL CÓDIGO
lista = ["a", "b", "a", "c", "b", "d"]

nueva_lista = list(sorted(set(lista)))
print(nueva_lista)

lista = ["a", "b", "a", "c", "b", "d"]
vistos = set()
nueva_lista = [] 

for i in lista :
    if i not in vistos:  # mira si dentro del conjunto no se encuentra el valor 
        vistos.add(i)   # si no esta  añade el valor al conjunto y vuelve a preguntar si ya esta o lo añade
        nueva_lista.append(i)

print(f"El resultado es : {nueva_lista}")

# ------------------------------------------------------------------------------------
# Ejercicio 4 _ Contar frecuencias de palabras 
    # Dado un texto, retorna un diccionario con la frecuencia de cada palabra (ignora mayúsculas).
    # Al final, imprime la palabra que más se repite.
# ------------------------------------------------------------------------------------
# 1 ENTENDER EL PROBLEMA 

    # 1 ENTRADA _ qué me dan 
      # texto(str)

    # 2 PROCESO _ qué hago con eso
      # crear un diccionario con la frecuencia de palabras 

    # 3 SALIDA _ qué debo mostrar 
      # retornar un diccionario con la frecuancia de palabras
# ------------------------------------------------------------------------------------
# 2 BOSQUEJO A MANO 

  # texto = "El perro y el gato y el perro"
  # {'el': 3, 'perro': 2, 'y': 2, 'gato': 1}
  # Más repetida: 'el' (3 veces)

# ------------------------------------------------------------------------------------
# 3 DESCUBRIR EL PATRON 

  #  texto.lower().split() para tokenizar. Usa dict.get(k, 0) + 1 para acumular. 
  # Para la más frecuente: max(conteo, key=conteo.get).

# ------------------------------------------------------------------------------------
#  4 ESCRIBIR EL CÓDIGO
texto = "El perro y el gato y el perro"
conteo = {}
for palabra in texto.lower().split():
    conteo[palabra] = conteo.get(palabra, 0) + 1

print(conteo)
#"Busca en conteo la palabra que tenga el valor más grande y guárdala en mas."
mas = max(conteo, key=conteo.get)  #  key le dice a max = Para comparar las palabras, mira el valor que tiene cada una."     get es lo que obtiene ese valor.
print(f"Más repetida: '{mas}' ({conteo[mas]} veces)")
# ------------------------------------------------------------------------------------


