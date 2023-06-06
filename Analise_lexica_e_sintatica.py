#Antes de executar o código veja o arquivo "readme.txt"

import ply.lex as lex #Biblioteca que permite análise Léxica
import ply.yacc as yacc #Bibliota que  permite a análise sintatica
from tabulate import tabulate #Biblioteca que mostrará a tabela para melhorar a visualização do resultado do código

#Lista global de armazenamento
saidas = []

#       ANALISE LÉXICA   #

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
    'procedure': 'procedure',
    'program': 'program',
    'print': 'print',
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

    #Operador eridade
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
    #Operadores de calculo matemático
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
   
def reserved(t):
    r'reserved.values'
    return t
   
#Regra de tratamento de erros
def t_error(t):
    return saidas.append((t.lineno, t.lexpos, 'invalido', t.value, 'caractere não reconhecido'))
    t.lexer.skip(1)


#        ANALISE SINTÁTICA      #

def p_statements_multiple(p):
    '''
    statements : statements statement
    '''

def p_statements_single(p):
    '''
    statements : statement
    '''

def p_statement_comentarios(p):
    '''
    statement : op_comentario
    '''

#def p_statement_ifsuldeminas(p):
#    '''
#    statement : IFSULDEMINAS OP_FINALLINHA
#    '''

def p_statement_while(p):
    '''
    statement : while op_a_parenteses cond_param op_f_parenteses op_a_chaves statements op_f_chaves
    '''

def p_statement_para(p):
    '''
    statement : for op_a_parenteses var op_igual int op_virgula cond_param op_virgula var op_igual var op_mais int  op_f_parenteses op_a_chave statements op_f_chave
              | for op_a_parenteses reserved op_igual int op_virgula cond_param op_virgula var op_igual var op_mais int  op_f_parenteses op_a_chave statements op_f_chave
              | for op_a_parenteses var op_igual int op_virgula cond_param op_virgula reserved op_igual var op_mais int  op_f_parenteses op_a_chave statements op_f_chave
              | for op_a_parenteses var op_igual int op_virgula cond_param op_virgula var op_igual reserved op_mais int  op_f_parenteses op_a_chave statements op_f_chave
              | for op_a_parenteses reserved op_igual int op_virgula cond_param op_virgula reserved op_igual var op_mais int  op_f_parenteses op_a_chave statements op_f_chave
              | for op_a_parenteses var op_igual int op_virgula cond_param op_virgula reserved op_igual reserved op_mais int  op_f_parenteses op_a_chave statements op_f_chave
              | for op_a_parenteses reserved op_igual int op_virgula cond_param op_virgula var op_igual reserved op_mais int  op_f_parenteses op_a_chave statements op_f_chave
              | for op_a_parenteses reserved op_igual int op_virgula cond_param op_virgula reserved op_igual reserved op_mais int  op_f_parenteses op_a_chave statements op_f_chave

              | for op_a_parenteses var op_igual var op_virgula cond_param op_virgula var op_igual var op_mais int  op_f_parenteses op_a_chave statements op_f_chave
              | for op_a_parenteses reserved op_igual var op_virgula cond_param op_virgula var op_igual var op_mais int  op_f_parenteses op_a_chave statements op_f_chave
              | for op_a_parenteses var op_igual reserved op_virgula cond_param op_virgula var op_igual var op_mais int  op_f_parenteses op_a_chave statements op_f_chave
              | for op_a_parenteses var op_igual var op_virgula cond_param op_virgula reserved op_igual var op_mais int  op_f_parenteses op_a_chave statements op_f_chave
              | for op_a_parenteses var op_igual var op_virgula cond_param op_virgula var op_igual reserved op_mais int  op_f_parenteses op_a_chave statements op_f_chave
              | for op_a_parenteses reserved op_igual reserved op_virgula cond_param op_virgula var op_igual var op_mais int  op_f_parenteses op_a_chave statements op_f_chave
              | for op_a_parenteses reserved op_igual var op_virgula cond_param op_virgula reserved op_igual var op_mais int  op_f_parenteses op_a_chave statements op_f_chave
              | for op_a_parenteses reserved op_igual var op_virgula cond_param op_virgula var op_igual reserved op_mais int  op_f_parenteses op_a_chave statements op_f_chave
              | for op_a_parenteses var op_igual reserved op_virgula cond_param op_virgula reserved op_igual var op_mais int  op_f_parenteses op_a_chave statements op_f_chave
              | for op_a_parenteses var op_igual reserved op_virgula cond_param op_virgula var op_igual reserved op_mais int  op_f_parenteses op_a_chave statements op_f_chave
              | for op_a_parenteses var op_igual var op_virgula cond_param op_virgula reserved op_igual reserved op_mais int  op_f_parenteses op_a_chave statements op_f_chave
              | for op_a_parenteses reserved op_igual reserved op_virgula cond_param op_virgula reserved op_igual reserved op_mais int  op_f_parenteses op_a_chave statements op_f_chave

              | for op_a_parenteses var cond_param op_virgula var op_igual var op_mais int  op_f_parenteses op_a_chave statements op_f_chave
              | for op_a_parenteses reserved cond_param op_virgula var op_igual var op_mais int  op_f_parenteses op_a_chave statements op_f_chave
              | for op_a_parenteses var cond_param op_virgula reserved op_igual var op_mais int  op_f_parenteses op_a_chave statements op_f_chave
              | for op_a_parenteses var cond_param op_virgula var op_igual reserved op_mais int  op_f_parenteses op_a_chave statements op_f_chave
              | for op_a_parenteses reserved cond_param op_virgula reserved op_igual var op_mais int  op_f_parenteses op_a_chave statements op_f_chave
              | for op_a_parenteses reserved cond_param op_virgula var op_igual reserved op_mais int  op_f_parenteses op_a_chave statements op_f_chave
              | for op_a_parenteses var cond_param op_virgula reserved op_igual reserved op_mais int  op_f_parenteses op_a_chave statements op_f_chave
              | for op_a_parenteses reserved cond_param op_virgula reserved op_igual reserved op_mais int  op_f_parenteses op_a_chave statements op_f_chave
    '''

