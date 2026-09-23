# TALLER EJERCICIOS PASO A PASO 
# -----------------------------------------------------------------------------------------------------------------------------------
# RECORDEMOS EL METODO 
#  1 ENTENDER(E.P.S) -> 2 BOSQUEJO A MANO -> 3 DESCUBRIR EL PATRÓN
#  4 ESCRIBIR EL CÓDIGO -> 5 PRUEBA DE ESCRITORIO
# -----------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 1 _ Función para calcular el IVA
    # Escribir una función calcular_iva(precio) que reciba un precio y retorne el IVA (15%). Usarla desde el programa principal.
# ------------------------------------------------------------------------------------
# 1 ENTENDER EL PROBLEMA 

    # 1 ENTRADA _ qué me dan 
      # un precio

    # 2 PROCESO _ qué hago con eso
      # multiplicar por 0.15 dentro de la función

    # 3 SALIDA _ qué debo mostrar 
      # el IVA calculado

# ------------------------------------------------------------------------------------
# 2 BOSQUEJO A MANO 

  # def calcular_iva(precio):
  #     return precio * 0.15
  # Uso
  # iva = calcular_iva(80)   # 12.0  
  # imprimo iva              # 12.0  

# ------------------------------------------------------------------------------------
# 3 DESCUBRIR EL PATRON 

  # Este ejercicio parece trivial pero contiene la idea clave: la función no muestra
  # nada, solo devuelve un número. El print se hace fuera.

  # Ventaja: la función se puede reusar en 100 sitios distintos, cada uno decide si
  # mostrar, sumar, guardar o comparar el resultado.

# ------------------------------------------------------------------------------------
#  4 ESCRIBIR EL CÓDIGO

def calcular_iva (precio) :
    return precio * 0.15

precio = float(input("Precio: $ "))
iva = calcular_iva(precio)
print(f"IVA de ${precio} : ${iva:.2f}")
# ------------------------------------------------------------------------------------
# 🚀 Ahora tú
# Amplíala: define calcular_total(precio) que retorne precio + IVA usando la
# función anterior.
def calcular_total(precio):
    return precio + calcular_iva(precio)

precio_total = calcular_total(precio)
print(f"El precio total es ${precio_total:.2f}")
# -----------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 2 _ Función es_primo(n)
    # Escribir una función que reciba un número y retorne True si es primo, False si no.
# ------------------------------------------------------------------------------------
# 1 ENTENDER EL PROBLEMA 

    # 1 ENTRADA _ qué me dan 
      # un entero n

    # 2 PROCESO _ qué hago con eso
      # el algoritmo del módulo 3 dentro de la función

    # 3 SALIDA _ qué debo mostrar 
      # True o False
# ------------------------------------------------------------------------------------
# 2 BOSQUEJO A MANO 

  # es_primo(7) → devuelve True
  # es_primo(10) → devuelve False
  # es_primo(1) → devuelve False

  # Uso: if es_primo(numero): ...

# ------------------------------------------------------------------------------------
# 3 DESCUBRIR EL PATRON 

  # Encapsular el algoritmo de primos en una función lo vuelve reutilizable.
  # Ahora podemos, por ejemplo, imprimir todos los primos del 1 al 100 con un
  # bucle que llame a es_primo para cada número.

  # Fíjate que la función retorna un bool. Se puede usar directamente en un if: if es_primo(n):.

# ------------------------------------------------------------------------------------
#  4 ESCRIBIR EL CÓDIGO
def es_primo (n) :
    
    if n < 2 :
        return False
    else:
        for i in range (2,n):
            if n % i == 0:
                return False

    return True

num = int(input("Ingrese numero : "))
if es_primo (num) :
    print(f"{num} es primo")
else :
    print(f"{num} NO es primo")

# --- Uso 2: listar primos entre 2 y 30 ---

print("Primos entre 2 y 30:")
for k in range(2, 31):
    
    if es_primo(k):
        print(k, end=" ")
# ------------------------------------------------------------------------------------
# 🚀 Ahora tú
# Escribe una función contar_primos(a, b) que cuente cuántos primos hay entre a y b.
def contar_primos(a, b):
    contador = 0

    for i in range(a, b + 1):
        if es_primo(i):
            contador = contador + 1

    return contador


# Programa principal

a = int(input("\n Ingrese el inicio: "))
b = int(input("Ingrese el final: "))

cantidad = contar_primos(a, b)

print(f"Hay {cantidad} numeros primos entre {a} y {b}")
    
# -----------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 3 _ Suma de dígitos con función recursiva
    # Escribir una función suma_digitos(n) que retorne la suma de los dígitos de un número.
