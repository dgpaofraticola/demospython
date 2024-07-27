print("*********************")
print("Tu tienda de Manzanas")
print("*********************")

print("Por favor ingrese su nombre:")
nombre = input()
print("Por favor ingrese su apellido:")
apellido = input()

ncompleto = nombre +" "+ apellido


manzanas = 20
precio = 5

print("Gracias",ncompleto,"por visitarnos, tenemos el agrado de contarle que tenemos en stock", manzanas,"manzanas a un valor de",precio,"pesos.")

print("¿Cuántas manzanas deseas", nombre,"?")
cantidadManzanas = input()
cantidadManzanas = int (cantidadManzanas)

print("Tu saldo a pagar es de", cantidadManzanas * precio,"pesos")
print("**********************")
print("Recuerde",ncompleto ,"que usted ha solicitado", cantidadManzanas,"manzanas a un valor de", precio,"pesos.")
print("**********************")
print("Ahora quedan en stock", manzanas-cantidadManzanas,"manzanas")
print("**********************")
print("Gracias por su pedido, esperamos que regrese muy pronto =)")