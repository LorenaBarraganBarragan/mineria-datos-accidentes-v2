import pandas as pd

from sklearn.preprocessing import (
    MinMaxScaler,
    StandardScaler,
    RobustScaler
)

from sklearn.decomposition import PCA

class TransformacionDatos:

    def __init__(self, ruta):
        self.ruta = ruta
        self.df = None

    def cargar(self):
        self.df = pd.read_csv(self.ruta)
        return self.df

    def diagnosticar(self):
        print("Filas:", len(self.df))
        print("Columnas:", len(self.df.columns))

        print("\nValores nulos:")
        print(self.df.isnull().sum())

        print("\nDuplicados:", self.df.duplicated().sum())
        
    def tratar_nulos(self):
        self.df = self.df.copy()

        self.df["PRECIPITACION_FALTANTE"] = (
            self.df["PRECIPITACION_MM"].isnull().astype(int)
        )

        self.df["PRECIPITACION_MM"] = (
            self.df["PRECIPITACION_MM"].fillna(0)
        )

        columnas_categoricas = [
            "GRAVEDAD_ACCIDENTE",
            "CLASE_ACCIDENTE",
            "LLUVIA",
            "COD_INFRACCION",
            "TIPO_INFRACCION",
            "CLASE_VEHICULO_INFRACTOR",
            "SERVICIO_VEHICULO_INFRACTOR"
        ]

        for columna in columnas_categoricas:
            self.df[columna] = (
                self.df[columna].fillna("Sin dato")
            )

        mediana = self.df["COMPARENDOS"].median()
        self.df["COMPARENDOS"] = (
            self.df["COMPARENDOS"].fillna(mediana)
        )

        return self.df
    
    def codificar(self):
        self.df = self.df.copy()

        # Codificación ordinal de la gravedad
        mapa_gravedad = {
            "Solo daños": 0,
            "Con heridos": 1,
            "Con muertos": 2,
            "Sin dato": -1
        }

        self.df["GRAVEDAD_ACCIDENTE"] = (
            self.df["GRAVEDAD_ACCIDENTE"].map(mapa_gravedad)
        )

        # Variables para codificación One-Hot
        columnas_categoricas = [
            "CLASE_ACCIDENTE",
            "LLUVIA",
            "COD_INFRACCION",
            "TIPO_INFRACCION",
            "CLASE_VEHICULO_INFRACTOR",
            "SERVICIO_VEHICULO_INFRACTOR"
        ]

        # Aplicar One-Hot Encoding
        self.df = pd.get_dummies(
            self.df,
            columns=columnas_categoricas,
            dtype=int
        )

        return self.df
    
    def comparar_escaladores(self):
        variables_numericas = [
            "ACCIDENTES",
            "PRECIPITACION_MM",
            "COMPARENDOS"
        ]

        datos_numericos = self.df[variables_numericas].copy()

        # MinMaxScaler
        minmax = MinMaxScaler()
        datos_minmax = pd.DataFrame(
            minmax.fit_transform(datos_numericos),
            columns=variables_numericas
        )

        # StandardScaler
        standard = StandardScaler()
        datos_standard = pd.DataFrame(
            standard.fit_transform(datos_numericos),
            columns=variables_numericas
        )

        # RobustScaler
        robust = RobustScaler()
        datos_robust = pd.DataFrame(
            robust.fit_transform(datos_numericos),
            columns=variables_numericas
        )

        return {
            "MinMaxScaler": datos_minmax,
            "StandardScaler": datos_standard,
            "RobustScaler": datos_robust
        }
        
    def escalar(self):
        variables_numericas = [
            "ACCIDENTES",
            "PRECIPITACION_MM",
            "COMPARENDOS"
        ]

        scaler = RobustScaler()

        self.df[variables_numericas] = scaler.fit_transform(
            self.df[variables_numericas]
        )

        return self.df
    
    def aplicar_pca(self):
        variables_pca = self.df.select_dtypes(
            include="number"
        ).columns.tolist()

        variables_pca.remove("PRECIPITACION_FALTANTE")

        datos_pca = self.df[variables_pca]

        # PCA completo para obtener la varianza explicada
        pca = PCA()
        pca.fit(datos_pca)

        self.varianza_explicada = pca.explained_variance_ratio_
        self.varianza_acumulada = (
            pca.explained_variance_ratio_.cumsum()
        )

        # PCA reducido a 5 componentes
        pca_reducido = PCA(n_components=5)

        datos_reducidos = pca_reducido.fit_transform(
            self.df[variables_pca]
        )

        self.df_pca = pd.DataFrame(
            datos_reducidos,
            columns=["PC1", "PC2", "PC3", "PC4", "PC5"],
            index=self.df.index
        )

        self.df_reducido = pd.concat(
            [
                self.df[
                    ["FECHA", "PRECIPITACION_FALTANTE"]
                ],
                self.df_pca
            ],
            axis=1
        )

        return self.df_reducido
    
    def guardar_reducido(self, ruta):
        self.df_reducido.to_csv(ruta, index=False)
        print(f"Dataset reducido guardado en: {ruta}")