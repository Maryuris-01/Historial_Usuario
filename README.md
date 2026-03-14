# _**Historia de Usuario**_

## _**Descripción**_

Este programa permite registrar la compra de un producto teniendo en cuenta el nombre, el precio y la cantidad del mismo.

Cuando el programa recibe estos datos, calcula
automáticamente el costo total de la compra y muestra un resumen con la información registrada

## _**¿Cómo funciona?**_

_El programa funciona siguendo un algoritmo, el cual consiste en:_

1. Le da la bienvenida al usuario
2. Le pide al usuario que ingrese el nombre del producto que quiere comprar
3. Le pide al usuario que ingrese el precio unitario del producto
4. Si el usuario ingresa un valor inválido, el programa le muestra un mensaje
pidiéndole que ingrese un valor válido
5. El programa le pide al usuario que digite qué cantidad desea llevar
6. En caso de que el usuario digite un valor inválido, le muestra un mensaje pidiéndole que ingrese un valor válido
7. Teniendo estos tres datos en cuenta, el programa calcula el total que el usuario debe pagar
8. Cuando ya el usuario sabe el valor que debe pagar, el programa le muestra el historial de la compra


## _**Variables**_ 
El programa hace uso de las siguientes variables:

1. Nombre_Del_Producto: Guarda el nombre del producto ingresado por el usuario.

2. Precio_Unitario: Guarda el precio unitario del producto.

3. Cantidad: Guarda la cantidad de productos.

4. Costo_Total_Calculado: Guarda el resultado del cálculo del valor total.

## _**Uso de colores**_
Las variables utilizadas para definir los colores son:

![alt text](image.png)

## _**Estructura del programa**_
## _**Uso de ciclos**_

 1. Se hace uso del While True para ejecutar el programa hasta que los datos ingresados sean correctos. 

 2. Se hace uso de if para validar los datos que el usuario ingrese.

 3. Se hace uso de try y except para evitar que el programa se detenga en caso de que el usuario ingrese un valor incorrecto.


## _**¿Cómo se calcula el costo total?**_
El costo total se calcula multiplicando el precio unitario por la cantidad:

Costo_Total_Calculado = Precio_Unitario * Cantidad

## _**Vista en la consola**_

![alt text](image-2.png)

## _**Autor**_
_Maryuris Aragón M._













