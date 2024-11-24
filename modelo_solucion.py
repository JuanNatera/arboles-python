#Clase Ciudad
class Ciudad:
    def __init__(self, nombre:str, anno_creacion:int, poblacion:int) -> None:
        self.nombre = nombre
        self.anno_creacion = anno_creacion
        self.poblacion = poblacion
    
    def __str__(self) -> str:
        return str(self.nombre)
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def __eq__(self, otro_objeto: "Ciudad") -> bool:
        if not isinstance(otro_objeto, Ciudad):
            return False
        return self.nombre == otro_objeto.nombre
    
    def __hash__(self) -> int:
        return hash(self.__str__())
    
    def __lt__(self, otro_objeto:"Ciudad") -> bool:
        if not isinstance(otro_objeto, Ciudad):
            return False
        return self.poblacion < otro_objeto.poblacion