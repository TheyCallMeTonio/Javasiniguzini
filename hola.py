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