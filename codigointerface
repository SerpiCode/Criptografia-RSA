import PySimpleGUI as sg
from projDire.func import *


lista_encript = []
lista_pure = []
msg_dscpt = []
chavePub = [0]
alfabeto = {
        'A': 2, 'B': 3, 'C': 4, 'D': 5,
        'E': 6, 'F': 7, 'G': 8, 'H': 9,
        'I': 10, 'J': 11, 'K': 12, 'L': 13,
        'M': 14, 'N': 15, 'O': 16, 'P': 17,
        'Q': 18, 'R': 19, 'S': 20, 'T': 21,
        'U': 22, 'V': 23, 'W': 24, 'X': 25,
        'Y': 26, 'Z': 27, ' ': 28
    }


# Definir janelas
def janela_inicio():
    sg.theme('Dark')
    layout = [
        [sg.Text('Criptografia RSA')],
        [sg.Button('Clique para começar')]
    ]
    return sg.Window('Início', layout=layout, finalize=True, element_justification='c')


def janela_escolher():
    sg.theme('Dark')
    layout = [
        [sg.Text('Escolha uma das três opções:\n1 - Gerar chave pública\n2 - Encriptar\n3 - Desencriptar\n')],
        [sg.Button('Opção 1'), sg.Button('Opção 2'), sg.Button('Opção 3')]
    ]
    return sg.Window('Escolha', layout=layout, finalize=True, element_justification='c')


def opcao1():
    sg.theme('Dark')
    layout = [
        [sg.Text('Digite um par de números primos \"p\" e \"q\":\n')],
        [sg.Text('Número P:'), sg.Input(key='numP', size=(10, 10)),
         sg.Text('Número Q:'), sg.Input(key='numQ', size=(10, 10))],
        [sg.Text('Agora, digite um expoente \"e\" relativamente primo a (p - 1)(q - 1):')],
        [sg.Input(key='numE', size=(10, 10))],
        [sg.Button('Confirmar')]
    ]
    return sg.Window('Opção Um', layout=layout, finalize=True, element_justification='c')


def opcao2():
    sg.theme('Dark')
    layout = [
        [sg.Text('Digite a mensagem que será encriptada: '), sg.Input(size=(10, 10), key='encript')],
        [sg.Text('Informe a chave pública obtida anteriormente:')],
        [sg.Text('N: '), sg.Input(size=(10, 10), key='n'), sg.Text('E: '), sg.Input(size=(10, 10), key='e')],
        [sg.Button('Confirmar')]
    ]
    return sg.Window('Opção Dois', layout=layout, finalize=True, element_justification='c')


def opcao3():
    sg.theme('Dark')
    layout = [
        [sg.Text('Digite um par de números primos \"p\" e \"q\":\n')],
        [sg.Text('Número P:'), sg.Input(key='numP', size=(10, 10)), sg.Text('Número Q:'),
         sg.Input(key='numQ', size=(10, 10))],
        [sg.Text('Agora, digite um expoente \"e\" relativamente primo a (p - 1)(q - 1):')],
        [sg.Input(key='numE', size=(10, 10))],
        [sg.Button('Confirmar')]
    ]
    return sg.Window('Opção 3', layout=layout, finalize=True, element_justification='c')


def pergunta():
    sg.theme('Dark')
    layout = [
        [sg.Text('Deseja realizar outra operação?')],
        [sg.Button('Sim'), sg.Button('Não')]
    ]
    return sg.Window('Finalizar', layout=layout, finalize=True, element_justification='c')


# Criar janela inicial:
inicio, escolher, opcaoum, opcaodois, perg, opcaotres = janela_inicio(), None, None, \
    None, None, None

