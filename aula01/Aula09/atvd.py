import json
import os

ARQUIVO = "biblioteca.json"

def carregar_dados():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_dados(biblioteca):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(biblioteca, f, ensure_ascii=False, indent=2)

def cadastrar_livro(biblioteca):
    titulo = input("Título: ")
    autor = input("Autor: ")
    ano = input("Ano: ")
    livro = {"titulo": titulo, "autor": autor, "ano": ano}
    biblioteca.append(livro)
    salvar_dados(biblioteca)
    print("1Livro cadastrado com sucesso!")

def listar_livros(biblioteca):
    if not biblioteca:
        print("Nenhum livro cadastrado.")
    else:
        for i, livro in enumerate(biblioteca, start=1):
            print(f"{i}. {livro['titulo']} - {livro['autor']} ({livro['ano']})")

def atualizar_livro(biblioteca):
    listar_livros(biblioteca)
    if not biblioteca:
        return
    try:
        indice = int(input("Digite o número do livro que deseja atualizar: ")) - 1
        if 0 <= indice < len(biblioteca):
            livro = biblioteca[indice]
            livro["titulo"] = input(f"Título ({livro['titulo']}): ") or livro["titulo"]
            livro["autor"] = input(f"Autor ({livro['autor']}): ") or livro["autor"]
            livro["ano"] = input(f"Ano ({livro['ano']}): ") or livro["ano"]
            salvar_dados(biblioteca)
            print(" Livro atualizado com sucesso!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")

def excluir_livro(biblioteca):
    listar_livros(biblioteca)
    if not biblioteca:
        return
    try:
        indice = int(input("Digite o número do livro que deseja excluir: ")) - 1
        if 0 <= indice < len(biblioteca):
            removido = biblioteca.pop(indice)
            salvar_dados(biblioteca)
            print(f" Livro '{removido['titulo']}' excluído com sucesso!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")

def menu():
    biblioteca = carregar_dados()
    while True:
        print("\n--- Biblioteca Digital ---")
        print("1. Cadastrar livro")
        print("2. Listar livros")
        print("3. Atualizar livro")
        print("4. Excluir livro")
        print("5. Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar_livro(biblioteca)
        elif opcao == "2":
            listar_livros(biblioteca)
        elif opcao == "3":
            atualizar_livro(biblioteca)
        elif opcao == "4":
            excluir_livro(biblioteca)
        elif opcao == "5":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()