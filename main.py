import jocs

while True:
    print("================================")    
    print("--BENVINGUT/DA AL MINI ARCADE--")
    print("================================")
    print("1. Jugar Pedra Paper Tisores")
    print("2. Jugar a endevinar els numero")
    print("S per sortir")
    opcio = input("Tria una opcio: ")
    if opcio == "1":
        import jocs.Pedra_Paper_Tisores
        jocs.Pedra_Paper_Tisor
    elif opcio == "2":
        import endevinar_numero
        endevinar_numero.jugar()
    elif opcio.upper() == "S":
        print("Gracies per jugar! Fins aviat!")
        break
    else:
        print("Opcio no valida, si us plau tria una opcio correcta.")
