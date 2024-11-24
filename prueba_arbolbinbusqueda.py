from modelo_solucion import *
from arboles2023 import *
#Creacion de Ciudades
ciudad00 = Ciudad("Madrid", 1850, 1983821)
ciudad01 = Ciudad("Barcelona", 1910, 1833821)
ciudad02 = Ciudad("Cartagena", 1763, 2088210)
ciudad03 = Ciudad("Sevilla", 1970, 393821)
ciudad04 = Ciudad("Moros", 1990, 283821)
ciudad05 = Ciudad("Soledad", 1960, 193825)
ciudad06 = Ciudad("Tenerife", 1870, 63432)
#Creacion de instancia
arbol01 = ArbolBinarioBusqueda()

#Adicion de elementos al arbol
arbol01.insertar(ciudad03)
arbol01.insertar(ciudad04)
arbol01.insertar(ciudad02)
arbol01.insertar(ciudad05)
arbol01.insertar(ciudad01)
arbol01.insertar(ciudad06)
arbol01.insertar(ciudad00)

#Visualización
print("Arbol:\n",arbol01.verArbol())
print("Ciudad de mayor población:",arbol01.buscarCiudadMaxPoblacion())


