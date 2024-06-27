##Ejercicio 1:

from datetime import date, timedelta

class Fecha:
    def __init__(self,dd=None, mm=None, aaaa=None):
        if dd is None or mm is None or aaaa is None:
            today = date.today()
            self.dd = today.day
            self.mm = today.month
            self.aaaa = today.year
        else: 
            self.dd = dd
            self.mm = mm
            self.aaaa = aaaa

    def __str__(self):
        return f"{self.dd:02d}/{self.mm:02d}/{self.aaaa}"

    def __add__(self,days):
        fecha_original = date(self.aaaa, self.mm, self.dd)
        nueva_fecha = fecha_original + timedelta(days=days)
        return Fecha(nueva_fecha.day, nueva_fecha.month, nueva_fecha.year)

    def __eq__ (self, other):
        return (self.dd == other.dd) and (self.mm == other.mm) and (self.aaaa == other.aaaa)


    def calcular_dif_fecha(self, otra_fecha):
        fecha1 = date(self.dd, self.mm, self.aaaa)
        fecha2 = date(otra_fecha.dd, otra_fecha.mm, otra_fecha.aaaa)
        diferencia = abs(fecha1 - fecha2).days
        return diferencia



##Ejercicio 2:

from datetime import date, timedelta

class Alumno:
    def __init__(self, nombre, dni, fecha_ingreso, carrera):
        self.datos = {
            "Nombre" : nombre,
            "DNI" : dni,
            "FechaIngreso" : fecha_ingreso,
            "Carrera" : carrera
        }

    def cambiar_datos(self, nombre=None, dni=None, fecha_ingreso=None, carrera= None):
        if nombre:
            self.datos["Nombre"] = nombre
        if dni:
            self.datos["DNI"] = dni
        if fecha_ingreso:
            self.datos["FechaIngreso"] = fecha_ingreso
        if carrera:
            self.datos["Carrera"] = carrera
        
    def antiguedad(self):
        fecha_ingreso = self.datos["FechaIngreso"]
        hoy = date.today()
        años_antiguedad = hoy.year - fecha_ingreso.year - ((hoy.month, hoy.day) < (fecha_ingreso.month, fecha_ingreso.day))
        return años_antiguedad

    def __str__(self):
        return f"Nombre: {self.datos['Nombre']}, DNI: {self.datos['DNI']}, Fecha de Ingreso: {self.datos['FechaIngreso']}, Carrera: {self.datos['Carrera']}"
    
    def __eq__(self, other):
        return self.datos == other.datos

    
    ##Ejercicio 3:

from datetime import date
import random
import string

class Alumno:
    def __init__(self, nombre, dni, fecha_ingreso, carrera):
        self.datos = {
            "Nombre": nombre,
            "DNI": dni,
            "FechaIngreso": fecha_ingreso,
            "Carrera": carrera
        }

class Nodo:
    def __init__(self, alumno=None):
        self.alumno = alumno
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
    
    def lista_ejemplo(self, cantidad_alumnos):
        for _ in range(cantidad_alumnos):
            nuevo_alumno = self.generar_alumno_aleatorio()
            self.agregar_al_final(nuevo_alumno)
    
    def agregar_al_final(self, alumno):
        nuevo_nodo = Nodo(alumno)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
    
    def generar_alumno_aleatorio(self):
        nombres = ["Guido", "Jimena", "Lucas", "Antonela", "Carlos", "Luana"]
        apellidos = ["González", "Pérez", "Rodríguez", "Fernández", "López"]
        carrera = ["Ingeniería Informática", "Medicina", "Derecho", "Administración"]
        
        nombre_completo = random.choice(nombres) + " " + random.choice(apellidos)
        dni = random.randint(10000000, 99999999)
        fecha_ingreso = date(random.randint(2015, 2023), random.randint(1, 12), random.randint(1, 28))
        carrera_alumno = random.choice(carrera)
        
        return Alumno(nombre_completo, dni, fecha_ingreso, carrera_alumno)
    
    def __iter__(self):
        self.nodo_actual = self.cabeza
        return self
    
    def __next__(self):
        if self.nodo_actual is None:
            raise StopIteration
        else:
            alumno = self.nodo_actual.alumno
            self.nodo_actual = self.nodo_actual.siguiente
            return alumno
    
    def imprimir_lista(self):
        actual = self.cabeza
        while actual:
            print(actual.alumno)
            actual = actual.siguiente


##Ejercicio 4:

def ordenar_por_fecha_ingreso(self):
        if self.cabeza is None or self.cabeza.siguiente is None:
            return
        actual = self.cabeza
        while actual:
            siguiente = actual.siguiente
            while siguiente:
                if actual.alumno.datos["FechaIngreso"] > siguiente.alumno.datos["FechaIngreso"]:
                    # Intercambiar los datos de los alumnos en los nodos
                    actual.alumno, siguiente.alumno = siguiente.alumno, actual.alumno
                siguiente = siguiente.siguiente
            actual = actual.siguiente

##Ejercicio 5: 

import pickle
import os

class Alumno:
    def __init__(self, nombre, dni, fecha_ingreso, carrera):
        self.nombre = nombre
        self.dni = dni
        self.fecha_ingreso = fecha_ingreso
        self.carrera = carrera
    
    def __str__(self):
        return f"Nombre: {self.nombre}, DNI: {self.dni}, Fecha de Ingreso: {self.fecha_ingreso}, Carrera: {self.carrera}"

    class ListaAlumnos:
    def __init__(self):
        self.alumnos = []
    
    def agregar_alumno(self, alumno):
        self.alumnos.append(alumno)
    
    def guardar_en_archivo(self, nombre_archivo):
        try:
            with open(nombre_archivo, 'wb') as f:
                pickle.dump(self.alumnos, f)
            print(f"Lista de alumnos guardada en '{nombre_archivo}' correctamente.")
        except IOError as e:
            print(f"Error al guardar el archivo: {e}")
    
    @staticmethod
    def cargar_desde_archivo(nombre_archivo):
        try:
            with open(nombre_archivo, 'rb') as f:
                alumnos = pickle.load(f)
            lista_alumnos = ListaAlumnos()
            lista_alumnos.alumnos = alumnos
            return lista_alumnos
        except IOError as e:
            print(f"Error al cargar el archivo: {e}")
            return None

def crear_directorio(nombre_directorio):
    try:
        os.mkdir(nombre_directorio)
        print(f"Directorio '{nombre_directorio}' creado correctamente.")
    except FileExistsError:
        print(f"El directorio '{nombre_directorio}' ya existe.")
    except OSError as e:
        print(f"Error al crear el directorio '{nombre_directorio}': {e}")

def mover_directorio(origen, destino):
    try:
        os.rename(origen, destino)
        print(f"Directorio movido de '{origen}' a '{destino}' correctamente.")
    except OSError as e:
        print(f"Error al mover el directorio: {e}")

def borrar_archivo(nombre_archivo):
    try:
        os.remove(nombre_archivo)
        print(f"Archivo '{nombre_archivo}' borrado correctamente.")
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe.")
    except OSError as e:
        print(f"Error al borrar el archivo '{nombre_archivo}': {e}")

def borrar_directorio(nombre_directorio):
    try:
        os.rmdir(nombre_directorio)
        print(f"Directorio '{nombre_directorio}' borrado correctamente.")
    except FileNotFoundError:
        print(f"El directorio '{nombre_directorio}' no existe.")
    except OSError as e:
        print(f"Error al borrar el directorio '{nombre_directorio}': {e}")