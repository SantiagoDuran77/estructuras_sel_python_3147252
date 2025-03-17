'''
Estructura de control if:
Se utiliza para tomar desiciones
basadas en expresiones condicionales
'''
#Ejemplo 1: if Simple
edad= int(input("Ingresa tu edad:"))
documento= input ("Tienes documento?(si/no):")
#condicional: si la edad es mayor o igual a 18
if edad >= 18 and documento== 'si':
    #codigo para cuenado es mayor a 18
    print("Es mayor de edad, puedes votar")
else:
    #codigo para cuando es menor a 18
    print("Eres menor de edad, o no tienes documento, no puedes votar")
#codigo que se ejecuta siempre
print("Fin del programa")