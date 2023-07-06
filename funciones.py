import numpy as np

lista_rut=[]
lista_puesto=[]
acumulador=0
platinum =120000
gold = 80000 
silver= 50000
total_plati=0
total_gold=0
total_silver=0
cant_p=0
cant_g=0
cant_s=0
acumulador_t_cant=0
acumulador_repe=0
def opcion():
    while True:
        try:
            opcion = int(input("""
                BIENVENIDA/O A "CREATIVOS"

                1. Comprar entradas
                2. Mostrar ubicaciones disponibles
                3. Ver listado de asistentes
                4. Mostrar ganancias totales
                5. Salir
                ingrese una opcion: """))
            if opcion >=1 and opcion <=5:
                break
            else:
                print("ERROR! debe ingresar una de las opciones mostradas")
        except:
            print("ERROR! debe ser un numero entero")
        
def comprar():
    while True:
        try:
            comprar=int(input("Ingresa la cantidad de entradas quiere(maximo 3): "))
            if comprar==1 or comprar==2 or comprar==3:
                try:
                    rut=int(input("Intrucciones a seguir:\n su rut se debe ingresar sin punto'.'o guion'-'\n si su rut lleva k remplacelo por un '1'"))
                    if rut>=100000000 and rut <=999999999:
                        try:
                            puesto=int(input("elija el asiento que desea comprar(del 1 al 100"))
                            if puesto>=1 and puesto <=100:
                                if puesto >=1 and puesto <=20:
                                    total_plati=comprar * platinum
                                    acumulador=total_plati+acumulador
                                    cant_p=comprar+cant_p
                                    acumulador_t_cant=cant_p+acumulador_t_cant
                                else:
                                    pass
                                if puesto >=21 and puesto <=50:
                                    total_gold=comprar * gold
                                    acumulador=total_gold+acumulador
                                    cant_g=comprar+cant_g
                                    acumulador_t_cant=cant_g+acumulador_t_cant
                                else:
                                    pass
                                if puesto >=51 and puesto <=100:
                                    total_silver=comprar * silver
                                    acumulador=total_silver+acumulador
                                    cant_s=comprar+cant_s
                                    acumulador_t_cant=cant_s+acumulador_t_cant
                                else:
                                    pass
                            else:
                                print("ERROR! debe ingresar correctamente el asiento del 1 al 100")
                        except:
                            print("ERROR! debe ser solo numeros entero")
                  
                    else:
                        print("ERROR! debe ingresar correctamente su rut")
                except:
                    print("ERROR! debe ser solo numeros entero")
                
            else:
                print("ERROR! debes elegir entre 1, 2 o 3 entradas")
        except:
            print("ERROR! debe ser un numero entero")

def ubicaciones():
    ubi=np.array([(1,2,3,4,5,6,7,8,9,10),(11,12,13,14,15,16,17,18,19,20),(21,22,23,24,25,26,27,28,29,30),(31,32,33,34,35,36,37,38,39,40,),(41,42,43,44,45,46,47,48,49,50),(51,52,53,54,55,56,57,58,59,60),(61,62,63,64,65,66,67,68,69,70),(71,72,73,74,75,76,77,78,79,80),(81,82,83,84,85,86,87,88,89,90),(91,92,93,94,95,96,97,98,99,100)])
    print(ubi)


def listado():
    print(lista_rut.sort)


def total_comprita():
    print(f"""
            |Tipo Entrada       Cantidad            Total
            |Platinum $120.000     {cant_p}                 {total_plati}
            |--------------------------------------------------------
            |Gold $80.000          {cant_g}                 {total_gold}
            |--------------------------------------------------------
            |Silver $50.000        {cant_s}                 {total_silver}      
            |--------------------------------------------------------
            |TOTAL                 {acumulador_t_cant}                 {acumulador}  """)
    

def salir():
    print("""
    Matias Oyanedel 
    06-07-2023""")



