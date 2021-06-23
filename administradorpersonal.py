# crear una calculadora de nuestras finanzas que reste nuestros ingresos con nuestros gastos y nos muestre el saldo,
# y nos muestr tambien en que fue el gasto y el ingreso y los montos en diccionarios
from os import name


def run():
    menu = """***BIENVENIDO A TU ADMINISTRADOR PERSONAL***
    1) VER INGRESOS
    2) VER GASTOS
    3) VER SALDO ACTUAL 
    """
    opcion = int(input("Escribe el numero de la opcion que deseas ver:"))
    nombre_ing = input("Ingresa aqui el NOMBRE del INGRESO: ")
    monto_ing = int(input("Ingresa aqui el MONTO del INGRESO"))
    lista_ing = [nombre_ing,monto_ing]
    print(lista_ing)
    ingresos = { nombre_ing:monto_ing}
    print(ingresos)



if __name__=="__main__":
    run()