import colorama as co
import os
import msvcrt as key

# Diccionario con los colores
color= {1:co.Fore.GREEN,2:co.Fore.YELLOW,3:co.Fore.RED}
co.init()
def mover(fila,columna,color):
  #Borro según SO
  if os.name == "nt":
    os.system("cls")
  else:
    os.system("clear")
  #Cambio el color
  print(color,end= "")
  #Desplazo el texto columna
  print(co.Cursor.FORWARD(columna),end= "")
  #Desplazo el texto fila
  print(co.Cursor.DOWN(fila),end= "")
  print("Me muevo mundo")

col= 1
fila= 5
columna= 5

movimiento= ""
while movimiento != b"0":
  mover(fila,columna,color[col])
  print(color[1],end= "")
  print(co.Cursor.FORWARD(0))
  print(co.Cursor.DOWN(10 - fila),end="")
  print("Pulsa c para cambiar de color")
  print("Pulsa s para subir")
  print("Pulsa b para bajar")
  print("Pulsa i para izquierda")
  print("Pulsa d para derecha")
  print("Pulsa 0 para salir")
  movimiento = key.getch().lower()
  if movimiento == b"c":
    col += 1
    if col > 3:
      col = 1
  elif movimiento == b"s":
    fila -= 1
    if fila < 0:
      fila = 0
  elif movimiento == b"b":
    fila += 1
    if fila > 10:
      fila = 10
  elif movimiento == b"i":
    columna -=1
    if columna <0 :
      columna = 0
  elif movimiento == b"d":
    columna += 1
