import pandas as pd
from sklearn.model_selection import train_test_split


class PreparacionArbol:
    """Prepara los datos para el árbol de decisión."""

    def __init__(self, ruta_dataset):
        self.ruta_dataset = ruta_dataset
        self.datos = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None

    def cargar_datos(self):
        """Carga el CSV sin modificar el archivo original."""

        self.datos = pd.read_csv(self.ruta_dataset)

        self.datos.columns = (
            self.datos.columns
            .str.strip()
            .str.replace("*", "", regex=False)
        )

        print("Dataset cargado correctamente.")
        print("Dimensiones:", self.datos.shape)
        print("Columnas:", list(self.datos.columns))

        return self.datos

    def preparar_variables(self):
        """Define los predictores y la variable objetivo."""

        if self.datos is None:
            raise ValueError("Primero debes cargar el dataset.")

        columnas_base = ["ACCIDENTES", "COMPARENDOS"]

        faltantes = [
            col for col in columnas_base
            if col not in self.datos.columns
        ]

        if faltantes:
            raise ValueError(f"Faltan columnas: {faltantes}")

        datos_modelo = self.datos.copy()

        datos_modelo["ACCIDENTES"] = pd.to_numeric(
            datos_modelo["ACCIDENTES"], errors="coerce"
        )

        datos_modelo["COMPARENDOS"] = pd.to_numeric(
            datos_modelo["COMPARENDOS"], errors="coerce"
        )

        # Variables predictoras disponibles en el CSV.
        columnas_predictoras = [
            "COMPARENDOS",
            "CLASE_ACCIDENTE_Atropello",
            "CLASE_ACCIDENTE_Caida Ocupante",
            "CLASE_ACCIDENTE_Choque",
            "CLASE_ACCIDENTE_Otro",
            "CLASE_ACCIDENTE_Volcamiento",
            "CLASE_VEHICULO_INFRACTOR_AUTOMOVIL",
            "CLASE_VEHICULO_INFRACTOR_CAMIONETA",
            "CLASE_VEHICULO_INFRACTOR_MOTOCICLETA",
            "CLASE_VEHICULO_INFRACTOR_Sin dato",
            "SERVICIO_VEHICULO_INFRACTOR_PARTICULAR",
            "SERVICIO_VEHICULO_INFRACTOR_Sin dato"
        ]

        columnas_predictoras = [
            col for col in columnas_predictoras
            if col in datos_modelo.columns
        ]

        if not columnas_predictoras:
            raise ValueError(
                "No se encontraron las columnas predictoras esperadas."
            )

        datos_modelo = datos_modelo.dropna(
            subset=["ACCIDENTES"] + columnas_predictoras
        ).copy()

        # Variable objetivo:
        # 0 = 8 accidentes o menos.
        # 1 = más de 8 accidentes.
        y = (datos_modelo["ACCIDENTES"] > 8).astype(int)

        # X contiene únicamente las variables predictoras.
        X = datos_modelo[columnas_predictoras].copy()

        print("\nVariables predictoras:")
        print(list(X.columns))

        print("\nDistribución de las clases:")
        print(y.value_counts().sort_index())
        print("0 = 8 accidentes o menos")
        print("1 = más de 8 accidentes")

        return X, y

    def separar_train_test(self, X, y):
        """Divide los datos en entrenamiento y prueba."""

        if y.nunique() < 2:
            raise ValueError(
                "Se necesitan ambas clases para entrenar el árbol."
            )

        self.X_train, self.X_test, self.y_train, self.y_test = (
            train_test_split(
                X,
                y,
                test_size=0.20,
                random_state=42,
                stratify=y
            )
        )

        print("\nSeparación realizada correctamente.")
        print("Registros de entrenamiento:", len(self.X_train))
        print("Registros de prueba:", len(self.X_test))

        print("\nDimensiones:")
        print("X_train:", self.X_train.shape)
        print("X_test:", self.X_test.shape)
        print("y_train:", self.y_train.shape)
        print("y_test:", self.y_test.shape)

        return (
            self.X_train,
            self.X_test,
            self.y_train,
            self.y_test
        )
