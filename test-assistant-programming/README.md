# Test Assistant Programming

## Descrição

Projeto de exemplos simples em Python para exercícios de refatoração, depuração
e explicação de algoritmos. Contém scripts didáticos que demonstram leitura de
entrada, cálculos básicos e utilitários (ex.: verificação de número primo).

## Estrutura de arquivos

- [debug.py](debug.py): Script interativo que lê quantidades e preços de três
  itens, aplica imposto fixo (10%) e um cupom de desconto percentual; exibe um
  recibo simples formatado.
- [num_primo.py](num_primo.py): Implementação da função `is_primo(n: int) -> bool`
  (usa `math.isqrt` para otimizar a verificação). Contém docstring em português
  no estilo Google.
- [refatoracao.py](refatoracao.py): Função `calcular_estatisticas` que retorna
  (total, média, maior, menor) de uma sequência numérica; inclui um exemplo de
  execução em `__main__` e docstring estilo Google.
- [explicacao_num_primo.md](explicacao_num_primo.md): Anotações/explanação sobre
  o algoritmo de verificação de números primos.
- [explicacao_refatoracao.md](explicacao_refatoracao.md): Notas sobre a
  refatoração de `refatoracao.py`.
- [explicacao-debug.md](explicacao-debug.md): Notas sobre o script `debug.py`.

## Como executar

Recomenda-se usar um ambiente virtual com Python 3.8+ (necessário para
`math.isqrt`). Abaixo há instruções básicas:

1. Ativar/crear ambiente (opcional):

```bash
python -m venv .venv
source .venv/Scripts/activate    # Windows (PowerShell/CMD use .venv\Scripts\Activate)
pip install --upgrade pip
```

2. Executar os scripts:

- `debug.py` (interativo):

```bash
python debug.py
```

O script pedirá o nome do cliente, quantidades e preços dos três itens e o
percentual do cupom de desconto; em seguida imprime o recibo.

- `refatoracao.py` (demo inclusão de `calcular_estatisticas`):

```bash
python refatoracao.py
```

Isso executa o bloco `__main__` e imprime total, média, maior e menor de uma
lista de exemplo.

- `num_primo.py` (uso como módulo):

```python
from num_primo import is_primo

print(is_primo(7))  # True
print(is_primo(12)) # False
```

`num_primo.py` não contém um runner interativo por padrão; importe a função
quando precisar usá-la em outros scripts ou no REPL.

## Tecnologias e ferramentas

- Linguagem: Python (3.8+)
- Módulos da biblioteca padrão usados: `math` e `typing`
- Recomendações: executar em ambiente virtual (`venv`) para isolar dependências

## Notas e contribuições

- Os arquivos `explicacao_*.md` contêm comentários e justificativas das escolhas
  de implementação — úteis para estudo e revisão.
- Contribuições são bem-vindas: abra um branch, faça alterações e submeta um
  pull request com uma descrição clara das mudanças.

---

Se quiser, eu posso:

- Adicionar um pequeno conjunto de testes unitários (`pytest`) para as funções;
- Criar um script de execução automatizada ou exemplos mais detalhados;
- Incluir checagem de entradas em `debug.py` para maior robustez.

Escolha uma dessas opções ou diga o que prefere que eu faça a seguir.
