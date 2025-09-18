import json
import os

ARQUIVO = "biblioteca.json"

# ----------- Funções -----------

def carregar():
    """Carrega os dados do arquivo JSON, ou cria lista vazia se não existir."""
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar(biblioteca):
    """Salva os dados no arquivo JSON."""
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(biblioteca, f, ensure_ascii=False, indent=2)

def cadastrar(biblioteca):
    """Adiciona um novo livro."""
    titulo = input("Título: ")
    autor = input("Autor: ")
    ano = input("Ano: ")
    livro = {"titulo": titulo, "autor": autor, "ano": ano}
    biblioteca.append(livro)
    salvar(biblioteca)
    print("Livro cadastrado!")

def listar(biblioteca):
    """Mostra todos os livros cadastrados."""
    if not biblioteca:
        print("Nenhum livro cadastrado.")
    else:
        for i, livro in enumerate(biblioteca, start=1):
            print(f"{i}. {livro['titulo']} - {livro['autor']} ({livro['ano']})")

def atualizar(biblioteca):
    """Permite editar os dados de um livro existente."""
    listar(biblioteca)
    if not biblioteca:
        return
    indice = int(input("Número do livro para atualizar: ")) - 1
    if 0 <= indice < len(biblioteca):
        livro = biblioteca[indice]
        livro["titulo"] = input(f"Título ({livro['titulo']}): ") or livro["titulo"]
        livro["autor"] = input(f"Autor ({livro['autor']}): ") or livro["autor"]
        livro["ano"] = input(f"Ano ({livro['ano']}): ") or livro["ano"]
        salvar(biblioteca)
        print("Livro atualizado!")

def excluir(biblioteca):
    """Remove um livro da lista."""
    listar(biblioteca)
    if not biblioteca:
        return
    indice = int(input("Número do livro para excluir: ")) - 1
    if 0 <= indice < len(biblioteca):
        removido = biblioteca.pop(indice)
        salvar(biblioteca)
        print(f"Livro '{removido['titulo']}' excluído!")

# ----------- Programa principal -----------

def menu():
    biblioteca = carregar()
    while True:
        print("\n--- Biblioteca Digital ---")
        print("1. Cadastrar livro")
        print("2. Listar livros")
        print("3. Atualizar livro")
        print("4. Excluir livro")
        print("5. Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar(biblioteca)
        elif opcao == "2":
            listar(biblioteca)
        elif opcao == "3":
            atualizar(biblioteca)
        elif opcao == "4":
            excluir(biblioteca)
        elif opcao == "5":
            print("Encerrando...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()