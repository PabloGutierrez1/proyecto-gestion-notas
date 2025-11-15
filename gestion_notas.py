#Pablo Gutierrez: 21550852-8
class Estudiante:
    def __init__(self, rut, nombre, apellido, edad, materia):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.materia = materia
        self.nota1 = 0
        self.nota2 = 0
        self.nota3 = 0
        self.nota4 = 0

    def ingreso_nota(self, nota1, nota2, nota3, nota4):
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4
    
    def notas_promedio(self):
        promedio = (self.nota1 * 0.4 + self.nota2 * 0.4 + self.nota3 * 0.1 + self.nota4 * 0.1)
        return promedio
    
    def estado_estudiante(self):
        if self.notas_promedio() >= 4:
            return "Aprobado"
        else:
            return "Reprobado"

    def descripcion_estudiante(self):
        print(f"Estudiante:\n"
            f"Rut: {self.rut}\n"
            f"Nombre: {self.nombre} {self.apellido}\n"
            f"Edad: {self.edad}\n"
            f"Nota: {self.notas_promedio():.2f}\n"
            f"Estado: {self.estado_estudiante()}\n"
            f"Materia: {self.materia}\n")

def info_estudiante():
    rut = input("Ingrese el rut del estudiante: ")
    nombre = input("Ingrese el nombre del estudiante: ")
    apellido = input("Ingrese el apellido del estudiante: ")
    edad = input("Ingrese la edad del estudiante: ")
    materia = input("Ingrese la materia correspondiente del estudiante: ")
    return Estudiante(rut, nombre, apellido, edad, materia)

def ingreso_notas(estudiantes):                                                 
    rut = input("Ingrese el rut del estudiante para el que desea registrar las notas: ")
    for estudiante in estudiantes:
        if estudiante.rut == rut:
            nota1 = float(input("Ingrese la primera nota: "))
            nota2 = float(input("Ingrese la segunda nota: "))
            nota3 = float(input("Ingrese la tercera nota: "))
            nota4 = float(input("Ingrese la cuarta nota: "))
            estudiante.ingreso_nota(nota1, nota2, nota3, nota4)
            print(f"Se registraron las notas para el estudiante {estudiante.nombre}")
            return
    print("El rut ingresado no se encuentra registrado.")

def listar_notas(estudiantes):
    print("******** Notas Estudiantes ********")
    for estudiante in estudiantes:
        estudiante.descripcion_estudiante()

def principal():
    estudiantes = []
    while True:
        print("******** Bienvenido a la aplicación de Sistema de Notas ********")
        print("1.- Ingrese un Alumno.")
        print("2.- Ingresar notas de Alumno.")
        print("3.- Listar Notas de Alumnos.")
        print("4.- Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            estudiante = info_estudiante()
            estudiantes.append(estudiante)
            print("Estudiante ingresado correctamente.")
        elif opcion == "2":
            if not estudiantes:
                print("No hay estudiantes registrados.")
            else:
                ingreso_notas(estudiantes)
        elif opcion == "3":
            if not estudiantes:
                print("No hay estudiantes registrados.")
            else:
                listar_notas(estudiantes)
        elif opcion == "4":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")

principal()
