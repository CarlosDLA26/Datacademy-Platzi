# Python Cardio
# Reto 1: Area de un triangulo

area_triangulo = lambda base, altura : (base*altura)/2 

def tipo_triangulo(a, b, c):
    if (a == b and b == c):
        return "El triángulo es equilatero."
    elif ((a == b and b != c) or (a == c and c != b) or (b == c and c != a)):
        return "El triángulo es isóceles."
    elif(a != b and b != c and a != c):
        return "El triángulo es escaleno."

def main():
    a = float(input("Digite el primer lado: "))
    b = float(input("Digite el segundo lado: "))
    c = float(input("Digite el tercer lado: "))
    print(tipo_triangulo(a, b, c))
    
if __name__ == "__main__":
    main()
