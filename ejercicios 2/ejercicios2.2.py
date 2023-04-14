#creando una funcion que noos devuelva los numeros primos 
#entre 0 y el argumento que pasamos

def es_primo(num):
    #verificamos que el numero pasado no pueda dividirse por ningun numero entre 2 y ese mismo numero -1
    for i in range(2,num-1):
        #si es divisible por alguno retornamos false y termina en bucle
        if num%i==0: return False
        #si termina en bucle significa que no fue divisible entonces es primo
    return True

#creando funcion que retorna una lista con todos los primos
def primos_hasta(num):
    #creamos la lista
    primos = []
    for i in range(3,num+1):
        #verificamos si el valor es primo
        resultado = es_primo(i)
        #en caso de que sea lo agregamos a la lista
        if resultado == True: primos.append(i)
        #devolvemos la lista
    return primos 

resultado = primos_hasta(98)
print(resultado)