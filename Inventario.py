import time

rosa = "\033[95m"
verde = "\033[92m"
azul = "\033[94m"
amarillo = "\033[93m"
reset = "\033[0m"

#Hacemos uso de While True para repetir el código siempre y cuando las condiciones que hay en el mismo se cumplan 
while True:
    #Hacemos uso del try para 
    try:
        
        print(rosa + "🌸✨Bienvenido🌸✨" + reset)

        Nombre_Del_Producto = str(input(verde + "Ingrese el nombre del producto \n" + reset))
        Precio_Unitario = float(input(verde + "Ingrese el precio del producto \n" + reset))
        Cantidad = int(input(verde + "Ingrese la cantidad que desea llevar \n" + reset ))
        print(rosa + "La cantidad de productos que ha llevado es de"+ reset, Cantidad )
          
        Costo_Total_Calculado = Precio_Unitario * Cantidad
        print(azul + "El costo total es de :" + reset,Costo_Total_Calculado)
        
        break
    
    except ValueError:
        print("Haz ingresado un dato incorrecto,intenta otra vez")
        
    


    