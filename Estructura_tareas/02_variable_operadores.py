# TALLER EJERCICIOS PASO A PASO 
# -----------------------------------------------------------------------------------------------------------------------------------
# RECORDEMOS EL METODO 
#  1 ENTENDER(E.P.S) -> 2 BOSQUEJO A MANO -> 3 DESCUBRIR EL PATRÓN
#  4 ESCRIBIR EL CÓDIGO -> 5 PRUEBA DE ESCRITORIO
# -----------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 1 _ CalcularIVA (15%) y precio final 
    # Leer el precio de un producto sin IVA y mostrar el IVA y el precio final. 
    # El IVA en Ecuador es 15%.
# ------------------------------------------------------------------------------------
# 1 ENTENDER EL PROBLEMA 

    # 1 ENTRADA _ qué me dan 
      # precio (input)

    # 2 PROCESO _ qué hago con eso
      # iva = precio × 0.15; total = precio + iva

    # 3 SALIDA _ qué debo mostrar 
      # el IVA y el total
# ------------------------------------------------------------------------------------
# 2 BOSQUEJO A MANO 

  # precio = 80
  # iva   = 80 × 0.15 = 12
  # total = 80 + 12   = 92
    
# ------------------------------------------------------------------------------------
# 3 DESCUBRIR EL PATRON 

  # Dos cálculos separados que usan el mismo dato de entrada. El 0.15 es una
  # constante del problema — puedes definirla arriba con IVA = 0.15 para
  # dejarla clara.
# ------------------------------------------------------------------------------------
#  4 ESCRIBIR EL CÓDIGO
IVA = 0.15

precio = float(input("Precio sin IVA : "))
iva = precio * IVA
total = precio + iva

print(f"IVA: ${iva:.2f}")
print(f"Total: ${total:.2f}")

# ------------------------------------------------------------------------------------
# 🚀 Ahora tú
# Añadir un descuento del 10% que se aplique antes del IVA. 
# Muestra los tres valores: descuento, IVA, total.

descuento = precio *0.10
total = total - descuento

print(f"Descuento: ${descuento:.2f}")
print(f"Total: ${total:.2f}")

# -----------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 2 _ Par o Impar
    # Leer un número entero y determinar si es par o impar.
# ------------------------------------------------------------------------------------
# 1 ENTENDER EL PROBLEMA 

    # 1 ENTRADA _ qué me dan 
      # num (input)

    # 2 PROCESO _ qué hago con eso
      # verificar si num % 2 == 0

    # 3 SALIDA _ qué debo mostrar 
      # "par" o "impar"
# ------------------------------------------------------------------------------------
# 2 BOSQUEJO A MANO 

  # num = 7
  # 7 / 2 = 3, sobra 1 → impar
  # 4 / 2 = 2, sobra 0 → par
  # 0 / 2 = 0, sobra 0 → par (el cero es par)  
# ------------------------------------------------------------------------------------
# 3 DESCUBRIR EL PATRON 

  # El residuo con % es la clave. Si al dividir para 2 el residuo es 0, el número es
  # par; si no, impar.
  
# ------------------------------------------------------------------------------------
#  4 ESCRIBIR EL CÓDIGO

num = int(input("Ingrese un numero : "))
resultado = "par" if num % 2 == 0 else "impar"

print (f"{num} es {resultado}")

# ------------------------------------------------------------------------------------
# 🚀 Ahora tú
# Modifícalo para que además diga si es múltiplo de 3, de 5, o de ambos.
if num % 3 == 0 and num % 5 == 0:
    print(f"{num} es multiplo de 3 y 5 ")
elif num % 3 == 0:
    print(f"{num} es multiplo 3")
elif num % 5 == 0:   
    print(f"{num} es multiplo 5") 
else:
    print(f"No es multiplo de 3 ni 5")

# -----------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 3 _  Convertir tiempos: segundo a hh:mm:ss
    # Leer una cantidad total de segundos y mostrarla como hh:mm:ss. Ejemplo:
    # 3725 segundos → 01:02:05.
# ------------------------------------------------------------------------------------
# 1 ENTENDER EL PROBLEMA 

    # 1 ENTRADA _ qué me dan 
      # total (segundos)

    # 2 PROCESO _ qué hago con eso
      # dividir sucesivamente para 3600 y 60 usando // y %

    # 3 SALIDA _ qué debo mostrar 
      # el tiempo formateado
# ------------------------------------------------------------------------------------
# 2 BOSQUEJO A MANO 

  # total = 3725 segundos
  # horas    = 3725 // 3600 = 1        sobran 125
  # minutos  = 125  // 60   = 2        sobran 5
  # segundos = 5
  # resultado: 01:02:05 
# ------------------------------------------------------------------------------------
# 3 DESCUBRIR EL PATRON 

  # Este ejercicio muestra la potencia de combinar // y %. La división entera te
  # dice cuántas unidades grandes caben (horas); el residuo, lo que sobra para
  # las unidades más pequeñas.
