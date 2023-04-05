"""
alumnos ={
    'nombre' : "Juan",
    'apellido' : "Perez",
    'cedula' : "0107693849",
    'dirreccion' : "Cuenca",
    'email' : "juan@gmail.com"
         }

print(f"Los datos del alumno son: \n\t{alumnos}")

print(f"La cedula es: \n\t{alumnos['cedula']}")
print(f"El email es: \n\t{alumnos['email']}")

alumnos["cedula"] = 1105050775
print(f"La cedula es: \n\t{alumnos['cedula']}")

alumnos["genere}o"] = "Masculino"
print(f"Los datos del alumno son: \n\t{alumnos}")

"""


instituto = {
    'carreras' : ["Big Data", "Software","Infraestructura","Entrenamiento","Audiovisual"],
    'materias' : ["Machine","BDR","BDNR","Probabilidad","Legislacion","Fundamentos"],
    'profesores' : ["Lady","Hector","Veronica","Diana","Germania","Catherine"],
    'Notas' : [72.16,71.94,82.75,70.01,90.10,80.50] 
            } 

print(f"Las Carreras del Instituto son: \n\t{instituto['carreras']}")
print(f"Las Materias de Big Data son: \n\t{instituto['materias']}")
print(f"Los Profesores de Big Data son: \n\t{instituto['profesores']}")
print(f"Las Notas finales son: \n\t{instituto['Notas']}")


# print("El promedio de las notas de la carrera de Big Data son:\n\t", sum(instituto["Notas"])/len(instituto["Notas"]))
"""
suma = 0
for e in instituto["Notas"]:
    suma += e

print("El promedio de las notas de la carrera de Big Data son:\n\t", suma/len(instituto["Notas"]))
"""

# print("El promedio de las notas de la carrera de Big Data son:\n\t", round(suma/len(instituto["Notas"]),2)) # Para redondear o poner cierto numeros de decimales

print(max(instituto["Notas"])) # para el numero mayor
print(min(instituto["Notas"])) # para el numero menor 

"""
print("La posicion de la nota minima\n\t",instituto["Notas"].index(min(instituto["Notas"])))
print("El profesor:\n\t",instituto["profesores"][instituto["Notas"].index(min(instituto["Notas"]))])
print("La materia es:\n\t",instituto['materias'][instituto["Notas"].index(min(instituto["Notas"]))])
 """
 
print("La menor nota es:\n\t" , min(instituto["Notas"]) , 
      "\nLa posicion de la nota minima es: \n\t" , instituto["Notas"].index(min(instituto["Notas"])) , 
      "\nEl profesor de la materia es:\n\t",instituto["profesores"][instituto["Notas"].index(min(instituto["Notas"]))],
      "\nLa materia es:\n\t",instituto['materias'][instituto["Notas"].index(min(instituto["Notas"]))]
      )