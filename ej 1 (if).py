precio = 10000
print(f"Bienvenido al teatro!\nHay descuentos en el precio de los asientos dependediendo de la edad del usuario\nEl precio general de los asientos es ${precio}")
edad = int(input("\nPor favor ingrese su edad: "))

if edad < 5:
    print("Al ser menor de 5 años no puede ingresar al teatro")
    exit()
if 5 <= edad <= 14:
    des = 0.35
if 15 <= edad <= 19:
    des = 0.25
if 20 <= edad <= 45:
    des = 0.10
if 46 <= edad <= 65:
    des = 0.25
if edad >= 66:
    des = 0.35

descuento_total = precio * des
precio_final = precio - descuento_total

print(f"Debido a su edad ha obtenido un descuento {des * 100}%, en este caso el precio de su asiento quedo ${precio_final}.")