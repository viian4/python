def fizzBuzz(n: int):
    """
    QUESTÃO 1: FizzBuzz
    Retorna uma lista de 1..n substituindo:
      - múltiplos de 3 por 'Fizz'
      - múltiplos de 5 por 'Buzz'
      - múltiplos de 15 por 'FizzBuzz'
    """
    resultado = []
    for f in range(1, n + 1):
        if f % 15 == 0:
            resultado.append("FizzBuzz")
        elif f % 3 == 0:
            resultado.append("Fizz")
        elif f % 5 == 0:
            resultado.append("Buzz")
        else:
            resultado.append(f)
    return resultado

# Exemplo de uso:
print(fizzBuzz(20))
   