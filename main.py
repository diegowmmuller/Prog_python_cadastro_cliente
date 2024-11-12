from programa_cadastro_cliente.lib.interface import *
from programa_cadastro_cliente.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoexiste(arq):
     criararquivo(arq)


while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:      ######## resposta 1
        lerarquivo('cursoemvideo.txt')   # Opção de listar o conteudo do arquivo
    elif resposta == 2:    ######## respost 2
        cabecalho('NOVO CADASTRO')                 # Opção criar um novo cadastro
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        cadastrar(arq, nome, idade)
    elif resposta == 3:     ######## resposta 31
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)