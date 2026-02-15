# Implementación del cifrado César

def cifrado_cesar(texto, desplazamiento):
    resultado = ""
    for char in texto:
        if char.isalpha():
            codigo = ord(char) + desplazamiento
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')
            codigo = (codigo - base) % 26
            resultado += chr(base + codigo)
        else:
            resultado += char
    return resultado


# Programa principal
# Solicita al usuario el mensaje a cifrar y el valor de cambio, asegurándote de que el valor de cambio sea un número entero entre 1 y 25. Si el usuario ingresa un valor no válido, muestra un mensaje de error y vuelve a solicitar el valor de cambio.
shift = 0
while shift == 0:
    try:
        shift = int(input("Ingresa el valor de cambio del cifrado (1..25): "))
        if shift not in range(1, 26):
            raise ValueError
    except ValueError:
        shift = 0
        print("¡Valor de cambio inválido!")


# Para descifrar el mensaje, puedes reutilizar la función de cifrado pero con un desplazamiento negativo. Solicita al usuario el mensaje cifrado y el valor de cambio, y muestra el mensaje descifrado.
def descifrado_cesar(texto, desplazamiento):
    return cifrado_cesar(texto , desplazamiento)
# Programa principal para descifrar
def menu():
    print("\n--- MENÚ ---")
    print("1.cifrar mensaje")
    print("2.descifrar mensaje")
    print("0.salir")
# Implementa un menú que permita al usuario elegir entre cifrar un mensaje, descifrar un mensaje o salir del programa. El programa debe continuar ejecutándose hasta que el usuario decida salir.
while True:
    menu()
    opcion = input("Selecciona una opción: ")
    if opcion == "1":
        text = input("Ingresa un mensaje: ")
        shift = 0
        while shift == 0:
            try:
                shift = int(input("Ingresa el valor de cambio del cifrado (1..25): "))
                if shift not in range(1, 26):
                    raise ValueError
            except ValueError:
                shift = 0
                print("¡Valor de cambio inválido!")
        cipher = cifrado_cesar(text, shift)
        print("Mensaje cifrado:", cipher)
    elif opcion == "2":
        text = input("Ingresa el mensaje cifrado: ")
        shift = 0
        while shift == 0:
            try:
                shift = int(input("Ingresa el valor de cambio del cifrado (1..25): "))
                if shift not in range(1, 26):
                    raise ValueError
            except ValueError:
                shift = 0
                print("¡Valor de cambio inválido!")
        deciphered = descifrado_cesar(text, shift)
        print("Mensaje descifrado:", deciphered)
    elif opcion == "0":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida, por favor intenta de nuevo.")
menu()
