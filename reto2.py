# Python Cardio
# Reto 2: piedra papel o tijera

def ppt(player1, player2):
    # True -> Victoria de jugador 1
    # False -> Victoria de jugador 2
    if(player1 == player2):
        return "Empate"
    
    elif((player1 == "tijeras") and (player2 == "papel")):
        return True
    
    elif((player1 == "tijeras") and (player2 == "piedra")):
        return False
    
    elif((player1 == "papel") and (player2 == "tijeras")):
        return False
    
    elif((player1 == "papel") and (player2 == "piedra")):
        return True
    
    elif((player1 == "piedra") and (player2 == "tijeras")):
        return True
    
    elif((player1 == "piedra") and (player2 == "papel")):
        return False
    
    return "Usen solo piedra, papel o tijeras."

def main():
    contador_p1 = 0
    contador_p2 = 0
    
    while(contador_p1 < 3 and contador_p2 < 3):
        player1 = input("Jugador 1 ¿piedra, papel o tijera? ")
        player2 = input("Jugador 2 ¿piedra, papel o tijera? ")
        
        juego = ppt(player1, player2)
        
        if(juego == "Empate"):
            print("Ronda empatada")
            
        elif(juego):
            contador_p1 = contador_p1 + 1
            print("Jugador 1 gana la ronda.")
        else:
            contador_p2 = contador_p2 + 1
            print("Jugador 2 gana la ronda.")
        
        print("---PUNTUACIONES---")
        print("Jugador 1 -> {}".format(contador_p1))
        print("Jugador 2 -> {}".format(contador_p2))
        print("------------------")
    
    if(contador_p1 > contador_p2):
        print("EL JUGADOR 1 GANA EL JUEGO.")
    else:
        print("EL JUGADOR 2 GANA EL JUEGO.")
    

if __name__ == "__main__":
    main()
    