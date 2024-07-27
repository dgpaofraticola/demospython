from datetime import datetime

print("**************************************")
print("******** BIENVENIDOS A LA ************")
print("******* TIENDA DE MASCOTAS ***********")
print("**************************************")

inventario = {
    "perro": 10,
    "gato": 8,
    "pajaro": 25,
    "iguana": 2
}

def calcular_suma_animales():
    return sum(inventario.values())

print("Por favor ingrese su nombre:")
nombre = input()

print("Ahora su apellido:")
apellido = input()
nombre_completo = nombre + " " + apellido

print("Agradecemos", nombre_completo, "que nos visite.")

compras = []

def mostrar_menu():
    print("")
    print("********************************")
    print("Selecciona la opción que deseas:")
    print("1: Conocer cuántos animales tiene la tienda")
    print("2: Comprar un animal")
    print("3: Mostrar compras")
    print("4: Cerrar programa")

def mostrar_inventario():
    print("***** INVENTARIO *****")
    for llave, valor in inventario.items():
        print(f"    {llave}: {valor}")
        
    print("En total tenemos:", calcular_suma_animales(), "animales")

def comprar_animal():
    carrito = []
    
    while True:
        print("¿Qué animal quieres comprar?")
        print("Escribe F para terminar la compra o V para ver el carrito")
        animal = input().strip().lower()
        
        if animal == "F":
            break
        
        if animal == "V":
            print(f"Tu carrito contiene: {', '.join([a.capitalize() for a in carrito])}")
            continue
        
        if animal not in inventario:
            print(f"Lo sentimos, no contamos con {animal}.")
        elif inventario[animal] == 0:
            print(f"No tenemos en stock {animal}.")
        elif animal in carrito:
            print(f"{animal.capitalize()} ya se encuentra en el carrito.")
        else:
            carrito.append(animal)
            inventario[animal] -= 1
            print(f"{animal.capitalize()} agregado al carrito.")
        
    if carrito:
        print("El contenido de tu carrito es:")
        for animal in carrito:
            print(f"      {animal.capitalize()}")
        
        fecha = datetime.now()
        compras.append((nombre_completo, carrito, fecha)) 

def mostrar_compras():
    print("    ")
    print("***** COMPRAS REALIZADAS *****")
    for compra in compras:
        nombre_cliente, carrito, fecha = compra
        print(f"    {nombre_cliente} compró {', '.join([a.capitalize() for a in carrito])} en {fecha}")

while True:
    mostrar_menu()
    try:
        respuesta = int(input())
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue

    if respuesta == 1:
        mostrar_inventario()
    elif respuesta == 2:
        comprar_animal()
    elif respuesta == 3:
        mostrar_compras()
    elif respuesta == 4:
        print("Saliendo del programa")
        break
    else:
        print("Opción no válida, por favor seleccione una opción del 1 al 4.")
