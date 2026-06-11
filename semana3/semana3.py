import numpy as np
import matplotlib.pyplot as plt

from medmnist import BreastMNIST
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import os

os.makedirs("semana3", exist_ok=True)

from skimage.feature import hog

from sklearn.metrics import (
    accuracy_score, confusion_matrix, ConfusionMatrixDisplay
)


dataset = BreastMNIST(split="train", download=True)

imagens = []
labels = []

for img, label in dataset:
    imagens.append(np.array(img))

    labels.append(int(np.array(label).squeeze()))

x = np.array(imagens)
y = np.array(labels)

print("=== DATASET ===")
print("Número de imagens: ", len(x))
print("Formato original: ", x.shape)


x = x.reshape(len(x), -1)

print("Formato achatado: ", x.shape)


x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


log_model = LogisticRegression(max_iter=5000)
log_model.fit(x_train, y_train)
y_pred_log = log_model.predict(x_test)
acc_log = accuracy_score(y_test, y_pred_log)

print("\n=== LOGISTIC REGRESSION ===")
print("Accuracy: ", acc_log)

cm_log = confusion_matrix(y_test, y_pred_log)

disp = ConfusionMatrixDisplay(cm_log)
disp.plot()

plt.title("Confusion Matrix - Logistic Regression")
plt.savefig("semana3/confusion_logistic.png")
plt.show()


rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

rf_model.fit(x_train, y_train)

y_pred_rf = rf_model.predict(x_test)

acc_rf = accuracy_score(y_test, y_pred_rf)

print("\n=== RANDOM FOREST ===")
print("Accuracy: ", acc_rf)

cm_rf = confusion_matrix(y_test, y_pred_rf)

disp = ConfusionMatrixDisplay(cm_rf)
disp.plot()

plt.title("Confusion Matrix - Random Forest")
plt.savefig("semana3/confusion_rf.png")
plt.show()


erros = np.where(y_test != y_pred_rf)[0]

n_erros = min(9, len(erros))

fig, axes = plt.subplots(3, 3, figsize=(8, 8))

for ax, idx in zip(axes.ravel(), erros[:n_erros]):

    imagem = x_test[idx].reshape(28, 28)
    ax.imshow(imagem, cmap="gray")

    ax.set_title(
        f"Real:{y_test[idx]} Pred:{y_pred_rf[idx]}"
    )

    ax.axis("off")

plt.tight_layout()
plt.savefig("semana3/erros_rf.png")
plt.show()


print("\n=== HOG FEATURES ===")

x_hog = []

for img in imagens:

    features = hog(
        img,
        orientations=9,
        pixels_per_cell=(4, 4),
        cells_per_block=(2, 2),
        feature_vector=True
    )

    x_hog.append(features)

x_hog = np.array(x_hog)

print("Formato HOG: ", x_hog.shape)


x_train_hog, x_test_hog, y_train_hog, y_test_hog = train_test_split(
    x_hog,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


hog_log = LogisticRegression(max_iter=5000)
hog_log.fit(x_train_hog, y_train_hog)
y_pred_hog_log = hog_log.predict(x_test_hog)

acc_hog_log = accuracy_score(y_test_hog, y_pred_hog_log)

print("\nHOG + Logistic Regression")
print("Accuracy: ", acc_hog_log)

cm_hog_log = confusion_matrix(y_test_hog, y_pred_hog_log)

disp = ConfusionMatrixDisplay(cm_hog_log)
disp.plot()

plt.title("Confusion Matrix - HOG Logistic")
plt.savefig("semana3/confusion_hog_logistic.png")
plt.show()


hog_rf = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

hog_rf.fit(x_train_hog, y_train_hog)

y_pred_hog_rf = hog_rf.predict(x_test_hog)

acc_hog_rf = accuracy_score(y_test_hog, y_pred_hog_rf)

print("\nHOG + Random Forest")
print("Accuracy: ", acc_hog_rf)

cm_hog_rf = confusion_matrix(y_test_hog, y_pred_hog_rf)

disp = ConfusionMatrixDisplay(cm_hog_rf)
disp.plot()

plt.title("Confusion Matrix - HOG Random Forest")
plt.savefig("semana3/confusion_hog_rf.png")
plt.show()