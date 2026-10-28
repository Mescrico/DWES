opcion = 0
while opcion != 3:
    
    print("1) Ver catálogo  2) Buscar  3) Salir")
    
    opcion = int(input("Opción: "))
   
    match opcion:
        case 1:
            print("Mostrando catálogo...")
        case 2:
            print("Buscando...")
        case 3:
            print("Hasta la proxima")


