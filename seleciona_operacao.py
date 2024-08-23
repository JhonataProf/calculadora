from operacoes import soma, subtrair, dividir, multiplicar

def seleciona_operacao(operacao):
    if operacao == '+':
        return soma
    elif operacao == '-':
        return subtrair
    elif operacao == '/':
        return dividir
    elif operacao == '*':
        return multiplicar
    else:
        return 'Operação não permitida'
