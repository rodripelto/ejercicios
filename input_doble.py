def input_doble(mensaje_in, mensaje_fin):
    """
    Método que acepta una frase al inicio y una frase al final, lo introducido por el usuario se encuentrá
    entre las dos frases
    """
    entrada = ""
    tecla = 0

    def mensaje(borrar=0):
        # Limpio la linea
        print("\r", " "*borrar, end="\r", flush=True)
        # Escribo la frase
        print("\r", mensaje_in, " ", entrada, " ",
              mensaje_fin, sep="", end="\r", flush=True)
        # Escribo la frase hasta la entrada para posicionar el cursor
        print("\r", mensaje_in, " ", entrada, sep="", end="", flush=True)
    mensaje()
    while tecla != 13:
        tecla = ord(key.getch())
        if tecla != 8:
            entrada += chr(tecla)
        else:  # Para la tecla borrar
            entrada = entrada[:-1]  # Borro lo último
        entrada = entrada.rstrip()  # Elimino espacios y retornos de carro
        # Le sumo 2 ya que tenemos un espacio y longitud de entrada vale uno menos que cuando se escribió
        mensaje(len(mensaje_in)+len(entrada)+len(mensaje_fin)+2)
    print("\n")  # Para que ponga un salto de linea
    return entrada  # Elimino espacios y retornos de carro
