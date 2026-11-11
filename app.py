print("SISTEMA DE GESTION ACADEMICA")
print("***********")

estudiante = input("Ingrese el nombre del estudiante: ")

nota1 = float(input("Ingrese la Primera nota: "))
nota2 = float(input("Ingrese la Segunda nota: "))
nota3 = float(input("Ingrese la Tercera nota: "))

promedio = (nota1 + nota2 + nota3) / 3
print("----------------------------")
print("Estudiante:", estudiante)
print("Promedio:", promedio)

if promedio >= 11:
    print("Estado: APROBADO")
else:
    print("Estado: DESAPROBADO")

print("***********")
print("Proceso finalizado")
