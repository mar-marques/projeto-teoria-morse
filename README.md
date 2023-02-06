# projeto-teoria-morse


 #### Motivação
 
Este programa é resultado de um projeto de pesquisa desenvolvido em minha iniciação científica na área de matemática. O programa recebe como entrada uma Função de Morse discreta e um complexo simplicial. O programa consegue classificar os simplexos como simplexos regulares ou simplexos críticos. Todos os simplexo críticos são alocados na lista C. Contudo, os simplexos regulares ainda são classidicados como "cabo" ou "ponta". Caso o simplexo regular for "cabo" será guardado em A; caso o o simplexo regular for "ponta" será guardado em B. A saída do programa é a impressão de três listas (variáveis A,B e C) que representam o campo vetorial gradiente induzido pela função f no complexo simplicial K.

 #### Em resumo, temos
 - Entrada.
      - Uma função de Morse discreta guardada na variável f e o complexo simplicial guardado na variável K.
 - Processamento.
      - Classifica os simplexos de K. Aloca os simplexo nas lista A, B e C de acordo com sua classificação. 
 - Saída
      - Impressão das listas A, B e C que são uma representação do campo vetorial gradiente induzido pela função f no complexo simplicial K
