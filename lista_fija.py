# Creo una lista vacia para guardar las palabras
palabras = []
# Creo un bucle for que dara 10 vueltas
for i in range(10):
    # Pido que escriban la palabra
    palabra = input("Escriba una palabra: ")
    #La añado a la lista
    palabras.append(palabra)
# Diversas formas de imprimir la lista
# Forma facil y rapida que proporciona python
# Bajo mi punto de vista no se debe de usar si quieres hacer una buena presentación de datos
print(palabras)
# Forma rapida que nos da python, algo mejor que la anterior pero tampoco se deberia usar
print(*palabras)
# Creamos un bucle y vamos presentando los datos, de esta manera podemos tener acceso a cada dato
# y podemos tratarlos.
for elemento in palabras:
    print(elemento)
