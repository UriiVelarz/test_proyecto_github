def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

def main():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    opcion = int(input("Seleccione una operación (1-Suma, 2-Resta, 3-Multiplicación, 4-División, 5-Salir): "))
    
    if opcion == 1:
        print("Suma:", suma(num1, num2))
    elif opcion == 2:
        print("Resta:", resta(num1, num2))
    elif opcion == 3:
        print("Multiplicación:", multiplicacion(num1, num2))
    elif opcion == 4:
        try:
            print("División:", division(num1, num2))
        except ValueError as e:
            print(e)
    elif opcion == 5:
        print("Saliendo del programa...")

if __name__ == "__main__":
    main()
