from executa_calculadora import executa_calculadora
from seleciona_operacao import seleciona_operacao

saida = ''
input_um = 0
input_dois = 0
operacao = ''

while saida != 'exit':
    (input_um, input_dois, operacao) = executa_calculadora(input_um, input_dois, operacao)

    if input_um == 'exit' or input_dois == 'exit' or operacao  == 'exit':
        saida = 'exit'
    if saida != 'exit':
        resultado = ''
        
        operacao_selecionada = seleciona_operacao(operacao)

        if callable(operacao_selecionada):
            resultado = operacao_selecionada(input_um, input_dois)
        else:
            print(operacao_selecionada)

        if resultado != '':
            print(f'O resultado da operação {operacao} é: {resultado}')