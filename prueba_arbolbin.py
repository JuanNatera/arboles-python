from modelo_solucion import *
from arboles2023 import *
#Creacion de Ciudades
ciudadRaiz = Ciudad("Madrid", 1850, 1983821)
ciudad01 = Ciudad("Barcelona", 1910, 1833821)
ciudad02 = Ciudad("Cartagena", 1763, 208821)
ciudad03 = Ciudad("Sevilla", 1970, 393821)
ciudad04 = Ciudad("Moros", 1990, 283821)
ciudad05 = Ciudad("Soledad", 1960, 193825)
ciudad06 = Ciudad("Tenerife", 1870, 63432)
#Creacion de Nodos
raiz = ArbolBinario(ciudadRaiz)
nodo01 = ArbolBinario(ciudad01)
nodo02 = ArbolBinario(ciudad02)
nodo03 = ArbolBinario(ciudad03)
nodo04 = ArbolBinario(ciudad04)
nodo05 = ArbolBinario(ciudad05)
nodo06 = ArbolBinario(ciudad06)
#Conexion de nodos
raiz.hijo_izquierdo = nodo01
raiz.hijo_derecho = nodo02
nodo02.hijo_izquierdo = nodo03
nodo01.hijo_derecho = nodo04
nodo03.hijo_derecho = nodo05
nodo03.hijo_izquierdo = nodo06
#Visualización
print("Arbol:\n",raiz.verArbol())
#Zona de influencia
print("Zona de Influencia:",raiz.buscarZona("Sevilla"))
print("Zona de Influencia:",raiz.buscarZona("Soledad"))
print("Zona de Influencia:",raiz.buscarZona("Madrid"))

