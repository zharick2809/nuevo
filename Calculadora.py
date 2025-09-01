print("Bienvenido a la calculadora")
print("Selecciona la operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion = input("Ingresa el número de la operación (1/2/3/4): ")
if opcion == "1": 
   num1 = float(input("ingrese el primer numero"))
   num2 = float(input("ingrese el segundo numero "))
   resultado = num1 + num2 
   print("el resultado de la suma es:",resultado)

if opcion == '2':
    num1 = float (input("ingrese el primer numero"))
    num2 = float (input ("ingrese el segundo numero"))
    resultado = num1-num2
    print(f"{num1} + {num2} = {resultado}")

if opcion == "3":
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    resultado = num1 * num2
    print("El resultado de la multiplicación es:", resultado)