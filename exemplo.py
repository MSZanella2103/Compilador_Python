# Exemplo de codigo Python complexo
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Teste das funções
num = 5
print("O fatorial de", num, "é", factorial(num))
print("A sequência de Fibonacci até", num, "é:")
for i in range(num+1):
    print(fibonacci(i))
