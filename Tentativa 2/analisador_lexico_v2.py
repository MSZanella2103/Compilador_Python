import ply.lex as lex
import ply.yacc as yacc

# Tokens
tokens = (
    'VARIABLE',
    'NUMBER',
    'RESERVED',
    'SYMBOL',
)

# Regular expressions for tokens
t_VARIABLE = r'[a-zA-Z]\w*'
t_NUMBER = r'\d+(\.\d+)?'
t_RESERVED = r'program|var|begin|end|if|then|else|while|do|match|appened|writeln|elif'
t_SYMBOL = r'\+|\-|\*|/|\(|\)|\{|\}|\;|\=|\<\>|\<|\>|\<=|\>=|\:=|\+=|=-|:|"|.'

# Ignored characters
t_ignore = ' \t'

# Error handling
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Caractere inválido: {t.value[0]}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Parsing rules
def p_program(p):
    '''program : RESERVED VARIABLE RESERVED statements RESERVED'''
    print("Código compilado com sucesso.")

def p_statements(p):
    '''statements : statements statement
                  | statement'''
    pass

def p_statement(p):
    '''statement : RESERVED variables ';'
                 | RESERVED
                 | error'''
    pass

def p_variables(p):
    '''variables : variables ',' VARIABLE
                 | VARIABLE'''
    pass

def p_error(p):
    if p:
        print(f"Erro de sintaxe: token inesperado '{p.value}'")
    else:
        print("Erro de sintaxe: fim inesperado do código")

# Build the parser
parser = yacc.yacc()

def read_code_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    code = ''.join(lines)
    return code

def main():
    filename = input("Digite o nome do arquivo: ")

    try:
        code = read_code_from_file(filename)
        lexer.input(code)
        parser.parse(code)
    except FileNotFoundError:
        print("Arquivo não encontrado.")

if __name__ == "__main__":
    main()