# psi-atividade2-marcospaulo

## Respondendo algumas perguntas

### 1. Onde estão os modelos ORM deste projeto?
Estão no script `models.py` em que estão os modelos `autores` e `livros` representados como classes `Autor` e `Livro`.

### 2. Qual classe representa o lado "um" e qual representa o lado "muitos" no relacionamento?
classe `Autor`: 1 \
classe `Livro`: N

### 3. Para que serve o `ForeignKey` em `Livro.autor_id`?
Possibilita a relação de `1:N` entre as classes `Autor` e `Livro` em que `Livro.autor_id` relaciona com o id da classe `Autor`. Assim, portanto, poderiamos fazer por exemplo "Listar os livros de um determinado autor".

### 4. O que acontece se você esquecer o `session.commit()` após inserir os dados?
Simplesmente não vai implementar a adição dos dados em que `commit()` é responsável por salvar permanentemente as alterações de transação no banco de dados.