def es_palindromo(palabra):
    if palabra == palabra[::-1]:
        print("Es Palindromo")
    else:
        print("No es palindromo")


def run():
    palabra = input('Ingrese la palabra a verificar: ').replace(' ','').lower()
    es_palindromo(palabra)


if __name__== '__main__':
    run()

