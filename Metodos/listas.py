#region
#LEN cuenta la cantidad de elementos de una lista

#APPEND agrega un elemento a la lista
#INSERT agrega un elemento a la lista en el indice especificado
#EXTEND agrega varios elementos a la lista

#POP elimina un elemento de una lista pide indice y devuelve valor
#REMOVE remueve un elemento de una lista, pide valor
#CLEAR elimina todos los elementos de una lista

#SORT ordena una lista de forma ascendente a descendente
#REVERSE invierte los elementos de una lista
#endregion

#creando una lista con list()
lista = list(["Hola","Bull", 19])

#devuelve la cantidad de elementos
resultado1 = len(lista)

#agregando un elemento a la lista
lista.append("Decimelo")

#agregando un elemento a la lista en un indice especifico
lista.insert(2,"ensayo")

#agregando varios elementos a la lista
lista.extend([False,2023])

#eliminando un elemento de la lista por su indice
lista.pop(-2) #-1 para eliminar el ultimo, -2 para el penultimo etc..

#removiendo un elemento de la lista por su valor
lista.remove("ensayo")

#eliminando todos los elementos de la lista
#lista.clear()

#ordena la lista en forma ascendente con .reverse es descendente
#lista.sort()

#revierte el orden de la lista
lista.reverse()

#verificando si un elemento se encuentra en la lista
elemento_encontrado = lista.index("Bull")
print(elemento_encontrado)