# Criar loop de eventos:
while True:
    window, event, values = sg.read_all_windows()

    # Quando a janela for fechada
    if window == inicio and event == sg.WIN_CLOSED:
        break
    if window == escolher and event == sg.WIN_CLOSED:
        break
    if window == opcaoum and event == sg.WIN_CLOSED:
        break
    if window == perg and event == sg.WIN_CLOSED:
        break
    if window == opcaodois and event == sg.WIN_CLOSED:
        break
    if window == opcaotres and event == sg.WIN_CLOSED:
        break

    # Inicio
    if window == inicio and event == 'Clique para começar':
        escolher = janela_escolher()
        inicio.hide()

    # Opção 1:
    if window == escolher and event == 'Opção 1':
        opcaoum = opcao1()
        escolher.hide()
    if window == opcaoum:
        numP = int(values['numP'])
        numQ = int(values['numQ'])
        numE = int(values['numE'])
        calc = (numP - 1) * (numQ - 1)
        if conferirPrimalidade(numP) == 1 or conferirPrimalidade(numQ) == 1:
            sg.popup('O número que você digitou não é primo.')
        elif calcularMDC(numE, calc) != 1:
            sg.popup('O número que você digitou não é relativamente primo a (p - 1)*(q - 1)')
        else:
            n = numP * numQ
            chavePub = [n, numE]
            with open('chavePublica.txt', 'w') as f1:
                for valor in chavePub:
                    f1.write(str(valor) + '\n')
            sg.popup('Chave pública gerada com sucesso.')
            perg = pergunta()
            opcaoum.hide()

    # Opção 2:
    if window == escolher and event == 'Opção 2':
        opcaodois = opcao2()
        escolher.hide()
        if chavePub != [0]:
            sg.popup('Chave pública:\n\n' + 'N: ' + str(chavePub[0]) + '\nE: ' + str(chavePub[1]) + '\n')
        else:
            sg.popup('Nenhuma chave pública gerada até o momento.')
    if window == opcaodois:
        lista_cript = []
        lista_final = []
        mensagem = str(values['encript']).upper()
        numN = int(values['n'])
        numE = int(values['e'])
        for elemento in range(0, len(mensagem)):
            res = analyse(alfabeto, mensagem[elemento])
            lista_cript.append(res)
        for elemento in range(len(lista_cript)):
            calculo = pow(lista_cript[elemento], numE, numN)
            lista_final.append(calculo)
        with open('mensagem_encript.txt', 'w') as f2:
            for valor in lista_final:
                f2.write(str(valor) + '\n')
        sg.popup('Mensagem encriptada com sucesso.')
        perg = pergunta()
        opcaodois.hide()

    # Opção 3:
    if window == escolher and event == 'Opção 3':
        opcaotres = opcao3()
        escolher.hide()
    if window == opcaotres:
        with open('mensagem_encript.txt', 'r') as f3:
            for valor in f3:
                lista_encript.append(int(valor))
        numP = int(values['numP'])
        numQ = int(values['numQ'])
        numE = int(values['numE'])
        calc = (numP - 1)*(numQ - 1)
        if conferirPrimalidade(numP) == 1 or conferirPrimalidade(numQ) == 1:
            sg.popup('O número que você digitou não é primo.')
        elif calcularMDC(numE, calc) != 1:
            sg.popup('O número que você digitou não é relativamente primo a (p - 1)*(q - 1)')
        else:
            n = numP * numQ
            d = calcularInverso(numE, calc)
            for elemento in range(0, len(lista_encript)):
                calculo = pow(lista_encript[elemento], d, n)
                lista_pure.append(calculo)
            for elemento in lista_pure:
                res = get_key(elemento, alfabeto)
                msg_dscpt.append(res)
            with open('mensagem_desencript.txt', 'w') as f4:
                for valor in msg_dscpt:
                    f4.write(str(valor))
            sg.popup('Mensagem desencriptada com sucesso.')
            perg = pergunta()
            opcaotres.hide()
    
    # Quando queremos voltar pra janela anterior
    if window == perg and event == 'Sim':
        perg.hide()
        escolher.un_hide()
    elif window == perg and event == 'Não':
        break
