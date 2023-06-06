import Analise_lexica
import ply.yacc as yacc

tokens = Analise_lexica.tokens

# Definição da gramática
def p_expression_statement(p):
    '''expression_statement : expression SEMICOLON'''
    # Aqui você pode fazer o que quiser com a expressão
    print("Expressão:", p[1])

def p_expression(p):
    '''expression : expression op_mais term
                  | expression op_menos term
                  | term'''
    if len(p) > 2:
        if p[2] == '+':
            p[0] = p[1] + p[3]
        elif p[2] == '-':
            p[0] = p[1] - p[3]
    else:
        p[0] = p[1]

def p_term(p):
    '''term : term op_vezes factor
            | term op_divide factor
            | factor'''
    if len(p) > 2:
        if p[2] == '*':
            p[0] = p[1] * p[3]
        elif p[2] == '/':
            p[0] = p[1] / p[3]
    else:
        p[0] = p[1]

def p_factor(p):
    '''factor : NUMBER
              | LPAREN expression RPAREN'''
    if len(p) > 2:
        p[0] = p[2]
    else:
        p[0] = p[1]

def p_error(p):
    print("Erro de sintaxe")

# Constrói o analisador sintático
parser = yacc.yacc()

# Função para analisar uma expressão
def parse_expression(expression):
    result = parser.parse(expression)
    return result

# Exemplo de uso
result = parse_expression('2 + 3 * 4')
print(result)