def p_statement_atribuicaoValorVariavel(p):
    '''
    statement : var op_igual expr
            | var op_igual string
            | var op_igual var
            | var op_igual reserved
            | var op_igual int
            | var op_igual double
            | var op_igual CHAR
            | var op_igual funcao
            | var op_somar int
            | var op_somar double
            | var op_somar var
            | var op_somar reserved
            | var op_diminuir int
            | var op_diminuir double
            | var op_diminuir var
            | var op_diminuir reserved
            | reserved op_igual expr
            | reserved op_igual string
            | reserved op_igual var
            | reserved op_igual reserved
            | reserved op_igual int
            | reserved op_igual double
            | reserved op_igual CHAR
            | reserved op_igual funcao
            | reserved op_somar int
            | reserved op_somar double
            | reserved op_somar var
            | reserved op_somar reserved
            | reserved op_diminuir int
            | reserved op_diminuir double
            | reserved op_diminuir var
            | reserved op_diminuir reserved
    '''

def p_statement_condicionais(p):
    '''
    statement : if op_a_parenteses cond_param op_f_parenteses op_a_chave statements op_f_chave
            | if op_a_parenteses cond_param op_f_parenteses op_a_chave statements op_f_chave senaose
            | if op_a_parenteses cond_param op_f_parenteses op_a_chave statements op_f_chave senaose else op_a_chave statements op_f_chave
            | if op_a_parenteses cond_param op_f_parenteses op_a_chave statements op_f_chave else op_a_chave statements op_f_chave
    '''

#def p_statement_funcao_invocada(p):
#    '''
#    statement : funcao OP_FINALLINHA
#    '''

def p_statement_definir_funcao(p):
    '''
    statement : funcao op_a_chave statements op_f_chave
    '''

