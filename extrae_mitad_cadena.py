# """
# Escribe un programa que dada una cadena  de caracteres devuelva la mitad inicial de la cadena
# """
# Método clásico usaremos for para recorrer la cadena y extraer la mitad
# Pido que se escriba una frase
cadena = input("Escriba una frase: ")
# preparo la nueva cadena ya que ire concatenando los caracteres de la original
nuevacadena=""
# Usamos el método len para contar la longitud de la cadena y como queremos la mitad lo dividimos entre 2
# OJO range
# no admite flotantes como argumento así que lo pasamos a int
for i in range(int(len(cadena)/2)):
    # Accedo por indice a cada posición de la cadena y la voy concatenando
    nuevacadena += cadena[i]
# Imprimo la nueva cadena
print(nuevacadena)
# Método Python, otros lenguajes también tienen métodos propios para extraer sub cadenas.
# Empiezo en el primer carácter indice cero: termino en la mitad: voy de uno en uno
nuevacadena1 = cadena[0:int(len(cadena)/2):1]
# Imprimo la nueva cadena
print(nuevacadena1)
