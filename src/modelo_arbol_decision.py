from pathlib import Path

import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


class ModeloArbolDecision:
    """Entrena, evalúa y explica un árbol de decisión."""

    def __init__(self, random_state=42, max_depth=4):
        self.random_state = random_state
        self.max_depth = max_depth
        self.modelo = None

    def entrenar(self, X_train, y_train):
        """Entrena el árbol de decisión."""

        self.modelo = DecisionTreeClassifier(
            max_depth=self.max_depth,
            random_state=self.random_state,
        )

        self.modelo.fit(X_train, y_train)
        return self.modelo

    def evaluar(self, X_train, X_test, y_train, y_test):
        """Calcula las métricas del modelo."""

        if self.modelo is None:
            raise ValueError("Primero debes entrenar el modelo.")

        pred_train = self.modelo.predict(X_train)
        pred_test = self.modelo.predict(X_test)

        resultados = {
            "Accuracy entrenamiento": accuracy_score(y_train, pred_train),
            "Accuracy prueba": accuracy_score(y_test, pred_test),
            "Profundidad real": self.modelo.get_depth(),
            "Número de hojas": self.modelo.get_n_leaves(),
        }

        print("RESULTADOS DEL MODELO")
        print("-" * 40)

        for nombre, valor in resultados.items():
            if "Accuracy" in nombre:
                print(f"{nombre}: {valor:.2%}")
            else:
                print(f"{nombre}: {valor}")

        print("\nREPORTE DE CLASIFICACIÓN")
        print(
            classification_report(
                y_test,
                pred_test,
                labels=[0, 1],
                target_names=["Accidentes bajos", "Accidentes altos"],
                zero_division=0,
            )
        )

        print("MATRIZ DE CONFUSIÓN")
        print(confusion_matrix(y_test, pred_test, labels=[0, 1]))

        return resultados

    def graficar(self, X, nombre_archivo="arbol_decision.png"):
        """Muestra y guarda la imagen del árbol."""

        if self.modelo is None:
            raise ValueError("Primero debes entrenar el modelo.")

        plt.figure(figsize=(22, 12))

        plot_tree(
            self.modelo,
            feature_names=list(X.columns),
            class_names=["Accidentes bajos", "Accidentes altos"],
            max_depth=self.max_depth,
            filled=True,
            rounded=True,
            fontsize=9,
        )

        plt.title(f"Árbol de decisión: profundidad máxima {self.max_depth}")
        plt.tight_layout()

        raiz_proyecto = Path(__file__).resolve().parent.parent
        carpeta = raiz_proyecto / "docs" / "diagramas"
        carpeta.mkdir(parents=True, exist_ok=True)

        ruta = carpeta / nombre_archivo

        plt.savefig(ruta, dpi=200, bbox_inches="tight")
        plt.show()
        plt.close()

        print("Árbol guardado en:", ruta)

    def extraer_reglas(self, X):
        """Devuelve las reglas del árbol en texto."""

        if self.modelo is None:
            raise ValueError("Primero debes entrenar el modelo.")

        return export_text(
            self.modelo,
            feature_names=list(X.columns),
            decimals=2,
        )