# ------------------------------------------------------------------------------------
# 1 ENTENDER EL PROBLEMA 

    # 1 ENTRADA _ qué me dan 
      # un entero n

    # 2 PROCESO _ qué hago con eso
      # extraer dígitos con % y //, acumular

    # 3 SALIDA _ qué debo mostrar 
      # la suma de los dígitos
# ------------------------------------------------------------------------------------
# 2 BOSQUEJO A MANO 

  # suma_digitos(4783):
  # suma = 0
  # 4783 % 10 = 3   → suma = 3,  n = 478
  #  478 % 10 = 8   → suma = 11, n = 47
  #   47 % 10 = 7   → suma = 18, n = 4
  #    4 % 10 = 4   → suma = 22, n = 0
  # fin → return 22
# ------------------------------------------------------------------------------------
# 3 DESCUBRIR EL PATRON 

  # Otra vez el patrón acumulador, esta vez dentro de una función. El bucle
  # while n > 0 extrae dígitos uno por uno.
  # Usamos abs(n) para que funcione con negativos.

# ------------------------------------------------------------------------------------
#  4 ESCRIBIR EL CÓDIGO
def sumar_digitos(n):
    n = abs(n)     # por si hay numero negativos
    suma = 0
    while n > 0 :
        suma = suma + n % 10 
        n = n // 10
    return suma

num = int(input("Número: "))
print(f"Suma: {sumar_digitos(num)}")

# También sirve para varios
for x in [123, 4783, 999]:
    print(f"{x} → {suma_digitos(x)}")
# ------------------------------------------------------------------------------------
# 🚀 Ahora tú
# Escribe es_narcisista(n): retorna True si el número es igual a la suma de sus dígitos elevados 
# al número de dígitos. Ej.: 153 = 1³+5³+3³.
def es_narcisista(n):
     n = abs(n)
     original =  n
     c = 0
     while n > 0:
            n = n // 10
            c = c + 1
            
     suma = 0
     n = n 

     while n > 0:
        digitos = n % 10 
        suma = suma + digito ** c
        n = n // 10 

     return suma == original

if es_narcisista(num):
    print(f"{num} es narcisista")
else:
    print(f"{num} NO es narcisista")
# -----------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 4 _ Menúmodular con funciones
    # Rediseñar el menú de saludar/despedir del módulo 3, pero esta vez con cada opción como función separada.
# ------------------------------------------------------------------------------------
# 1 ENTENDER EL PROBLEMA 

    # 1 ENTRADA _ qué me dan 
      # opciones del menú

    # 2 PROCESO _ qué hago con eso
      # función por opción, menú principal que las llama

    # 3 SALIDA _ qué debo mostrar 
      # el resultado de cada opción
# ------------------------------------------------------------------------------------
# 2 BOSQUEJO A MANO 

  # saludar()   → pide nombre, muestra saludo
  # despedir()  → pide nombre, muestra despedida 
  # menu()      → muestra opciones y llama a la función correcta
# ------------------------------------------------------------------------------------
# 3 DESCUBRIR EL PATRON 

  # Dividir el programa en funciones lo vuelve mantenible: cada función hace
  # UNA cosa; el bucle principal solo despacha.
  # Además cada función se puede probar por separado.

# ------------------------------------------------------------------------------------
#  4 ESCRIBIR EL CÓDIGO
def saludar (nombre,saludo="Hola"):
    print(f"{saludo} {nombre}" )

def despedir (nombre,saludo="Adios"):
    print(f"{saludo} {nombre}")

def mostrar_menu ():
    print("\nBienvenido usuario :\n")
    print("------MENÚ------")
    print("1.Saludar")
    print("2.Despedida")
    print("3.Salir")

# Programa principal
while True:
    mostrar_menu()
    opcion = input("Opción: ")
    if opcion == "1":
        nombre = input("Ingrese su nombre : ")
        saludar(nombre)
    elif opcion == "2":
        nombre = input("Ingrese su nombre : ")
        despedir(nombre)
    elif opcion == "3":
        print("Adiós")
        break
    else:
        print("Opción inválida")
# ------------------------------------------------------------------------------------
# 🚀 Ahora tú
# Añade una función calcular() que pida dos números y muestre suma, resta, multiplicación
# y división. Nueva opción del menú.
def menu():

    print("\nBienvenido usuario\n")
    print("----- MENÚ -----")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")


def calcular(operacion, a, b):

    if operacion == "suma":
        print(f"{a} + {b} = {a + b}")

    elif operacion == "resta":
        print(f"{a} - {b} = {a - b}")

    elif operacion == "multiplicacion":
        print(f"{a} x {b} = {a * b}")

    elif operacion == "division":
        if b != 0:
            print(f"{a} ➗ {b} = {a / b}")
        else:
            print("División inválida")


