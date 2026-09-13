# TALLER EJERCICIOS PASO A PASO 
# -----------------------------------------------------------------------------------------------------------------------------------
# RECORDEMOS EL METODO 
#  1 ENTENDER(E.P.S) -> 2 BOSQUEJO A MANO -> 3 DESCUBRIR EL PATRÓN
#  4 ESCRIBIR EL CÓDIGO -> 5 PRUEBA DE ESCRITORIO
# -----------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 1 _ Contar del 1 al N
    # Leer un número N y mostrar los números del 1 al N.
# ------------------------------------------------------------------------------------
# 1 ENTENDER EL PROBLEMA 

    # 1 ENTRADA _ qué me dan 
      # n (entero)

    # 2 PROCESO _ qué hago con eso
      # recorrer desde 1 hasta N con un for

    # 3 SALIDA _ qué debo mostrar 
      # los N números uno por línea
# ------------------------------------------------------------------------------------
# 2 BOSQUEJO A MANO 

  # n = 5
  # for i in range(1, 6):   # 1, 2, 3, 4, 5
  # print(i) 

# ------------------------------------------------------------------------------------
# 3 DESCUBRIR EL PATRON 

  # Si quiero contar del 1 al N, uso range(1, N+1). El segundo número es
  # exclusivo: range(1, 6) da 1, 2, 3, 4, 5, no llega a 6.
  # El error clásico es escribir range(1, N): te falta el último número.
# ------------------------------------------------------------------------------------
#  4 ESCRIBIR EL CÓDIGO

n = int(input("Ingrese la cantidad a contar : "))

for i in range(1, n + 1):      # ¡ojo con el n+1!
    print(i)
# ------------------------------------------------------------------------------------
# 🚀 Ahora tú
# Cámbialo para que muestre del N al 1 (hacia atrás). Pista: range(n, 0, -1).
num = int(input("Ingrese la cantidad a contrar en reversa: "))
for i in range(num,0,-1) :
    print(i)
# -----------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 2 _ Suma de los primeros N naturales
    # Leer N y calcular la suma de 1 + 2 + 3 + ... + N.
# ------------------------------------------------------------------------------------
# 1 ENTENDER EL PROBLEMA 

    # 1 ENTRADA _ qué me dan 
      # n (entero)

    # 2 PROCESO _ qué hago con eso
      # acumular en una variable con un bucle

    # 3 SALIDA _ qué debo mostrar 
      # la suma total
# ------------------------------------------------------------------------------------
# 2 BOSQUEJO A MANO 

  # n = 5, suma = 0 (INICIALIZACIÓN)
  # i=1:  suma = 0 + 1 = 1
  # i=2:  suma = 1 + 2 = 3
  # i=3:  suma = 3 + 3 = 6
  # i=4:  suma = 6 + 4 = 10
  # i=5:  suma = 10 + 5 = 15   ← resultado

# ------------------------------------------------------------------------------------
# 3 DESCUBRIR EL PATRON 

  # Aquí aparece el patrón acumulador: una variable (suma) que se va
  # aumentando dentro del bucle.
  # La regla de oro del acumulador: inicializarlo en 0 si vas a sumar, en 1 si
  # vas a multiplicar. Y siempre fuera del bucle, porque si lo pones dentro, en
  # cada vuelta lo reseteas.

  # Curiosidad: Python tiene sum(range(1, n+1)) que hace lo mismo en una
  # línea. Pero como estamos aprendiendo, usamos el bucle explícito.
# ------------------------------------------------------------------------------------
#  4 ESCRIBIR EL CÓDIGO
n = int(input("Cantidad de numero para la suma : "))
suma = 0                    # INICIALIZACIÓN del acumulador

for i in range(1, n + 1):
    suma = suma + i         # equivale a: suma += i

