#creando diccionario con dict()
diccionario = dict(nombre="Jhostin", apellido="Arango")

#las listas noo pueden ser claves y usamos frozenset para meter conjuntos
diccionario = {frozenset(["Arango", "Rios"]): "jaja"}

#creando diccinarios con fromkeys()
diccionario = dict.fromkeys(["nombre", "apellido", "edad"])

#creando diccionarios con fromkeys() cambiando el valor por defecto a "no se"
diccionario = dict.fromkeys(["nombre", "apellido", "edad"], "no se")

print(diccionario)