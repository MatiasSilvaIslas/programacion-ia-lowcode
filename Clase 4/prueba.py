# Define una función para calcular el área de un triángulo.
def area_triangulo():
    base = float(input("Ingresa la base del triángulo: "))
    altura = float(input("Ingresa la altura del triángulo: "))
    # Recibe la base y la altura, las multiplica y divide el resultado entre 2.
    area = (base * altura) / 2
    # Devuelve el área calculada para que pueda utilizarse fuera de la función.
    return area

# implementa la funcion para calcular el área de un triángulo y mostrar el resultado.
resultado = area_triangulo()
print(f"El área del triángulo es: {resultado}") 


#Funcion para calcular el área de un círculo.
def area_circulo():
    radio = float(input("Ingresa el radio del círculo: "))
    # Calcula el área usando la fórmula π * radio^2.
    area = 3.14159 * (radio ** 2)
    # Devuelve el área calculada para que pueda utilizarse fuera de la función.
    return area 
