import random # importamo la clase random
import os # importa la clase os
import time # Importamos la clase time

""" En primer lugar comentar que el código completo no es mio, 
es de un usuario del grupo Python en español (Principiantes) "Giane Sotto" de FaceBook
que pidio ayuda ya que tenia errores, Yo lo he modificado para que funcione como creo que es el Juego,
puede que no coincida con el juego real)"""

#------- Método o Función que devuelve un numero aleatorio------
""" Hay que acostumbrarse a usar funciones o metodos si el código se repite en el progara
En este caso creo que no seria necesario ya que se trabaja mas haciendolo que no"""

def lanzar_dado():
    return random.randint(1,6) # Aleatorio entre 1 y 6 puntuación de dados

#------- Fin del Método -----

#------- Metodo para el lamzamiento de los dados --------

#------- Metodo para borrar consola

def borrar():
  if os.name=="nt":
    os.system ("cls") # Se borra la consola Windows
  elif os.name=="posix":
    os.system ("clear") # Se borra la consola Linux

#------- Fin del metodo

def lanzar_los_dados(mensaje):
    borrar()
    print("Necesitas un",mensaje,"para ganar")
    print("\n*** Se tiran 2 dados***")
    time.sleep(2) # Espero 2 segundos para darle emoción, no me gusta usar sleep pero por no complicar la cosa
    borrar() 
    dado_uno=lanzar_dado()
    dado_dos=lanzar_dado()
    # Intento de efecto que se mueven los numeros
    for con in range(20):
        print("Necesitas un",mensaje,"para ganar")
        print("Los dados estan girando", lanzar_dado(), lanzar_dado())
        time.sleep(0.50)
        borrar()

    print("El primer dado ha caido en",dado_uno) # Voy a usar este formato en print me gusta mas
    print("El el segundo dado ha caido en",dado_dos)
    total_tirada = dado_uno + dado_dos
    time.sleep(5)
    print("\nEl total de la tirada a sido:",total_tirada)
    time.sleep(5)
    borrar()
    return dado_dos, dado_uno, total_tirada

#------- Fin del Método -----

#------- Lo primero sera declarar todas la variables que vamos a usar en el ambito

punto = 0 # Determina el valor de lo conocido como puto, tambien determinara si es una segunda tirada cuando no valga cero 
presupuesto = 1000 # Determina la cantidad de dinero al entra a la partida, podriamos pedirlo por teclado
apuesta = 0 # Determina la cantidad que apostaremos
dado_uno = 0 # Variable que contendra el valor de la tirada del dado uno
dado_dos = 0 # Variable que contendra el valor de la tirada del dado dos
total_tirada = 0 # Variable con la suma de los 2 dados
salir= False # Control del juego

#------- Fin de declaración de variables

# Damos la bien venida al jugador
borrar() # Borramos la pantalla.
print("BIEN VENIDO A LA MESA DE CRAPS.")
print("Juega contra la casa de apuestas")
print("Tienes incialmente ",presupuesto," € para poder jugar.")
time.sleep(3) # Espero tres segundo ya que voy a borrar la pantalla mas adelante

# Comienza la logica del juego

while presupuesto > 0 and salir  == False: # Se mantendra la ejecución hasta que nos arruinemos.
    while apuesta < 10 or apuesta > presupuesto: # No saldra hasque que la apuesta sea mayor de 100 y menor que el presupuesto
        borrar() 
        apuesta = int(input(f"Inserte la cantidad que desea apostar mayor a 10€ y menor a {presupuesto}€: "))
    # No sabia que se podia hacer de esta manera    
    dado_dos, dado_uno, total_tirada = lanzar_los_dados("7 ó 11")

    if total_tirada == 7 or total_tirada == 11: # Comprobamos si el valor es ganador
        print("¡FELICIDADES! Usted ha ganado la cantidad de:",apuesta)
        presupuesto += apuesta # Sumamos las ganancias al presupuesto
        print("Ahora dispone de:",presupuesto,"€ para apostar")
        apuesta=0 # Ponemos apuest a cero
    elif total_tirada == 2 or total_tirada == 3 or total_tirada == 12: # Si no hemos canado comprobamos si hemos perdido
        print("TIRADA PERDIDA \n Gana la casa de apuestas y se queda con lo apostado:",apuesta,"€")
        presupuesto -= apuesta # Restamos lo apostado al presupuesto 
        print("Ahora dispone de:",presupuesto,"€ para apostar")
        apuesta=0 # Ponemos apuest a cero
    else: # Si no hemos ganado ni perdido tenemos lo que denominan punto
        print("\nPUNTO")
        punto = total_tirada
        print("Su punto o tirada a alcanzado: ",punto)
        """ respuesta es una variable local que solo permanecera 
        en el ambito del else por eso no la declaramos con las otras """
        respuesta = input("¿Desea redoblar la apuesta? ") # Preguntamos si quiere doblar la apuesta
        """ Como python diferencia mayusculas y minusculas si en la siguiente comprobación nos escriben Si, sI, SI
        no nos dectectaria si es igual, podriamos hacer un if con tantos or como necesitaramos, en este caso 3 pero
        podria darse la circustancia que fueran 100 variaciones posibles y seria todo un reto, por eso vamos a usar
        un pequeño truco y es para en este caso a minuscula la variable respuesta y de esta manera compararlo solo con
        un si en minuscula, lo podriamos hacer pasandolo a mayuscula"""
        if respuesta.lower() == "si": # Si la respuesta es sí, comprobaremos si tiene presupuesto suficiente 
                            # y doblamos la apuesta
            # Comprobamos que el presupuesto - la apueta que no hemos descontado todabía es mayor que la apuesta
            if (presupuesto-apuesta) > apuesta: # Esto realmente no se si pertenece al juego
                apuesta = apuesta * 2 # Doblamos la apuesta
            else:
                print("Lo sentimos mucho pero no tiene presupuesto para doblar la apuesta")

        print("En esta tidada apusta ", apuesta,"€")
        time.sleep(2)
        total_tirada=0
        while total_tirada != 7 and total_tirada != punto:
            dado_dos, dado_uno, total_tirada = lanzar_los_dados(str(punto))
        
        if total_tirada ==7: # Si es igual a site a perdido
            # Podemos tenerlo en un metodo ya que lo repetimos
            print("TIRADA PERDIDA \n Gana la casa de apuestas y se queda con lo apostado:",apuesta,"€")
            presupuesto -= apuesta # Restamos lo apostado al presupuesto 
            print("Ahora dispone de:",presupuesto,"para apostar")

        else: # Si no es un 7 entonces es la tirada ganadora ya que en otro caso seguiria en el while
            # Podemos tenerlo en un metodo ya que lo repetimos
            print("¡FELICIDADES! Usted ha ganado la cantidad de:",apuesta,"€")
            presupuesto += apuesta # Sumamos las ganancias al presupuesto
            print("Ahora dispone de:",presupuesto,"€ para apostar")
    apuesta=0 # Ponemos apuesta a cero
    respuesta = input("¿Quieres segir jugando? ")
    borrar() 
    if respuesta.lower() == "no":
        salir = True # Cambiamos flag para salir

if presupuesto > 0 :
    print("Buena decisión, el juego es muy malo, te llevas a casa", presupuesto,"€")
else: 
    print("Lo sentimos mucho te has arruinado, no puedes seguir jugando") 
