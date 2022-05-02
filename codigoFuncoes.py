# Como vocês não estão familiarizados com python, vou explicar o que acontece nessa função. A variável count é um contador que varia de 2 a num-1, sendo num 
# o número informado pelo usuário. Se em algum momento a função conseguir dividir o número pelo contador, é retornado 1 e o número não é primo. Caso não, é retornado 9 e o número é primo.

def conferirPrimalidade(num): # Função que confere se o número recebido é primo.
    valor = 0
    for count in range(2, num-1):
        if num % count == 0:
            valor = 1
    return valor

def calcularMDC(num1, num2): # Função que calcula o MDC entre dois números.
    while num2 != 0:
        resto = num1 % num2
        num1 = num2
        num2 = resto
    return num1

# Função que transforma letras em números. Essa função e analyse funcionam de forma quase idêntica. O que acontece aqui, basicamente, é que um ciclo
# for é criado, com duas variáveis (key, value) que funcionam como um índice para, respectivamente, a chave do objeto e seus dados. Nesse caso, caso a chave 
# for igual a letra que o usuário informou (as chaves e seus valores estão todos contidos no dicionário alfabeto) a função retorna o número que corresponde a letra digitada.

def analyse(alfabeto, val): 
    for key, value in alfabeto.items(): 
         if key == val:
             return value

# Aqui o processo é o mesmo, mas ao invés de analisar a chave e retornar o valor, ele analisa o valor e retorna a chave.

def get_key(val, alfabeto): # Função que transforma números em letras.
    for key, value in alfabeto.items():
         if val == value:
             return key

# Esse pow sinceramente não sei explicar muito bem, mas basicamente a função calcula o num1 elevado ao expoente (nesse caso, -1) e divide por num2. É obtido um resto, que é retornado como o inverso.

def calcularInverso(num1, num2): # Função que calcula o inverso.
    res = pow(num1, -1, num2)
    return res