# ------------------------------------------------------------------------------------
#  4 ESCRIBIR EL CÓDIGO

total  = int(input("Segundos totales: "))

horas = total // 3600
resto = total % 3600
minutos = resto // 60
segundos = resto % 60

print(f"{horas}:{minutos:02d}:{segundos:02d}")
# ------------------------------------------------------------------------------------
# 🚀 Ahora tú
# Al revés: leer hh:mm:ss y convertir a segundos totales. Tendrás que usar split(":").
tiempo = input("Ingresa la hora (hh:mm:ss): ")

horas, minutos, segundos = tiempo.split(":")

horas = int(horas)
minutos = int(minutos)
segundos = int(segundos)

total = horas * 3600 + minutos * 60 + segundos

print(f"Segundos totales: {total}")
# -----------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 4 _ Cambio de billetes
    # Un cajero solo tiene billetes de $20, $10, $5 y $1. Dado un monto, mostrar
    # cuántos billetes de cada uno se necesitan (usando la mínima cantidad).
# ------------------------------------------------------------------------------------
# 1 ENTENDER EL PROBLEMA 

    # 1 ENTRADA _ qué me dan 
      # monto (entero)

    # 2 PROCESO _ qué hago con eso
      # dividir sucesivamente por 20, 10, 5, 1 con // y %

    # 3 SALIDA _ qué debo mostrar 
      # cantidad de billetes de cada tipo
# ------------------------------------------------------------------------------------
# 2 BOSQUEJO A MANO 

  # monto = 87
  # $20: 87 // 20 = 4, sobra 7
  # $10:  7 // 10 = 0, sobra 7
  # $5 :  7 //  5 = 1, sobra 2   
  # $1 :  2 //  1 = 2, sobra 0
# ------------------------------------------------------------------------------------
# 3 DESCUBRIR EL PATRON 

  # Es el mismo patrón que segundos→horas, pero con billetes. La idea general
  # se llama algoritmo greedy (voraz): en cada paso agarras la mayor
  # denominación que quepa.
  # Trabajamos siempre con el resto, no con el monto original.  
# ------------------------------------------------------------------------------------
#  4 ESCRIBIR EL CÓDIGO
monto = int(input("Monto: $ "))
resto = monto

b50 = resto // 50
resto = resto % 50

b20 = resto // 20 
resto = resto % 20

b10 = resto // 10 
resto = resto % 10

b5 = resto // 5
resto = resto % 5

b1 = resto // 1
resto = resto % 1

print(f"$50 x {b50}")
print(f"$20 x {b20}")
print(f"$10 x {b10}")
print(f"$5  x {b5}")
print(f"$1  x {b1}")

# ------------------------------------------------------------------------------------
# 🚀 Ahora tú
# Añadir billete de $50 al inicio. Después probar con monedas de $0.25, $0.10, $0.05 y $0.01
# (necesitas trabajar con centavos).
monto = float(input("Monto: $"))

centavos = round(monto * 100)  # round() sirve para redondear un número. (monto*100) tranforma el dolar a centavo 

c25 = centavos // 25
centavos = centavos % 25
 
c10 = centavos // 10
centavos = centavos % 10

c5 = centavos // 5
centavos = centavos % 5

c1 = centavos // 1
centavos = centavos % 1

print(f"$0.25 x {c25}")
print(f"$0.10 x {c10}")
print(f"$0.05 x {c5}")
print(f"$0.01 x {c1}")
# -----------------------------------------------------------------------------------------------------------------------------------
#📝 Ejercicios propuestos
# -----------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 5 _ Suma dígitos de un numero de 3 cifras
    # Lee un número de 3 cifras y muestra la suma de sus dígitos.
    # Ejemplo: 435 → 4+3+5 = 12.
# ------------------------------------------------------------------------------------
# 1 ENTENDER EL PROBLEMA 

    # 1 ENTRADA _ qué me dan 
      # num(input)

    # 2 PROCESO _ qué hago con eso
      # sumar los digitos

    # 3 SALIDA _ qué debo mostrar 
      # la suma total de los digitos
# ------------------------------------------------------------------------------------
# 2 BOSQUEJO A MANO 

  # num = 435
  # suma = 4+3+5   
  # total = 12
# ------------------------------------------------------------------------------------
# 3 DESCUBRIR EL PATRON 

  # se tendra que dividir // para sacar las decenas, se utilizara 
  # el residuo de cada división % para las centenas y unidades

# ------------------------------------------------------------------------------------
#  4 ESCRIBIR EL CÓDIGO
num = int(input("Ingrese los digitos: "))
resto  = num

centenas = num // 100
resto = resto % 100

decenas = resto // 10
resto = resto % 10

unidades = resto % 10

suma = centenas + decenas + unidades

print(f"Suma: {suma}")

# -----------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 6 _ Convertir minutos a horas y minutos
    # Lee una cantidad de minutos y muéstrala como «X horas Y minutos». Ejemplo: 
    # 135 → «2 horas 15 minutos».
