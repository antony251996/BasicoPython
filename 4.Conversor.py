def exchange(moneda,cantidad):
    result = 0
    if moneda == 1:
        result = round(cantidad * 0.00027,2)
        print(f"Los {cantidad} pesos colombianos equivalen a {result} dolares")
    elif moneda == 2:
        result = round(cantidad * 0.27,2)
        print(f"Los {cantidad} soles peruanos equivalen a {result} dolares")
    elif moneda == 3:
        result = round(cantidad * 0.0014,2)
        print(f"Los {cantidad} pesos chiles equivales a {result} dolares")


if __name__ =="__main__":
    moneda = int(input("""
    Ingresa el la moneda que deseas cambiar a dolar:
        [1] Pesos Colombianos
        [2] Soles Peruanos
        [3] Pesos Chilenos
    Selecciona: """))
    print("********************************************")
    cantidad = float(input("Ingresa la cantidad que quieres convertir: "))
    exchange(moneda,cantidad)