animals = []
again = True

while again:
    print("")
    print("Menú del Zoológico")
    print("")
    print("1- Crear animal para la lista")
    print("2- Ver la lista de todos sus animales")
    print("3- Borrar animal por ID")
    print("4- Borrar animal por nombre")
    print("5- Borrar todos los animales")
    print("6- Listar animal por ID")
    print("")
    menu = int(input("Elija el número de la acción a ejecutar: "))

    if menu == 1:
        print("")
        new_animal = input("Escriba el nombre del animal: ").lower()
        animals.append(new_animal)
        print("")
        print("¡Animal creado!")
        continuar = int(input("¿Desea seguir en el menú? 1=Si o 2=No "))
        if continuar != 1:
            again = False

    elif menu == 2:
        print("")
        print(f"Tu lista de animales es: {animals}")
        print("")
        continuar = int(input("¿Desea seguir en el menú? 1= Si o 2= No "))
        if continuar != 1:
            again = False
    
    elif menu == 3:
        print("")
        delete_id = int(input("Escriba el ID del animal que quiere eliminar: "))
        killed1 = animals.pop(delete_id)
        print(f"Se eliminó [{killed1}] de la lista")
        continuar = int(input("¿Desea seguir en el menú? 1= Si o 2= No "))
        if continuar != 1:
            again = False
    
    elif menu == 4:
        print("")
        print(f"Tu lista de animales es: {animals}")
        delete_name = input("Escriba el nombre del animal a eliminar: ").lower()
        killed2 = animals.remove(delete_name)
        print(f"Animal eliminado: {delete_name}")
        continuar = int(input("¿Desea seguir en el menú? 1= Si o 2= No "))
        if continuar != 1:
            again = False

    elif menu == 5:
        animals.clear()
        print("")
        print("La lista ha sido borrada")
        continuar = int(input("¿Desea seguir en el menú? 1= Si o 2= No "))
        if continuar != 1:
            again = False
    
    elif menu == 6:
        print("")
        position = int(input("Escriba el ID del animal a mostrar: "))
        print(animals[position])
        continuar = int(input("¿Desea seguir en el menú? 1= Si o 2= No "))
        if continuar != 1:
            again = False
    
    else:
        print("Opción inválida, elija nuevamente")