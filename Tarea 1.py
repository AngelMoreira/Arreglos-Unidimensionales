cantidad = int(input("Ingrese la cantidad de temperaturas que desea ingresar: "))
temperaturas = []

for i in range(cantidad):
    temp = float(input(f"Ingrese la temperatura {i+1}: "))
    temperaturas.append(temp)

media = sum(temperaturas) / cantidad
contador = sum(1 for temp in temperaturas if temp >= media)

print(f"La media de las temperaturas es: {media:.2f}")
print(f"Cantidad de temperaturas mayores o iguales a la media: {contador}")
