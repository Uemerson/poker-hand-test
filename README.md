# Comentando as principais funções da classe PokerHand

#### isDenominationSequence

---

Essa função tem como objetivo verificar se as cartas estão em sequência numerica. Como parametro é passado a mão que o jogador está, depois eu crio um vetor com apenas os valores numericos retirando os naipes. Ordeno eles e crio uma lista com o menor numero e com maior numero da mão do jogador. No final é retornado se o vetor ordenado é igual a lista em sequência. Verificando assim se os valores numericos contido na mão do jogador está em sequência.

Exemplo de sequência numerica: 1, 2, 3, 4, 5 ou T, J, Q, k, A.

#### isSameDenomination

---

Essa função tem como objetivo verificar se os valores numericos da mão do jogador estão se repetindo. Como primeiro paramentro é passado a mão que o jogador está, depois eu crio um vetor com apenas os valores numericos retirando os naipes. Depois é criado um novo vetor ordenado que vai trazer quantas valores numericos estão se repetindo na mão do jogador. Por exemplo se a mão do jogador tiver (5H, 5H, 5H, 2C, 2C) o vetor gerado será [2, 3] pois o numero cinco repetiu três vezes e o numero dois duas vezes. Outro exemplo (1C, 1C, 1H, 1H, 1H) vai gerar um vetor [5] pois o numero um repetiu cinco vezes na mão do jogador. Assim se eu quero saber se a mão que estou passando como parametro tem 3 valores numericos se repetindo e nenhum outro eu passo a mão como primeiro parametro e o segundo parametro eu passo um vetor da seguinte forma [1, 1, 3]. O vetor que contém a quantidade de cartas repetidas desta função sempre é ordenado, logo o segundo parametro também tem ser ordenado para ser comparado de forma correta. A soma dos elementos do vetor gerado sempre dá cinco. No final da função sempre é comparado se o vetor gerado é igual ao vetor passado como função.

#### isSameSuit

---

Essa função tem como objetivo verificar se os naipes da mão do jogador estão se repetindo. Como primeiro paramentro é passado a mão que o jogador está, depois eu crio um vetor com apenas os naipes retirando os numeros. Depois é criado um novo vetor ordenado que vai trazer quantos naipes estão se repetindo na mão do jogador. Por exemplo se a mão do jogador tiver (5H, 5H, 5H, 2C, 2C) o vetor gerado será [2, 3] pois o naipe (H) repetiu 3 vezes e o (C) repetiu duas vezes. Outro exemplo (1C, 1C, 1H, 1H, 1H) vai retornar apenas [2, 3] pois o naipe (C) repetiu duas vezes e o naipe (H) repetiu três vezes. Assim se eu quero saber se a mão que estou passando como parametro tem 2 naipes se repetindo e nenhum outro eu passo a mão como primeiro parametro e o segundo parametro eu passo um vetor da seguinte forma [1, 1, 1, 2]. O vetor que contém a quantidade de cartas repetidas desta função sempre é ordenado, logo o segundo parametro também tem ser ordenado para ser comparado de forma correta. A soma dos elementos do vetor gerado sempre dá cinco. No final da função sempre é comparado se o vetor gerado é igual ao vetor passado como função.

#### checkRoyalFlush

---

O royal flush é preciso verificar se se a mão do jogador está na ordem T, J, Q, K, A e com os mesmos naipes. Então criei uma lista de 10 a 14 (A) e retirei os valores numericos da mão que é passada como parametro e uso a função isSameSuit para verificar se a mão está com os mesmos naipes, verificando se a mão do jogador é um royal flush.

#### checkStraightFlush

---

O straight flush é a mão do jogador em qualquer sequência (menos a sequência mais alta T, J, Q, K, A) e com os mesmos naipes. Para verificar se a mão do jogador (primeiro parametro) tem essa jogada basta usar a função isDenominationSequence e isSameSuit em conjunto. Logo se as duas funções retornarem True a mão do jogador é straight flush.

#### checkFourOfAKind

---

O four of a kind é a mão do jogador que contém quatro numeros repetidos e outro qualquer. Para verificar se a mão do jogador (primeiro parametro) tem essa jogada basta usar a função isSameDenomination com segundo parametro [1, 4].

#### checkFullHouse

---

O full house é a mão do jogador que contém dois numeros repetidos e outros três numeros repetidos diferentes. Para verificar se a mão do jogador (primeiro parametro) tem essa jogada basta usar a função isSameDenomination com segundo parametro [2, 3].

#### checkTwoPair

---

O two pair é a mão do jogador que contém dois numeros repetidos e outros dois numeros repetidos diferentes e o outro qualquer. Para verificar se a mão do jogador (primeiro parametro) tem essa jogada basta usar a função isSameDenomination com segundo parametro [1, 2, 2].

#### checkOnePair

---

O one pair é a mão do jogador que contém dois numeros repetidos e outros e os outros três qualquer (não repetidos). Para verificar se a mão do jogador (primeiro parametro) tem essa jogada basta usar a função isSameDenomination com segundo parametro [1, 1, 1, 2].

#### checkFlush

---

O flush é a mão do jogador que contém os cinco naipes repetidos. Para verificar se a mão do jogador (primeiro parametro) tem essa jogada basta usar a função isSameSuit com segundo parametro [5].

#### checkStraight

---

O straight é a mão do jogador que contém cinco cartas numericas em sequência. Para verificar se a mão do jogador (primeiro parametro) tem essa jogada basta usar a função isDenominationSequence.

#### checkThreeOfAKind

---

O three of a kind é a mão do jogador que contém três numeros repetidos e outros e os outros dois qualquer (não repetidos). Para verificar se a mão do jogador (primeiro parametro) tem essa jogada basta usar a função isSameDenomination com segundo parametro [1, 1, 3].

#### highCard

---

High Card retorna a carta mais alta da mão do jogador, sendo que a carta A se torna nesse caso o valor numerico um. Para isso eu pego a mão do jogador retiro os naipes e ordeno de forma inversa esse vetor que contém os valores numeros da mão do jogador e pego o primeiro elemento. Lembrando que as letras que representam os valores numericos são substituidas pelos numeros que elas valem e nesse caso o A é substituido por um.

### checkPokerHand

---

Um função que eu criei para printar a mão do jogador.

### powerPokerHand

---

Essa função tem como objetivo chamar as funções que verificam o tipo de mão que o jogador possui e atribuir um valor para elas da maior para menor retornando um numero de 10 a 1 para os tipos de mão. Caso nenhuma mão seja encontrada retorna o valor 0.

### compare_with

---

Essa função compara a mão da classe (self) e outra mão que é passada como parametro. Ela utiliza a função powerPokerHand para atribuir um valor numerico para ambas as mãos e verifica qual valor é maior, retornando Result.WIN sempre que a mão da classe (self) for maior que a segunda mão passada como parametro e Result.LOSS caso não seja. Caso as mão sejam de valor igual, exemplo primeira mão (three of a kind) e a segunda também, é chamado a função highCard para ver qual das mãos tem a maior carta e dar um desempate, ou caso não seja encontrada nenhuma mão para ambas (quando é retornado 0) essa função também é chamada, comparando qual a mior carta é a maior. Se caso a highCard esteja na mão da classe (self) então retorna Result.WIN caso não, retorna Result.LOSS.
