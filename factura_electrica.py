#servicio de electricidad
def menu():
  print("Menú")
  print("Opción 1: Tarifa residencial")
  print("Opción 2: Tarifa comercial")
  print("Opción 3: Salir del programa")
  return input("Ingrese una opción del menú (en número): ")
def cal_consumo():
  lectura_anterior = int(input("Ingrese lectura anterior: "))
  lectura_actual = int(input("Ingrese lectura actual: "))
  return lectura_actual - lectura_anterior
def factura(cargo_fijo,precio_kw,consumo,descuento,iva,ing_bruto,t_tarifa):
  subtotal = precio_kw * consumo + cargo_fijo
  total = subtotal * (iva + ing_bruto ) - descuento
  print(f"Su tarifa es {t_tarifa}")
  print(f"Su consumo ha dido de {consumo}kw")
  if descuento > 0:
    print(f"Ha obtenido un descuento de {descuento}")
  else:
    print("Su consumo ha sido elevado, no obtine ningun descuento")
  print(f"Subtotal: {subtotal}") 
  print(f"IVA {(iva - 1) * 100}%")
  if ing_bruto > 0:
    print(f"Ing. Brutos {(ing_bruto -1) * 100}%")
  print(f"El total de la factura es {total}") 
while (opcion:=menu()) != "3":
  descuento = 0
  if opcion == "1":
    t_tarifa = "Tarifa residencial"
    cargo_fijo = 299.37
    precio_kw = 3.37
    iva = 1.21
    ing_bruto = 0
    consumo = cal_consumo()
    if consumo < 250:
        descuento = 150
    factura(cargo_fijo,precio_kw,consumo,descuento,iva,ing_bruto,t_tarifa)    
  elif opcion == "2":
    t_tarifa = "Tarifa comercial"
    cargo_fijo = 315.25
    precio_kw = 4.55
    iva = 1.21
    ing_bruto = 1.05
    consumo = cal_consumo()
    if consumo < 150:
      descuento = 20
    factura(cargo_fijo,precio_kw,consumo,descuento,iva,ing_bruto,t_tarifa)
  else:
    print("Error. Intentelo de nuevo ingresando una opción valida del menú")
else:
  print("Ha decidido salir. gracias por utilizar el programa")
