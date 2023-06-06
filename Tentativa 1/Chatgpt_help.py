import re

letters = (r'[a-zA-Z]\w*', 'variavel')
number = (r'\d+(\.\d+)?', 'numero')

palavras_reservadas = ["program", "var", "begin", "end", "if", "then", "else", "while", "do", "match", "appened"]

simbolos = ['+', '-', '*', '/', '(', ')', '{', '}', ';', '=', '<>', '<', '>', '<=', '>=', ':=', '+=', '-=']

def parser(code):
    tokens = []
    position = 0
    tam_codigo = len(code)

    while position < tam_codigo:
        if code[position].isspace():
            position += 1
            continue

        if re.match(number[0], code[position:]):
            match = re.match(number[0], code[position:])
            number_value = match.group()
            tokens.append((number[1], number_value))
            position += len(number_value)
            continue

        if re.match(letters[0], code[position:]):
            match = re.match(letters[0], code[position:])
            identifier = match.group()
            if identifier in palavras_reservadas:
                tokens.append(('Palavra reservada', identifier))
            else:
                tokens.append(('Identificador', identifier))
            position += len(identifier)
            continue

        if code[position] in simbolos:
            tokens.append(('Simbolo', code[position]))
            position += 1
            continue

        print('Erro léxico: caractere desconhecido', code[position])
        position += 1

    return tokens