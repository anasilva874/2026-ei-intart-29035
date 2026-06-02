import os
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

import medmnist
from medmnist import INFO


DATASET = "breastmnist"

CLASS_NAMES = {
    0: "Maligno",
    1: "Benigno"
}

os.makedirs("imagens", exist_ok=True)


info = INFO[DATASET]
DataClass = getattr(medmnist, info["python_class"])

train_dataset = DataClass(
    split="train",
    download=True
)

print("=" * 50)
print("INFORMAÇÕES DO DATASET")
print("=" * 50)
print(f"Dataset: {DATASET}")
print(f"Número de amostras: {len(train_dataset)}")
print("\nClasses:")
print("0 -> Benigno")
print("1 -> Maligno")


labels = np.array(train_dataset.labels).flatten()


classes = np.unique(labels)

fig, axes = plt.subplots(
    len(classes),
    5,
    figsize=(12, 6)
)

for row, classe in enumerate(classes):

    indices = np.where(labels == classe)[0][:5]

    for col, idx in enumerate(indices):

        image, label = train_dataset[idx]

        axes[row, col].imshow(image, cmap="gray")
        axes[row, col].axis("off")
        axes[row, col].set_title(CLASS_NAMES[classe])

plt.suptitle("Exemplos de Imagens por Classe", fontsize=14)
plt.tight_layout()

plt.savefig(
    "imagens/exemplos_classes.png",
    bbox_inches="tight"
)

plt.show()


contagem = Counter(labels)

plt.figure(figsize=(8, 5))

plt.bar(
    [CLASS_NAMES[c] for c in contagem.keys()],
    contagem.values()
)

plt.title("Distribuição das Classes")
plt.xlabel("Classe")
plt.ylabel("Número de Amostras")

for i, valor in enumerate(contagem.values()):
    plt.text(i, valor + 2, str(valor), ha="center")

plt.savefig(
    "imagens/distribuicao_classes.png",
    bbox_inches="tight"
)

plt.show()


todos_pixeis = []

for image, label in train_dataset:
    todos_pixeis.append(np.array(image))

todos_pixeis = np.array(todos_pixeis)

print("\n" + "=" * 50)
print("ESTATÍSTICAS DOS PIXEIS")
print("=" * 50)

print(f"Shape do dataset: {todos_pixeis.shape}")
print(f"Valor mínimo: {todos_pixeis.min()}")
print(f"Valor máximo: {todos_pixeis.max()}")
print(f"Média: {todos_pixeis.mean():.4f}")
print(f"Desvio padrão: {todos_pixeis.std():.4f}")


plt.figure(figsize=(8, 5))

plt.hist(
    todos_pixeis.flatten(),
    bins=50
)

plt.title("Distribuição dos Valores dos Píxeis")
plt.xlabel("Valor do Pixel")
plt.ylabel("Frequência")

plt.savefig(
    "imagens/distribuicao_pixeis.png",
    bbox_inches="tight"
)

plt.show()


print("\n" + "=" * 50)
print("DISTRIBUIÇÃO DAS CLASSES")
print("=" * 50)

total = len(labels)

for classe, quantidade in sorted(contagem.items()):

    percentagem = (quantidade / total) * 100

    print(
        f"{CLASS_NAMES[classe]}: "
        f"{quantidade} amostras "
        f"({percentagem:.2f}%)"
    )


print("\nAnálise concluída com sucesso!")
print("Gráficos guardados na pasta 'imagens'.")