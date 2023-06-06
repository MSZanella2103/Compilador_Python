#Antes de executar o código veja o arquivo "readme.txt"

import ply.lex as lex #Biblioteca python que permite analise Léxica
from tabulate import tabulate #Biblioteca que mostrará a tabela para melhorar a visualização do resultado do código

#Lista global de armazenamento
saidas = []

#Padrão para adicionar os tokens que serão impressas pelo compilador
def add_lista_saida(t, erro):
    saidas.append((t.lineno, t.lexpos, t.type, t.value, erro))      
    return t

#Palavras reservadas do compilador python
reserved ={
    'and' : 'and',
    'array' : 'array',
    'begin' : 'begin',
    'boolean': 'boolean',
    'case': 'case',
    'const': 'const',
    'def': 'def',
    'div': 'div',
    'do': 'do',
    'downto': 'downto',
    'else': 'else',
    'end': 'end',
    'endwhile': 'endwhile',
    'endif': 'endif',
    'false': 'false',
    'for': 'for',
    'function': 'function',
    'if': 'if',
    'integer': 'integer',
    'mod': 'mod',
    'not': 'not',
    'of': 'of',
    'or': 'or',
    'print': 'print',
    'procedure': 'procedure',
    'program': 'program',
    'range': 'range',
    'repeat': 'repeat',
    'return': 'return',
    'then': 'then',
    'to': 'to',
    'true': 'true',
    'until': 'until',
    'var': 'var',
    'while': 'while',
    'write': 'write',
    'writeln': 'writeln',
}


#Lista para o nome dos tokens
tokens = [
    #Operadores de comando do código

    #Operadores matemáticos
    'op_mais', # "+"
    'op_menos', # "-"
    'op_vezes', # "*"
    'op_divide', # "/"
    'op_modulo', # "%"

    #Operadores de execução
    'op_dois_pontos', # ":"
    'op_ponto_virgula', # ";"
    'op_virgula', # ","
    'op_ponto', # "."

    #Operadores de impressão
    'op_aspas',    #""
    'op_comentario',   ##

    #Operadores de atribuição
    'op_negacao', # "~"
    'op_igual', # "="
    'op_somar', # "+="
    'op_diminuir', # "-="
    'op_multiplicar', # "*="
    'op_divisao', # "/="

    #Operadores relacionais
    'op_menorque', # "<"
    'op_maiorque', # ">"
    'op_menorigualque', # "<="
    'op_maiorigualque', # ">="
    'op_igualigual', # "=="
    'op_diferente', # "!="
    'op_e', # "&"
    'op_ou', # "|"

    #Operador e Prioridade
    'op_a_parenteses', # "("
    'op_f_parenteses', # ")"
    'op_a_colchete', # "["
    'op_f_colchete', # "]"
    'op_a_chave', # "{"
    'op_f_chave', # "}"

    #identificadores
    'int',
    'double',
    'string',
    'char',
    'variavel',

    'ignora', #Ignora quebras de linha e espaços em branco
    'variavel_mf', #Variável mal formada
    'numero_mf', #numero mal formado
    'string_mf', #string mal formada
] + list(reserved.values()) #Junta com palavras reservadas para verificação


# Ignora espacos em branco

def t_ignora(t):
    r'[ \t]+'
    pass

# Tokens simples

def t_op_mais(t):
    r'\+'
    return t

def t_op_menos(t):
    r'\-'
    return t

def t_op_vezes(t):
    r'\*'
    return t

def t_op_divide(t):
    r'\/'
    return t

def op_modulo(t):
    r'\%'
    return t

    #Operadores de execução
def t_op_dois_pontos(t):
    r'\:'
    return t

def t_op_ponto_virgula(t):
    r'\;'
    return t

def t_op_virgula(t):
    r'\,'
    
def t_op_ponto(t):
    r'\.'
    return t

def t_op_comentario(t):
    r'\#.*'
    return t
   
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_op_negacao(t):
    r'\~'
    return t

def t_op_igual(t):
    r'\='
    return t

def t_op_somar(t):
    r'\+='
    return t

def t_op_diminuir(t):
    r'\-='
    return t

def t_op_multiplicar(t):
    r'\*='
    return t

def t_op_divisao(t):
    r'\/='
    return t

def t_op_maiorque(t):
    r'\>'
    return t

def t_op_menorque(t):
    r'\<'
    return t

def t_op_menorigualque(t):
    r'\<\='
    return t

def t_op_maiorigualque(t):
    r'\>\='
    return t

def t_op_igualigual(t): 
    r'\=='
    return t

def t_op_diferente(t):
    r'\!\='
    return t

def t_op_e(t):
    r'\&'
    return t

def t_op_ou(t):
    r'\|'
    return t

def t_op_a_parenteses(t):
    r'\('
    return t

def t_op_f_parenteses(t):
    r'\)'
    return t

def t_op_a_colchete(t):
    r'\['
    return t
    
def t_op_f_colchete(t):
    r'\]'
    return t
    
def t_op_a_chave(t):
    r'\{'
    return t
    
def t_op_f_chave(t):
    r'\}'
    return t


#Tokens complexos

def t_string(t):
    r'("[^"]*")'
    return t

def t_string_mf(t):
    r'("[^"]*)'
    return t

def t_variavel_mf(t):
    r'([0-9]+[a-z]+)|([@!#$%&*]+[a-z]+|[a-z]+\.[0-9]+|[a-z]+[@!#$%&*]+)'
    return t

def t_numero_mf(t):
    r'([0-9]+\.[a-z]+[0-9]+)|([0-9]+\.[a-z]+)|([0-9]+\.[0-9]+[a-z]+)'
    return t

def t_int(t):
    r'\d+'
    max = (len(t.value)) #Definindo o valor maximo que o "int" suporta que é 255
    if (max > 255):
        return add_lista_saida(t, f"Tamanho do número maior que o suportado")
    else:
        t.value = int(t.value)
        return t
    
def t_double(t):
    r'([0-9]+\.[0-9]+)|([0-9]+\.[0-9]+)'
    return t

def t_variavel(t):
   r'[a-zA-Z]\w*'
   if t.value in reserved:
       t.type = reserved[t.value]
       return add_lista_saida(t, f"Palavra Reservada")
   else:
       return add_lista_saida(t, f"Nenhum")
   
#Regra de tratamento de erros
def t_error(t):
    return saidas.append((t.lineno, t.lexpos, 'invalido', t.value, 'caractere não reconhecido'))
    t.lexer.skip(1)

lexer = lex.lex()

# Função para analisar o código em um arquivo
def analyze_code(filename):
    with open(filename, 'r') as file:
        code = file.read()
        lexer.input(code)
        table = []
        headers = ["Line", "Position", "Token Type", "Value", "Error"]
        for tok in lexer:
            if tok.type in reserved.values():
              tok.type = "Palavra Reservada"  
            table.append([tok.lineno, tok.lexpos, tok.type, tok.value, ""])
        print(tabulate(table, headers, tablefmt="grid"))

analyze_code('exemplo.py')