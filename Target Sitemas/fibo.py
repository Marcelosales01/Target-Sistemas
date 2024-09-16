def sequencia_fib(limit):
    fib_sequencia = [0, 1]
    while fib_sequencia[-1] < limit:
        fib_sequencia.append(fib_sequencia[-1] + fib_sequencia[-2])
    return fib_sequencia

def pertence_a_sequencia(num):
    fib_sequencia = sequencia_fib(num)
    if num in fib_sequencia:
        return f"O número {num} pertence à sequência de Fibonacci."
    else:
        return f"O número {num} não pertence à sequência de Fibonacci."

# Exemplo de uso
numero = int(input("Informe um número: "))
print(pertence_a_sequencia(numero))

