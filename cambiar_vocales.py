# Pido que se escriba una frase
cadena = input("Escriba una frase: ")
# Monto una lista con las vocales, lo podría hacer con un for y los caracteres ascci
vocales = ["a","e","i","o","u"]
# Pido el carácter para sustituir
caracter = input("¿Por que carácter quieres sustituir las vocales: ")
# recorro la lista de vocales para ir sustituyendo
for vocal in vocales:
    # Uso replace para sustituir, en primer lugar carácter a sustituir y en segundo lugar carácter por el que
    # sustituyo
    cadena = cadena.replace(vocal,caracter)
# Muestro la cadena final
print(cadena)
