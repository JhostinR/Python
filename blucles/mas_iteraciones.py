
frutas = ["manzana", "mango", "pera", "papaya"]
cadena = "Hola Jhostin"
numeros = [2,10,8,9]

#evitano que se coma una pera con la sentencia continue
for fruta in frutas:
    if fruta == "pera":
        continue
    print(f"Me voy a comer una {fruta}")

#evitar que el bucle siga ejecutandose
for fruta in frutas:
    print(f"Me voy a comer una {fruta}")
    if fruta == "papaya":
        break
else:
    print("Terminado")
    
#recorrer una cadena de texto
for letra in cadena:
    print(letra)

#for en una sola linea de codigo
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)