def p_parametro_condicional(p):
    '''
    cond_param :  var op_menorque int
                | var op_menorque double
                | var op_menorque var
                | var op_menorque reserved

                | reserved op_menorque int
                | reserved op_menorque double
                | reserved op_menorque var
                | reserved op_menorque reserved

                | var op_maiorque int
                | var op_maiorque double
                | var op_maiorque var
                | var op_maiorque reserved

                | reserved op_maiorque int
                | reserved op_maiorque double
                | reserved op_maiorque var
                | reserved op_maiorque reserved

                | var op_menorigualque int
                | var op_menorigualque double
                | var op_menorigualque var
                | var op_menorigualque reserved

                | reserved op_menorigualque int
                | reserved op_menorigualque double
                | reserved op_menorigualque var
                | reserved op_menorigualque reserved

                | var op_maiorigualque int
                | var op_maiorigualque double
                | var op_maiorigualque var
                | var op_maiorigualque reserved

                | reserved op_maiorigualque int
                | reserved op_maiorigualque double
                | reserved op_maiorigualque var
                | reserved op_maiorigualque reserved

                | var op_igualigual int
                | var op_igualigual double
                | var op_igualigual var
                | var op_igualigual reserved

                | reserved op_igualigual int
                | reserved op_igualigual double
                | reserved op_igualigual var
                | reserved op_igualigual reserved

                | var op_diferente int
                | var op_diferente double
                | var op_diferente var
                | var op_diferente reserved

                | reserved op_diferente int
                | reserved op_diferente double
                | reserved op_diferente var
                | reserved op_diferente reserved

                | var op_e int
                | var op_e double
                | var op_e var
                | var op_e reserved

                | reserved op_e int
                | reserved op_e double
                | reserved op_e var
                | reserved op_e reserved

                | varop_ou int
                | varop_ou double
                | varop_ou var
                | varop_ou reserved

                | reservedop_ou int
                | reservedop_ou double
                | reservedop_ou var
                | reservedop_ou reserved

    '''

#def p_reserv(p):
#    '''reserv : MOVER
#               | MOVER_DIREITA
#               | MOVER_ESQUERDA
#               | MOVER_CIMA
#               | MOVER_BAIXO
#               | POSICAO_COBRA
#               | POSICAO_ALIMENTO
#               | PONTUACAO
#               '''

#def p_aux(p):
#    'aux : AUX'

def p_impressao(p):
    '''impressao : print'''

def p_true_false(p):
    '''true_false : true
                   | false
                   '''

def p_parametros_condicionais_grupo(p):
    '''
    cond_param : cond_param op_e cond_param
              | cond_param op_ou cond_param
    '''

def p_expressao_numero(p):
    '''
    expr : int
        | double
    '''

def p_expressao_variavel(p):
    '''
    expr : var
          | reserved
    '''

def p_expressao_operacao(p):
    '''
    expr : expr op_mais expr
        |  expr op_menos expr
        |  expr op_vezes expr
        |  expr op_divide expr
        |  expr op_modulo expr
    '''

def p_expressao_grupo(p):
    '''
    expr : op_a_parenteses expr op_f_parenteses
    '''

def p_parametro_vazio(p):
    '''
    param_vazio :
    '''

def p_parametro(p):
    '''
    param : int
        | double
        | string
        | char
        | var
        | reserved
    '''

def p_parametro_grupo(p):
    '''
    param : param op_virgula param
    '''

def p_regra_funcao(p):
    '''
    funcao :  op_a_parenteses param_vazio op_f_parenteses
        |  op_a_parenteses param op_f_parenteses
    '''

def p_senao_se(p):
    '''
    senaose : elif op_a_parenteses cond_param op_f_parenteses op_a_parenteses statements op_f_parenteses
    '''

def p_senao_se_grupo(p):
    '''
    senaose : senaose senaose
            | senaose
    '''


#       APRESENTAÇÃO NO TERMINAL O RESULTADO DA ANALISE       #

# Constrói o analisador sintático
parser = yacc.yacc()

# Função para analisar o código em um arquivo
def analyze_code(filename):
    with open(filename, 'r') as file:
        code = file.read()
        lexer = lex.lex()
        lexer.input(code)
        table = []
        headers = ["Line", "Position", "Token Type", "Value", "Error"]
        for tok in lexer:
            if tok.type in reserved.values():
                tok.type = "Palavra Reservada"
            table.append([tok.lineno, tok.lexpos, tok.type, tok.value, ""])
        print(tabulate(table, headers, tablefmt="grid"))
        parser.parse(code)

analyze_code('exemplo.py')