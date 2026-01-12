nombre=input("Ingrese su nombre de usuario: ")
contraseña =input("Digite su contraseña: ")

if contraseña == "pepito1234" and nombre=="pepito":
    print("Bienvenido \n")
    saldo=1000

    print("Desea comprar algun producto?")
    print("1. Si")
    respuesta=input("2. No \n")

    if respuesta=="1":
        print("--------------------\nLISTADO DE PRODUCTOS\n 1) Camisa - $500\n 2) Pantalon - $700\n 3) Zapatos - $1200\n")
        print("Saldo: $", saldo)
        producto=input("Seleccione el producto a comprar (1-3): ")

        if producto=="1":
            if saldo >=500:
                saldo -=500
                print("Compra exitosa! Su saldo restante es: $", saldo)   

            else:
                print("Saldo insuficiente para comprar la camisa (",saldo,").")

        elif producto =="2":
            if saldo>=700:
                saldo -=700
                print("Compra exitosa! Su saldo restante es: $", saldo)

            else:
                print("Saldo insuficiente para comprar el pantalon (",saldo,").")

        elif producto =="3":
            if saldo>=1200:
                saldo -=1200
                print("Compra exitosa! Su saldo restante es: $", saldo)
            else:
                print("Saldo insuficiente para comprar los zapatos (",saldo,").")
        else:
            print("Producto no válido.")

    elif respuesta=="2":
        print("Gracias por visitar nuestra tienda.")
    else:
        print("Opción no válida.")

else: print("Contraseña o nombre de usuario incorrectos, vuelva a intentarlo.") 

def nombre(x="world"):
    print("Hola, "+x+"!")
nombre()
otronombre=input("digite su nombre: ") .strip().title()
nombre(otronombre)

Anumero=int(input("Digite un número: "))
Bnumero=int(input("Digite otro número: "))
def masiso(a,b):
    return a+b
resultado=masiso(Anumero, Bnumero)
print("El resultado de la suma es:",resultado)

aPotencia=int(input("ponme la base: "))
bExponente=int(input("ponme el exponente: "))
def potencias(base,exponente):
    return pow(base,exponente)
print("El resultado de la potencia es:",potencias(aPotencia,bExponente))

aNumber=int(input("Digite un número: "))
bNumber=int(input("Digite otro número: "))

def multiplicación(a,b):
    return a*b
resultado = multiplicación(aNumber, bNumber)

print(aNumber,"x",bNumber," = ",resultado)

def resta(a=3,b=2):
    return a-b

print("Con valores por defecto la resta es:",resta())
print("Usando el orden con sólo un valor:",resta(5))
print("Usando el orden con todos valores:",resta(5,3))
print("Usando el nombre de los parámetros:",resta(a=5,b=3))
print("Usando el nombre de un parámetro:",resta(b=3))

##Con valores por defecto la resta es: 1
#Usando el orden con sólo un valor: 3 
#Usando el orden con todos valores: 2
#Usando el nombre de los parámetros: 2
#Usando el nombre de un parámetro: 0

def main():
    name = input("What's your name?: ").strip().title()
    hello(name)
def hello(to="Wolrd"):
    print("hello, "+to+"!")
main()

def hello(to="Wolrd"):
    print("hello, "+to+"!")
name=input("What's your name?: ").strip().title()
hello(name)

dinero=1000
compra=int(input("¿cuanto dinero vamos a gastar?: "))
def comprar(precio):
    global dinero
    print(f"Dinero restante: {dinero}$")
    dinero -= precio
comprar(compra)
print(f"Dinero final: {dinero} $")

menor= int(input("Dame un poco de tu dinero: "))
print("Gracias! ahora tienes:", dinero-menor,"$")

# Diccionarios que indican si una habitación está reservada en cierto mes
reservada1 = {mes: False for mes in range(1, 13)}
reservada2 = {mes: False for mes in range(1, 13)}
reservada3 = {mes: False for mes in range(1, 13)}

