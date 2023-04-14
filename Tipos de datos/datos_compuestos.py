#Creando uns lista se puede modificar
lista = ["Jhostin Arango", "Soy estudiante", True, 1.77]
#creando una lista no se puede modificar
tupla = ("Jhostin Arango", "Soy estudiante", True, 1.77)

#valido
lista[3] = "Falsedad"

#no valido
#tupla[3] = "Falsedad"

#creando un conjunto (set) (no se accede a elementos por indice, no almacena datos duplicados)
conjunto = {"Jhostin Arango", "Soy estudiante", True, 1.77, "Soy estudiante"}

#print(conjunto[3]) no puede acceder al elemento

#creando un diccionario (dict) (la estructura es: key : value y separamos con comas)
diccionario = {
    'nombre': "Jhostin Arango",
    'profesion': "Estudiante",
    'emocionado': False,
    'altura': 1.77,
    'dato duplicado': "Estudiante"
}
print(diccionario['altura'] + 0.03 + 0.20)