while True:

    menu()

    opcion = input("Opción: ")

    if opcion == "1":

        a = float(input("Ingrese número 1: "))
        b = float(input("Ingrese número 2: "))

        calcular("suma", a, b)

    elif opcion == "2":

        a = float(input("Ingrese número 1: "))
        b = float(input("Ingrese número 2: "))

        calcular("resta", a, b)

    elif opcion == "3":

        a = float(input("Ingrese número 1: "))
        b = float(input("Ingrese número 2: "))

        calcular("multiplicacion", a, b)

    elif opcion == "4":

        a = float(input("Ingrese número 1: "))
        b = float(input("Ingrese número 2: "))

        calcular("division", a, b)

    elif opcion == "5":

        print("¡Adiós!")
        break

    else:

        print("Opción inválida")

# -----------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 5 _ Función área de rectángulo
    # Función area_rectangulo(base, altura) que retorne el área.
# ------------------------------------------------------------------------------------
# 1 ENTENDER EL PROBLEMA 

    # 1 ENTRADA _ qué me dan 
      # numero(input)

    # 2 PROCESO _ qué hago con eso
      # buscar elarea de rectangulo con la formula

    # 3 SALIDA _ qué debo mostrar 
      # retorna el área 
# ------------------------------------------------------------------------------------
# 2 BOSQUEJO A MANO 

  # base = 5  ; altura = 6
  # area = 5 x 6
  # resultado = 30 

# ------------------------------------------------------------------------------------
# 3 DESCUBRIR EL PATRON 

  # Para crear una funcion el patron siempre van a ser los datos de un rectangulo 
  # si desea buscar el área, la area se puede encontrar con la formula.

# ------------------------------------------------------------------------------------
#  4 ESCRIBIR EL CÓDIGO
def area_rectangulo(base,altura):
    return base * altura 

base = float(input("ingrese la base del rectangulo: "))
altura = float(input("ingrese la altura del rectangulo: "))

print(f"El area del un rectangulo es {area_rectangulo(base,altura)}")

# -----------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 6 _ Función máximo de tres 
    # Función maximo(a, b, c) que retorne el mayor de tres números.
# ------------------------------------------------------------------------------------
# 1 ENTENDER EL PROBLEMA 

    # 1 ENTRADA _ qué me dan 
      # a,b,c(input)

    # 2 PROCESO _ qué hago con eso
      # encontrar el maximo de tres numeros.

    # 3 SALIDA _ qué debo mostrar 
      # el resultado mostrara el mayor.
# ------------------------------------------------------------------------------------
# 2 BOSQUEJO A MANO 

  # a = 7  ; b = 9  , c = 5
  # mayor = 7 
  # 9 > 7 =  Si entonces mayor = 9
  # 5 > 9 = No 
  # resultado = 9   

# ------------------------------------------------------------------------------------
# 3 DESCUBRIR EL PATRON 

  # Ir comparando sucesivamente con operadores de comparación , utilizamamos 
  # el patron campeon.
  # tampien podemos hacer de manera mas rapida con max().

# ------------------------------------------------------------------------------------
#  4 ESCRIBIR EL CÓDIGO
# -----------------------------------------------------------------------------------------------------------------------------------
def maximo(a, b, c):
    return max(a, b, c) 

def maximo_manual (a,b,c):
    mayor = a
    if b > mayor : mayor = b

    if c > mayor : mayor = c
   
    return mayor 


print(f"El mayor de (5,9,3) es {maximo_manual(5,9,3)} ")

print(f"El mayor de (5,9,3) es {maximo(5,9,3)} ")

# -----------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 7 _ Función es_biesto(año)
    # Un año es bisiesto si es divisible entre 4 y no entre 100, O si es divisible entre 400.
# ------------------------------------------------------------------------------------
# 1 ENTENDER EL PROBLEMA 

    # 1 ENTRADA _ qué me dan 
      # año(input)

    # 2 PROCESO _ qué hago con eso
      # calcular si año es bisiesto

    # 3 SALIDA _ qué debo mostrar 
      # resultado = año bisiesto
# ------------------------------------------------------------------------------------
# 2 BOSQUEJO A MANO 

  # año = 2024
  # 2024 % 4 == 0  y 2024 % 100 != 0  o 2024 % 400 == 0
  # 0 == 0 Si    y   24 != 0 Si     o    24 == 0 No
  #             V               O           F
  #                         Verdadero
  #  resultado = 2024 si es bisiesto    
# ------------------------------------------------------------------------------------
# 3 DESCUBRIR EL PATRON 

  # El orden de los if importa: 2000 es divisible por 400, es bisiesto (aunque también por 100).

# ------------------------------------------------------------------------------------
#  4 ESCRIBIR EL CÓDIGO
def es_bisiesto(año):

    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    else :
        return False

