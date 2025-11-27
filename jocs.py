import robot
import random


def janken():
    print("==============================================")
    print("Benvingut/da al joc de Pedra, Paper o Tisores!")
    print("==============================================")
    print("Introdueix fins quantes rondes vols jugar:")
    print("1. Si vols jugar fins que un jugador arribi a 3 punts.")
    print("2. Si vols jugar fins 5 rondes.")
    opcio = input("Tria una opció: ").strip()

    if opcio == "1":
        rondes_a_guanyar = 3
        max_rondes = None
    elif opcio == "2":
        rondes_a_guanyar = None
        max_rondes = 5
    else:
        print("Opció no vàlida. Si us plau, intenta-ho de nou.")
        return

    punts_jugador = 0
    punts_maquina = 0
    ronda = 1
    opcions = ["pedra", "paper", "tisores"]

    while True:
        if max_rondes is not None and ronda > max_rondes:
            break
        if rondes_a_guanyar is not None and (punts_jugador >= rondes_a_guanyar or punts_maquina >= rondes_a_guanyar):
            break

        print(f"Ronda {ronda}:")
        jugador = input("Tria pedra, paper o tisores: ").strip().lower()

        if jugador not in opcions:
            print("Elecció no vàlida. Si us plau, intenta-ho de nou.")
            continue

        # La màquina tria aleatòriament; si tens una funció a robot.py, substitueix-ho per robot.<funció>()
        maquina = random.choice(opcions)
        print(f"La màquina ha triat: {maquina}")

        if jugador == maquina:
            print("Empat!")
        elif (jugador == "pedra" and maquina == "tisores") or \
             (jugador == "paper" and maquina == "pedra") or \
             (jugador == "tisores" and maquina == "paper"):
            print("Has guanyat aquesta ronda!")
            punts_jugador += 1
        else:
            print("La màquina ha guanyat aquesta ronda!")
            punts_maquina += 1

        print(f"Punts - Tu: {punts_jugador}, Màquina: {punts_maquina}")
        ronda += 1

    # Resultat final
    if punts_jugador > punts_maquina:
        print("Has guanyat la partida! 🎉")
    elif punts_maquina > punts_jugador:
        print("La màquina ha guanyat la partida!")
    else:
        print("La partida ha acabat en empat.")
