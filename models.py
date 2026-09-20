from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


# TODO: crie o modelo Autor.
# Campos: id, nome, pais.
# Relacionamento: livros.

class Autor(Base):
    __tablename__ = "autores"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(nullable=False, unique=True)
    pais: Mapped[str] = mapped_column(nullable=False)

    livro: Mapped[List["Livro"]] = relationship(back_populates="autor")

# TODO: crie o modelo Livro.
# Campos: id, titulo, ano, autor_id.
# Relacionamento: autor.

class Livro(Base):
    __tablename__ = "livros"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    titulo: Mapped[str] = mapped_column(nullable=False)
    ano: Mapped[int] = mapped_column(nullable=False)
    autor_id: Mapped[int] = mapped_column(ForeignKey("autores.id"))

    autor: Mapped["Autor"] = relationship(back_populates="livro")
