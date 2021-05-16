# Python Cardio
# Reto 3: kilometros <-> millas

def conversor_km_millas(d, opcion = 1):
    
    '''
    Parameters
    ----------
    d : float
        Distancia a convertir
    opcion : int, optional
        Selector de conversor. The default is 1.
        1 -> millas a kilometros
        2 -> kilometros a millas

    Returns
    -------
    float
        devuelve la conversión realizada
    '''
    
    if(opcion == 1):
        return d*1.609344
    elif(opcion == 2):
        return d*0.621371


def main():
    print("Conversor millas <-> kilómetros")
    print("Seleccione la conversión que desea hacer (Solo ponga el dígito):")
    print("1. millas a kilómetros")
    print("2. kilómetros a millas")
    d = int(input())
    dis = float(input("Digite la distancia a convertir: "))
    
    if (d == 1):
        print("{} millas son {} kilometros".format(dis, conversor_km_millas(dis)))
    elif(d == 2):        
        print("{} kilometros son {} millas".format(dis, conversor_km_millas(dis, 2)))

if __name__ == "__main__":
    main()