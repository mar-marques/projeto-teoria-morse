# projeto-teoria-morse


 ### Motivação
 
Este programa é resultado de um projeto de pesquisa desenvolvido em minha iniciação científica na área de matemática. O programa recebe como entrada uma função de Morse discreta e um complexo simplicial. O programa consegue classificar os simplexos como simplexos regulares ou simplexos críticos. Todos os simplexo críticos são alocados na lista C. Contudo, os simplexos regulares ainda são classificados como "cabo" ou "ponta". Caso o simplexo regular for "cabo" será guardado em A; caso o o simplexo regular for "ponta" será guardado em B. A saída do programa é a impressão de três listas (variáveis A,B e C) que representam o campo vetorial gradiente induzido pela função f no complexo simplicial K.

### Como executar

Abra o arquivo CampoGradiente.py em um editor de texto. No arquivo, existem as varáveis K e f. Na variável K deve-se colocar os simplexos do complexo simplicial da seguinte forma: cada simplexo deve ser escrito entre parênteses e com um espaço entre os vértices que o compõe. Por exemplo, caso o complexo simplicial de interesse for representado pela forma de um triângulo com vértices a,b,c temos que K = ("a","b","c","a b","b c","a c","a b c"). Depois, na variável f deve-se colocar as associações da função de Morse da seguinte forma: cada associação deve conter primeiramente um simplexo descrito da mesma forma que na variável K e um valor numérico separados por vírgula. Por exemplo, suponha o complexo simplicial em forma de triângulo como visto anteriormente e a função de Morse dada por f = {(a,1), (b,3), (c,5), (ab, 2), (ac,8), (bc,6), (abc,7)}, então teriamos que colocar no arquivo f =(["a", 1], ["b", 3], ["c", 5], ["a b", 2], ["a c", 8], ["b c", 6], ["a b c", 7]). Atenção, os simplexos devem ser sempre escrito na mesma ordem de vértices tanto em K como em f. Por exemplo, o programa não roda corretamente se na variável K um simplexo está descrito por "a b" e na variável f por "b a". Veja que a ordem escrita dos vértices é alterada. Para executar o programa é necessário estar com o Python instalado na máquina. No Terminal, vá até a pasta onde o arquivo CampoGradiente.py está salvo. Por fim, digite: python CampoGradiente.py

 ### Em resumo, temos
 - Entrada.
      - Uma função de Morse discreta guardada na variável f e o complexo simplicial guardado na variável K.
 - Processamento.
      - Classifica os simplexos de K. Aloca os simplexo nas lista A, B e C de acordo com sua classificação. 
 - Saída
      - Impressão das listas A, B e C que são uma representação do campo vetorial gradiente induzido pela função f no complexo simplicial K
