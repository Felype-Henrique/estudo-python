1. Qual a vantagem de transformar cada linha do arquivo em dicionários
em vez de trabalhar apenas com strings?

É mais claro e intuitivo acessar aluno['nome'] do que lembrar que o nome está na posição 1. O código fica mais fácil de ler e manter.

2. Em que situações pode ser útil retornar uma tupla de registros (como
nos exercícios ex01 e ex02) em vez de apenas uma lista de linhas?

Tupla não pode ser modificada, então protege os dados contra alterações acidentais depois de carregados.

3. O que você achou mais desafiador: ler o arquivo ou transformar as
linhas em estruturas de dados (dicionários)?

Transformar em dicionários, porque exige pensar na estrutura dos dados e tratar casos especiais. Ler o arquivo é bem mais simples.