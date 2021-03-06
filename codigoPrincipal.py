from projDire.func import *

chavePub = [0]
pergunta_loop = "S"
# Esse alfabeto é um dicionário (dicionário: funciona como um array, mas com detalhes a mais) que é usado pra criptografar/descriptografar mensagens.
alfabeto = {
        'A': 2, 'B': 3, 'C': 4, 'D': 5,
        'E': 6, 'F': 7, 'G': 8, 'H': 9,
        'I': 10, 'J': 11, 'K': 12, 'L': 13,
        'M': 14, 'N': 15, 'O': 16, 'P': 17,
        'Q': 18, 'R': 19, 'S': 20, 'T': 21,
        'U': 22, 'V': 23, 'W': 24, 'X': 25,
        'Y': 26, 'Z': 27, ' ': 28
    }

# loop pra executar as ações quantas vezes quiser.
while pergunta_loop == "S":
    pergunta = int(input("Escolha uma das três opções:\n1 - Gerar chave pública\n2 - Encriptar\n3 - Desencriptar\n"))
    if pergunta == 1:
        print("Digite um par de números primos \"p\" e \"q\":\n")
        p = int(input("Número p: "))
        if conferirPrimalidade(p) == 1:   # Se a função conferirPrimalidade retornar 1, o número não é primo.
            print("O número que você digitou não é primo.")
        else:
            q = int(input("Número q: "))
            if conferirPrimalidade(q) == 1:
                print("O número que você digitou não é primo.")
            else:
                e = int(input("Agora, digite um expoente \"e\" relativamente primo a (p - 1)(q - 1): "))
                calc = (p - 1)*(q - 1)
                if calcularMDC(e, calc) != 1:  # Caso o MDC entre esses dois números não for 1, não serão coprimos. A função calcularMDC confere isso.
                    print("O número que você digitou não é relativamente primo a (p - 1)(q - 1).")
                else:
                    n = p * q
                    chavePub = [n, e]
                    with open('chavePublica.txt', 'w') as arquivo:  # Esse último comando escreve a chave pública em um arquivo .txt que pode ser acessado pelo usuário.
                        for valor in chavePub:
                            arquivo.write(str(valor) + '\n')
                        print("Chave pública gerada com sucesso.\n")
        pergunta_loop = input("Digite \"S\" para realizar outra operação: ").upper()
    elif pergunta == 2:
        if chavePub != [0]:  # chavePub é uma lista que contém a chave pública. Se ela estiver vazia, nenhuma chave pública foi gerada.
            with open('chavePublica.txt', 'r') as arquivo:
                print("Chave pública:")
                for valor in chavePub:  # Ciclo for responsável por printar a chave pública, caso já tenha sido gerada.
                    if valor is not None:
                        print(valor)
        else:
            print("Nenhuma chave pública gerada até o momento.")

        lista_cript = []
        lista_final = []
        mensagem = input("Digite a mensagem de texto que será encriptada: ").upper()  # O comando .upper() garante que a mensagem digitada esteja toda em letras maiúsculas. Se caso a letra digitada for minúscula, ela é convertida pra maiúscula.
        print("Agora, digite a chave pública recebida anteriormente: ")
        n = int(input("n: "))
        e = int(input("e: "))
        for elemento in range(0, len(mensagem)):  # ciclo for responsável por transformar letras em números, por meio da função analyse. Após transformados, os números são adicionados a lista_cript.
            res = analyse(alfabeto, mensagem[elemento])
            lista_cript.append(res)
        for elemento in range(len(lista_cript)): # outro ciclo for responsável por realizar a operação de módulo, e adicionar os números encontrados a lista_final.
            calculo = pow(lista_cript[elemento], e, n)
            lista_final.append(calculo)
        with open('mensagem_encript.txt', 'w') as arquivo: # mensagem encriptada sendo escrita em um arquivo .txt.
            for valor in lista_final: 
                arquivo.write(str(valor) + ' ')
        print("Mensagem criptografada com sucesso.\n")
        pergunta_loop = input("Digite \"S\" para realizar outra operação: ").upper()
    elif pergunta == 3:
        lista_encript = []
        lista_pure = []
        msg_dscpt = []
        with open('mensagem_encript.txt', 'r') as f3:
                for valor in f3:
                        lista_encript.append(int(valor))
        print("\nDigite um par de números primos \"p\" e \"q\":\n")
        p = int(input("Número p: "))
        if conferirPrimalidade(p) == 1:
            print("O número que você digitou não é primo.")
        else:
            q = int(input("Número q: "))
            if conferirPrimalidade(q) == 1:
                print("O número que você digitou não é primo.")
            else:
                n = p * q
                e = int(input("Agora, digite um expoente \"e\" relativamente primo a (p - 1)(q - 1): "))
                calc = (p - 1) * (q - 1)
                if calcularMDC(e, calc) != 1:
                    print("O número que você digitou não é relativamente primo a (p - 1)(q - 1).")
                else:
                    d = calcularInverso(e, calc) # função que calcula o inverso.
                    for elemento in range(0, len(lista_encript)):
                        calculo = pow(lista_encript[elemento], d, n) # novamente, módulo sendo calculado.
                        lista_pure.append(calculo)
                    for elemento in lista_pure:
                        res = get_key(elemento, alfabeto) # ciclo for usando a função get_key para transformar os números obtidos em letras.
                        msg_dscpt.append(res)
                    with open('mensagem_desencript.txt', 'w') as arquivo: # mensagem desencriptada sendo escrita em um arquivo .txt.
                        for valor in msg_dscpt:
                            arquivo.write(str(valor))
                    print("Mensagem desencriptada com sucesso.")
                    pergunta_loop = input("\nDigite \"S\" para realizar outra operação: ").upper()
