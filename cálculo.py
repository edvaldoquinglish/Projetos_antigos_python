import math

def combinacoes(n, k):
    """
    Calcula combinações C(n, k) = n! / (k!(n-k)!)
    """
    return math.comb(n, k)

def probabilidade_acerto(total_numeros, numeros_escolhidos, acertos):
    """
    Calcula a probabilidade de acertar exatamente 'acertos' números
    """
    # Combinações de escolher acertos corretos
    acertos_corretos = combinacoes(numeros_escolhidos, acertos)
    # Combinações de escolher os restantes incorretos
    restantes_incorretos = combinacoes(total_numeros - numeros_escolhidos, numeros_escolhidos - acertos)
    # Total de combinações possíveis para uma aposta
    total_combinacoes = combinacoes(total_numeros, numeros_escolhidos)
    
    prob = (acertos_corretos * restantes_incorretos) / total_combinacoes
    return prob

def main():
    total_numeros = 100  # 0 a 99
    numeros_escolhidos = 5  # números por aposta
    
    print(f"Total de combinações possíveis para escolher {numeros_escolhidos} números de {total_numeros}:")
    total = combinacoes(total_numeros, numeros_escolhidos)
    print(total, "combinações\n")
    
    # Probabilidades de acertar 5, 4, 3 números
    for acertos in range(5, 2, -1):
        p = probabilidade_acerto(total_numeros, numeros_escolhidos, acertos)
        print(f"Probabilidade de acertar {acertos} números: {p:.10f} ({p*100:.10f}%)")

if __name__ == "__main__":
    main()
    