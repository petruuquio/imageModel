# Explicacao do debug

## Causa do erro

O problema principal era uma combinacao de erros de sintaxe e de tipo:

1. Na leitura do preco do item 1, faltavam aspas na mensagem do `input`:
   - Estava: `item1 = float(input(Preço do item 1? ))`
   - Isso gera `SyntaxError`, pois o texto nao estava entre aspas.

2. O valor do cupom era lido como texto (`str`) e usado em conta numerica:
   - Estava: `desconto_cupom = (input(...))`
   - Depois: `desconto_cupom / 100`
   - Isso gera `TypeError`, porque nao e possivel dividir string por numero.

3. A linha do desconto dentro do `if` estava sem indentacao:
   - Isso causa `IndentationError`.

4. O print do item 2 estava sem `f`-string:
   - Mostrava `{total_item2:.2f}` literalmente em vez do valor formatado.

## Correcao aplicada

- Adicionadas aspas no `input` do item 1.
- Conversao do cupom para `float`.
- Ajustada a indentacao do `print` dentro do bloco `if`.
- Corrigido o `print` do item 2 para `f-string`.

Com isso, o script volta a executar corretamente e exibir os valores formatados no resumo final.
