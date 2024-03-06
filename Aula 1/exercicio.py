nomes = ['PLAYSTATION 5', 'XBOX SERIES X', 'XBOX SERIES S']
precos = [4500, 4500, 3700]
quantidades = [3, 10, 7]

def imprimir_produto():
    nome = input("Digite o nome do produto que você deseja consultar: ")

    if nome.upper() in nomes:
        indice = nomes.index(nome.upper())
        print(f"""
        Nome: {nomes[indice]}
        Preço: {precos[indice]}
        Quantidade: {quantidades[indice]}
        """) 
    else: 
        print("Produto indisponível ou inexistente") 
        imprimir_produto()

def excluir_produto():
    nome = input("Digite o nome do produto que você deseja excluir: ")

    if nome.upper() in nomes:
        indice = nomes.index(nome.upper())
        nomes.pop(indice)
        precos.pop(indice)
        quantidades.pop(indice)

        print(f"{nome.upper()} excluído com sucesso!")
    else:
        print("Produto indisponível ou inexistente") 
        excluir_produto()

def menu():
    print("""
    1 - Listar produto
    2 - Excluir produto
    0 - EXIT
    """)

while True:
    menu()
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        imprimir_produto()
    elif opcao == 2:
        excluir_produto() 
    elif opcao == 0:
        break


