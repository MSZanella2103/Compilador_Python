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
    statement : WHILE op_a_parenteses cond_param op_f_parenteses op_a_chaves statements op_f_chaves
    '''

def p_statement_para(p):
    '''
    statement : for op_a_parenteses variavel op_igual int op_virgula cond_param op_virgula variavel op_igual variavel op_mais int  op_f_parenteses op_a_chave statements op_f_chave
              | for op_a_parenteses reserv op_igual int op_virgula cond_param op_virgula variavel op_igual variavel op_mais int  op_f_parenteses op_a_chave statements op_f_chave
              | for op_a_parenteses variavel op_igual int op_virgula cond_param op_virgula reserv op_igual variavel op_mais int  op_f_parenteses op_a_chave statements op_f_chave
              | for op_a_parenteses variavel op_igual int op_virgula cond_param op_virgula variavel op_igual reserv op_mais int  op_f_parenteses op_a_chave statements op_f_chave
              | for op_a_parenteses reserv op_igual int op_virgula cond_param op_virgula reserv op_igual variavel op_mais int  op_f_parenteses op_a_chave statements op_f_chave
              | for op_a_parenteses variavel op_igual int op_virgula cond_param op_virgula reserv op_igual reserv op_mais int  op_f_parenteses op_a_chave statements op_f_chave
              | for op_a_parenteses reserv op_igual int op_virgula cond_param op_virgula variavel op_igual reserv op_mais int  op_f_parenteses op_a_chave statements op_f_chave
              | for op_a_parenteses reserv op_igual int op_virgula cond_param op_virgula reserv op_igual reserv op_mais int  op_f_parenteses op_a_chave statements op_f_chave

              | for op_a_parenteses variavel op_igual variavel op_virgula cond_param op_virgula variavel op_igual variavel op_mais int  op_f_parenteses op_a_chave statements op_f_chave
              | for op_a_parenteses reserv op_igual variavel op_virgula cond_param op_virgula variavel op_igual variavel op_mais int  op_f_parenteses op_a_chave statements op_f_chave
              | for op_a_parenteses variavel op_igual reserv op_virgula cond_param op_virgula variavel op_igual variavel op_mais int  op_f_parenteses op_a_chave statements op_f_chave
              | for op_a_parenteses variavel op_igual variavel op_virgula cond_param op_virgula reserv op_igual variavel op_mais int  op_f_parenteses op_a_chave statements op_f_chave
              | for op_a_parenteses variavel op_igual variavel op_virgula cond_param op_virgula variavel op_igual reserv op_mais int  op_f_parenteses op_a_chave statements op_f_chave
              | for op_a_parenteses reserv op_igual reserv op_virgula cond_param op_virgula variavel op_igual variavel op_mais int  op_f_parenteses op_a_chave statements op_f_chave
              | for op_a_parenteses reserv op_igual variavel op_virgula cond_param op_virgula reserv op_igual variavel op_mais int  op_f_parenteses op_a_chave statements op_f_chave
              | for op_a_parenteses reserv op_igual variavel op_virgula cond_param op_virgula variavel op_igual reserv op_mais int  op_f_parenteses op_a_chave statements op_f_chave
              | for op_a_parenteses variavel op_igual reserv op_virgula cond_param op_virgula reserv op_igual variavel op_mais int  op_f_parenteses op_a_chave statements op_f_chave
              | for op_a_parenteses variavel op_igual reserv op_virgula cond_param op_virgula variavel op_igual reserv op_mais int  op_f_parenteses op_a_chave statements op_f_chave
              | for op_a_parenteses variavel op_igual variavel op_virgula cond_param op_virgula reserv op_igual reserv op_mais int  op_f_parenteses op_a_chave statements op_f_chave
              | for op_a_parenteses reserv op_igual reserv op_virgula cond_param op_virgula reserv op_igual reserv op_mais int  op_f_parenteses op_a_chave statements op_f_chave

              | for op_a_parenteses variavel cond_param op_virgula variavel op_igual variavel op_mais int  op_f_parenteses op_a_chave statements op_f_chave
              | for op_a_parenteses reserv cond_param op_virgula variavel op_igual variavel op_mais int  op_f_parenteses op_a_chave statements op_f_chave
              | for op_a_parenteses variavel cond_param op_virgula reserv op_igual variavel op_mais int  op_f_parenteses op_a_chave statements op_f_chave
              | for op_a_parenteses variavel cond_param op_virgula variavel op_igual reserv op_mais int  op_f_parenteses op_a_chave statements op_f_chave
              | for op_a_parenteses reserv cond_param op_virgula reserv op_igual variavel op_mais int  op_f_parenteses op_a_chave statements op_f_chave
              | for op_a_parenteses reserv cond_param op_virgula variavel op_igual reserv op_mais int  op_f_parenteses op_a_chave statements op_f_chave
              | for op_a_parenteses variavel cond_param op_virgula reserv op_igual reserv op_mais int  op_f_parenteses op_a_chave statements op_f_chave
              | for op_a_parenteses reserv cond_param op_virgula reserv op_igual reserv op_mais int  op_f_parenteses op_a_chave statements op_f_chave
    '''

def p_statement_atribuicaoValorVariavel(p):
    '''
    statement : VARIAVEL OP_ATRIB_IGUAL expr OP_FINALLINHA
            | VARIAVEL OP_ATRIB_IGUAL STRING OP_FINALLINHA
            | VARIAVEL OP_ATRIB_IGUAL VARIAVEL OP_FINALLINHA
            | VARIAVEL OP_ATRIB_IGUAL reserv OP_FINALLINHA
            | VARIAVEL OP_ATRIB_IGUAL INTEIRO OP_FINALLINHA
            | VARIAVEL OP_ATRIB_IGUAL DOUBLE OP_FINALLINHA
            | VARIAVEL OP_ATRIB_IGUAL CHAR OP_FINALLINHA
            | VARIAVEL OP_ATRIB_IGUAL funcao OP_FINALLINHA
            | VARIAVEL OP_ATRIB_MAIS_IGUAL INTEIRO
            | VARIAVEL OP_ATRIB_MAIS_IGUAL DOUBLE
            | VARIAVEL OP_ATRIB_MAIS_IGUAL VARIAVEL
            | VARIAVEL OP_ATRIB_MAIS_IGUAL reserv
            | VARIAVEL OP_ATRIB_MENOS_IGUAL INTEIRO
            | VARIAVEL OP_ATRIB_MENOS_IGUAL DOUBLE
            | VARIAVEL OP_ATRIB_MENOS_IGUAL VARIAVEL
            | VARIAVEL OP_ATRIB_MENOS_IGUAL reserv
            | reserv OP_ATRIB_IGUAL expr OP_FINALLINHA
            | reserv OP_ATRIB_IGUAL STRING OP_FINALLINHA
            | reserv OP_ATRIB_IGUAL VARIAVEL OP_FINALLINHA
            | reserv OP_ATRIB_IGUAL reserv OP_FINALLINHA
            | reserv OP_ATRIB_IGUAL INTEIRO OP_FINALLINHA
            | reserv OP_ATRIB_IGUAL DOUBLE OP_FINALLINHA
            | reserv OP_ATRIB_IGUAL CHAR OP_FINALLINHA
            | reserv OP_ATRIB_IGUAL funcao OP_FINALLINHA
            | reserv OP_ATRIB_MAIS_IGUAL INTEIRO
            | reserv OP_ATRIB_MAIS_IGUAL DOUBLE
            | reserv OP_ATRIB_MAIS_IGUAL VARIAVEL
            | reserv OP_ATRIB_MAIS_IGUAL reserv
            | reserv OP_ATRIB_MENOS_IGUAL INTEIRO
            | reserv OP_ATRIB_MENOS_IGUAL DOUBLE
            | reserv OP_ATRIB_MENOS_IGUAL VARIAVEL
            | reserv OP_ATRIB_MENOS_IGUAL reserv
    '''

def p_statement_condicionais(p):
    '''
    statement : IF OP_ABRE_PARENTESES cond_param OP_FECHA_PARENTESES OP_ABRE_CHAVES statements OP_FECHA_CHAVES
            | IF OP_ABRE_PARENTESES cond_param OP_FECHA_PARENTESES OP_ABRE_CHAVES statements OP_FECHA_CHAVES senaose
            | IF OP_ABRE_PARENTESES cond_param OP_FECHA_PARENTESES OP_ABRE_CHAVES statements OP_FECHA_CHAVES senaose ELSE OP_ABRE_CHAVES statements OP_FECHA_CHAVES
            | IF OP_ABRE_PARENTESES cond_param OP_FECHA_PARENTESES OP_ABRE_CHAVES statements OP_FECHA_CHAVES ELSE OP_ABRE_CHAVES statements OP_FECHA_CHAVES
    '''

def p_statement_funcao_invocada(p):
    '''
    statement : funcao OP_FINALLINHA
    '''

def p_statement_definir_funcao(p):
    '''
    statement : funcao OP_ABRE_CHAVES statements OP_FECHA_CHAVES
    '''

def p_parametro_condicional(p):
    '''
    cond_param :  VARIAVEL OP_REL_MENOR INTEIRO
                | VARIAVEL OP_REL_MENOR DOUBLE
                | VARIAVEL OP_REL_MENOR VARIAVEL
                | VARIAVEL OP_REL_MENOR reserv

                | reserv OP_REL_MENOR INTEIRO
                | reserv OP_REL_MENOR DOUBLE
                | reserv OP_REL_MENOR VARIAVEL
                | reserv OP_REL_MENOR reserv

                | VARIAVEL OP_REL_MAIOR INTEIRO
                | VARIAVEL OP_REL_MAIOR DOUBLE
                | VARIAVEL OP_REL_MAIOR VARIAVEL
                | VARIAVEL OP_REL_MAIOR reserv

                | reserv OP_REL_MAIOR INTEIRO
                | reserv OP_REL_MAIOR DOUBLE
                | reserv OP_REL_MAIOR VARIAVEL
                | reserv OP_REL_MAIOR reserv

                | VARIAVEL OP_REL_MENOR_IGUAL INTEIRO
                | VARIAVEL OP_REL_MENOR_IGUAL DOUBLE
                | VARIAVEL OP_REL_MENOR_IGUAL VARIAVEL
                | VARIAVEL OP_REL_MENOR_IGUAL reserv

                | reserv OP_REL_MENOR_IGUAL INTEIRO
                | reserv OP_REL_MENOR_IGUAL DOUBLE
                | reserv OP_REL_MENOR_IGUAL VARIAVEL
                | reserv OP_REL_MENOR_IGUAL reserv

                | VARIAVEL OP_REL_MAIOR_IGUAL INTEIRO
                | VARIAVEL OP_REL_MAIOR_IGUAL DOUBLE
                | VARIAVEL OP_REL_MAIOR_IGUAL VARIAVEL
                | VARIAVEL OP_REL_MAIOR_IGUAL reserv

                | reserv OP_REL_MAIOR_IGUAL INTEIRO
                | reserv OP_REL_MAIOR_IGUAL DOUBLE
                | reserv OP_REL_MAIOR_IGUAL VARIAVEL
                | reserv OP_REL_MAIOR_IGUAL reserv

                | VARIAVEL OP_REL_DUPLO_IGUAL INTEIRO
                | VARIAVEL OP_REL_DUPLO_IGUAL DOUBLE
                | VARIAVEL OP_REL_DUPLO_IGUAL VARIAVEL
                | VARIAVEL OP_REL_DUPLO_IGUAL reserv

                | reserv OP_REL_DUPLO_IGUAL INTEIRO
                | reserv OP_REL_DUPLO_IGUAL DOUBLE
                | reserv OP_REL_DUPLO_IGUAL VARIAVEL
                | reserv OP_REL_DUPLO_IGUAL reserv

                | VARIAVEL OP_REL_DIFERENTE INTEIRO
                | VARIAVEL OP_REL_DIFERENTE DOUBLE
                | VARIAVEL OP_REL_DIFERENTE VARIAVEL
                | VARIAVEL OP_REL_DIFERENTE reserv

                | reserv OP_REL_DIFERENTE INTEIRO
                | reserv OP_REL_DIFERENTE DOUBLE
                | reserv OP_REL_DIFERENTE VARIAVEL
                | reserv OP_REL_DIFERENTE reserv

                | VARIAVEL OP_REL_E INTEIRO
                | VARIAVEL OP_REL_E DOUBLE
                | VARIAVEL OP_REL_E VARIAVEL
                | VARIAVEL OP_REL_E reserv

                | reserv OP_REL_E INTEIRO
                | reserv OP_REL_E DOUBLE
                | reserv OP_REL_E VARIAVEL
                | reserv OP_REL_E reserv

                | VARIAVEL OP_REL_OU INTEIRO
                | VARIAVEL OP_REL_OU DOUBLE
                | VARIAVEL OP_REL_OU VARIAVEL
                | VARIAVEL OP_REL_OU reserv

                | reserv OP_REL_OU INTEIRO
                | reserv OP_REL_OU DOUBLE
                | reserv OP_REL_OU VARIAVEL
                | reserv OP_REL_OU reserv

    '''

def p_reserv(p):
    '''reserv : MOVER
               | MOVER_DIREITA
               | MOVER_ESQUERDA
               | MOVER_CIMA
               | MOVER_BAIXO
               | POSICAO_COBRA
               | POSICAO_ALIMENTO
               | PONTUACAO
               '''

def p_aux(p):
    'aux : AUX'

def p_impressao(p):
    '''impressao : PRINTF
                  | IMP'''

def p_true_false(p):
    '''true_false : TRUE
                   | FALSE
                   '''

def p_parametros_condicionais_grupo(p):
    '''
    cond_param : cond_param OP_REL_E cond_param
              | cond_param OP_REL_OU cond_param
    '''

def p_expressao_numero(p):
    '''
    expr : INTEIRO
        | DOUBLE
    '''

def p_expressao_variavel(p):
    '''
    expr : VARIAVEL
          | VARIAVEL OP_FINALLINHA
          | reserv
    '''

def p_expressao_operacao(p):
    '''
    expr : expr OP_MAT_MAIS expr
        |  expr OP_MAT_MENOS expr
        |  expr OP_MAT_VEZES expr
        |  expr OP_MAT_DIVIDE expr
        |  expr OP_MAT_MODULO expr
    '''

def p_expressao_grupo(p):
    '''
    expr : OP_ABRE_PARENTESES expr OP_FECHA_PARENTESES
    '''

def p_parametro_vazio(p):
    '''
    param_vazio :
    '''

def p_parametro(p):
    '''
    param : INTEIRO
        | DOUBLE
        | STRING
        | CHAR
        | VARIAVEL
        | reserv
    '''

def p_parametro_grupo(p):
    '''
    param : param OP_EXEC_VIRGULA param
    '''

def p_regra_funcao(p):
    '''
    funcao :  OP_ABRE_PARENTESES param_vazio OP_FECHA_PARENTESES
        |  OP_ABRE_PARENTESES param OP_FECHA_PARENTESES
    '''

def p_senao_se(p):
    '''
    senaose : ELIF OP_ABRE_PARENTESES cond_param OP_FECHA_PARENTESES OP_ABRE_CHAVES statements OP_FECHA_CHAVES
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