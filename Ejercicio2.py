print("==============================")
print("=== BIENVENIDO AL PROGRAMA ===")
print("==============================")

# Solicitar tres números enteros desde teclado
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

# Determinar el número más grande
if num1 >= num2 and num1 >= num3:
    num_mayor = num1
elif num2 >= num1 and num2 >= num3:
    num_mayor = num2
else:
    num_mayor = num3

# Determinar el número más pequeño
if num1 <= num2 and num1 <= num3:
    num_menor = num1
elif num2 <= num1 and num2 <= num3:
    num_menor = num2
else:
    num_menor = num3

# Determinar el número de en medio
if num_menor < num1 < num_mayor:
    num_medio = num1
elif num_menor < num2 < num_mayor:
    num_medio = num2
else:
    num_medio = num3

# Mostrar los resultados en pantalla
print("El número",num_mayor, "es el número más grande de los tres")
print("El número",num_menor, "es el número más pequeño de los tres")
print("El número",num_medio, "es el número de en medio de los tres")

print("FIN DEL PROGRAMA")