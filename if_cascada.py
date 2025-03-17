'''
if en cascada:
Estructura de control que permite
evaluar varias condiciones en 
cascada, es decir, si la primera
condicion no se cumple, 
se evalua la siguiente
y asi sucesivamente
'''
#Ejemplo 1: 
#Modificar el programa de votacion
#para que considere las edad de 17
#años

edad = int(input("Ingresa tu edad:"))
if edad >= 18:
    print("Puedes votar")
elif edad < 10:
    print("Eres muy pequeño, tienes registro civil")
elif edad == 18:
    print("Bienvenido ciudadano, puedes votar con contraseña")
elif edad== 17:
    print("Puedes votar el proximo año")
elif edad < 17:
    print("No puedes votar aun")
print ("Fin del programa")