def hab(monto, habitacion, mes):
    precios = {1: 500, 2: 120, 3: 1200}

    # Escoger el diccionario según la habitación
    if habitacion == 1:
        reservada = reservada1
    elif habitacion == 2:
        reservada = reservada2
    elif habitacion == 3:
        reservada = reservada3
    else:
        print("Opción inválida.")
        return monto

    # Verificar si está reservada
    if reservada[mes]:
        print(f"La habitación #{habitacion} ya está reservada en el mes {mes}.")
    elif monto >= precios[habitacion]:
        print(f"Habitación #{habitacion} reservada con éxito en el mes {mes}.")
        monto -= precios[habitacion]
        reservada[mes] = True
        print(f"Crédito restante: ${monto}")
    else:
        print("Crédito insuficiente para reservar esta habitación.")

    return monto


# Bucle para atender varios clientes
while True:
    print("\n--- NUEVO CLIENTE ---")
    montocliente = int(input("Digite su crédito disponible: "))

    habitacion = int(input(
        "1) Habitación#1: $500\n"
        "2) Habitación#2: $120\n"
        "3) Habitación#3: $1200\n"
        "Seleccione una habitación (1/2/3): "
    ))

    mes = int(input("Digite el mes en el que se quedará (1-12): "))

    # Llamada a la función
    montocliente = hab(montocliente, habitacion, mes)

    # Preguntar si desea continuar
    continuar = input("\n¿Desea registrar otra reserva? (s/n): ").lower()
    if continuar != "s":
        print("\nGracias por usar el sistema de reservas. ¡Hasta luego!")
        break

i=3
while i !=0:
    print("Meow!")
    i= i-1

print("Woof!\n"*3, end="")

for i in range(3):
    print("Oink!")

for i in ["Cat","Dog","Pig"]:  
    print(i)

for i in range(1,6):
    print("Hello, world.")

for i in range(1,11):
    print(i)

x = int(input('digite un númerico: '))
print("woof!\n"*x, end="")

while True:
    n=int(input("Que es n?: "))
    if n>0:
        break

for i in range(n):
    print("meow!")

def otro():
    n=int(input("Quien es n?: "))
    for i in range(n):
        print("meow!")
otro()

respuesta = "s"  # Inicializamos con "s" para entrar al bucle

while respuesta == "s":  # El bucle sigue mientras la respuesta sea "s"
    print("Sigo repitiendo el bucle")
    respuesta = input("¿Quieres seguir? (s/n): ").lower()

print("¡Bucle terminado!")

while True:
    word=(input("ingrese una palabra: "))
    for i in range(10):
        print(word)
    respuesta=input("¿desea continuar? (s/n): ").lower()
    if respuesta!="s":
        break
print("¡Bucle terminado!")

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = -1
        
        if n>0:
            return n 

def meow(n):
    for _ in range(n):
        print("Meow!")

main()

tabla=int(input("dame un numero: "))
for i in range(1,11):
    print(tabla,"x",i,"=",tabla*i)

def square(n):
    return pow(n,2)
u=int(input("Dame un número: "))
cuadrado = square(u)
print("la raiz cuadrada de",u,"es:",cuadrado)

nombre=input("ingrese su nombre: ")
match nombre:
    case "Henry" | "Ron" | "Hermione":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("No pertenece a ninguna casa")
    
print("hellow world")
word=int(input("Ingrese un numero: "))
if word %2==0:
    print("El número ",word," es par")
else:
    print("El numero ",word," es impar")

nombre = input("Ingrese su nombre: ").strip()

x=int(input("ingrese un número: "))
y=int(input("Ingrese otro número: "))
if x==y:
    print("los números son iguales")
else:
    print("los números no son iguales")

nota = int(input("Ingrese su nota (0-100):"))
if 90 <= nota:
    print("A")
elif 80<= nota:
    print("B")
elif 70 <= nota:
    print("C")
elif 60 <= nota:
    print("D")
else:
    print("F")

def main():
    o=int(input("ingrese un numero: "))
    if even(o):
        print("El número ",o," es par")
    else:
        print("El numero ",o," es impar")
def even(n):
    return n % 2 == 0

main() 