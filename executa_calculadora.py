from recebe_numero import recebe_numero

def executa_calculadora(input_um, input_dois, operacao):
    input_um = recebe_numero('Digite um valor para a operação Matemática: \n')
    if input_um == 'exit':
        return input_um, input_dois, operacao
    
    input_dois = recebe_numero('Digite um valor para a operação Matemática: \n')
    if input_dois == 'exit':
        return input_um, input_dois, operacao
    
    operacao = input(f'Digite o simbolo da operação Matemática para os valores: \n {input_um} \n {input_dois} \n')
    if operacao == 'exit':
        return input_um, input_dois, operacao
    return input_um, input_dois, operacao
