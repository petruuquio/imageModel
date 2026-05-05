# ENTRADA DE DADOS
cliente = input("Qual é seu nome? ")

# Quantidades como inteiros (contagem de itens); preços como float para permitir centavos
qtd1 = int(input("Quantidade do item 1: "))
item1 = float(input("Preço do item 1? "))

qtd2 = int(input("Quantidade do item 2: "))
item2 = float(input("Preço do item 2? "))

qtd3 = int(input("Quantidade do item 3: "))
item3 = float(input("Preço do item 3? "))

# CÁLCULOS DOS ITENS
total_item1 = qtd1 * item1
total_item2 = qtd2 * item2
total_item3 = qtd3 * item3

# Subtotal é a soma dos totais dos itens — antes de impostos e descontos
subtotal = total_item1 + total_item2 + total_item3
# Regra de negócio: imposto fixo de 10% sobre o subtotal
imposto = subtotal * 0.10

# DESCONTO
desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))

# O cupom é lido como percentual (ex: 15 para 15%). Mantemos o valor percentual
# em `desconto_cupom` para exibição; convertemos para fração apenas no cálculo.
desconto = subtotal * (desconto_cupom / 100)

# TOTAL FINAL
# Mantemos cálculo de total sem arredondamento aqui; o arredondamento é apenas
# para exibição no recibo/fatura, evitando pequenas discrepâncias de formato.
total = subtotal + imposto - desconto

# EXIBIÇÃO
linha = "=" * 31
separador = "-" * 31

print(linha)
print(f" Cliente: {cliente}")
print(linha)
print(f" Item 1:        R$ {total_item1:.2f}")
print(f" Item 2:        R$ {total_item2:.2f}")
print(f" Item 3:        R$ {total_item3:.2f}")
print(separador)
print(f" Subtotal:      R$ {subtotal:.2f}")
print(f" Imposto (10%): R$ {imposto:.2f}")

# Só exibimos a linha de desconto quando o cupom informado for maior que zero
if desconto_cupom > 0:
	# Exibimos o percentual arredondado sem casas decimais para ficar legível
	print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")

print(linha)
# Arredondamento para duas casas no total ao imprimir; usamos `round` para deixar
# explícito que queremos reduzir a representação flutuante antes da formatação.
print(f" TOTAL:         R$ {round(total, 2):.2f}")
print(linha)