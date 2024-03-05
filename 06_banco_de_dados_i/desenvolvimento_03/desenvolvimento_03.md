## Entidade Usuário
| ID_USER | NOME     |
| ------- | -------- |
| 1       | Reinaldo |
| 2       | Nestor   |
| 3       | Raquel   |
| 4       | Tati     |
| 5       | Lia      |
| 6       | Paty     |

## Entidade Telefone
| ID_TELEFONE | TELEFONE     | FK_ID_USER |
| ----------- | ------------ | ---------- |
| 1           | 68 0945-8723 | 1          |
| 2           | 68 8734-2343 | 1          |
| 3           | 68 2143-5469 | 1          |
| 4           | 92 5400-0043 | 2          |
| 5           | 87 4300-0000 | 3          |
| 6           | 41 5400-1232 | 4          |
| 7           | 41 4345-5555 | 4          |
| 8           | 98 1234-5678 | 5          |
| 9           | 71 2123-2425 | 6          |

## Entidade Endereço
| ID_ENDERECO | RUA          | NUMERO | CIDADE         | ESTADO | CEP       | PAIS   | FK_ID_USER |
| ----------- | ------------ | ------ | -------------- | ------ | --------- | ------ | ---------- |
| 1           | Rua 10       | 34     | São Paulo      | SP     | 12345-000 | Brasil | 1          |
| 2           | Avenida Bela | 45     | Paulo Afonso   | BA     | 00034-000 | Brasil | 2          |
| 3           | Rua Cardoso  | 100    | Salvador       | BA     | 22222-000 | Brasil | 3          |
| 4           | Bairro Canoa | 002    | Rio de Janeiro | RJ     | 34251-324 | Brasil | 4          |
| 5           | Rua 50       | 41     | Maceió         | AL     | 32450-435 | Brasil | 5          |
| 6           | Rua 01       | 500    | Pinheiros      | SP     | 90000-000 | Brasil | 6          |

## Entidade Email
| ID_EMAIL | EMAIL                 | FK_ID_USER |
| -------- | --------------------- | ---------- |
| 1        | reinaldo000@gmail.com | 1          |
| 2        | reinaldo@outlook.com  | 1          |
| 3        | nestor123@gmail.com   | 2          |
| 4        | raquel@outlook.com    | 3          |
| 5        | tati000@gmail.com     | 4          |
| 6        | tati@outlook.com      | 4          |
| 7        | lia@outlook.com       | 5          |
| 8        | paty@outlook.com      | 6          |