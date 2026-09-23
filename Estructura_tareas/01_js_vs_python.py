# TALLER PRIMER EJERCICIOS PASO A PASO 
# -----------------------------------------------------------------------------------------------------------------------------------
# RECORDEMOS EL METODO 
# 1 ENTENDER(E.P.S) -> 2 BOSQUEJO A MANO -> 3 DESCUBRIR EL PATRÓN
# 4 ESCRIBIR EL CÓDIGO -> 5 PRUEBA DE ESCRITORIO
# -----------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 1 _ saludo personalizado
# leer el nombre del usuario y saludarlo por su nombre
# ------------------------------------------------------------------------------------
# 1 ENTENDER EL PROBLEMA 

    # 1 ENTRADA _ qué me dan 
      # nombre (inpunt)

    # 2 PROCESO _ qué hago con eso
      # concatenar << Hola >> con el nombre 

    # 3 SALIDA _ qué debo mostrar 
      # el saludo completo
# ------------------------------------------------------------------------------------
# 2 BOSQUEJO A MANO 

  # nombre = "Ana"
  # salida = Hola, Ana. Bienvenida al curso.
# ------------------------------------------------------------------------------------
# 3 DESCUBRIR EL PATRON 

  # hay un solo dato ( nombre ) y no hay que hacer cuentas ,
  # solo formar un mensaje. Este es el patrón más simple: leer -> mostrar.
  
  # como inpunt () ya devuelve str, no necesitamos convertir nada.  
# ------------------------------------------------------------------------------------
#  4 ESCRIBIR EL CÓDIGO

nombre = "Ana"
print(f"Hola {nombre}. Bienvenida al curso.")
# ------------------------------------------------------------------------------------
# 🚀 Ahora tú
# Amplíalo para que además pida la edad y muestre «tienes X años».

edad = 15
print (f"Hola {nombre}, tienes {edad} años. Bienvenido al curso")
# -----------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 2 _ Promedio de tres notas 
# Leer tres notas de un estudiante y mostrar su promedio.
# ------------------------------------------------------------------------------------
# 1 ENTENDER EL PROBLEMA 

    # 1 ENTRADA _ qué me dan 
      # n1, n2, n3 (inpunt)

    # 2 PROCESO _ qué hago con eso
      # sumar tres notas y dividir para 3

    # 3 SALIDA _ qué debo mostrar 
      # mostrar el promedio
# ------------------------------------------------------------------------------------
# 2 BOSQUEJO A MANO 

  # n1 = 8 , n2 = 6 , n3 = 10
  # paso 1 : sumo 8 + 6 + 10 = 24
  # paso 2 : 24/3 = 8
  # paso 3 : "promedio : 8"   
# ------------------------------------------------------------------------------------
# 3 DESCUBRIR EL PATRON 

  # El proceso tiene dos pasos continuos primero sumar
  # y luego dividir 
  # ------------------------------------------------------------------------------------
#  4 ESCRIBIR EL CÓDIGO

n1 = float (input("ingrese la nota 1: "))
n2 = float (input("ingrese la nota 2: "))
n3 = float (input("ingrese la nota 3: "))

promedio = (n1 + n2 + n3) / 3

print (f"Promedio es igual a : {promedio:.1f}")
# ------------------------------------------------------------------------------------
# 🚀 Ahora tú
# Modifícalo para que muestre «Aprueba» si el promedio es ≥ 7 y «Reprueba» si no.
# (Necesitas el if del módulo 3).

if promedio >= 7 :
    print(f"Aprueba 🤩 con un promedio de {promedio:.2f}")
else :
    print(f"Reprueba 😥 con un promedio de {promedio:.2f}")
# -----------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 3 _ Área y perímetro de un rectangulo
# Leer la base y la altura de un rectángulo y mostrar su área
# y su perímetro. Recuerda: área = base × altura, perímetro = 2 × (base + altura).
# ------------------------------------------------------------------------------------
# 1 ENTENDER EL PROBLEMA 

    # 1 ENTRADA _ qué me dan 
      # base , altura (inpunt)

    # 2 PROCESO _ qué hago con eso
      # aplicar las formulas

    # 3 SALIDA _ qué debo mostrar 
      # el área y el perímetro
# ------------------------------------------------------------------------------------
# 2 BOSQUEJO A MANO 

  # base = 5 , altura = 3
  # área = 5 x 3 = 15
  # perímetro = 2(5 x 3) = 16  
# ------------------------------------------------------------------------------------
# 3 DESCUBRIR EL PATRON 

  # Dos entradas y dos salidas, idependientes: cada formula 
  # usa base y altura por separado. No hay bucles ni decisiones.
  # ------------------------------------------------------------------------------------
#  4 ESCRIBIR EL CÓDIGO    

base = float(input("Ingresa el valor de la base : "))
altura = float(input("Ingresa el valor de la altura : "))

Área = base * altura
Perímetro = 2*(base + altura)

print(f"El área es de {Área:.2f} y el perímetro es de {Perímetro:.2f}")
# ------------------------------------------------------------------------------------
# 🚀 Ahora tú
# Ampliar para leer el radio de un círculo y mostrar área (π·r²) y perímetro (2·π·r). 
# Usa import math y math.pi.

import math    #Permite utilizar funciones y valores matemáticos de Python     

radio = float(input("ingrese el radio de un circulo: "))

area = math.pi * radio**2
perimetro = 2 * math.pi * radio

