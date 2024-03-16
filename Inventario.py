import random

inventario = []
opcion = ''

print ('¿Que acción desea realizar?')

# Procedimiento que valida que la opcion ingresada sea correcta
def elegir_opcion(opc):
    opc = input ('Agregar un nuevo producto al inventario (A), Eliminar un producto existente (E), Mostrar el inventario actual (M) o salir (S): ').lower()
    while opc != 'a' and opc != 'e' and opc != 'm' and opc != 's':
        print ('Ingrese una opcion valida')
        opc = input ('Agregar un nuevo producto al inventario (A), Eliminar un producto existente (E), Mostrar el inventario actual (M) o salir (S): ').lower()
    global opcion
    opcion = opc

elegir_opcion(opcion)
# El programa inicia en caso que no elijamos salir
while opcion != 's':
# Solicita nombre y cantidad de producto que deseamos agregar al inventario
    if opcion == 'a':
        Nombre = input ('Indique el nombre del producto: ')
        Cantidad = input ('Cantidad inicial del producto: ')
        # Lo agrego al inventario
        inventario.append({Nombre: Cantidad})
    if opcion == 'e':
        buscado = input ('Indique el producto que desea eliminar: ')
        for i in range(len(inventario)):
            if inventario[i] == buscado:
                del inventario[i]
                break
    if opcion =='m':
        for i in range(len(inventario)):
            print (f'Nombre:', inventario[i], 'unidades')
    elegir_opcion(opcion)
print ('Cerrando programa')