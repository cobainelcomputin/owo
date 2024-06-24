import os
os.system("cls")

#10 productos
#id= p001,producto, stock, precio, tipo animal, minimo 5

folio=10000

productos=[ #id #producto #stock #precio #tipo animal #precio
            "P001", "Collar gato",100,"Gato", "Fat Cat", 2000,
            "P002", "Collar Perro",100, "Perro", "Fat Dog", 2500,
            "P003", "Juguete raton",100,"Gato", "Milu", 1500,
            "P004","Juguete hueso chillòn",100, "Perro", "Milu", 200,
            "P005", "Alimento Premiun Gato", 50, "Gato", "Pro Plan", 25000,
            "P006", "Alimento Premiun Perro", 50, "Perro","Bravery", 50000,
            "P007", "Rascador pequeño", 70, "Gato", "Mochi", 8000,
            "P008", "Freebe", 50, "Perro", "Dog It", 3000,
            "P009", "Antipulga Gato", 70, "Gato", "Gato Limpio",  3500,
            "P010", "Antipulga Perro", 70, "Perro","Perro Limpio", 5000]


#Folio, fecha, id, cantidad, total
#Ventas 20

ventas=[
    [10001,"10-06-2024","p001",2,4000], # 0
    [10002,"10-06-2024","p002",1,2500]  # 1
        ]

def get_folio():
   elemento= len(ventas)-1
   return ventas[elemento]
print ("ultimo folio: ", get_folio())


def buscar_id(id_producto):
       try:
        i = productos.index(id_producto)
        return i
       except:
            return -1


opcion=0

