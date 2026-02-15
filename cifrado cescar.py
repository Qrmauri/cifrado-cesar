# Función de cifrado César
def cifrado_cesar(texto, desplazamiento):
    resultado = ""
    for char in texto:
        if char.isalpha():
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')
            
            codigo = (ord(char) - base + desplazamiento) % 26
            resultado += chr(base + codigo)
        else:
            resultado += char
    return resultado


# Función de descifrado
def descifrado_cesar(texto, desplazamiento):
    return cifrado_cesar(texto, -desplazamiento)


# Función para pedir shift válido
def pedir_shift():
    while True:
        try:
            shift = int(input("Ingresa el valor de cambio (1..25): "))
            if shift in range(1, 26):
                return shift
            else:
                print("¡Valor fuera de rango!")
        except ValueError:
            print("¡Debes ingresar un número entero!")


# Menú
def menu():
    print("\n--- MENÚ ---")
    print("1. Cifrar mensaje")
    print("2. Descifrar mensaje")
    print("0. Salir")


# Programa principal
while True:
    menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        texto = input("Ingresa un mensaje: ")
        shift = pedir_shift()
        print("Mensaje cifrado:", cifrado_cesar(texto, shift))

    elif opcion == "2":
        texto = input("Ingresa el mensaje cifrado: ")
        shift = pedir_shift()
        print("Mensaje descifrado:", descifrado_cesar(texto, shift))

    elif opcion == "0":
        print("¡Hasta luego!")
        break

    else:
        print("Opción no válida, intenta nuevamente.")
