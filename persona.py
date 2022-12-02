class persona:
    nombre        = str
    edad          = int
    centroEstudio = str
    
    def __init__(self, nombre, edad, centroEstudio):
        self.nombre = nombre
        self.edad = edad
        self.centroEstudio = centroEstudio
        
    def conversar (self, otra_persona):
        return f"Hola {otra_persona.nombre} me llamo {self.nombre}, estudio en {self.centroEstudio}" 
    
if __name__ == "__main__":
    persona1 = persona("Juan", 18, "Yavirac")
    persona2 = persona("Alisson", 21, "UCE")
                       
    print(persona1.conversar(persona2))
