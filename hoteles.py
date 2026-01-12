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