print(f"Suma: {suma}")
# ------------------------------------------------------------------------------------
# 🚀 Ahora tú
# Adaptarlo para calcular la suma de los pares del 2 al 100. Pista: range(2, 101, 2).
suma_Par = 0
for i in range(2,n+1) :
    if(i % 2 == 0):
        suma_Par = suma_Par + i

print(f"La suma de los pares es : {suma_Par}")
# -----------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 3 _ Factorial de N
    # Leer N y calcular el factorial (N! = 1 × 2 × 3 × ... × N). Ejemplo: 5! = 120.
# ------------------------------------------------------------------------------------
# 1 ENTENDER EL PROBLEMA 

    # 1 ENTRADA _ qué me dan 
      # n (entero)

    # 2 PROCESO _ qué hago con eso
      # acumulador multiplicativo

    # 3 SALIDA _ qué debo mostrar 
      # el factorial
# ------------------------------------------------------------------------------------
# 2 BOSQUEJO A MANO 

  # n = 5, fact = 1 (INICIALIZACIÓN)

  # i=1:  fact = 1 * 1 = 1
  # i=2:  fact = 1 * 2 = 2
  # i=3:  fact = 2 * 3 = 6
  # i=4:  fact = 6 * 4 = 24
  # i=5:  fact = 24 * 5 = 120   ← resultado

# ------------------------------------------------------------------------------------
# 3 DESCUBRIR EL PATRON 

  # Mismo patrón que el ejercicio anterior, pero multiplicativo. Lo que cambia es
  # la inicialización: si empiezas en 0, todo el resultado será 0 (porque cualquier
  # cosa × 0 = 0). Empezar en 1 es la clave.
# ------------------------------------------------------------------------------------
#  4 ESCRIBIR EL CÓDIGO
n = int(input("Infgrese el numero a factorizar : "))
fact = 1                    # INICIALIZACIÓN: 1 porque vamos a multiplicar

for i in range(1, n + 1):
    fact = fact * i         # o: fact *= i

print(f"{n}! = {fact}")

# ------------------------------------------------------------------------------------
# 🚀 Ahora tú
# ¿Qué pasa con N muy grande (100!)? Python maneja enteros infinitos, pruébalo. En JS con enteros normales explotaría.
# -----------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 4 _ Cuántos aprobaron
    # Leer las notas de N estudiantes (una por una) y contar cuántos aprobaron (nota ≥ 70).
# ------------------------------------------------------------------------------------
# 1 ENTENDER EL PROBLEMA 

    # 1 ENTRADA _ qué me dan 
      # n (cantidad) y n notas

    # 2 PROCESO _ qué hago con eso
      # recorrer con for y contar con un contador

    # 3 SALIDA _ qué debo mostrar 
      # cuántos tienen nota ≥ 70
# ------------------------------------------------------------------------------------
# 2 BOSQUEJO A MANO 

  # n = 4, aprobados = 0 (INICIALIZACIÓN)

  # nota=8 → 8 >= 7 → aprobados = 1
  # nota=5 → 5 >= 7 → NO cambia
  # nota=9 → 9 >= 7 → aprobados = 2
  # nota=6 → 6 >= 7 → NO cambia

  # resultado: 2 aprobados
# ------------------------------------------------------------------------------------
# 3 DESCUBRIR EL PATRON 

  # Aquí aparece el patrón contador: como el acumulador, pero solo suma 1
  # cuando pasa algo. Se combina con un if dentro del bucle.

  # Fíjate que hay dos bucles imaginarios juntos: (1) uno que lee las N notas, (2)
  # dentro del cuerpo, un if que decide si aumentar el contador.

# ------------------------------------------------------------------------------------
#  4 ESCRIBIR EL CÓDIGO
n = int(input("¿Cuántos estudiantes?: "))
aprobados = 0                       # contador arranca en 0

for i in range(n):
    nota = float(input(f"Nota {i+1}: "))
    if nota >= 7:                   # el 7 es el umbral (o 70 si es sobre 100)
        aprobados += 1              # aumenta solo si aprobó

