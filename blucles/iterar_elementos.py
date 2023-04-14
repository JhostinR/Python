animales = ["gato", "perro", "loro", "cocodrilo", "gorila"]
numeros = [52,16,14,72,11]

#recorriendo la lista animales
for animal in animales:
    print(f'Ahora la variable animal es igual a: {animal}')

#recorriendo la lista de numeros y multiplicando por 10
for numero in numeros:
    resultado = numero * 10
    print(resultado)

#iterando dos listas del mismo tamaño al mismo tiempo
for numero,animal in zip(animales,numeros):
    print(f'recorriendo lista 1: {numero}')
    print(f'recorriendo lista 2: {animal}')

#forma no optima de recorrer una lista con su indice (no funciona en conjuntos)
for num in range(len(numeros)):
    print(numeros[num])

#forma correcta de recorrer una lista con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'el indice es: {indice} y el valor es: {valor}')
    
#usando el for/else
for numero in numeros:
    print(f"ejecutando el ultimo bucle, valor actual: {numero}")
else:
    print("el bucle termino")
    
#todo lo anterior funciona igualmente en tuplas y en conjuntos