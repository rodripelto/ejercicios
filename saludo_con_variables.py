# Escrito por Rodrigo Cabrera
# Solicito el nombre
nombre = input("Escribe tú nombre: ")
#Solicito el apellido
apellido = input("Escribe tú apellido: ")
#Solicito la edad y la dejo como string
edad = input("Escribe tú edad: ")
# Distintas formas de presentar los mensages por pantalla
print("Hola",nombre,apellido,"tienes",edad,"años")
print(f"Hola {nombre} {apellido} tienes {edad} años")
print("Hola {} {} tienes {} años".format(nombre,apellido,edad))
print("Hola " +nombre + " " + apellido + " tienes " + edad +" años")
