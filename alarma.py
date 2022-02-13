import time

def alarma(repeticion):
  color = {"Verde":"\033[0;32m","Rojo":"\033[0;31m","Blanco":"\033[0;37m"}
  for i in range(repeticion):
	  print(color["Rojo"], end="")
	  print("ALARMA", end="", flush=True)
	  time.sleep(1)
	  print("\r", end="")
	  print("      ", end="\r")
	  time.sleep(1)
	  print(color["Blanco"], end="")


for i in range(10):
	print("Hola Mundo")
	time.sleep(0.25)
	if i == 5:
		alarma(5)
