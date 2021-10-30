def lista_string():
    """
    Método para pedir al usuario una lista de string
    Devuelve una lista de string
    """
    seguir=True # Bandera para controlar bloque
    palabras=[] # Lista que contendra los números a analizar

    # Bloque para obtener la lista de números
    while seguir:
        palabra = input("Introduzca una palabra: ")
        if palabra!="":
            palabras.append(palabra)
        else:
            seguir=False # Cambio la bandera para que salga del bucle, también podría haber usado break
    return palabras
