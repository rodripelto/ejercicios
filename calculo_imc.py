peso = float(input("Pon tu peso: ").replace(",","."))
altura = float(input("Pon tu altura: ").replace(",","."))
imc = peso / altura ** 2
if imc < 18.5:
  print("Tu IMC es bajo")
elif 18.5<= imc < 25:
  print("Tú IMC es normal")
elif 25 <= imc < 30:
  print("Tú IMC es sobre peso")
else:
  print("Tú IMC es obeso")
