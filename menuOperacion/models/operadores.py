import os

class Operacion:
    def __init__(self):
        self.__num1 = 0
        self.__num2 = 0
        self.__resultado = 0
    
    def realizarSuma(self):
        self.__resultado = self.__num1 + self.__num2
        
    def realizarResta(self):
        self.__resultado = self.__num1 - self.__num2
       
    
    def realizarMultiplicacion(self):
        self.__resultado = self.__num1 * self.__num2
    
    def realizarDivision(self):
        self.__resultado = self.__num1 / self.__num2

    
    def pedirNumeros(self):
        try:
            mensaje =  "=============================\n"
            mensaje += "| Ingresa los datos         |\n"
            mensaje += "=============================\n"
            mensaje += "| Ingresa el primer numero   \n"
            mensaje += "=============================\n"
            print(mensaje)
            self.__num1 = int(input())  
            mensaje2 =  "=============================\n"
            mensaje2 += "| Ingresa el segundo numero   \n"
            mensaje2 += "=============================\n"
            print(mensaje2)
            self.__num2 = int(input()) 
        except ValueError as ex:
            clear = lambda: os.system('cls')
            clear()
            print("El valor no es numerico Error: " + str(ex))
            print("oprime una tecla para continuar y la tecla enter")
            input()
              
    def imprimirResultado(self):
        clear = lambda: os.system('cls')
        clear()
        mensaje2 =  "==================================\n"
        mensaje2 += "| El resultado de la operacion es:\n"
        mensaje2 += "==================================\n"
        mensaje2 += "| " + str(self.__resultado)
        print(mensaje2)
        print("==================================\n")
        print("oprime una tecla para continuar y enter")
        input()
        clear = lambda: os.system('cls')
        clear()
    
    def enviarController(self,opcion):
        if opcion == 1:
            self.pedirNumeros()
            self.realizarSuma()
            self.imprimirResultado()
        if opcion == 2:
            self.pedirNumeros()
            self.realizarResta()
            self.imprimirResultado()
        if opcion == 3:
            self.pedirNumeros()
            self.realizarMultiplicacion()
            self.imprimirResultado()
        if opcion == 4:
            self.pedirNumeros()
            if self.__num2 == 0:
                print("El numero a dividir no puede ser cero (0)")
                print("oprime una tecla para continuar y la tecla enter")
                input()
                clear = lambda: os.system('cls')
                clear()
            else:
                self.realizarDivision()
                self.imprimirResultado()
        
        
        
    
    