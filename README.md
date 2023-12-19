
# Problema-BeeCrowd-1084-Programacao-Gulosa-PAA
O problema exemplo em questão será o problema #1084 ("Apagando e Ganhando") da plataforma Beecrowd:
https://www.beecrowd.com.br/judge/pt/problems/view/1084
         
DICA: como fazer as entradas e saídas no BeeCrowd, para vários tipos de
linguagem: https://www.beecrowd.com.br/judge/pt/faqs/about/examples

⇒ Trabalho em grupo de dois discentes (dupla)

⇒ Descrição:

Juliano é fã do programa de auditório Apagando e Ganhando, um programa no qual os participantes são selecionados via um sorteio e recebem prêmios em dinheiro por participarem. No programa, o apresentador escreve um número de N dígitos em uma lousa. O participante então deve apagar exatamente D dígitos do número que está na lousa; o número formado pelos dígitos que restaram é então o prêmio do participante. Juliano foi finalmente selecionado para participar do programa, e pediu que você escrevesse um programa que, dados o número que o apresentador escreveu na lousa, e quantos dígitos Juliano tem que apagar, determina o valor do maior prêmio que Juliano pode ganhar.

# ENTRADA
A entrada contém vários casos de teste. A primeira linha de cada caso de teste contém dois inteiros N e D (1 ≤ D < N ≤ 10^5), indicando a quantidade de dígitos do número que o apresentador escreveu na lousa e quantos dígitos devem ser apagados. A linha seguinte contém o número escrito pelo apresentador, que não contém zeros à esquerda. O final da entrada é indicado por uma linha que contém apenas dois zeros, separados por um espaço em branco.

# SAÍDA
Para cada caso de teste da entrada, seu programa deve imprimir uma única linha na saída, contendo o maior prêmio que Juliano pode ganhar.


# Exemplo </br>
Entrada 1:</br>
4 2</br>
3759</br>
Saída 1:
79<</br>

⇒ Requisitos Técnicos:
   * A implementação deve ser feita em uma linguagem de programação de sua escolha.

   * Submeta o código de sua solução na plataforma BeeCrowd (https://www.beecrowd.com.br/judge/pt/problems/view/1084) para verificar a eficácia (corretude) de seu algoritmo.
   
  * Certifique-se de que sua implementação siga o paradigma da Programação Gulosa:

       - Entender o problema: Primeiro, compreenda claramente o problema que está tentando resolver. Identifique os objetivos e as restrições do problema.

       - Identificar a estratégia gananciosa: Determine qual é a estratégia gananciosa apropriada para o problema. Pergunte a si: qual é a escolha que parece ser a melhor a cada passo, com base nas informações disponíveis até agora?

       - Definir a estrutura de solução: Estabeleça uma estrutura de solução que comece com uma solução vazia e vá sendo construída passo a passo, tomando decisões gananciosas a cada etapa.

       - Escrever o algoritmo guloso: Implemente o algoritmo guloso usando a estratégia identificada. Certifique-se de que a lógica de escolha gananciosa esteja corretamente incorporada ao algoritmo.

       - Verificar a viabilidade: Avalie se a solução gulosa é viável. Isso significa garantir que a solução atenda a todas as restrições do problema, como limites de capacidade ou condições específicas.

       - Analisar a otimalidade: Determine se a solução gulosa produz a solução ótima. Nem sempre o algoritmo guloso levará a uma solução ótima, mas em muitos casos, ele se aproxima o suficiente da solução ótima.

       - Implementar mecanismos de parada: Integre mecanismos de parada no algoritmo para garantir que ele saia quando a solução desejada for encontrada ou quando não for possível encontrar uma solução gananciosa.

       - Testar e depurar: Teste sua implementação em várias entradas e verifique se ela produz resultados corretos. Depure quaisquer erros ou problemas de lógica que possam surgir.
