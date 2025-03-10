'''
Operadores logicos 

Aquellos que operan unicamente
con valores booleanos(V F)
Acorde a las tablas de verdad
'''

#Ejemplo 1:Operador not
y = not True
print("El resultado de operar con not es", y );

#Ejemplo 2:Operador and
y = False and True
print("El resultado de operar con and es", y );

#Ejemplo 3:Operador or
y = False or True
print("El resultado de operar con not es", y );

'''
Jerarquia de precedencia de operadores 
(logicos inclusive)
1.  ()
2.  **
3.  *, /, %
4.  +,-
5.  >, <, >=, <=, !=, ==
6.  not
7.  and
8.  or
9.  =
'''

#ejemplo 4: Jerarquia de operadores
y = False and not True or False
print("El resultado de operar con jerarquia de operadores es" ,y);