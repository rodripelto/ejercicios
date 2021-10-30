def input_int(mensaje):
    """
    Este método solo aceptara números enteros y devolverá un numero entero
    """
    for caracter in mensaje:
        key.putwch(caracter)
    entrada = ""
    tecla = 0
    while tecla != 13:
        tecla = ord(key.getch())
        # print(tecla) # Print para depuración
        if tecla >= 48 and tecla <= 57:  # Si es numero
            entrada += chr(tecla)
            key.putwch(chr(tecla))
        elif tecla == 45 or tecla == 43:  # Si es + o -
            if len(entrada) < 1:  # Solo si es el primer dígito
                key.putwch(chr(tecla))
                entrada += chr(tecla)
        elif tecla == 8:  # Para la tecla borrar
            key.putwch(chr(tecla))  # Me muevo atrás
            key.putwch(chr(32))  # Escribo espacio para borrar
            key.putwch(chr(tecla))  # Me muevo atrás para colocar el cursor
            entrada = entrada[:-1]  # Borro lo último

    key.putwch("\n")  # Para que ponga un salto de linea
    # Si lo han dejado vacío o solo + o - entonces 0
    if len(entrada) < 1 or entrada == "+" or entrada == "-":
        entrada = ""
    else:
        try:
            entrada = int(entrada)
        except ValueError:
            entrada = ""
    return entrada