año = int(input("Ingrese año : "))

if es_bisiesto(año):
    print(f"El {año} es bisiesto ")
else :
    print(f"El {año} no es bisiesto")

# Pruebas
for y in [2024, 2023, 2000, 1900]:
    print(f"{y}: {es_bisiesto(y)}")

# -----------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 8 _ Función factorial y combinatoria
    # Función factorial(n) y luego combinatoria(n, k) = n! / (k! · (n-k)!).
# ------------------------------------------------------------------------------------
# 1 ENTENDER EL PROBLEMA 

    # 1 ENTRADA _ qué me dan 
      # num(input)

    # 2 PROCESO _ qué hago con eso
      # calcular el factorial de un numero luego hacer combinatoria.

    # 3 SALIDA _ qué debo mostrar 
      # mostrar el resultado de la factorial y luego el resultado de combinatoria 
# ------------------------------------------------------------------------------------
# 2 BOSQUEJO A MANO 

  # n = 5 
  # k = 2    
  # factorial = 5 X 4 X 3 X 2 X 1 = 120

  # factorial = 2 X 1 = 2 
  # factorial = 3 X 2 X 1 = 6   
  # combinatoria = 5! / (2! x (5-2)!)
  # resultado = 120 / (2 x (6)) = 10

# ------------------------------------------------------------------------------------
# 3 DESCUBRIR EL PATRON 

  # Una función usa otra. Modular como debe ser.
  # se utiliza un acumulador para sacar el valor total del factorial.

# ------------------------------------------------------------------------------------
#  4 ESCRIBIR EL CÓDIGO
def factorial_expre(n):

    resultado = 1
    expresion = ""

    for i in range(1, n + 1):

        resultado = resultado * i
        expresion = expresion + str(i)

        if i < n:    # aqui es para que alultimonumeor no le quede una "X"
            expresion = expresion + " x "

    print(f"{expresion} = {resultado}")

def factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact

def combinatoria(n, k):
    combi = 0
    if k >= 0 and k <= n:
        combi = factorial(n) // (factorial(k) * factorial(n - k))
        return f"{factorial (n)}! / ({factorial(k)}! x {factorial(n-k)}!) = {combi}"
    
    else : 
        print("Ingrese un numero valido")



n = int(input("Ingrese un número: "))
k = int(input("Ingrese un número: "))

print(factorial(n))
print(combinatoria(n,k))

# -----------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 9 _ Calculadora modular 
    # Programa que use funciones separadas para cada operación (sumar, restar, multiplicar, dividir) y un menú que llame a la correcta.
# ------------------------------------------------------------------------------------
# 1 ENTENDER EL PROBLEMA 

    # 1 ENTRADA _ qué me dan 
      # a (input) ; b(input)

    # 2 PROCESO _ qué hago con eso
      # segun la operación que el usuario escoja debemos hacer el proceso.

    # 3 SALIDA _ qué debo mostrar 
      # el resultado de la operacion que eligieron .
# ------------------------------------------------------------------------------------
# 2 BOSQUEJO A MANO 

  # a = 8  ;  b = 2  ; r = 0
  # suma = 8 + 2 = 10
  # resta = 8 - 2 = 6 
  # multiplicacion = 8 x 2 = 16
  # division = 8 / 2 = 4 
  # salimos ... 
  # invalido ....
  # r = suma o resta o multiplicacion o division 
  
# ------------------------------------------------------------------------------------
# 3 DESCUBRIR EL PATRON 

  # tenemos que crear funciones para cada operacion , creamos un menu para que el usuario 
  # escoja la operacion y se realise la operación.
  
# ------------------------------------------------------------------------------------
#  4 ESCRIBIR EL CÓDIGO
def sumar(a,b): return a + b
def resta (a,b): return a - b
def multiplicacion(a,b): return a*b
def dividir(a,b):
    if b == 0:
        return None            # None = "no válido"
    return a / b

while True:
    menu()
    opcion = int(input("Opción: "))

    if opcion == 5:
        print("Adios")
        break

    a = float(input("Ingrese número 1: "))
    b = float(input("Ingrese número 2: "))
    
    if opcion == 1: r = sumar(a,b)

    elif opcion == 2: r = resta(a,b)

    elif opcion == 3: r = multiplicacion(a,b)

    elif opcion == 4:
        r = dividir(a, b)
        if r is None:
            print("No se puede dividir entre 0")
        continue   # continua para que regrese al menu sin guardar nada en resultado

    else:
        print("Opcion invalida");continue    # continua para que no salga error ya que no hay funcion que se realize , y no se guarda nada en resulatado 
    print(f"Resulatado : {r}")  

# -----------------------------------------------------------------------------------------------------------------------------------
