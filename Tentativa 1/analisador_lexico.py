#re = Regular Expression
import re

# [a-zA-Z] = Entende todas as letras do afabeto, sendo maiusculas ou minusculas
# \w" = A gramatica pode ser seguida desde 0 a mais caracteres, também para caracteres alfanuméricos
letters = (r'[a-zA-Z]\w*', 'variavel')

tipo_variaveis = ["integer", "int", "char", "double", "float", "string"]

# d+ = Representa 1 ou mais digitos
# \. = Corresponde ao ponto ("."), que é usado para transformar o número em decimal, se colocar (",") dará erro
# ? = tanto o ".", tanto "d+" são opcionais, ou seja, números decimais são opcionais
number = (r'\d+(\.\d+)?', 'numero')

# Palavras reservadas que possuem um comando especifico no código e não podem ser colocadas como variaveis
palavras_reservadas = ["program", "var", "begin", "end", "if", "then", "else", "while", "do", "match", "appened", "writeln", "elif"]

# Simbolos que se usa no código para saberação, identação ou fator matemático
simbolos = ['+', '-', '*', '/', '(', ')', '{', '}', ';', '=', '<>', '<', '>', '<=', '>=', ':=', '+=', '=-', ':']


def match(token_type):
    if position < len(tokens) and tokens[position][0] == token_type:
        return tokens[position]
    else:
        raise SyntaxError('Erro sintático: esperado ' + token_type)

def parser():
    global position
    position = 0

    try:
        match('program')
        match('var')
        match(';')
        match('begin')

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

def tokenize(code):
    tokens = []
    position = 0
    code_length = len(code)

    while position < code_length:
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
            elif identifier in tipo_variaveis:
                tokens.append(('Tipo de variavel', identifier))
            else:
                tokens.append(('Identificador', identifier))
            position += len(identifier)
            continue

        if code[position] in simbolos:
            tokens.append(('Simbolo', code[position]))
            position += 1
            continue

        position += 1

    return tokens

# Input que o usuário coloca o nome do arquivo
nome_arquivo = input("Digite o nome do arquivo: ")

try:
    # Abre o arquivo para leitura
    with open(nome_arquivo, 'r') as arquivo:
        codigo = arquivo.read()
        tokens = tokenize(codigo)
        parser()

except FileNotFoundError:
    print("Arquivo não encontrado.")