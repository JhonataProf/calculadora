def recebe_numero(message: str):
    input_var = input(message)
    input_var = float(input_var) if input_var != 'exit' else input_var
    return input_var