print(f"El área del circulo es {area:.2f} ")
print(f"El perimetro del circulo es {perimetro:.2f} ")
# -----------------------------------------------------------------------------------------------------------------------------------
# 📝 EJERCICIOS PROPUESTOS (solución oculta)
# -----------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 4 _ Convertir grados Celsius a fahrenheit
# Pide una temperatura en grados Celsius y muéstrala en Fahrenheit.
# Fórmula: F = C × 9/5 + 32.
# ------------------------------------------------------------------------------------
# 1 ENTENDER EL PROBLEMA 

    # 1 ENTRADA _ qué me dan 
      # celsius (input)

    # 2 PROCESO _ qué hago con eso
      # aplicar las formulas

    # 3 SALIDA _ qué debo mostrar 
      # los grados celsius tranformados a fahrenheit
# ------------------------------------------------------------------------------------
# 2 BOSQUEJO A MANO 

  # celcius = 25
  # fathrenheit = 25 x 9/5 + 32
  # "25°C grados celsius a fahrenheit es 77 °F"
# ------------------------------------------------------------------------------------
# 3 DESCUBRIR EL PATRON 

  # una entrada y una salida independientes : cada formula  
# ------------------------------------------------------------------------------------
#  4 ESCRIBIR EL CÓDIGO    

celsius = int(input("ingrese los grados celsius : "))

fahrenheit = celsius * 9/5 + 32
print(f"{celsius} °C a °F es : {fahrenheit}°F")
# -----------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 5 _ Segundosa horas, minutos y segundos
# Pide un total de segundos y muéstralos como hh:mm:ss. 
# Ej.: 3725 segundos → 1:02:05.
# ------------------------------------------------------------------------------------
# 1 ENTENDER EL PROBLEMA 

    # 1 ENTRADA _ qué me dan 
      # total de segundos (input)

    # 2 PROCESO _ qué hago con eso
      # calculas las horas , minutos y segundos 

    # 3 SALIDA _ qué debo mostrar 
      # mostrar como hh:mm:ss
# ------------------------------------------------------------------------------------
# 2 BOSQUEJO A MANO 

  # total_segundos = 3725
  # horas = 3725 // 3600
  # resto = 3725 % 3600
  # minutos = 125 // 60   
  # segundos = 1125 % 60   
  # " 1:02:05"   
# ------------------------------------------------------------------------------------
# 3 DESCUBRIR EL PATRON 

  # el total de segundos se va reduciendo con la division. 
  # nos sirve va de manera ascendente  
# ------------------------------------------------------------------------------------  
#  4 ESCRIBIR EL CÓDIGO  
  
total_segundos = int(input("ingrese el total de segundos : "))

horas = total_segundos // 3600
resto = total_segundos % 3600
minutos = resto // 60   
segundos = resto % 60   

print(f"{horas}:{minutos:02d}:{segundos:02d}")
# -----------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 6 _ Intercambiar dos varibles 
# Lee dos números y muéstralos intercambiados. Python permite hacerlo
# en una sola línea, muy diferente a JS.
# ------------------------------------------------------------------------------------
# 1 ENTENDER EL PROBLEMA 

    # 1 ENTRADA _ qué me dan 
      # ingresar a y b (input)

    # 2 PROCESO _ qué hago con eso
      # hacer el intercambio con un metodo de python

    # 3 SALIDA _ qué debo mostrar 
      # mostrar el  intercambio
# ------------------------------------------------------------------------------------
# 2 BOSQUEJO A MANO 

  #  a = 5, b = 8
  #  a = b y b = a 
  #  a = 8; b = 5 
# ------------------------------------------------------------------------------------
# 3 DESCUBRIR EL PATRON 

  # no contiene un patron solo vamos hacer un intercambio, no muestra 
  # que deba cumplir un condicion el numero para hacer el intercambio
# ------------------------------------------------------------------------------------ 
#  4 ESCRIBIR EL CÓDIGO  

a = int(input("ingrese el numero de a : "))
b = int(input("ingrese el numero de b : "))

a,b = b,a

print(f"a = {a} y b = {b}")
# -----------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 7 _ Calcular el IVA (15% Ecuador) 
# Lee el precio de un producto sin IVA y muestra el IVA (15%) y el total.
# ------------------------------------------------------------------------------------
# 1 ENTENDER EL PROBLEMA 

    # 1 ENTRADA _ qué me dan 
      # ingresar precio de producto (input)

    # 2 PROCESO _ qué hago con eso
      # calcular el iva del producto 

    # 3 SALIDA _ qué debo mostrar 
      # mostrar el total del producto con el Iva incluido
# ------------------------------------------------------------------------------------
# 2 BOSQUEJO A MANO 

  #  precio = 100
  #  IVA = (100 * 15)/100
  #  Total = 100 + 15
  #  "el Iva es de $ 15"
  #  "El total de producto es $ 115"  
# ------------------------------------------------------------------------------------
# 3 DESCUBRIR EL PATRON 

  # no contiene un patrón sucesivo solo debemos calcular el valor del iva 
  # para un x producto.  
# ------------------------------------------------------------------------------------  
#  4 ESCRIBIR EL CÓDIGO 

precio = int(input("ingrese el precio del producto : "))
Iva = (precio * 15)/100
total = precio + Iva

print(f"El valor de  Iva es de $ {Iva:.2f}")
print(f"El valor total del producto es de $  {total:.2f}") 