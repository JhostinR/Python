# ===========================================================================
# Importaciones de clases y librerias necesarias
# ===========================================================================
# region 
from models.menu import Menu
from models.operadores import Operacion
import os
# endregion


# ===========================================================================
# VARIABLES GLOBALES
# ===========================================================================
# region
# clases globales para utilizar el registro de logs y la impresion de actividades e instancia de metodos
menu = Menu()
operador = Operacion()
opcion = 1
# endregion

# ===========================================================================
# METODO MAIN
# ===========================================================================
# region 
def main(opcion):
    while opcion != 0:
        menu.mostrarTitulo()
        menu.mostrarMenu()
        try:
            opcion = int(input())
        except ValueError as ex:
            clear = lambda: os.system('cls')
            clear()
            print("El valor no es numerico Error: " + str(ex))
            print("oprime una tecla para continuar")
            input()
        
        if opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4:
            clear = lambda: os.system('cls')
            clear()
            operador.enviarController(opcion)
        if opcion == 0:
            clear = lambda: os.system('cls')
            clear()
            mensaje =  "======================\n"
            mensaje += "| Hasta luego...     |\n"
            mensaje += "======================\n"
            print(mensaje)
        else:
            clear = lambda: os.system('cls')
            clear()
            print ("La opcion escogida es incorrecta\n escoge otra opcion\n\n")
# endregion
    
# Metodo para inicializar el metodo main    
if __name__ == '__main__':
    main(opcion)