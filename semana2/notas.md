# Semana 2 — Reflexão

**Ana Silva** 
**29035**

---

## As classes são visivelmente diferentes? O que distingue um caso maligno de um benigno?

Ao observar as imagens do dataset, é possível notar algumas diferenças entre as duas classes, mas estas nem sempre são evidentes. Em vários casos, as imagens classificadas como malignas parecem apresentar padrões menos uniformes e regiões mais irregulares. Já as imagens benignas tendem a mostrar estruturas mais homogéneas e organizadas.

No entanto, as diferenças são muitas vezes subtis e difíceis de identificar apenas através da observação visual. Sem conhecimentos médicos especializados, seria bastante complicado distinguir corretamente muitos dos casos. Esta dificuldade ajuda a perceber a importância dos modelos de Machine Learning e Deep Learning, que conseguem detetar padrões e características que podem passar despercebidos ao olho humano.

---

## O dataset está equilibrado?

A análise da distribuição das classes mostrou que o dataset não está perfeitamente equilibrado. Existe uma diferença no número de amostras de cada classe, embora não seja extremamente elevada.

Este desequilíbrio pode influenciar o desempenho do modelo durante o treino. Se uma das classes estiver mais representada, o modelo pode acabar por favorecer essa classe nas previsões. Por essa razão, avaliar apenas a accuracy pode não ser suficiente. É importante utilizar outras métricas, como precision, recall e F1-score, para obter uma visão mais completa do desempenho do modelo.

Caso o desequilíbrio fosse mais significativo, poderiam ser aplicadas técnicas como oversampling da classe minoritária, undersampling da classe maioritária ou data augmentation para reduzir esse problema.


---

## Que diferenças notas relativamente à Semana 1?

A principal diferença relativamente à Semana 1 está na forma como os dados são representados.

Na semana anterior, o trabalho foi realizado com dados tabulares. Cada amostra era descrita através de 30 características numéricas já extraídas das imagens originais, como o raio, a textura ou a área do tumor. Ou seja, o processo de extração de características já tinha sido efetuado previamente.

Nesta semana, pelo contrário, trabalhamos diretamente com imagens. Em vez de receber características prontas a utilizar, o modelo recebe os próprios píxeis da imagem, organizados numa matriz de 28 × 28. Isto permite que o algoritmo aprenda automaticamente quais são as características mais relevantes para distinguir entre as diferentes classes.


## O que se ganha ao trabalhar com imagens?

Trabalhar diretamente com imagens traz várias vantagens. A principal é a possibilidade de o modelo descobrir padrões complexos sem necessidade de definir manualmente quais são as características importantes. Além disso, técnicas como as Redes Neuronais Convolucionais (CNNs) conseguem explorar relações espaciais entre píxeis e aprender representações muito mais ricas dos dados.

Por outro lado, esta abordagem também apresenta alguns desafios. Os modelos tendem a exigir mais capacidade computacional, mais tempo de treino e, muitas vezes, uma maior quantidade de dados para obter bons resultados. Existe ainda um maior risco de overfitting caso o modelo se adapte demasiado aos dados de treino.

