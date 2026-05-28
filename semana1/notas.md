# Semana 1 — Reflexão

**Ana Silva** 
**29035**

---

## O que se perde quando uma imagem é reduzida a um conjunto de números?

Quando uma imagem é reduzida a um conjunto de números, perde-se uma grande quantidade de informação visual presente na imagem original. As características extraídas representam apenas alguns aspetos específicos previamente definidos, ignorando muitos detalhes. A imagem original contém padrões complexos, texturas, formas irregulares e pequenas variações que podem não estar representadas nas variáveis do dataset. Além disso, a forma como diferentes regiões da imagem se relacionam entre si também pode conter informação relevante para o diagnóstico.

---

## Que informação pode existir na imagem original que estas características não capturam?

As características numéricas podem não capturar:

padrões visuais subtis;
irregularidades específicas das células;
relações de espaço entre diferentes regiões;
detalhes de textura;
variações locais difíceis de resumir numericamente;
informação contextual da imagem completa.

---

## Análise da confusion matrix — que tipo de erro é mais grave?


O erro mais grave neste contexto é um falso negativo, ou seja, quando um tumor maligno é classificado incorretamente como benigno. Este tipo de erro é perigoso por poder levar à ausência de tratamento a tempo para um paciente que realmente possui cancro. Como consequência, a doença pode evoluir sem ser detetada, reduzindo bastante as hipóteses de sucesso do tratamento.


---