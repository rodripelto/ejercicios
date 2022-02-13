import random
clave = str(random.randrange(1000,10000))
intentos = 0
while intentos<10:
  intentos += 1
  usuario= input("Introduzca la clave: ")
  if len(usuario)==  4:
    if clave != usuario:
      acierto = 0
      for dig in usuario:
        if dig in clave:
          acierto+= 1
      print("Clave incorrecta, has acertado",acierto,"números")
    else:
      print("Clave correcta")
      break
  else:
    print("La clave tiene que tener 4 digitos")
else:
  print("Demasiados intentos")
print("Has usado",intentos,"intentos")
print(clave)
