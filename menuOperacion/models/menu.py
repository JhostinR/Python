class Menu:
    def __init__(self):
        self.__titulo = ""
        self.__mensaje = ""
        
    def mostrarTitulo(self):
        self.__titulo =  "======================\n"
        self.__titulo += "| Bienvenido al menu |\n"
        self.__titulo += "======================\n"
        print(self.__titulo)
    
    def mostrarMenu(self):
        self.__mensaje  = "| 1. Sumas           |\n"
        self.__mensaje += "| 2. restas          |\n"
        self.__mensaje += "| 3. Multiplicacion  |\n"
        self.__mensaje += "| 4. Division        |\n"
        self.__mensaje += "| 0. Salir           |\n"
        self.__mensaje += "======================\n"
        self.__mensaje += "| escoge una opcion  |\n"
        self.__mensaje += "======================\n"
        print(self.__mensaje)
        
        
    