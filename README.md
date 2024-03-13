# Bingo
Trabalho universitário para a disciplina de Programação I | Universidade Federal Fluminense | 2020.1 (Período 1)

# Enunciado original
Sistema de um "bingo eletrônico"  

  
Deve ser implementado um sistema de "bingo eletrônico". O sistema deverá ser capaz de gerar uma quantidade solicitada pelo usuário de cartelas com 10 (dez) números cada de 00 a 99, definidos aleatoriamente mas de forma que duas cartelas não possuam todos os números iguais. As cartelas serão salvas em um arquivo texto onde cada linha corresponderá aos números de uma cartela, separados por um espaço em branco.  
    
Uma vez definidas as cartelas, um outro programa será responsável por ler o arquivo de cartelas e realizar o sorteio. O sorteio deve simular o uso de um "globo de bingo", de forma que os números de 00 (zero) a 99 (noventa e nove) estarão armazenados em alguma estrutura na memória e o sorteio será da posição deste número. Uma vez sorteado o número deverá ser removido da estrutura e inserido numa outra com os números já sorteados. A cada iteração do sorteio o sistema deverá informar os seguintes dados: (i) último número sorteado, (ii) números já sorteados, (iii) lista de cartelas com quantidade de números já sorteados ordenada em ordem decrescente; caso uma cartela tenha 9 (nove) números já sorteados (iv) o sistema deve incluir um alerta o informando. Após alguma cartela estar completa o sistema deverá encerrar o sorteio e informar (v) a quantidade de números sorteados, (vi) a lista de números sorteados, (vii) quantas e (viii) quais cartelas foram vencedoras.


## Restrições

a) Não será admitido o uso de funções de ordenação pré-implementadas.
b) O método de ordenação implementado deve ser necessariamente "selectionsort", "shellsort" ou "quicksort".
c) O código deverá prezar pela legibilidade; identificadores devem refletir seu significado.
d) Este projeto poderá ser feito em grupos de até 3 (três) pessoas.
e) Em caso de haver mais de uma pessoa na elaboração do projeto, a submissão deverá incorporar um breve relatório que descreva o grau de participação de cada integrante da equipe e quais as atividades que cada um desempenhou.
f) A nota de cada integrante de uma equipe não será necessariamente a mesma.
