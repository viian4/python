# =============================================================================
#  Plataforma de Testes de Lógica de Programação (versão Python)
#  Como executar: python teste_bruna.py
# =============================================================================

# =============================================================================
#  ENGINE DE TESTES (NÃO MODIFICAR ESTA SEÇÃO)
# =============================================================================

def deep_equal(a, b):
    if a is b or a == b:
        return True

    if isinstance(a, dict) and isinstance(b, dict):
        if a.keys() != b.keys():
            return False
        return all(deep_equal(a[k], b[k]) for k in a)

    if isinstance(a, (list, tuple)) and isinstance(b, (list, tuple)):
        if len(a) != len(b):
            return False
        return all(deep_equal(x, y) for x, y in zip(a, b))

    return False


def run_tests(problem_name, user_function, test_cases):
    print(f"\n--- Executando Testes para: [{problem_name}] ---")
    passes = 0
    for index, test in enumerate(test_cases):
        test_name = test.get("name", f"Teste {index + 1}")
        try:
            result = user_function(*test["input"])
            passed = deep_equal(result, test["expected"])
            if passed:
                print(f"  ✅ {test_name}: Passou")
                passes += 1
            else:
                print(f"  ❌ {test_name}: Falhou")
                print(f"     - Entrada:  {test['input']}")
                print(f"     - Esperado: {test['expected']}")
                print(f"     - Recebido: {result}")
        except Exception as e:
            print(f"  ❌ {test_name}: Erro durante a execução - {e}")
    print("--------------------------------------------------")
    print(f"Resultado para [{problem_name}]: {passes} de {len(test_cases)} testes passaram.")
    print("--------------------------------------------------")


# =============================================================================
#  ÁREA DE CÓDIGO  (MODIFIQUE APENAS AQUI)
# =============================================================================

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
        if f% 15 == 0:
            resultado.append("FizzBuzz")
        elif f% 3 == 0:
            resultado.append("Fizz")
        elif f % 5 == 0:
             resultado.append("Buzz")
        else:
            resultado.append(f)
    return resultado
    print(fizzBuzz(20)) 



def fatorial(num: int):
    """
    QUESTÃO 2: Fatorial
    Retorna num! (com 0! = 1). Lança ValueError para negativos.
    """
    if num < 0:
        raise ValueError("nao tem fatorial negativo.")
    resultado = 1
    for i in range(2, num + 1):
        resultado *= i
    return resultado
 


def ehPalindromo(s: str):
    """
    QUESTÃO 3: Verificador de Palíndromo
    Ignora espaços, pontuação e maiúsculas/minúsculas.
    """
    import re
    s_limpo = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return s_limpo == s_limpo[::-1]

def fibonacci(n: int):
    """
    QUESTÃO 4: Sequência de Fibonacci
    Retorna o n-ésimo termo (F(0)=0, F(1)=1).
    """
    if n < 0:
        raise ValueError("n deve ser >= 0")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def encontrarMediana(arr1, arr2):
    """
    QUESTÃO 5: Mediana de Dois Arrays (assuma arrays já ordenados).
    Solução simples: mescla e calcula a mediana.
    """
    arr = sorted(arr1 + arr2)
    n = len(arr)
    mediana = n // 2
    if n % 2 == 0:
        return (arr[mediana - 1] + arr[mediana]) / 2
    else:
        return arr[mediana]

def ehPar(num: int):
    """
    QUESTÃO 6: Par ou Ímpar
    Retorna True se par, False se ímpar.
    """
    return num % 2 == 0  


def removerDuplicatas(arr):
    """
    QUESTÃO 7: Remover Duplicatasui
    Retorna nova lista sem duplicatas, preservando a ordem do primeiro aparecimento.
    """
    resultado = []
    vistos = set()
    for v in arr:
        if v not in vistos:
            resultado.append(v)
            vistos.add(v)
    return resultado



def encontrarMaior(numeros):
    """
    QUESTÃO 8: Encontrar o Maior Número
    Retorna o maior elemento da lista.
    
    """
    if not numeros:
        return None
    maior = numeros[0]
    for n in numeros[1:]:
        if n > maior:
            maior = n
    return maior


# =============================================================================
#  DEFINIÇÃO E EXECUÇÃO DOS TESTES (NÃO MODIFICAR ESTA SEÇÃO)
# =============================================================================

if __name__ == "__main__":
    # FizzBuzz
    run_tests("FizzBuzz", fizzBuzz, [
        {"name": "Teste básico (n=5)", "input": [5], "expected": [1, 2, "Fizz", 4, "Buzz"]},
        {"name": "Teste com FizzBuzz (n=15)", "input": [15], "expected": [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"]},
        {"name": "Teste pequeno (n=1)", "input": [1], "expected": [1]},
    ])

    # Fatorial
    run_tests("Fatorial", fatorial, [
        {"name": "Teste padrão (5!)", "input": [5], "expected": 120},
        {"name": "Teste de caso base (0!)", "input": [0], "expected": 1},
        {"name": "Teste de caso base (1!)", "input": [1], "expected": 1},
    ])

    # Palíndromo
    run_tests("Palíndromo", ehPalindromo, [
        {"name": "Teste simples", "input": ["Arara"], "expected": True},
        {"name": "Teste com frase e espaços", "input": ["Anotaram a data da maratona"], "expected": True},
        {"name": "Teste com pontuação e maiúsculas", "input": ["Ame a ema!"], "expected": True},
        {"name": "Teste negativo", "input": ["Plataforma"], "expected": False},
    ])

    # Fibonacci
    run_tests("Fibonacci", fibonacci, [
        {"name": "Teste termo 7", "input": [7], "expected": 13},
        {"name": "Teste termo 0", "input": [0], "expected": 0},
        {"name": "Teste termo 1", "input": [1], "expected": 1},
        {"name": "Teste termo 10", "input": [10], "expected": 55},
    ])

    # Mediana
    run_tests("Mediana de Arrays", encontrarMediana, [
        {"name": "Teste com resultado ímpar", "input": [[1, 3], [2]], "expected": 2},
        {"name": "Teste com resultado par", "input": [[1, 2], [3, 4]], "expected": 2.5},
        {"name": "Teste com arrays de tamanhos diferentes", "input": [[1, 5, 10], [2, 3, 7, 8]], "expected": 5},
    ])

    # Par ou Ímpar
    run_tests("Par ou Ímpar", ehPar, [
        {"name": "Teste com número par", "input": [10], "expected": True},
        {"name": "Teste com número ímpar", "input": [7], "expected": False},
        {"name": "Teste com zero", "input": [0], "expected": True},
    ])

    # Remover Duplicatas
    run_tests("Remover Duplicatas", removerDuplicatas, [
        {"name": "Teste com números", "input": [[1, 2, 2, 3, 4, 4, 5]], "expected": [1, 2, 3, 4, 5]},
        {"name": "Teste com strings", "input": [["a", "b", "a", "c"]], "expected": ["a", "b", "c"]},
        {"name": "Teste sem duplicatas", "input": [[10, 20, 30]], "expected": [10, 20, 30]},
        {"name": "Teste com array vazio", "input": [[]], "expected": []},
    ])

    # Encontrar o Maior Número
    run_tests("Encontrar o Maior Número", encontrarMaior, [
        {"name": "Teste padrão", "input": [[10, 50, 2, 9, 45]], "expected": 50},
        {"name": "Teste com números negativos", "input": [[-1, -5, -10]], "expected": -1},
        {"name": "Teste com um único elemento", "input": [[100]], "expected": 100},
    ])
