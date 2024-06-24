import os
os.system("cls")
import pyfiglet
from datetime import datetime


archivo= "productos.txt"
archivo_2= "ventas_productos.txt"

folio=10000

productos=[
          ]

ventas=[
       ]


def get_folio():
   return ventas(ventas) +1

def buscar_id(id_producto):
       try:
        i = productos.index(id_producto)
        return i
       except:
            return -1

       
def leer_datos_archivo(archivo):
    lista_datos = []
    with open(archivo, 'r') as file:

        for linea in file:
            linea=linea.strip()
            datos=linea.split(',')
            
            lista_datos.append(datos[0])
            lista_datos.append(datos[1])
            lista_datos.append(datos[2])
            lista_datos.append(int(datos[3]))
            lista_datos.append(datos[4])
            lista_datos.append(int(datos[5]))



def leer_datos_archivo_2(archivo_2):
    lista_ventas = []
    with open(archivo_2,'r') as file:

        for linea in file:
            linea=linea.strip()
            linea=linea.strip(',')

            lista_ventas.append(ventas[0])
            lista_ventas.append(ventas[1])
            lista_ventas.append(ventas[2])
            lista_ventas.append(int(ventas[3]))
            lista_ventas.append(int(ventas[4]))

    return lista_datos        
            



def buscar(id):
    lista_productos = []







opcion=0

print(pyfiglet.figlet_format("  Pet shop misifu :3"))
print("""Autores: Amaro Ulloa (✿◦’ᴗ˘◦)♡ 
         Alejandra Toledo =^._.^= """)
os.system("pause")
while opcion<=4:
    os.system("cls")

    print("""
           ≽^-˕-^≼ SISTEMA DE VENTAS ACCESORIOS MASCOTAS ≽^-˕-^≼
                    -----------------------------------
                        1. Vender Productos
                           2. Reportes.
                          3. Mantenedores
                         4. Adminitraciòn
                            5. Salir    
          

         """)
    
    opcion=int(input("Ingrese una opcion entre 1-5: "))

    
    match opcion:
        case 1:
            while True:
                print("     Venta de productos   ")
                productos.txt=buscar_id(input("Ingrese ID: "))
                print(producto[0],"",producto[1],"",producto[2],"",producto[3],producto[4],"",producto[5])
                
                a=buscar_id(id)

                if a != -1:
                    print("Encontrado en el elemento ", 0)
                    producto=productos[1]
                    print(producto[0],"",producto[1],"",producto[2],"",producto[3],producto[4],"",producto[5])
                    cantidad=int(input("Ingrese cantidad a comprar: "))

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
                os.system("pause")         

                    
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
                        #mostrar_tablas_ventas()
                        a=0
                        for a in ventas:
                            print(venta[0],"",venta[1],"",venta[2],"",venta[3])
                            total = a + venta[4]
                        print("Total=",a)
                
                        os.system("pause")

                    case 2:
                        fecha=int(input("Ingrese la fecha de venta (dd-mm-aaaa): "))
                         
                        a=0
                        for venta in ventas:
                            if venta[1]== fecha:
                                a = a + venta[2]
                                print(venta[0],"",venta[1],"",venta[2],"",venta[3])
                                print("Fecha de venta entregada.")
                                os.system("Pause")

                    case 3: 
                        fechaI_str=input("Ingrese la fecha de inicio (dd-mm-aaaa): ")
                        fechaT_str=input("Ingrese la fecha de termino (dd-mm-aaaa): ")

                        fechaI=datetime.strptime(fechaI_str, "%d-%m-%Y")
                        fechaT=datetime.strptime(fechaT_str, "%d-%m-%Y")

                        total=0

                        for venta in ventas:
                            fecha_venta= venta[0]
                            fecha_venta = datetime.strptime(venta[0], "%Y-%m-%d")
                            
                            if fechaI <= fecha_venta <= fechaT:
                                print(venta[0],"",venta[1],"",venta[2],"",venta[3]) 
                                total = total + venta[4]

                                print("El Total es: ",total)

                                os.system("pause")

                    case 4:
                        break

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

                    case 5:
                        print("\n Listar Mascotas a Vender \n")
                        for i in range(0,len(productos),6):
                            print(productos[i],"",productos[i+1],"", productos[i+2], "",productos[i+3],"",productos[i+4],"",productos[i+5])

                    case 6:
                        break

        case 4:
            os.system("cls")
            op=0
            while op<=3:
                print("""     Administraciòn

                      1-Cargar Datos
                      2-Respaldar Datos
                      3-Salir  

                      """)
                op=int(input("Ingrese una opcion 1-3: "))
                match op:

                    case 1:
                        print(" Cargar Datos ")

                    case 2:
                        print("Respaldo de datos")
                        lista_datos_Actualizada=[]
                        with open(archivo, 'w') as file:
                            ultima_linea=len(lista_datos_Actualizada)

                            c=1
                            for linea in lista_datos_Actualizada:
                                if c != ultima_linea:
                                    file.write(linea + '\n')
                                else:
                                    file.write(linea)
                                c=c+1
                                
                    case 3:
                        break           





    if opcion==5:
        break
print("Fin del menù")    
            