import formatação
from time import sleep
from random import choice
with open('palavras.txt') as arquivo:
    linhas = arquivo.read()
    lista_palavras = linhas.split('\n')
formatação.cabeçalho(f'{formatação.cor("azul")}Bem vindo ao jogo da forca{formatação.cor("fim")}')
escolha = choice(lista_palavras).upper()
acerto = 0
erro = 0
letras_erradas = ''
letras_acertadas = ''
while acerto != len(escolha) and erro != 6:
    print('*'*46)
    mensagem = ''
    for letra in escolha:
        if letra in letras_acertadas:
            mensagem += letra + ' '
        else:
            mensagem += '_ '
    print(mensagem)
    print(f'{formatação.cor("azul")}Você ja acertou: {formatação.cor("fim")}' + letras_acertadas)
    print(f'{formatação.cor("amarelo")}Você ja errou: {formatação.cor("fim")}' + letras_erradas)
    letra = str(input('Digite a letra: ')).upper().strip()
    if letra in escolha:
        print(f'{formatação.cor("ciano")}Você acertou{formatação.cor("fim")}')
        sleep(1)
        letras_acertadas += letra
        acerto += escolha.count(letra)
    else:
        print(f'{formatação.cor("vermelho")}Você errou{formatação.cor("fim")}')
        sleep(1)
        letras_erradas += letra
        erro += 1

if acerto == len(escolha):
    print(escolha)
    print(f'{formatação.cor("verde")}=' * 46)
    print('VOCÊ GANHOU!!!! PARABÉNS!!!'.center(46))
    print(f'{formatação.cor("verde")}={formatação.cor("fim")}' * 46)
else:
    print(f'{formatação.cor("vermelho")}=' * 46)
    print('VOCÊ PERDEU!!!'.center(46))
    print(f'{formatação.cor("vermelho")}={formatação.cor("fim")}' * 46)