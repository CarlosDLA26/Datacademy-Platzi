# Python Cardio
# Reto 5: Rangos cambiantes

def intervalo(a, b, c):
    if (a <= c <= b):
        print('El numero es: {}'.format(c))
    else:
        print('El numero es: {}'.format(c))
        c = float(input('Ingrese otro numero: '))
        intervalo(a, b, c)

def main():
    a = float(input('Ingrese un numero: '))
    b = float(input('Ingrese un numero mas alto que el anterior: '))
    c = float(input('Ingrese un numero mas: '))
    intervalo(a, b, c)
    
    
if __name__ == '__main__':
    main()