print(f"Aprobados: {aprobados} de {n}")
# ------------------------------------------------------------------------------------
# 🚀 Ahora tú
# Añade un contador para reprobados y muestra el porcentaje de aprobación.
numero_estudiantes = int(input("¿Cuántos estudiantes?  "))
apro = 0
rep = 0

for i in range(numero_estudiantes):
     nota = float(input(f"Nota {i+1}: "))
     if nota >= 7 :
        apro += 1
     else:
        rep += 1

porcentaje = apro / numero_estudiantes * 100

print(f"Aprobados: {apro} de {numero_estudiantes}")
print(f"Reprobados: {rep} de {numero_estudiantes}")
print(f"Porcentaje: {porcentaje} de {numero_estudiantes}")

# -----------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 5 _ La nota más alta (patrón campeón)
    # Leer las notas de N estudiantes y mostrar la nota más alta.
# ------------------------------------------------------------------------------------
# 1 ENTENDER EL PROBLEMA 

    # 1 ENTRADA _ qué me dan 
      # n y las n notas

    # 2 PROCESO _ qué hago con eso
      # guardar la nota más alta encontrada hasta ahora, actualizarla si aparece una mayor

    # 3 SALIDA _ qué debo mostrar 
      # la nota más alta
# ------------------------------------------------------------------------------------
# 2 BOSQUEJO A MANO 

  # nota máxima = -infinito (o = primera nota)

  # leo 6  → 6 > -inf → máx = 6
  # leo 9  → 9 > 6   → máx = 9
  # leo 4  → 4 > 9   → NO cambia
  # leo 8  → 8 > 9   → NO cambia
  # leo 10 → 10 > 9  → máx = 10

  # resultado: 10
# ------------------------------------------------------------------------------------
# 3 DESCUBRIR EL PATRON 

  # Patrón campeón (o mayor). Guardas la mejor nota vista hasta ese momento y
  # la actualizas cuando aparece una mayor.

  # El problema es cómo inicializar. Dos opciones:

  #  Con la primera nota leída (mejor): el bucle empieza en el segundo dato.
  # Con un valor imposible (float negativo infinito): el bucle empieza en el primero.

  # Aquí usamos la segunda porque queda más limpia con range(n).  
# ------------------------------------------------------------------------------------
#  4 ESCRIBIR EL CÓDIGO
numero_Notas = int(input("¿Cuántas notas? "))
maximo = 0

for i in range (numero_Notas):
    nota = float(input(f"Nota {i+1}: "))
    if nota > maximo :
        maximo = nota 

print (f"Máxima : {maximo}")
# ------------------------------------------------------------------------------------
# 🚀 Ahora tú
# Adaptarlo para encontrar la menor nota. Cambio: float("inf") y if nota < minima:.
minimo = 10
for i in range (numero_Notas):
    nota = float(input(f"Nota {i+1}: "))
    if nota < minimo :
        minimo = nota 

print (f"Minimo : {minimo}")
# -----------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 6 _ ¿Es primo?
    # Leer un número y determinar si es primo (solo divisible entre 1 y él mismo).
# ------------------------------------------------------------------------------------
# 1 ENTENDER EL PROBLEMA 

    # 1 ENTRADA _ qué me dan 
      # n (entero)

    # 2 PROCESO _ qué hago con eso
      # probar divisores de 2 hasta √n usando bandera

    # 3 SALIDA _ qué debo mostrar 
      # "n es primo" o "n no es primo"
# ------------------------------------------------------------------------------------
# 2 BOSQUEJO A MANO 

  # n = 17, es_primo = True (bandera)

  # Pruebo divisores del 2 al √17 ≈ 4:
  # 17 % 2 = 1 (no divide)
  # 17 % 3 = 2 (no divide)
  # 17 % 4 = 1 (no divide)

  # Ninguno dividió → 17 es primo ✓
