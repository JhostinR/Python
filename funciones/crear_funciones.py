#creando una funcion simple
#def saludar():
#    print("Welcome to manizales")
    
#ejecutando la funcion simple
#saludar()

#crear una funcion que tenga parametros
def saludar(nombre,genero):
    genero = genero.lower()
    if(genero == "masculino"):
        adjetivo = "rey"
    elif(genero == "femenino"):
        adjetivo = "reina"
    else:
        adjetivo = "amor"
        
    print(f"hola {nombre}, mi {adjetivo} ¿como estas?")
    
saludar("Natalia", "femenino") 
saludar("Jake", "masculino")
saludar("David", "no binario")

#crear una funcion que nos retorne valores
def crear_contraseña_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num 
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña,num
    
#desempaquetando la funcion
password,primer_numero = crear_contraseña_random(456)

#mostrando los resultados obtenidos y los datos utilizados para obtenerlo
print(f"Tu nueva contraseña es: {password}")
print(f"El numero utilizado para crearla fue: {primer_numero}")

    

