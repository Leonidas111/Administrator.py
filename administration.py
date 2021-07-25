import os
import time


def run():
    menu = """ ADMINISTRADOR PERSONAL
    1)Registrar Ingresos
    2)Registrar Egresos
    3)Ver presupuesto actual
    4)Ver lista de Ingresos y Egresos
    5)Salir
    Escribe el numero de la opcion aqui ==>  """
    opcion = int(input(menu))
    while opcion <=5 :
        #OPCION 1 REGISTRAR INGRESO:
        if opcion == 1:
            os.system("cls")
            with open ("./ingresos.py","a",encoding="utf-8") as ai:
                print("Escribe (0) cuando termines")
                ingreso = input("Escribe el ingreso:$. ")
                ai.write("\n")
                ai.write(ingreso)
                if ingreso == "0":
                    os.system("cls")
                    time.sleep(1.5)
                    return run()
        #OPCION 2 REGISTRAR EGRESOS:
        if opcion == 2:
            os.system("cls")
            with open ("./egresos.py","a",encoding="utf-8") as ae:
                print("Escribe (0) cuando termines")
                egreso = input("Escribe el egreso:$. ")
                ae.write("\n")
                ae.write(egreso)
                if egreso == "0":
                    os.system("cls")
                    time.sleep(1.5)
                    return run()
        #OPCION 3 VER PRESUPUESTO ACTUAL:
        if opcion == 3:
            os.system("cls")
            with open ("./ingresos.py","r",encoding="utf-8")as ai:
                total_ingresos =sum([int(line) for line in ai]) 
            print(f"Total ingresos = $. {total_ingresos}")
            with open ("./egresos.py","r",encoding="utf-8")as ae:
                total_egresos = sum([int(line) for line in ae])
            print(f"Total de egresos = $. {total_egresos}")
            print(f"El presupuesto total es = $. {total_ingresos-total_egresos} ")
            time.sleep(3.5)
            return run()
        #OPCION 4 VER LISTA INGRESOS Y EGRESOS:
        if opcion == 4:
            os.system("cls")
            with open ("./ingresos.py","r",encoding="utf-8")as ai:
                print("INGRESOS:")
                print("\n")
                for line in ai:
                    print(f"$.{line}")
            with open ("./egresos.py","r",encoding="utf-8")as ae:
                print("EGRESOS:")
                print("\n")
                for line in ae:
                    print(f"$.{line} ")
            time.sleep(3)
            return run()
        #OPCION 5 SALIR    
        if opcion == 5:
            exit()
    else:
        print("Ingresa una opcion correcta:")
        return run()


if __name__=="__main__":
    run()