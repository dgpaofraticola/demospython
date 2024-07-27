import random

def tirar_dados():
    return random.randint(2,12)

def pedir_respuesta():
    print("Ingresa tu predicción")
    print("1. Par")
    print("2. Impar")
    print("3. Salir del juego")
    
    return int(input())

def imprimir_resultado(numero, prediccion):
    es_par = numero % 2 == 0 #el remanente si es 0 es par, si es 1 es impar
    if es_par and prediccion == 1:
        print("¡GANASTE! el número que salió es el ", numero)
        
    elif not es_par and prediccion == 2:
        print("¡GANASTE! el número que salió es el ", numero)
         
    else:
        print("PERDISTE =P el número que salió es el ", numero)

while True:
    numero = tirar_dados()
    prediccion = pedir_respuesta()
    
    if prediccion == 3:
        break
    imprimir_resultado(numero, prediccion)
    
print("Gracias por jugar")
    
    
#print("tiro de dados:", tirar_dados())