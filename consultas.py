from sqlalchemy import select, func

from models import Autor, Livro


def listar_livros(session):
    # TODO: liste todos os livros com o nome do autor.
    stmt = select(Livro.titulo, Autor.nome).join(Livro.autor).where(Livro.autor_id == Autor.id)
    for livro, autor in session.execute(stmt):
        print(f"{livro} - {autor}")
        

def livros_por_autor(session, nome_autor):
    # TODO: liste os livros de um autor informado pelo nome.
    autor = str(input(nome_autor))
    stmt = select(Livro.titulo).join(Autor.livro).where(autor == Autor.nome)
    for livros in session.scalars(stmt):
        print(livros)


def buscar_livros(session, trecho):
    # TODO: busque livros por parte do título.
    titulo = str(input(trecho))
    stmt = select(Livro.titulo, Livro.ano, Autor.nome).join(Autor.livro).where(Livro.titulo == titulo)
    for titulo, ano, autor in session.execute(stmt):
        print(f"{titulo} ({ano}), {autor}")


def listar_autores_com_quantidade(session):
    # TODO: liste autores e a quantidade de livros de cada um.
    stmt = (
        select(Autor.nome, func.count(Livro.id))
        .join(Autor.livro)
        .group_by(Autor.id)
        .order_by(func.count(Livro.id).desc())
    )
    for autor, quant in session.execute(stmt):
        print(f"{autor} - {quant}")

def detalhes_livro(session, titulo):
    # TODO: mostre título, ano, autor e país do autor.
    titulo = str(input(titulo))
    stmt = (
        select(Livro.titulo, Livro.ano, Autor.nome, Autor.pais)
        .join(Autor.livro)
        .where(titulo == Livro.titulo, Livro.autor_id == Autor.id)
    )
    for titulo, ano, autor, autor_pais in session.execute(stmt):
        print(f"{titulo} ({ano}) - {autor}, {autor_pais}")
