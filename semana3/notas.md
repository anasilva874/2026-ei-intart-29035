# Semana 1 — Reflexão

**Ana Silva** 
**29035**

---


## Que impacto tem usar imagens em vez de características extraídas manualmente (Semana 1)?

Na Semana 1, os modelos utilizavam apenas 30 características numéricas extraídas das imagens, como área, perímetro e textura. Nesta semana, os modelos utilizam diretamente os píxeis das imagens, o que permite ter acesso a mais informação visual.

No entanto, os classificadores clássicos têm dificuldade em interpretar essa informação visual de forma eficiente. Apesar disso, trabalhar com imagens permite preservar detalhes que podem ter sido perdidos quando a imagem foi reduzida apenas a um conjunto de características numéricas.

---

## Que padrões visuais são difíceis para um classificador linear?

Os classificadores lineares analisam cada píxel individualmente e têm dificuldade em compreender relações espaciais entre diferentes regiões da imagem.

Padrões como formas irregulares, texturas complexas ou pequenas diferenças na distribuição das intensidades dos píxeis são particularmente difíceis de capturar. Além disso, pequenas alterações de posição ou orientação de uma estrutura podem alterar significativamente os valores dos píxeis, dificultando ainda mais a classificação.

---

## Os erros fazem sentido visualmente? Que casos são mais ambíguos?

Ao analisar as imagens classificadas incorretamente, observa-se que muitos dos erros ocorrem em casos visualmente ambíguos. Algumas imagens apresentam características intermédias entre as duas classes ou possuem padrões pouco definidos, tornando a distinção difícil mesmo para um observador humano.

Também se verifica que algumas imagens têm níveis de contraste reduzidos ou regiões de interesse menos evidentes. Nestas situações, os classificadores clássicos podem não conseguir identificar informação suficiente para tomar uma decisão correta.

De forma geral, os erros observados parecem coerentes com a dificuldade visual das imagens, sugerindo que o problema não está apenas no modelo, mas também na complexidade dos próprios dados.