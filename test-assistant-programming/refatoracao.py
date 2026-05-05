from typing import Sequence, Tuple


def calcular_estatisticas(numeros: Sequence[float]) -> Tuple[float, float, float, float]:
    """Calcula estatísticas básicas de uma sequência numérica.

    Args:
        numeros (Sequence[float]): Sequência de números (não vazia).

    Returns:
        Tuple[float, float, float, float]: Tupla contendo (total, média, maior, menor).

    Raises:
        ValueError: Se `numeros` for vazia.

    Examples:
        >>> calcular_estatisticas([1, 2, 3])
        (6.0, 2.0, 3, 1)
    """
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