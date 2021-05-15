def run(num,final):
    cont = 0
    pot=0
    while cont < final:
        print(f'{num} elevado {pot} = {num ** pot}')
        pot+=1
        cont = num ** pot


if __name__ == '__main__':
    num = int(input('Ingresa el numero que quieres conocer su potencia: '))
    final = int(input('Ingres hasta que numero deseas mostrar: '))
    run(num,final)