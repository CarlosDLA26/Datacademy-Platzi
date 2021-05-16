# Python Cardio
# Reto 4: Calculadora de volúmenes

from math import pi

vol_cono        = lambda h, r: (1/3)*h*pi*(r**2)
vol_cilindro    = lambda h, r: pi*(r**2)*h
vol_cubo        = lambda l: (l**3)
vol_piramide_bc = lambda l, h: ((l**2)*h)/3
vol_esfera      = lambda r: (4/3)*pi*(r**3)

def main():
    print("CALCULADORA DE VOLÚMENES")
    print("Seleccione la figura a la que desea calcular el volúmen (Solo el dígito):")
    print("1. Cono")
    print("2. Cilindro")
    print("3. Cubo")
    print("4. Pirámide de base cuadrada")
    print("5. Esfera")
    figura = int(input())
    
    if(figura == 1):
        h = float(input("Digite la altura del cono: "))
        r = float(input("Digite el radio del cono: "))
        print("El volumen es: {}".format(vol_cono(h, r)))
    elif(figura == 2):
        h = float(input("Digite la altura del cilindro: "))
        r = float(input("Digite el radio del cilindro: "))
        print("El volumen es: {}".format(vol_cilindro(h, r)))
    elif(figura == 3):
        l = float(input("Digite la medida de un lado del cubo: "))
        print("El volumen es: {}".format(vol_cubo(l)))
    elif(figura == 4):
        l = float(input("Digite la medida de un lado de la base de la piramide: "))
        h = float(input("Digite la altura de la piramide: "))
        print("El volumen es: {}".format(vol_piramide_bc(l, h)))
    elif(figura == 5):
        r = float(input("Digite el radio de la esfera: "))
        print("El volumen es: {}".format(vol_esfera(r)))
    else:
        print("Digite un número entre 1 y 5")
        
        
if __name__ == "__main__":
    main()