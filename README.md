# 📚 Sistema de Gerenciamento de Biblioteca

Este é um projeto simples em Python para simular a gestão de uma biblioteca. O sistema permite cadastrar livros, gerenciar usuários e controlar o empréstimo e a devolução de livros.

## ✨ Funcionalidades

- **Cadastro de Livros:** Adicionar novos livros à coleção da biblioteca.
- **Gestão de Usuários:** Criar usuários que podem realizar empréstimos.
- **Empréstimo:** Verificar disponibilidade e emprestar livros.
- **Devolução:** Registrar a devolução de livros e atualizar o status.
- **Consulta:** Listar apenas os livros que estão disponíveis para empréstimo.

## 🚀 Instalação e Execução

Como este é um projeto em Python puro, não há dependências externas.

1. Certifique-se de ter o Python instalado.
2. Salve o código em um arquivo (ex: `biblioteca.py`).
3. Execute o script:
   ```bash
   python biblioteca.py
   ```
   ## 💻 Exemplo de Uso

```
# Instanciando a biblioteca
minha_biblioteca = Biblioteca()

# Criando livros
livro1 = Livro("Dom Casmurro", "Machado de Assis", True)
livro2 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", True)

# Adicionando à biblioteca
minha_biblioteca.adicionar_livro(livro1)
minha_biblioteca.adicionar_livro(livro2)

# Criando um usuário
usuario = Usuario([])

# Listando livros disponíveis
minha_biblioteca.listar_livros_disponiveis()

# Emprestando um livro
usuario.pegar_livro(livro1)

# Tentando emprestar o mesmo livro novamente (deverá falhar)
usuario.pegar_livro(livro1)

# Devolvendo o livro
usuario.devolver_livro(livro1)

# Mostrando dados do livro
livro1.mostrar_dados()
```

## 🏗️ Estrutura do Código
O projeto é composto por três classes principais:

1. Livro
Representa um item físico na biblioteca.

- Atributos:
titulo: Nome do livro.
autor: Autor do livro.
disponivel: Status booleano (True/False).
Métodos:
mostrar_dados(): Exibe as informações do livro no console.
2. Usuario
Representa um leitor que interage com a biblioteca.

- Atributos:
livros_emprestados: Lista contendo os livros atualmente sob posse do usuário.
Métodos:
pegar_livro(livro): Verifica disponibilidade e realiza o empréstimo.
devolver_livro(livro): Verifica se o usuário possui o livro e realiza a devolução.
3. Biblioteca
Gerencia o acervo e os livros disponíveis.

- Atributos:
lista_de_livros: Lista contendo todos os livros cadastrados.
Métodos:
adicionar_livro(livro): Insere um novo livro no acervo.
listar_livros_disponiveis(): Exibe na tela apenas os livros com disponivel = True.

## ⚠️ Observações Técnicas

- Inicialização de Livros: Atualmente, o método __init__ da classe Livro ignora o parâmetro disponivel e define o status como True por padrão.
- Validação de Devolução: O método devolver_livro verifica se o livro está na lista do usuário antes de permitir a devolução.
