

| P.NOME     | U.NOME   | MATRICULA | SERIE  | DISCIPLINA | NOTA |
| ---------- | -------- | --------- | ------ | ---------- | ---- |
| Vitória    | Claudino | 5542      | 2º ano | Matemática | 7,0  |
| Luiz       | Silva    | 6215      | 1º ano | Português  | 8,0  |
| André      | Carvalho | 4521      | 3º ano | Matemática | 9,5  |
| Alan       | Vilela   | 3285      | 1º ano | História   | 8,0  |
| Figueiredo | Santos   | 4598      | 2º ano | Geografia  | 9,0  |


```python
ALUNO = {
    PNOME:string, UNOME:string, MATRICULA:number, SERIE:string, DISCIPLINA:string, NOTA:number
    'Vitória', 'Claudino', 5542, '2º ano', 'Matemática', 7.0
    'Luiz', 'Silva', 6215, '1º ano', 'Português', 8.0
    'André', 'Carvalho', 4521, '3º ano', 'Matemática', 9.5
    'Alan', 'Vilela', 3285, '1º ano', 'História', 8.0
    'Figueiredo', 'Santos', 4598, '2º ano', 'Geografia', 9.0
}
```

- Mostrar as informações apenas dos alunos aprovados (nota acima de 7,0):

$$
σ_{Nota > 7,0}(ALUNO)
$$

- Exibir as informações dos alunos do primeiro ano com nota maior ou igual a 8,0:

$$
σ_{Nota \geq 8,0 \land PNome = 'Primeiro'}(ALUNO)
$$

- Exibir apenas os nomes e as notas dos alunos:

$$
π_{PNome, UNome, Nota}(ALUNO)
$$

- Criar uma tabela PROFESSOR que apresente apenas o primeiro e o último nome do professor:

$$
π_{PNome, UNome}(PROFESSOR)
$$

- Criar uma tabela ALUNO com o primeiro e o último nome de cada:

$$
π_{PNome, UNome}(ALUNO)
$$

- Mostrar o resultado da união entre a tabela ALUNO(PNome, UNome) e a tabela PROFESSOR:

$$
π_{PNome, UNome}(ALUNO) ∪ π_{PNome, UNome}(PROFESSOR)
$$

- Exibir o resultado da intersecção entre a tabela ALUNO(PNome, UNome) e a tabela PROFESSOR:

$$
π_{PNome, UNome}(ALUNO) ∩ π_{PNome, UNome}(PROFESSOR)
$$

- Exibir o resultado da diferença entre a tabela ALUNO(PNome, UNome) e a tabela PROFESSOR:

$$
π_{PNome, UNome}(ALUNO) ~= π_{PNome, UNome}(PROFESSOR)
$$