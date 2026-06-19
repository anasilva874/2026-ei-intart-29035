import numpy as np
import matplotlib.pyplot as plt

import torch
import torch.nn as nn
import torch.optim as optim

from torch.utils.data import DataLoader
from torchvision import transforms

from medmnist import BreastMNIST

from sklearn.metrics import (
    confusion_matrix,
    ConfusionMatrixDisplay,
    accuracy_score
)
import os

os.makedirs("imagens", exist_ok=True)


# ==========================
# CONFIGURAÇÃO
# ==========================

BATCH_SIZE = 32
EPOCHS = 15
LEARNING_RATE = 0.001

CLASS_NAMES = {
    0: "Maligno",
    1: "Benigno"
}

# ==========================
# DATASETS
# ==========================


transform = transforms.Compose([
    transforms.ToTensor()
])

train_dataset = BreastMNIST(
    split="train",
    download=True,
    as_rgb=False,
    transform=transform
)

test_dataset = BreastMNIST(
    split="test",
    download=True,
    as_rgb=False,
    transform=transform
)

train_loader = DataLoader(
    train_dataset,
    batch_size=BATCH_SIZE,
    shuffle=True
)

test_loader = DataLoader(
    test_dataset,
    batch_size=BATCH_SIZE,
    shuffle=False
)

# ==========================
# CNN
# ==========================

class CNN(nn.Module):

    def __init__(self):
        super().__init__()

        self.conv = nn.Sequential(

            nn.Conv2d(
                in_channels=1,
                out_channels=16,
                kernel_size=3,
                padding=1
            ),

            nn.ReLU(),

            nn.MaxPool2d(2),

            nn.Conv2d(
                16,
                32,
                kernel_size=3,
                padding=1
            ),

            nn.ReLU(),

            nn.MaxPool2d(2)
        )

        self.fc = nn.Sequential(

            nn.Linear(
                32 * 7 * 7,
                128
            ),

            nn.ReLU(),

            nn.Linear(
                128,
                2
            )
        )

    def forward(self, x):

        x = self.conv(x)

        x = x.view(
            x.size(0),
            -1
        )

        x = self.fc(x)

        return x


model = CNN()

# ==========================
# LOSS E OTIMIZADOR
# ==========================

criterion = nn.CrossEntropyLoss()

optimizer = optim.Adam(
    model.parameters(),
    lr=LEARNING_RATE
)


# ==========================
# TREINO
# ==========================

loss_history = []

print("=== TREINO ===")

for epoch in range(EPOCHS):

    model.train()

    running_loss = 0

    for images, labels in train_loader:

        images = images.float()

        labels = labels.squeeze().long()

        optimizer.zero_grad()

        outputs = model(images)

        loss = criterion(
            outputs,
            labels
        )

        loss.backward()

        optimizer.step()

        running_loss += loss.item()

    epoch_loss = running_loss / len(train_loader)

    loss_history.append(
        epoch_loss
    )

    print(
        f"Época {epoch+1}/{EPOCHS}"
        f" - Loss: {epoch_loss:.4f}"
    )

# ==========================
# GRÁFICO LOSS
# ==========================

plt.plot(loss_history)

plt.title("Loss ao longo das épocas")
plt.xlabel("Época")
plt.ylabel("Loss")

plt.savefig("imagens/loss.png")
plt.show()

# ==========================
# TESTE
# ==========================

model.eval()

all_labels = []
all_preds = []

with torch.no_grad():

    for images, labels in test_loader:

        images = images.float()

        outputs = model(images)

        _, preds = torch.max(
            outputs,
            1
        )

        all_labels.extend(
            labels.squeeze().numpy()
        )

        all_preds.extend(
            preds.numpy()
        )

acc = accuracy_score(
    all_labels,
    all_preds
)

print("\nAccuracy:", acc)

# ==========================
# CONFUSION MATRIX
# ==========================

cm = confusion_matrix(
    all_labels,
    all_preds
)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=[
        "Maligno",
        "Benigno"
    ]
)

disp.plot()

plt.title("CNN - Confusion Matrix")

plt.savefig("imagens/confusion_matrix.png")
plt.show()
# ==========================
# IMAGENS ERRADAS
# ==========================

erros = []

model.eval()

with torch.no_grad():

    for idx in range(len(test_dataset)):

        image, label = test_dataset[idx]

        img_tensor = image.unsqueeze(0)

        output = model(img_tensor)

        pred = torch.argmax(output, dim=1).item()

        real = int(label.squeeze().item())

        if pred != real:

            erros.append(
                (
                    image.squeeze().numpy(),
                    real,
                    pred
                )
            )

print(f"\nNúmero de erros: {len(erros)}")

fig, axes = plt.subplots(
    3,
    3,
    figsize=(10, 10)
)

for ax, erro in zip(axes.ravel(), erros[:9]):

    image, real, pred = erro

    ax.imshow(
        image,
        cmap="gray"
    )

    ax.set_title(
        f"Real: {CLASS_NAMES[real]}\n"
        f"Prev: {CLASS_NAMES[pred]}"
    )

    ax.axis("off")

for ax in axes.ravel()[len(erros[:9]):]:
    ax.axis("off")

plt.tight_layout()

plt.savefig(
    "imagens/imagens_erradas.png",
    bbox_inches="tight"
)

plt.savefig("imagens/imagens_erradas.png")
plt.show()