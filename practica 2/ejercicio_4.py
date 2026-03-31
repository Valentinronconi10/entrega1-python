email = input("Ingrese su direccion de email: ")
if email.count("@") == 1:
    print("Contine exactamente 1 arroba")
    pos_arroba = email.find("@")
    pos = email.find("@")
    if pos > 0:
        print("Tiene caracteres antes")
    else:
        print("No tiene caracteres antes")
    pos_punto = email.find(".",pos_arroba)
    if pos_arroba > 0 and pos_punto > pos_arroba:
        print("Tiene al menos un punto despues de la @")
    else:
        print("No cumple condicion")

    if not email.startswith("@") and not email.startswith(".."):
        print("No Empieza con @ o ..")
    else: 
        print("Empieza con @ o ..")
    if not email.endswith("@")and not email.endswith(".."):
        print("No termina con @ o ..")
    else:
        print("Termina con @ o ..")

    
    pos_ultimo_punto = email.rfind(".")
    if pos_ultimo_punto != -1 and (len(email)) - pos_ultimo_punto -1 >= 2:
        print("Dominio valido")
    else:
        print("Dominio invalido")
else:
    print("No tiene exactamente un @")