def todo():
    while True:
        try:
            opcion = int(input("""
                BIENVENIDA/O A "CREATIVOS"

              ¿esta listo para comprar entradas
              del concierto VIP de “Michael Jam”?

                1. Comprar entradas
                2. Mostrar ubicaciones disponibles
                3. Ver listado de asistentes
                4. Mostrar ganancias totales
                5. Salir
                ingrese una opcion: """))
            if opcion >=1 and opcion <=5:
                if opcion==1:
                    while True:
                        try:
                            comprar=int(input("Ingresa la cantidad de entradas quiere(maximo 3): "))
                            if comprar==1 or comprar==2 or comprar==3:
                                try:
                                    print("Intrucciones a seguir:\n su rut se debe ingresar sin punto'.'o guion'-'\n si su rut lleva la letra 'k' remplacelo por un '1'")
                                    rut=int(input("Ahora siguiendo las intrucciones anteriores\n Por favor ingrese su rut: "))
                                    if rut>=100000000 and rut <=999999999:
                                        lista_rut.append(rut)
                                        while True:
                                            try:
                                                puesto=int(input("elija el asiento que desea comprar(del 1 al 100): "))
                                                if puesto>=1 and puesto <=100:
                                                    if puesto >=1 and puesto <=20:
                                                        total_plati=comprar * platinum
                                                        acumulador=total_plati+acumulador
                                                        cant_p=comprar+cant_p
                                                        acumulador_t_cant=cant_p+acumulador_t_cant
                                                    else:
                                                        pass
                                                    if puesto >=21 and puesto <=50:
                                                        total_gold=comprar * gold
                                                        acumulador=total_gold+acumulador
                                                        cant_g=comprar+cant_g
                                                        acumulador_t_cant=cant_g+acumulador_t_cant
                                                    else:
                                                        pass
                                                    if puesto >=51 and puesto <=100:
                                                        total_silver=comprar * silver
                                                        acumulador=total_silver+acumulador
                                                        cant_s=comprar+cant_s
                                                        acumulador_t_cant=cant_s+acumulador_t_cant
                                                    else:
                                                        pass
                                                    if lista_puesto==puesto:
                                                        print("No está disponible")
                                                        input("precione la tecla 'enter' para regresar")
                                                        break
                                                    else:
                                                        pass
                                                    lista_puesto.append(puesto)
                                                    acumulador_repe=1+acumulador_repe
                                                    if acumulador_repe==comprar:
                                                        break
                                                    else:
                                                        print("Por favor siga elijiendo asiento/s")
                                                else:
                                                    print("ERROR! debe ingresar correctamente el asiento del 1 al 100")
                                            except:
                                                print("ERROR! debe ser solo numeros entero")
                                
                                    else:
                                        print("ERROR! debe ingresar correctamente su rut")
                                except:
                                    print("ERROR! debe ser solo numeros entero")
                                
                            else:
                                print("ERROR! debes elegir entre 1, 2 o 3 entradas")
                        except:
                            print("ERROR! debe ser un numero entero")
                else:
                    pass
                if opcion==2:
                    ubi=np.array([(1,2,3,4,5,6,7,8,9,10),(11,12,13,14,15,16,17,18,19,20),(21,22,23,24,25,26,27,28,29,30),(31,32,33,34,35,36,37,38,39,40,),(41,42,43,44,45,46,47,48,49,50),(51,52,53,54,55,56,57,58,59,60),(61,62,63,64,65,66,67,68,69,70),(71,72,73,74,75,76,77,78,79,80),(81,82,83,84,85,86,87,88,89,90),(91,92,93,94,95,96,97,98,99,100)])
                    print(ubi)
                    input("preciona la tecla 'enter' para regresar al menu ")
                else:
                    pass
                if opcion==3:
                    print(lista_rut.sort)
                else:
                    pass
                if opcion==4:
                    print(f"""
                                |Tipo Entrada       Cantidad            Total
                                |Platinum $120.000     {cant_p}                 {total_plati}
                                |--------------------------------------------------------
                                |Gold $80.000          {cant_g}                 {total_gold}
                                |--------------------------------------------------------
                                |Silver $50.000        {cant_s}                 {total_silver}      
                                |--------------------------------------------------------
                                |TOTAL                 {acumulador_t_cant}                 {acumulador}  """)
                else:
                    pass
                if opcion==5:
                    print("""
                    Matias Oyanedel 
                    06-07-2023""")
                    break
                else:
                    pass
            else:
                print("ERROR! debe ingresar una de las opciones mostradas")
        except:
            print("ERROR! debe ser un numero entero")