
# Colores para la salida en la consola
rosa = "\033[95m"
verde = "\033[92m"
azul = "\033[94m"
amarillo = "\033[93m"
reset = "\033[0m"

#Usamos While True para repetir el ciclo 
while True:
    
    #Usamos try para intentar ejecutar el código
    try:
        
        #Mensaje de bienvenida
        print(rosa + "🌸✨Bienvenido🌸✨" + reset)

         # Solicitamos al usuario que ingrese el nombre del producto 
        Nombre_Del_Producto = (input(verde + "Ingrese el nombre del producto \n" + reset))
        
        #Solicitamos al usuario el precio del producto
        Precio_Unitario = float(input(verde + "Ingrese el precio del producto \n" + reset))
        
        # Validamos el precio
        if Precio_Unitario <= 0:
            print("El valor que ingresaste es inválido, por favor ingresa un valor válido")
            #Hacemos uso del continue para volver a repetir el ciclo
            continue
            

        #Solicitamos al usuario que ingrese el número de productos que desea llevar 
        Cantidad = int(input(verde + "Ingrese la cantidad que desea llevar \n" + reset ))

        # Validamos la cantidad
        if Cantidad <= 0:
            print("El valor que ingresaste es inválido, por favor ingresa un valor válido")
            
            # Hacemos uso del continue para volver a repetir el ciclo
            continue
        
        # Definimos la variable Costo_Total para calcular el total de la compra
        Costo_Total_Calculado = Precio_Unitario * Cantidad
        
        #Usamos print para mostrarle al usuario el historial de su compra
        print(rosa + "Datos del producto" + reset)
        print(verde + "Nombre del producto" + reset,  Nombre_Del_Producto)
        print(verde + "Precio unitario" + reset , Precio_Unitario)
        print(verde + "Cantidad" + reset , Cantidad)
        print(verde + "Costo total calculado" + reset , Costo_Total_Calculado)
        
        #Hacemos uso del break para salir del ciclo en el que estamos
        break
    
    # Usamos except para capturar el error si ocurre
    # Usamos ValueError para indicarle al usuario que hay un error 
    except ValueError:
        
    #Usamos print para mostrarle al usuario un mensaje en caso de que cometa un error
        print("Has ingresado un dato incorrecto,intenta otra vez")
        continue
        
        
#  ¿Qué hace el programa?
#Este programa tiene como funciones principales registrar productos con un nombre, un valor unitario y una cantidad específica del mismo

# ¿Cómo funciona?
#El programa le pide al usuario que ingrese el nombre del producto, el precio y la cantidad del mismo.
# Luego, el programa calcula el costo total calculado, ya que, multiplica el precio por la cantidad
# Por último, el programa muestra el historial de la compra con datos específicos como:
# El nombre del producto, el precio unitario, la cantidad y el costo total calculado
        
        
