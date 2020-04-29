# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 12:48:46 2020

@author: cristian
"""
#practica 1
print ("Bienvenido a emparejando.com")
print("=======================================")
print("Necesitamos conocer algunos datos sobre ti para encontrar tu pareja ideal")

nombre = input("Tu nombre: ")
fecha = int(input("¿Año de nacimiento? "))
taburete = input("¿Te gusta Taburete? [Si/No] ")

edad = 2020-fecha

print("Hola "+nombre+". Si no me equivoco tienes", edad,"años.")

if taburete in ('Si','si'):
    print("OK boomer. Lo tuyo va a ser un caso difícil")
else:
    print("Bueno, al menos es un comienzo. Veremos qué se puede hacer contigo.")

#practica 2
num=1

while (num<edad):
    print("Que no cumple",num)
    num+=1

print("¡ Que sí cumple",num,"!") 

#practica 3
num=1
for num in range(17):
    print("Que no cumpla",num)
    print("¡Que si cumpla",num,"!") 
    

#practica 4
datos=[nombre,edad,taburete]

for lista in datos:
    print(lista)
    
#practica 5   
datos={
      "nombre":nombre,
      "edad":edad,
      "taburete":taburete
      }

#practica 6
for tabla in datos.values():
    print(tabla)
abecedario= ' abcdefghijklmnñopqrstuvwxyz '

print("Bienvenidos a mi cifrador César")
print("=====================================================")

texto_claro=input("Introduce una frase para cifrarla: ")
clave=int(input("Introduce un numero para cifrar(Un número del 1 al 27):"))

texto_cifrado=""


for letra in texto_claro:
    nueva_posicion=abecedario.find(letra)+ clave
    letra_cifrada=int(nueva_posicion)%len(abecedario)
    texto_cifrado= texto_cifrado+str(abecedario[letra_cifrada])
print ("El mensaje cifrado es:" ,texto_cifrado)
print ("=====================================================")


#practica7
texto_descifrado=""
for letra in texto_cifrado:
    nueva_posicion= abecedario.find(letra)-clave
    letra_cifrada= int(nueva_posicion)%len(abecedario)
    texto_descifrado= texto_descifrado+str(abecedario[letra_cifrada])
print ("El mensaje descifrado es: " ,texto_descifrado)