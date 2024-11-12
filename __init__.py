def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Erro de valor. Digite um numero inteiro valido.')
            continue
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar.')
            return 0
        else:
            return n



def linha(tam = 42):
    return '-'*tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')

    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c = c+1
    print(linha())
    opc = leiaint('Sua Opção: ')
    return opc