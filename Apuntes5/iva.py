#Nicolas Bahena Ostermaier
#Apuntes - 4

precio = float(input("Precio del producto: $"))
cantidad = float(input("Cantidad del producto: "))

subtotal = precio * cantidad
iva = subtotal * 0.16
total = subtotal + iva

print(f"Subtotal: ${subtotal:.2}")
print(f"IVA: ${iva:.2}")
print(f"Total: ${total:.2}")
