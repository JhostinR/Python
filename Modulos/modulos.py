#importano un modulo y asignandole el nombre "saludom"
#import modulo_saludar as saludom

#desde ese modulo, importamos dos funciones
from modulo_saludar import saludar as saludom, saludar_raro as saludar_como_ñero

saludo = saludom("Jhostin")
saludo_raro = saludar_como_ñero("David")

#mostramos resultados
print(saludo)
print(saludo_raro)

#para ver las propiedades y metodos del namespace
#print(dir(saludom))

#accedemos al nombre de este modulo
print(__name__)

#accedemos al nombre del modulo llamado
#print(saludom.__name__)

