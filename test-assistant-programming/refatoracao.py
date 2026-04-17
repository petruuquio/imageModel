from typing import Sequence, Tuple


def calcular_estatisticas(numeros: Sequence[float]) -> Tuple[float, float, float, float]:
    """Retorna total, media, maior e menor valor de uma sequencia numerica."""
    if not numeros:
        raise ValueError("A lista de numeros nao pode ser vazia.")

    total = 0.0
    maior = numeros[0]
    menor = numeros[0]

    for valor in numeros:
        total += valor
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor

    media = total / len(numeros)
    return total, media, maior, menor


if __name__ == "__main__":
    valores = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
    total, media, maior, menor = calcular_estatisticas(valores)

    print("total:", total)
    print("media:", media)
    print("maior:", maior)
    print("menor:", menor)