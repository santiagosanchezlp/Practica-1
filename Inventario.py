inventario = {}
opcion = ''

print ('¿Que acción desea realizar?')

# Procedimiento que valida que la opcion ingresada sea correcta
def elegir_opcion(opc):
    print()
    opc = input('Agregar un nuevo producto al inventario (A), Eliminar un producto existente (E), Mostrar el inventario actual (M) o salir (S): ').lower()
    while opc != 'a' and opc != 'e' and opc != 'm' and opc != 's':
        print('Ingrese una opcion valida')
        opc = input('Agregar un nuevo producto al inventario (A), Eliminar un producto existente (E), Mostrar el inventario actual (M) o salir (S): ').lower()
    global opcion
    opcion = opc

elegir_opcion(opcion)
# El programa inicia en caso que no elijamos salir
while opcion != 's':
# Solicita nombre y cantidad de producto que deseamos agregar al inventario
    if opcion == 'a':
        nombre = input('Indique el nombre del producto: ')
        cantidad = input('Cantidad inicial del producto: ')
        while True:
            if cantidad.isdigit():
                cantidad = int(cantidad)
                break
            print('Ingrese una cantidad valida')
            cantidad = input('Cantidad inicial del producto: ')
        # Verificar si el producto se encuentra en el inventario. Si no está, lo agrega.
        if nombre in inventario:
            print('Producto duplicado. Por favor eliminelo y vuelva a ingresar el stock')
        else:
            inventario[nombre] = cantidad
    #Solicita nombre del producto a eliminar
    if opcion == 'e':
        buscado = input('Indique el producto que desea eliminar: ')
        # Verifica que el producto se encuentra en el inventario y si está, lo elimina
        if buscado in inventario:
            del inventario[buscado] 
        else:
            print ('El producto no se encuentra en el inventario.')                   
    # Muestra el inventario
    if opcion == 'm':
        print(f'Producto',' '*12,'Stock')
        for producto in inventario:
            print(producto, ' '*(20-len(producto)), inventario[producto], 'unidades.')
    elegir_opcion(opcion)