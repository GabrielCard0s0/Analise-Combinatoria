import math

def fatorial(n):
    """Calcula o fatorial de n."""
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def permutacao(n):
    """Calcula a permutação de n."""
    return fatorial(n)

def arranjo(n, k):
    """Calcula o arranjo de n em k."""
    return fatorial(n) // fatorial(n - k)

def combinacao(n, k):
    """Calcula a combinação de n em k."""
    return fatorial(n) // (fatorial(k) * fatorial(n - k))