# ------------------------------------------------------------------------------------
# 3 DESCUBRIR EL PATRON 

  # Aquí usamos el patrón bandera: una variable booleana que empieza en
  # True y cambia a False apenas se descarta.

  # Optimización clave: solo hace falta probar hasta √n, no hasta n.
  # Si n tiene un divisor mayor que √n, forzosamente tiene otro menor que ya habríamos
  # encontrado.
  # Un caso especial: 0 y 1 no son primos. Se descarta al inicio.
  
# ------------------------------------------------------------------------------------
#  4 ESCRIBIR EL CÓDIGO
numero = int(input("Ingrese un numero: "))

primo = True

if numero < 0:
    print("El numero es negativo , vuelva a ingresar otro numero ")

if numero < 2:
    primo = False

else:
    i = 2

    while i < numero and primo:
        if numero % i == 0:
            primo = False
        else:
            i = i + 1

if primo:
    print(f"El numero {numero} es primo")
    
elif numero >= 0:
    print(f"El numero {numero} no es primo")
# ------------------------------------------------------------------------------------
# 🚀 Ahora tú
# Genera una lista de todos los primos entre 2 y 100.
def primos(num):

    primo = True

    if num < 2:
        primo = False

    else:
        i = 2

        while i < num and primo:
            if num % i == 0:
                primo = False
            else:
                i = i + 1

    return primo

numero = int(input("Ingrese un numero: "))  
lista_primos= []
lista_noprimos= []

for i in range(2,numero) :
    pri = primos(i)
    
    if pri :
        lista_primos.append(i)
    else :
        lista_noprimos.append(i)

print(f"Los primos {lista_primos}")
print(f"Los no primos {lista_noprimos}")
# -----------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 7 _ Tabla de multiplicar
  #  Lee un número N y muestra su tabla de multiplicar (del 1 al 12).
# ------------------------------------------------------------------------------------
# 1 ENTENDER EL PROBLEMA 

    # 1 ENTRADA _ qué me dan 
      # num(entero)

    # 2 PROCESO _ qué hago con eso
      # multiplicar el num por cada numero del 1 al 12.

    # 3 SALIDA _ qué debo mostrar 
      # mostrar la multiplicación 
# ------------------------------------------------------------------------------------
# 2 BOSQUEJO A MANO 

  # num = 7

  # 7 X 1 = 7
  # 7 X 2 = 14
  # ...
  # 7 X 12 = 84
   
# ------------------------------------------------------------------------------------
# 3 DESCUBRIR EL PATRON 

  # se debe guardar la multiplicacion en un acumulador que debe empezar en 1 
  # vamos multiplicando desde el 1 al 12 de manera consecutiva , lo presnto 
  # en cada iteraccion.

# ------------------------------------------------------------------------------------
#  4 ESCRIBIR EL CÓDIGO
numero = int(input("Ingrese numero dela tabla que quiere presentar : "))
mult = 1
for i in range (1,12 + 1):
  mult = numero * i
  print(f"{numero} X {i} = {mult}")

# -----------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 8 _ Contar digitos de un numero 
  # Lee un número y cuenta cuántos dígitos tiene (sin convertir a string).
# ------------------------------------------------------------------------------------
# 1 ENTENDER EL PROBLEMA 

    # 1 ENTRADA _ qué me dan 
      # num (entero )

    # 2 PROCESO _ qué hago con eso
      # necesito dividir el numero por 10, hasta que llegue a 0 y contar 

    # 3 SALIDA _ qué debo mostrar 
      # mostrar el resultado del contador 
# ------------------------------------------------------------------------------------
# 2 BOSQUEJO A MANO 

  # num = 12345
  # 5 dígitos
# ------------------------------------------------------------------------------------
# 3 DESCUBRIR EL PATRON 

  # El patron consiste en dividir el num sobre 10 ,hasta que en 
  # cieto momento me de cero , conel contador vamos contando.

# ------------------------------------------------------------------------------------
#  4 ESCRIBIR EL CÓDIGO
n = int(input("Ingrese un número: "))

