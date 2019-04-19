#Python
#No se necesita indicar el tipo de variable, se guía por contenido
#for:
for i in elemento:
    pass

#Se concatena con coma
print("fhdjf", end = " ")
#Hacer cast
est = int(20)

#FUNCIONES:
#No necesita llaves.
def nombre_funcion:
    #Código
    return #algo

#LISTAS O ARREGLOS:
#Puede almacenar variables de diferentes tipos
#Sintaxis y propiedades
arreglo = [1, "dos", False, 5, [1, 2, 3]]
#Se puede sumar un elemento y se concatena al final.
arreglo += "Holi"
#Acceder a elementos:
arreglo[1]
#Borrar, añadir, longitud, buscar, eliminar, duplicados
del(arreglo[4])
arreglo.append(1)
arreglo.insert("ad", 23)
len(arreglo)
arreglo.index("afddd")
arreglo.remove(False)
arreglo.remove(1:2)
set(arreglo)
#Convertir cadena a lista
"1, 1, 1, 1".split(",")

#TUPLAS
#No se puede cambiar una vez creadas, tiene un aorden
#Encierra variables de diferente tipo
#Sintaxis
tupla = (1, 45, "ldjkfs", True)
#Longitud, búsqueda
len(tupla)
tupla.index(1)

#DICCIONARIOS
#Estrucutras de datosque guardan conjuntos clave-valor
#No pueden existir dos elementos con la misma clave
#Sintaxis
diccionario = {"Clave": "valor", 1:3, False:5}
diccionario["Clave"] = [23, 1]
diccionario[2] = [09]
#Para buscar un valor, se usa get con la clave
diccionario.get(1)
#Se busca y recorre con for
#Sintaxis de if, if-else, while, for, elif
if (5 > 10):
#-----
if (10 != 2):
    #Código
else:
    #Código
#------
while(1 == 2):
    #Código
#-------
for i in elemento:
    #Código
    pass
if (2 < 5):
    #Código
elif (4 == 1):

#Continue = Para seguir el ciclo cuando se cumple un condicional
#Pass = No hacer ciclo
#Else = Se puede usar con el for

#GENERADOR
#Son funciones que devuelven una lista pero poco a poco
#Es decir, elemento por elemento
#En vez de "return" se usa "yield", también puede llevar ambos
#Sintaxis
def nombre_Generador():
    #Código
    yield #algo

#EXCEPCIONES
#Para captura de excepciones se usa:
try:
    #Código
except #Excepción:

#Para "generar" excepciones, se usa raise
raise TypeError("Error")





#POO
#Sintaxis de clase, métodos, instancia, constructor
class Clase():

def metodo(self, arg1, arg2):
    self.atributo = 0

resultado = self.metodo(1, 2)

miClase = Clase()

#constructor y encapsulación
def __init__(self):
    self.atributo = 0
    #Encapsula el atributo2
    self.__atributo2 = 1

def __metodo():
    #código

#Herencia simple y Herencia múltiple

class Clase1():
    #Código y constructor

class Clase2(Clase1):
    #código

class  Clase3(Clase1, Clase2):
    #Código
#En la herencia múltiple, se da preferencia a la primera clase
#Por ende, se usa el constructor de la primera clase

#Sobreescribir métodos
#Sólo se escribe el mismo nombre del método en la Clase

#Uso de uper
# COMBAK:
class Clase4(Clase1):

    def __init__(self, atributo):
        super.__init__(#Atributos de la clase padre)
#Con super se manda a llamar a los métodos de la clase
#Padre que se tenga

#isinstance
#Se usa para saber a que instancia se refiere el objeto
isinstance(objeto, Clase)

#MÓDULOS
#Son archivos .py que se importan en un Código
#Se manejan como objetos
import nombre_archivo

nombre_archivo.función
#Ó
from nombre_archivo import clase o * #Para todo

#función o clase

#PAQUETES
#Son carpetas con módulos que se relacionan entre sí
#La carpeta debe tener un archivo con nombre __init__.py
#Para importar un módulo de un paquete es:
from nombre_paquete.nombre_archivo import *

#ARCHIVOS
#Para manipular archivos, se usa la librería io

#SERIALIZACIÓN
#Se usa para guardar en un fichero un objeto o diccionarios
#Se usa la biblioteca pickle