# ------------------------------------------------------------
# 1 ENTENDER EL PROBLEMA 

    # 1 ENTRADA _ qué me dan 
      # minutos (input)

    # 2 PROCESO _ qué hago con eso
      # calcular las horas y los minutos 

    # 3 SALIDA _ qué debo mostrar 
      # entregar el valor de horas y minutos 
# ------------------------------------------------------------------------------------
# 2 BOSQUEJO A MANO 

  # minutos = 135
  # horas = minutos // 60  sobran 
  # resto = minutos % 60   sobran 5 
# ------------------------------------------------------------------------------------
# 3 DESCUBRIR EL PATRON 

  # Se tendra que // dividir para sacar las horas
  # tendremos que sacar el residuo y con eso tenemos los minutos.

# ------------------------------------------------------------------------------------
#  4 ESCRIBIR EL CÓDIGO
minutos = int(input("Ingrese los minutos: "))

horas = minutos // 60
resto = minutos % 60

print(f"{horas} horas {resto} minutos")

# -----------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 7 _ Ïndice de masa corporal
    # Lee peso (kg) y estatura (m) y calcula el IMC. Fórmula: IMC = peso / 
    # estatura². Muestra el IMC con 2 decimales.
# ------------------------------------------------------------------------------------
# 1 ENTENDER EL PROBLEMA 

    # 1 ENTRADA _ qué me dan 
      # peso (input)
      # estatura (input)  

    # 2 PROCESO _ qué hago con eso
      # calcular , usando la formula IMC

    # 3 SALIDA _ qué debo mostrar 
      # muestra el IMC  con 3 decimales 
# ------------------------------------------------------------------------------------
# 2 BOSQUEJO A MANO 

  # peso = 70
  # altura = 1.75
  # IMC = 70 / 1.75 **2  

# ------------------------------------------------------------------------------------
# 3 DESCUBRIR EL PATRON 

  # no hay patrón tenemos una formula la cual debemos seguir
  
# ------------------------------------------------------------------------------------
#  4 ESCRIBIR EL CÓDIGO

peso = int(input("Ingrese su peso: "))
altura = float(input("Ingrese su estatura: "))

Imc = peso / (1.75**2)

print(f"El IMC  es de {Imc}")
# -----------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 8 _ Redondeo por cifra decimal
    # Lee un número decimal y una cantidad de decimales, y muéstralo redondeado.
    # Ejemplo: 3.14159 con 2 decimales → 3.14.
# ------------------------------------------------------------------------------------
# 1 ENTENDER EL PROBLEMA 

    # 1 ENTRADA _ qué me dan 
      # numero (input)
      # decimal (input)  

    # 2 PROCESO _ qué hago con eso
      # redondear el numero 

    # 3 SALIDA _ qué debo mostrar 
      # el numero redondeado con la cantidad de decimales elegidos
# ------------------------------------------------------------------------------------
# 2 BOSQUEJO A MANO 

  # numero = 3.14159
  # decimales = 2
  # redondeo = 3.14

# ------------------------------------------------------------------------------------
# 3 DESCUBRIR EL PATRON 

  # Redondear un numero con la cantidad de decimales elegidos 
  
# ------------------------------------------------------------------------------------
#  4 ESCRIBIR EL CÓDIGO

num = float(input("Ingrese un número decimal: "))
decimales = int(input("¿Cuántos decimales desea?: "))

# # La función round() redondea al entero más cercano
resultado = round(num, decimales)

print(f"Resultado: {resultado}")


# -----------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 9 _ Descuento por cantidad
    # Un producto vale $12. Si compras 10 o más te dan 15% de descuento, si
    # compras entre 5 y 9 te dan 5%. Calcula el total.
# ------------------------------------------------------------------------------------
# 1 ENTENDER EL PROBLEMA 

    # 1 ENTRADA _ qué me dan 
      # costo (float)
      # cantidad (input)

    # 2 PROCESO _ qué hago con eso
      # calcular el descuento segun la cantidad de productos elegidos 

    # 3 SALIDA _ qué debo mostrar 
      # mostrar el total con el descuento
# ------------------------------------------------------------------------------------
# 2 BOSQUEJO A MANO 

  # costo = 12
  # cantidad = 12  
  # subtotal = 12 x 12 = 144
  # descuento = 144 * 0.15 = 21.6  
  # total = 144 - 21.6

# ------------------------------------------------------------------------------------
# 3 DESCUBRIR EL PATRON 

  # Es una operación de calcular el descuento 
 
# ------------------------------------------------------------------------------------
#  4 ESCRIBIR EL CÓDIGO
cantidad = int(input("¿Cuántos productos compra?: "))

costo = 12
subtotal = cantidad * costo

if cantidad >= 10:
    descuento = subtotal * 0.15
elif cantidad >= 5:
    descuento = subtotal * 0.05
else:
    descuento = 0

total = subtotal - descuento

print(f"Subtotal: ${subtotal}")
print(f"Descuento: ${descuento}")
print(f"Total: ${total}")
# -----------------------------------------------------------------------------------------------------------------------------------