while opcion<=4:
    os.system("cls")

    print("""
           ≽^-˕-^≼ SISTEMA DE VENTAS ACCESORIOS MASCOTAS ≽^-˕-^≼
                    -----------------------------------
                        1. Vender Productos
                           2. Reportes.
                          3. Mantenedores
                            4. Salir

         """)
    
    opcion=int(input("Ingrese una opcion entre 1-4: "))

    
    match opcion:
        case 1:
            while True:
                print("     Venta de productos   ")
                id=input("Ingrese ID ")
                a=buscar_id(id)

                if a != -1:
                    print("Encontrado en el elemento ", a)
                    producto=productos[a]
                    print(producto[0],"",producto[1],"",producto[2],"",producto[3],producto[4],"",producto[5])
                    cantidad=int(input("Ingree cantidad a comprar: "))

                    if cantidad <=producto[6]:
                        print(" Stock disponible ")
                        total=cantidad*producto[6]
                        print(f"El total a pagar por {cantidad} productos es {total}")
                        respuesta=input("¿Desea realizar la compra? s/n: ")
                        if respuesta.lower() == "s":
                            producto[6]=producto[6]-cantidad #Stock Actualizado
                            #Grabar Venta
                            ventas.append([get_folio(),+1,fecha,id,cantidad,total ])
                    else:
                        print("Error, la cantidad ingresada supera el limite de Stock")
                respuesta=input("¿Desea comprar otro producto?")
                if respuesta.lower() == "n":
                    break         



                    
        case 2:
            os.system("cls")
            op=0
            while op<=4:
                print("""
                            REPORTES
                      
                      1. Gererar de ventas (con total)
                      2. Ventas por fecha especifica 
                      3. Ventas por rango de fecha
                      4. Salir al menu principal

                      """)
                op=int(input("Ingrese una opcion 1-4: "))

                match op:
                    case 1:
                        print("Ventas")
                        fecha=input("Ingrese la fecha de venta: ")

                        
                        for venta in ventas:
                            print(venta[0],"",venta[1],"",venta[2],"",venta[3])
                            a = a + venta[4]
                        print("Total=",a)



                    case 2:
                        fecha=int(input("Ingrese la fecha de venta: "))
                         
                        a=0
                        for venta in ventas:
                            if venta[1]== fecha:
                                a = a + venta[2]
                                print(venta[0],"",venta[1],"",venta[2],"",venta[3])
                                print("Fecha de venta entregada.")
                                os.system("Pause")

                    case 3: 
                        fechaI=input("Ingrese la fecha de inicio: ")
                        fechaT=input("Ingrese la fecha de termino: ")





        case 3:
            os.system("cls")
            op=0
            while op<=6:
                print("""
                        MANTENEDOR DE PRODUCTOS
                      .........................
                      1. Agregar
                      2. Buscar
                      3. Eliminar
                      4. Modificar
                      5. Listar
                      6. Salir al menù principal             
                    
                      """)
                op=int(input("Ingrese una opcion 1-6: "))

                os.system("cls")

                match op:
                    case 1: 
                        print("\nAgregar Accesorios\n")
                        print("Ingrese accesorio a agregar: ")
                        id_producto=input("Agregue la id del producto: ")
                        producto=input("Ingrese el producto: ")
                        stock_producto=int(input("Ingrese el Stock del producto: "))
                        tipo_animal=input("Ingrese para que animal es el producto: ")
                        marca=input("Ingrese marca del producto: ")
                        precio_producto=int(input("Ingrese el precio del producto: "))

                        productos.append([id_producto,producto,stock_producto,tipo_animal,marca,precio_producto])
                        print("Listo, accesorio agregado!")

                        os.system("Pause")

                    case 2:
                        id=input("\n Ingrese ID para buscar producto: \n")
                        i=buscar_id(id)

                        if i != -1:
                            print("ID producto encontrado en el indice ",i)
                            print(productos[i],"",productos[i+1],"", productos[i+2], "",productos[i+3],"",productos[i+4],"",productos[i+5])
                        else:
                         print("Error, Chip id no existe")
                         break

                        os.system("Pause")

                    case 3:
                        id_producto=input("Ingrese un Chip Id a eliminar: ")
                        i = buscar_id(id_producto)

                        if i != -1:
                            sw=1
                            print(productos[i],"",productos[i+1],"", productos[i+2], "",productos[i+3],"",productos[i+4],"",productos[i+5])
                            productos.pop(i)
                            productos.pop(i)
                            productos.pop(i)
                            productos.pop(i)
                            productos.pop(i)
                            productos.pop(i)

                            print("Producto exitosamente eliminado. ")
                        else:
                            print("Error, id de producto no identificado.")    

                    case 4: 
                        id_producto=input("Ingrese el codigo a eliminar: ")
                        i= buscar_id (id_producto)
                        if i != -1:
                            print("ID encontrado en el indice ",i)
                            print(productos[i],"",productos[i+1],"", productos[i+2], "",productos[i+3],"",productos[i+4],"",productos[i+5])
                            print("\n")
                            nuevo_producto=input("Ingrese el nuevo producto: ")
                            nuevo_stock_producto=int(input("Ingrese el nuevo stock del producto: "))
                            nuevo_tipo_animal=input("Ingrese el nuevo tipo de animal: ")
                            nueva_marca=input("Ingrese la nueva marca: ")
                            nuevo_precio_producto=int(input("Ingrese el nuevo precio: "))

                            productos[i+1]=nuevo_producto
                            productos[i+2]=nuevo_stock_producto
                            productos[i+3]=nuevo_tipo_animal
                            productos[i+4]=nueva_marca
                            productos[i+5]=nuevo_precio_producto

                            print("Listo, datos modificados.")
                        else:
                            print("Error, ID no encontrada.")

#cambiar range
                    case 5:
                        print("\n Listar Mascotas a Vender \n")
                        for i in range(0,len(productos),6):
                            print(productos[i],"",productos[i+1],"", productos[i+2], "",productos[i+3],"",productos[i+4],"",productos[i+5])

                    case 6:
                        break

                if op==6:
                    break #Sale del while y vuelve al While Principal

    if opcion==5:
        break
print("Fin del menù")    
            