n = abs(n)    # hace que n siempre sea positivo. abs() significa valor absoluto.

contador = 0

if n == 0:
    contador = 1
else:
    while n > 0:
        n = n // 10
        contador += 1

print(f"El número tiene  {contador}  dígitos")
# -----------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 9 _ Suma de pares e impares 
  # Lee N números y muestra la suma de los pares y la suma de los impares por separado.
# ------------------------------------------------------------------------------------
# 1 ENTENDER EL PROBLEMA 

    # 1 ENTRADA _ qué me dan 
      # num(entero)

    # 2 PROCESO _ qué hago con eso
      # identificar si un numero es par e impar y acumulador la suma de los
      # pares e impares en una variable

    # 3 SALIDA _ qué debo mostrar 
      # presentar la suma acumulada de los numeros pares e impares.

# ------------------------------------------------------------------------------------
# 2 BOSQUEJO A MANO 

  # num = 4
  # par = 0
  # impar = 0
  # 4 % 2 = 0                  entonces es un numero par 
  # par = par + 4 = 4          la variable par toma el 4 por verdadero 
  # impar = 0                  por falso entra a acumularse en la variable impar 

  # resulado = par 
  # resulado = impar
# ------------------------------------------------------------------------------------
# 3 DESCUBRIR EL PATRON 

  # El patron es que, los numeros ingresan y se verifica si el numero ingresado es par o impar 
  # segun el resultado por verdadero o falso se ingresa a realizar una operacion que en este caso es la suma 
  # el resultado se acumula en una variable. ese procesos se repite 
# ------------------------------------------------------------------------------------
#  4 ESCRIBIR EL CÓDIGO
num = int(input("Ingrese un cantidad numeros: "))
par = 0
impar = 0

for i in range(num +1 ):
  numero = int(input("Ingrese el numero : "))

  if numero % 2 == 0 :  par = par+numero
  else : impar = impar + numero

print(f"El resultado de la suma de los pares es {par}")
print(f"El resultado de la suma de los impares es {impar}")

# -----------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 10 _ Validar entrada (bicle con centinela)
  # Pide una edad y valida que esté entre 0 y 120. Si el usuario ingresa algo inválido, vuelve a pedirla.
# ------------------------------------------------------------------------------------
# 1 ENTENDER EL PROBLEMA 

    # 1 ENTRADA _ qué me dan 
      # edad (entero)

    # 2 PROCESO _ qué hago con eso
      # validar que la edad este entre el rango de 0 a 120 

    # 3 SALIDA _ qué debo mostrar 
      # presentar la edad con un mensaje esta dentro del rango.

# ------------------------------------------------------------------------------------
# 2 BOSQUEJO A MANO 

  # edad = 50
  # validar = 0<edad<120      si es verdadero pasa la validacion 
  # print ("La edad es valida")

# ------------------------------------------------------------------------------------
# 3 DESCUBRIR EL PATRON 

  # El numero que ingreso debera ser validado segun el rango establecido y presentar un mensaje 
  # de validacion , cada numero que ingrese  repetira este patron.

# ------------------------------------------------------------------------------------
#  4 ESCRIBIR EL CÓDIGO
while True:
    edad = int(input("Edad (0-120): "))
    if 0 <= edad <= 120:
        break                       # sale del while
    print("Inválida, intenta de nuevo")

print(f"Edad válida: {edad}")
# -----------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 11 _ Adivina el número
  # Genera un número secreto entre 1 y 100. El usuario intenta adivinar. En cada intento le dices si es «mayor» o «menor». Cuenta cuántos intentos usó. 
# ------------------------------------------------------------------------------------
# 1 ENTENDER EL PROBLEMA 

    # 1 ENTRADA _ qué me dan 
      # numero(entero)

    # 2 PROCESO _ qué hago con eso
      # generar un numero secreto el cual el usuario debe adivinar 
      # indicarle si el numero que ingrese esta cerca al numero secreto 
      # dandole pista como si es mayor o menor

    # 3 SALIDA _ qué debo mostrar 
      #El usuario averigua el numero presentandole un mensaje.
