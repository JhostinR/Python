diccionario = {
    "nombre": 'Jhostin',
    "apellido": 'Arango',
    "edad": 19
}
#nos devuelve un objeto dict_item
claves = diccionario.keys()

#obteniendo un elemento con get()(si no encuentra nada el programa sigue)
valor_de_jajaja = diccionario.get("jajaja")

#eliminando todo del diccionario
#diccionario.clear()

#eliminando un elemento del diccionario
diccionario.pop("apellido")

#obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()

print(diccionario_iterable)