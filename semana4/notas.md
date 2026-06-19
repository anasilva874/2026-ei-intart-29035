# Semana 4 – Rede Convolucional com PyTorch

**Ana Silva** 
**29035**

---


## Quantas épocas treinaste e porquê? Como sabias que era suficiente?

Foram utilizadas 15 épocas de treino. Este valor foi escolhido porque a loss diminuía de forma consistente durante as primeiras épocas e começava a estabilizar nas últimas. Quando a loss deixa de diminuir significativamente, é um sinal de que o modelo já aprendeu a maior parte dos padrões presentes nos dados e que continuar a treinar poderá trazer poucos benefícios.

---

## Compara as quatro semanas: tabular, pixels achatados e CNN. A CNN é sempre a melhor escolha?

Na Semana 1 foram utilizadas características numéricas já extraídas das imagens. Esta abordagem é simples e eficiente, mas perde alguma informação visual importante.

Na Semana 3 utilizaram-se os píxeis diretamente, mas os classificadores clássicos têm dificuldade em compreender a estrutura espacial das imagens.

A CNN conseguiu obter os melhores resultados porque foi desenvolvida especificamente para problemas de visão computacional. As camadas convolucionais conseguem identificar padrões, contornos e texturas relevantes para a classificação.

No entanto, a CNN nem sempre é a melhor escolha. Em datasets pequenos ou quando existem poucas imagens disponíveis, modelos mais simples podem ser mais rápidos, mais fáceis de interpretar e suficientemente eficazes.

---

## Se este modelo fosse colocado em produção num hospital amanhã, o que poderia correr mal para um paciente? O que seria necessário para esse risco ser aceitável?

O principal risco seria a existência de falsos negativos, ou seja, casos malignos classificados como benignos. Este tipo de erro poderia atrasar o diagnóstico e o tratamento de um paciente.

Para que o risco fosse aceitável, seria necessário validar o modelo com um conjunto de dados muito maior e mais diversificado, realizar testes em ambientes clínicos reais e garantir que as previsões do modelo fossem utilizadas apenas como apoio à decisão médica e não como substituição do diagnóstico realizado por profissionais de saúde.

---
