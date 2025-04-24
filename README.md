# Sistema de Loja Virtual em Python

Este é um sistema simples de loja virtual no terminal que demonstra o uso de tratamento de erros em Python com foco nas estruturas try/except/else.

## Funcionalidades

- Listar produtos disponíveis (opção 1)
- Adicionar produtos ao carrinho (opção 2)
- Visualizar carrinho e total da compra (opção 3)
- Finalizar compra/pagamento (opção 4)
- Ver histórico de compras realizadas (opção 5)
- Sair(opção 6)

## Exceções Tratadas

O sistema trata os seguintes erros comuns:

1. **ProdutoInexistenteError** - Quando o usuário tenta adicionar um produto que não existe no sistema.
2. **QuantidadeInvalidaError** - Quando o usuário tenta adicionar uma quantidade não numérica ou negativa.
3. **SaldoInsuficienteError** - Quando o saldo do cliente é insuficiente para concluir a compra.
4. **CarrinhoVazioError** - Quando o usuário tenta finalizar uma compra com o carrinho vazio.

## Como Usar

1. Execute o programa com `python Produto.py`
2. Siga o menu interativo:
   - Digite 1 para ver a lista de produtos
   - Digite 2 para adicionar um produto ao carrinho
   - Digite 3 para ver os itens do carrinho e o valor total
   - Digite 4 para finalizar a compra
   - Digite 5 para ver seu histórico de compras realizadas
   - Digite 6 para sair do programa

## Estrutura do Código

- **Uso completo de estruturas try/except/else/finally**
  - `try`: Bloco onde podem ocorrer exceções
  - `except`: Tratamento específico para cada tipo de exceção
  - `else`: Executado apenas quando não ocorrem exceções
  - `finally`: Executado sempre, independente de ocorrer exceção ou não

- **Exceções personalizadas**
  - Criação de classes de exceção específicas para diferentes tipos de erro
  - Mensagens de erro claras e detalhadas

- **Documentação abrangente**
  - Comentários explicativos em todas as funções
  - Documentação de parâmetros, exceções e valores de retorno

- **Funcionalidades extras**
  - Histórico de compras para acompanhar todas as transações realizadas
  - Mensagens de erro detalhadas com sugestões de como resolver o problema

## Requisitos Atendidos

- Visualização de produtos disponíveis
- Adição de produtos ao carrinho
- Informação de quantidade
- Cálculo e visualização do valor total
- Simulação de pagamento com saldo fictício
- Uso de estruturas try/except/else/finally
- Criação e uso de exceções personalizadas
- Tratamento de erros comuns (produto inexistente, quantidade inválida, etc.)
- Código comentado e organizado 
