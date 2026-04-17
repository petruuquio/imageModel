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
