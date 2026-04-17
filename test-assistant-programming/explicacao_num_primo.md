# Explicação do código `num_primo.py`

O arquivo `num_primo.py` implementa uma função enxuta para verificar se um número inteiro é primo.

```python
from math import isqrt


def is_primo(n: int) -> bool:
	"""Retorna True quando `n` é primo, caso contrário retorna False."""
	if n < 2:
		return False
	if n in (2, 3):
		return True
	if n % 2 == 0:
		return False

	limite = isqrt(n)
	for divisor in range(3, limite + 1, 2):
		if n % divisor == 0:
			return False

	return True
```

## O que foi melhorado

O código ficou mais limpo e idiomático com estes ajustes:

1. Uso de `isqrt` da biblioteca `math` para calcular a raiz inteira com mais clareza.
2. Inclusão da documentação da função com docstring.
3. Verificação de `2` e `3` de forma direta no mesmo teste.
4. Eliminação de cálculos desnecessários e uso de um limite mais preciso no laço.

## Explicação linha a linha

`from math import isqrt`  
Importa `isqrt`, que calcula a raiz quadrada inteira de um número de forma segura e legível.

`def is_primo(n: int) -> bool:`  
Define a função `is_primo`. Ela recebe um inteiro e retorna `True` ou `False`.

`"""Retorna True quando `n` é primo, caso contrário retorna False."""`  
Docstring que descreve o objetivo da função.

`if n < 2:`  
Números menores que 2 não são primos.

`return False`  
Encerra a função para esse caso.

`if n in (2, 3):`  
Trata rapidamente os menores números primos.

`return True`  
Confirma que 2 e 3 são primos.

`if n % 2 == 0:`  
Elimina todos os números pares maiores que 2.

`return False`  
Se for par, não é primo.

`limite = isqrt(n)`  
Calcula o maior divisor que precisa ser testado.

`for divisor in range(3, limite + 1, 2):`  
Percorre apenas divisores ímpares, de 3 até o limite.

`if n % divisor == 0:`  
Verifica se `n` é divisível por `divisor`.

`return False`  
Se existir um divisor exato, o número não é primo.

`return True`  
Se nenhum divisor foi encontrado, o número é primo.

## Como a função funciona

1. Números menores que 2 são rejeitados.
2. 2 e 3 são aceitos imediatamente.
3. Números pares maiores que 2 são rejeitados.
4. O restante dos casos testa apenas divisores ímpares até a raiz quadrada do número.
5. Se não houver divisores, o número é primo.

## Complexidade

O algoritmo tem complexidade de tempo aproximada de $O(\sqrt{n})$, o que é eficiente para uma verificação simples de primalidade.

## Exemplo de uso

```python
print(is_primo(7))   # True
print(is_primo(10))  # False
print(is_primo(13))  # True
print(is_primo(1))   # False
```
