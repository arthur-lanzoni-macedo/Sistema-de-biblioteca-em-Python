class Livro:
    def __init__(self, titulo, autor, disponivel):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True
        
    def mostrar_dados(self):
        print(f'Titulo: {self.titulo}')
        print(f'Autor: {self.autor}')
        print(f'Disponível: {self.disponivel}')


class Usuario:
    def __init__(self, livros_emprestados):
        self.livros_emprestados = []
    
    def pegar_livro(self, livro):
        if livro.disponivel:
            self.livros_emprestados.append(livro)
            livro.disponivel = False
            print(f"Sucesso: O livro '{livro.titulo}' foi emprestado.")
        else:
            print(f"Ops! O livro '{livro.titulo}' já está emprestado no momento e não pode ser retirado.")
            
    def devolver_livro(self, livro):
        if livro.disponivel in self.livros_emprestados:
            self.livros_emprestados.remove(livro)
            livro.disponivel = True
            print(f"O livro '{livro.titulo}' foi devolvido com sucesso!")
        else:
            print(f"Erro: O livro '{livro.titulo}' não consta na lista de emprestados.")