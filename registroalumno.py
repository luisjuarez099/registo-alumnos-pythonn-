def saludo():
    print('Hola  queridos alumnos de unedl de la carrera Derecho')
print("\n")
def alumno(clave,carrera):
    carrera=carrera.capitalize()
    print(f"Hola alumno/a {clave} de la carrera de {carrera}")
clave=(input("Nombre  del estudiante: "))
carrera=input("Carrera que cursa actualmente: ")

print("\n")

def calif():
    calif_list=[]
    num=0
    res=0
    for i in range(1,9):
        calif_list.append(int(input(f"Digita tus calificaciones {i}: ")))
    for x in calif_list:
        calif_list=tuple(calif_list)
        a=calif_list
        z=(sum(a)/8)
    print(f"Su promedio Total es de: {z}") 
    if z>=70:
        print("Aprobado. Nos vemos en el siguiente semestre. FELICIDADES \n")
    else:
        print(f"Vas a extraordinario. Su promedio Total es de: {z}")


def saludo_siaru():
    print("Bienvenido a Siaru la plataforma de alumnos UNEDL")

#-----------------------------

if __name__=='__main__':
    saludo()
    saludo_siaru()
    alumno(clave, carrera)
    calif()
    
'''tarea
hacer que valide caracteres diferente en clave
'''
