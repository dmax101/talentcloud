# Consultas

## Base de dados

| P.NOME     | U.NOME   | MATRICULA | SERIE  | DISCIPLINA | NOTA |
| ---------- | -------- | --------- | ------ | ---------- | ---- |
| Vitória    | Claudino | 5542      | 2º ano | Matemática | 7,0  |
| Luiz       | Silva    | 6215      | 1º ano | Português  | 8,0  |
| André      | Carvalho | 4521      | 3º ano | Matemática | 9,5  |
| Alan       | Vilela   | 3285      | 1º ano | História   | 8,0  |
| Figueiredo | Santos   | 4598      | 2º ano | Geografia  | 9,0  |

## Base para Relax

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
## Respostas

- Mostrar as informações apenas dos alunos aprovados (nota acima de 7,0):

$$
σ_{NOTA > 7,0}(ALUNO)
$$

- Exibir as informações dos alunos do primeiro ano com nota maior ou igual a 8,0:

$$
σ_{NOTA \geq 8,0 \land SERIE = '1º ano'}(ALUNO)
$$

- Exibir apenas os nomes e as notas dos alunos:

$$
π_{PNOME, UNOME, NOTA}(ALUNO)
$$

- Criar uma tabela PROFESSOR que apresente apenas o primeiro e o último nome do professor:

$$
π_{PNOME, UNOME}(PROFESSOR)
$$

- Criar uma tabela ALUNO com o primeiro e o último nome de cada:

$$
π_{PNOME, UNOME}(ALUNO)
$$

- Mostrar o resultado da união entre a tabela ALUNO(PNOME, UNOME) e a tabela PROFESSOR:

$$
π_{PNOME, UNOME}(ALUNO) ∪ π_{PNOME, UNOME}(PROFESSOR)
$$

- Exibir o resultado da intersecção entre a tabela ALUNO(PNOME, UNOME) e a tabela PROFESSOR:

$$
π_{PNOME, UNOME}(ALUNO) ∩ π_{PNOME, UNOME}(PROFESSOR)
$$

- Exibir o resultado da diferença entre a tabela ALUNO(PNOME, UNOME) e a tabela PROFESSOR:

$$
π_{PNOME, UNOME}(ALUNO) ≠ π_{PNOME, UNOME}(PROFESSOR)
$$