#creando una funcion de 3 parametros
#def frase(nombre,apellido,adjetivo):
#   return f"Hola {nombre} {apellido}, eres muy {adjetivo}"

#Utilizando keyword arguments
#frase_final = frase(adjetivo="Cool",nombre="Jhostin",apellido="Arango")

#creando la misma funcion con un parametro opcional y un valor por defecto
def frase(nombre,apellido,adjetivo ="Lampara"):
  return f"Hola {nombre} {apellido}, eres muy {adjetivo}"

frase_final = frase("Jhostin", "Arango", "Responsable")
print(frase_final)