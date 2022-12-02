class miClase:
    x = 5
    
p1= miClase()
print(p1.x)

class persona:
    nombre = str  
    edad   = int
    
    def __init__(self,nombre,edad):
        self.nombre = nombre 
        self.edad   = edad 
        
    def __str__(self):
        return f"Su nombre es: {self.nombre}. Y su edad es: {self.edad}"  
      
        
p2 = persona("Diego", 29) 

print(p2)  

class persona2:
    nombre = str
    edad   = int
    cedula = int
    
    def __init__(self, nombre, edad, cedula):
        self.nombre = nombre
        self.edad   = edad
        self.cedula = cedula
        
    def miFuncion(self):
        print("Hola mi nombre es" + self.nombre + "mi edad es: " + self.edad + "Mi numero de cedula es: " + self.cedula)
        
p3 = persona("Alexander", 30, "1711111111")
p3.miFuncion()  

p3.nombre = "Carlos"
p3.cedula = "12121212"

p3.miFuncion()
          
class persona:
    nombre = str  
    edad   = int
    estatura = int
    
    def __init__(self,nombre,edad, estatura):
        self.nombre = nombre 
        self.edad   = edad 
        self.estatura = estatura
        
    def __str__(self):
        return f"Su nombre es: {self.nombre}. Y su edad es: {self.edad}. Y su estatura es: {self.estatura}"  
      
        
p4 = persona("Diego", 29, 171) 

print(p4)

def p4.edad
print(p4)
