
def parser():
    global position
    position = 0

    try:
        while position < len(tokens) and tokens[position][0] != 'end':
            statement()

        match('end')
        match('.')
        print('Código compilado com sucesso.')
    except SyntaxError as e:
        print('Erro de sintaxe:', e)

def statement():
    if tokens[position][0] == 'var':
        match('var')
        match(':')
        match('Tipo de variavel')
        match(';')
    else:
        raise SyntaxError('Comando inválido')
