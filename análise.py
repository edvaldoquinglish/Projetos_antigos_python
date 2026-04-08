import math
import matplotlib.pyplot as plt

def combinacoes(n, k):
    """Calcula combinações C(n,k)"""
    return math.comb(n, k)

def probabilidade(total_numeros, numeros_escolhidos, acertos):
    """Calcula a probabilidade de acertar exatamente 'acertos' números"""
    return (combinacoes(numeros_escolhidos, acertos) * combinacoes(total_numeros - numeros_escolhidos, numeros_escolhidos - acertos)) / combinacoes(total_numeros, numeros_escolhidos)

def main():
    # ====== CONFIGURAÇÃO ======
    total_numeros = 100
    numeros_escolhidos = 5
    valor_aposta = 100  # AOA

    premios = {0: 0, 1: valor_aposta, 2: 2000, 3: 12000, 4: 500000, 5: 10000000}
    total_combinacoes = combinacoes(total_numeros, numeros_escolhidos)

    print(f"Total de combinações possíveis: {total_combinacoes:,}\n")

    acertos_list = list(range(0, numeros_escolhidos + 1))
    probabilidades = []
    ganhos_esperados = []

    print(f"{'Acertos':>7} | {'Probabilidade':>14} | {'Ganho por aposta':>17} | {'Ganho esperado':>15}")
    print("-"*65)

    ganho_esperado_total = 0
    for acertos in acertos_list:
        prob = probabilidade(total_numeros, numeros_escolhidos, acertos)
        ganho = premios[acertos]
        ganho_esperado = prob * ganho
        probabilidades.append(prob)
        ganhos_esperados.append(ganho_esperado)
        ganho_esperado_total += ganho_esperado
        print(f"{acertos:>7} | {prob:>14.10f} | {ganho:>17,} | {ganho_esperado:>15,.2f}")

    print("\nCusto de uma aposta:", valor_aposta, "AOA")
    print("Ganho esperado médio por aposta: {:.2f} AOA".format(ganho_esperado_total))
    print("Lucro líquido esperado por aposta: {:.2f} AOA".format(ganho_esperado_total - valor_aposta))

    custo_total = total_combinacoes * valor_aposta
    ganho_total = total_combinacoes * ganho_esperado_total
    lucro_liquido = ganho_total - custo_total

    print("\nSe apostar em todas as combinações:")
    print(f"Custo total: {custo_total:,} AOA")
    print(f"Ganho total esperado: {ganho_total:,.2f} AOA")
    print(f"Lucro líquido esperado: {lucro_liquido:,.2f} AOA")

    # ====== GRÁFICOS ======
    plt.figure(figsize=(12,6))

    # Probabilidades
    plt.subplot(1,2,1)
    plt.bar(acertos_list, probabilidades, color='skyblue')
    plt.title("Probabilidade de acertos")
    plt.xlabel("Números acertados")
    plt.ylabel("Probabilidade")
    plt.xticks(acertos_list)

    # Ganhos esperados
    plt.subplot(1,2,2)
    plt.bar(acertos_list, ganhos_esperados, color='orange')
    plt.title("Ganho esperado por aposta")
    plt.xlabel("Números acertados")
    plt.ylabel("Ganho esperado (AOA)")
    plt.xticks(acertos_list)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
    