# ------------------------------------------------------------------------------------
# 2 BOSQUEJO A MANO 

  # numero_secreto = 67
  # intentos = 6
  
  # numero = 30          El suario ingresa ese valor 
  # menor = 30 < 67      el numero ingresado es menor al numero secreto
  # mayor = numero       el numero ingresado es mayor al numero secreto4

  # intento = 6 - 1      aqui si el usuario se equivoca los intentos disminuyen 

  # numero = 67          otro numero
  # 67 = 67              como esto es verdadero 
  # mensaje (Felicidades 🎉)
# ------------------------------------------------------------------------------------
# 3 DESCUBRIR EL PATRON 

  # El usuario ingresa numeros hasta que adivine el numero secreto , el sistema 
  # le da pistas para ver que tan serca esta de lograrlo.

# ------------------------------------------------------------------------------------
#  4 ESCRIBIR EL CÓDIGO
numero_secreto = 65
intentos = 6
bandera = False

for i in range(1,intentos +1):
  numero = int(input("adivine el numero del 1 al 100 : "))
  if numero == numero_secreto : 
    bandera = True
    break
  else :
    if numero < numero_secreto :
      print("mayor") 
    else :
      print("menor")

    intentos = intentos - 1
    print(f"Quedan {intentos} intentos... \n")

if bandera :
  print(F"FELICIDADES 🎉 ")
else :
  print(f"A PERDIDO 😥 . El numero es {numero_secreto}")

# ////////////////////////////

import random

secreto = random.randint(1, 100)
intentos = 0

while True:
    intento = int(input("Adivina (1-100): "))
    intentos += 1
    if intento == secreto:
        print(f"¡Correcto en {intentos} intentos!")
        break
    elif intento < secreto:
        print("Es mayor")
    else:
        print("Es menor")

# -----------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 12 _ Serie de Fibonacci
  # Muestra los primeros N números de Fibonacci. La serie: 0, 1, 1, 2, 3, 5, 8, 13, 21... Cada número es la suma de los dos anteriores.
# ------------------------------------------------------------------------------------
# 1 ENTENDER EL PROBLEMA 

    # 1 ENTRADA _ qué me dan 
      # numero(entero)

    # 2 PROCESO _ qué hago con eso
      # ingresamos los dos primeros numeros de la serie fibonacci, realizamos una suma  
      #  de los dos anteriores para continuar la secuencia , asi sucesivamente .

    # 3 SALIDA _ qué debo mostrar 
      # Presentar la serie fibonacci

# ------------------------------------------------------------------------------------
# 2 BOSQUEJO A MANO 

  # num = 8    hasto donde quiero mi serie 

  # a = 0
  # b = 1
  # c= 0 + 1
  # a = 1     ahora a va a tomar a (b) 
  # c = 1     y b va a tomas a (c) asi sucesivamente....
  # .
  # .
  # .

  # print(Presento la lista de fibonacci)

# ------------------------------------------------------------------------------------
# 3 DESCUBRIR EL PATRON 

  # La serie fibonacci consiste en que cada número es la suma de los dos anteriores, 
  # aqui ya hay una secuencia en la que el siguiente numero es la suma de los dos anteriores.

# ------------------------------------------------------------------------------------
#  4 ESCRIBIR EL CÓDIGO
numero = int(input("Ingrese el numero de fibonacci que desea : "))
 
a,b = 0,1
for _ in range(numero + 1):   # _ "No necesito guardar este valor. 
  print(a,end=" ")            #  hace que deje un espacio y continúe en la misma línea.
  a, b = b, a + b  
  
print()

# //////////////////////

n = int(input("¿Cuántos? "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")

    c = a + b
    a = b
    b = c

print()
# -----------------------------------------------------------------------------------------------------------------------------------

 
