from math import isqrt


def is_primo(n: int) -> bool:
	"""Verifica se um número é primo.

	Args:
		n (int): Número inteiro a ser testado.

	Returns:
		bool: `True` se `n` for primo, `False` caso contrário.

	Examples:
		>>> is_primo(7)
		True
		>>> is_primo(4)
		False
	"""
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
