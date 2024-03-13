print("Bienvenido a bienes raices. Ingrese estos datos para continuar:")
sueldo = int(input("\nSueldo: "))
valor = int(input("El precio de la casa es de: "))
if sueldo >= 80000:
    porcentaje = 0.15
    c_a = 120
else:
    porcentaje = 0.30
    c_a = 84
pie = round(valor * porcentaje, 2)
valor_cuota = round((valor - pie) / c_a, 2)

print(f"\nPara obtener la casa debe dar un pie de ${pie}, y la cuota mensual quedaria en ${valor_cuota} por {'10' if sueldo >= 80000 else '7'} años.\n")