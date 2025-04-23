#  Trabalho realizado pelo julismo
class ProdutoInexistenteError(Exception):
    def __init__(self):
        super().__init__("Produto não existe no sistema")

class QuantidadeInvalidaError(Exception):
    def __init__(self):
        super().__init__("Quantidade inválida! Deve ser um número positivo.")

class SaldoInsuficienteError(Exception):
    def __init__(self):
        super().__init__("Saldo insuficiente para realizar a compra")

class CarrinhoVazioError(Exception):
    def __init__(self):
        super().__init__("Não é possível finalizar compra com carrinho vazio!")

# Classe para armazenar informações do produto
class Produto:
    def __init__(self, codigo, nome, preco):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco

# Classe principal do sistema
class Loja:
    def __init__(self):
        # Dicionário de produtos disponíveis
        self.produtos = {
            1: Produto(1, "Camiseta", 19.99),
            2: Produto(2, "Calça", 35.50),
            3: Produto(3, "Tênis", 179.99),
            4: Produto(4, "Boné", 39.95)
        }
        # Dicionário para o carrinho {codigo_produto: quantidade}
        self.carrinho = {}  
        # Saldo fictício do cliente
        self.saldo_cliente = 1000.0
        # Histórico de compras (funcionalidade extra)
        self.historico_compras = []

    def listar_produtos(self):
        print("\n=== Produtos Disponíveis ===")
        for produto in self.produtos.values():
            print(f"Código: {produto.codigo} | {produto.nome} - €{produto.preco:.2f}")
        print("=" * 30)

    def adicionar_carrinho(self, codigo_produto, quantidade):
        # Uso completo de try/except/else/finally conforme requisito
        try:
            # Validação da quantidade - geração de exceção personalizada
            if quantidade <= 0:
                raise QuantidadeInvalidaError()
            
            # Validação do código do produto - geração de exceção personalizada
            if codigo_produto not in self.produtos:
                raise ProdutoInexistenteError()
            
        except QuantidadeInvalidaError as e:
            # Tratamento da exceção personalizada
            print(f"\nErro: {e}")
            return False
            
        except ProdutoInexistenteError as e:
            # Tratamento da exceção personalizada
            print(f"\nErro: {e}")
            print("Produtos disponíveis:")
            for cod in self.produtos.keys():
                print(f"  - Código {cod}: {self.produtos[cod].nome}")
            return False
            
        except Exception as e:
            # Tratamento genérico para outros erros
            print(f"\nErro inesperado: {e}")
            return False
            
        else:
            # Bloco ELSE aqui executa apenas se não ocorrer nenhuma exceção e adiciona ao carrinho (ou atualiza quantidade)
            self.carrinho[codigo_produto] = self.carrinho.get(codigo_produto, 0) + quantidade
            print(f"\nProduto '{self.produtos[codigo_produto].nome}' adicionado ao carrinho!")
            return True
            
        finally:
            # Bloco FINALLY: executa sempre, independente de erros
            print("Operação de adição ao carrinho concluída.")
    
    def visualizar_carrinho(self):
        try:
            if not self.carrinho:
                print("\nCarrinho vazio!")
                return 0
            
        except Exception as e:
            print(f"\nErro ao verificar carrinho: {e}")
            return 0
            
        else:
            print("\n=== Seu Carrinho ===")
            total = 0
            for codigo, qtd in self.carrinho.items():
                produto = self.produtos[codigo]
                subtotal = produto.preco * qtd
                total += subtotal
                print(f"{produto.nome}: {qtd} x €{produto.preco:.2f} = €{subtotal:.2f}")
            print(f"\nTotal: €{total:.2f}")
            print("=" * 25)
            return total

    def finalizar_compra(self):
        try:
            if not self.carrinho:
                raise CarrinhoVazioError()
            
            total = sum(self.produtos[cod].preco * qtd for cod, qtd in self.carrinho.items())
            
            if total > self.saldo_cliente:
                raise SaldoInsuficienteError()

        except CarrinhoVazioError as e:
            print(f"\nErro: {e}")
            print("Adicione produtos ao carrinho antes de finalizar a compra.")
            return False
            
        except SaldoInsuficienteError as e:
            print(f"\nErro: {e}")
            print(f"Saldo atual: €{self.saldo_cliente:.2f}, Total da compra: €{total:.2f}")
            faltante = total - self.saldo_cliente
            print(f"Faltam €{faltante:.2f} para concluir a compra.")
            return False
            
        except Exception as e:
            print(f"\nErro inesperado ao finalizar compra: {e}")
            return False
            
        else:
            # Executa se não houver erros
            self.saldo_cliente -= total
            
            # Registra a compra no histórico (funcionalidade extra)
            compra = {"itens": {}, "total": total, "data": "Hoje"}
            for codigo, qtd in self.carrinho.items():
                produto = self.produtos[codigo]
                compra["itens"][produto.nome] = {"quantidade": qtd, "preco_unit": produto.preco}
            
            self.historico_compras.append(compra)
            
            print(f"\nCompra realizada com sucesso!")
            print(f"Valor total: €{total:.2f}")
            print(f"Saldo restante: €{self.saldo_cliente:.2f}")
            self.carrinho.clear()  # Limpa o carrinho após a compra
            return True
            
        finally:
            print("Operação de finalização concluída.")
            
    def mostrar_historico(self):
        "Mostra o histórico de compras realizadas (funcionalidade extra)"

        if not self.historico_compras:
            print("\nVocê ainda não realizou nenhuma compra.")
            return
            
        print("\n=== Histórico de Compras ===")
        for i, compra in enumerate(self.historico_compras, 1):
            print(f"Compra #{i} - Total: €{compra['total']:.2f}")
            print("Itens:")
            for nome, detalhe in compra["itens"].items():
                print(f"  - {nome}: {detalhe['quantidade']} x €{detalhe['preco_unit']:.2f}")
            print("-" * 25)

# Função principal para executar a loja
def main():
    """
    Função principal que inicia a loja virtual
    """
    # Instancia a loja
    loja = Loja()
    
    # Loop principal do programa
    while True:
        try:
            # Menu principal
            print("\n=== LOJA VIRTUAL ===")
            print("1. Listar produtos")
            print("2. Adicionar ao carrinho")
            print("3. Visualizar carrinho")
            print("4. Finalizar compra")
            print("5. Ver histórico de compras")
            print("6. Sair")
            
            # Captura a opção do usuário
            opcao = input("\nEscolha uma opção: ")
            
            # Trata cada opção do menu
            if opcao == "1":
                loja.listar_produtos()
                
            elif opcao == "2":
                # Mostra os produtos antes de perguntar qual adicionar
                loja.listar_produtos()
                try:
                    # Captura entrada do usuário
                    codigo = int(input("Digite o código do produto: "))
                    quantidade = int(input("Digite a quantidade: "))
                    loja.adicionar_carrinho(codigo, quantidade)
                except ValueError:
                    # Trata erro de digitação
                    print("\nErro: Digite apenas números!")
                    
            elif opcao == "3":
                loja.visualizar_carrinho()
                
            elif opcao == "4":
                loja.finalizar_compra()
                
            elif opcao == "5":
                loja.mostrar_historico()
                
            elif opcao == "6":
                print("\nObrigado por utilizar nossa loja virtual! Volte sempre!")
                break
                
            else:
                print("\nOpção inválida! Tente novamente.")
                
        except Exception as e:
            # Tratamento genérico para erros não previstos
            print(f"\nErro inesperado: {e}")
            input("Pressione Enter para continuar...")

# Ponto de entrada do programa
if __name__ == "__main__":
    main()