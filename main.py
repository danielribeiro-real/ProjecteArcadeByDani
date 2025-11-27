import jocs  


while True:
    print("================================")    
    print("      --- MINI ARCADE ---")
    print("================================")
    print("1. Pedra, Paper o Tisora")
    print("2. Endevina el Número")
    print("S. Sortir")
    print("================================")

    opcio = input("Tria una opció: ").strip().upper()

    if opcio == "1":
        jocs.janken()
    elif opcio == "2":
        jocs.nana()
    elif opcio == "S":
        print("Gràcies per jugar! Fins aviat!")
        break
    else:
        print("Opció no vàlida. Torna-ho a provar.")



