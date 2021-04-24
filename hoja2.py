print("Bienvenido")
print("")

def contraseña():
    contraGuardar = input("Ingrese una contraseña a guardar ")
    print("")
    contraComparar= input("Ingrese de nuevo la contraseña para comparar ")
    if contraGuardar==contraComparar:
        print("La contraseña es correcta")
    else :
        print("La contraseña es incorrecta")
        contraseña()

contraseña()
print("")
def grupo():
    nombre = input("Ingrese la inicial de su nombre en mayuscula ")
    print("")
    sexo = input("Ingrese su genero M o F : ")
    if sexo =="M" or sexo== "F":
        if nombre =="A" or nombre =="B" or nombre =="C" or nombre =="D" or nombre =="E" or nombre =="F" or nombre =="G" or nombre =="H" or nombre =="I" or nombre =="J" or nombre =="K" or nombre =="L" or nombre =="M" or nombre =="N" or nombre =="O" or nombre =="P" or nombre =="Q" or nombre =="R" or nombre =="S" or nombre =="T" or nombre =="U" or nombre =="V" or nombre =="W" or nombre =="X" or nombre =="Y" or nombre =="Z":
            if nombre =="A" or nombre =="B" or nombre =="C" or nombre =="D" or nombre =="E" or nombre =="F" or nombre =="G" or nombre =="H" or nombre =="I" or nombre =="J" or nombre =="K" or nombre =="L":
                if sexo =="F":
                    print ("Corresponde al grupo A")
            else:
                if sexo =="F":
                    print("Corresponde al grupo B")                  
            if nombre =="O" or nombre =="P" or nombre =="Q" or nombre =="R" or nombre =="S" or nombre =="T" or nombre =="U" or nombre =="V" or nombre =="W" or nombre =="X" or nombre =="Y" or nombre =="Z":
                if sexo =="M":
                    print ("Corresponde al grupo A")
            else:
                if sexo =="M":
                    print("Corresponde al grupo B")
        else:
            print("No ingreso la inicial de su nombre")
            grupo()
        
    else:
        print("No elijio su genero")
        grupo()

grupo()