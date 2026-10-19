
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class AnalisisExploratorio:
    """Clase para realizar el análisis exploratorio de los accidentes."""

    def __init__(self, ruta):
        """Inicializa la clase y recibe la ruta del dataset."""
        self.ruta = ruta
        self.df = None

    def cargar_datos(self):
        """Carga el dataset limpio desde un archivo CSV."""
        self.df = pd.read_csv(self.ruta)
        print("Dataset cargado correctamente.")
        return self.df

    def explorar_datos(self):
        """Muestra las dimensiones, columnas y tipos de datos."""
        if self.df is None:
            print("Primero debes cargar los datos.")
            return

        print("Cantidad de filas y columnas:", self.df.shape)

        print("\nNombres de las columnas:")
        print(self.df.columns.tolist())

        print("\nTipos de datos:")
        print(self.df.dtypes)

    
    def analizar_calidad(self):
        """Verifica valores nulos y registros duplicados."""
        if self.df is None:
            print("Primero debes cargar los datos.")
            return

        print("Cantidad de valores nulos por columna:")
        print(self.df.isnull().sum())

        print("\nTotal de valores nulos:")
        print(self.df.isnull().sum().sum())

        print("\nCantidad de registros duplicados:")
        print(self.df.duplicated().sum())
        
    def estadisticas_descriptivas(self):
        """Calcula estadísticas de las variables numéricas."""
        if self.df is None:
            print("Primero debes cargar los datos.")
            return

        columnas_numericas = [
            "ACCIDENTES",
            "PRECIPITACION_MM",
            "COMPARENDOS"
        ]

        print("Estadísticas descriptivas:")
        print(self.df[columnas_numericas].describe())

        
    def analizar_categorias(self):
        """Muestra la frecuencia de las variables categóricas."""
        if self.df is None:
            print("Primero debes cargar los datos.")
            return

        columnas_categoricas = [
            "GRAVEDAD_ACCIDENTE",
            "CLASE_ACCIDENTE",
            "LLUVIA"
        ]

        for columna in columnas_categoricas:
            print(f"\nFrecuencia de {columna}:")
            print(self.df[columna].value_counts())

            print("\nPorcentaje:")
            print(
                (self.df[columna].value_counts(normalize=True) * 100)
                .round(2)
            )
        
        
    
    def graficar_categoria(self, columna):
        """Genera el gráfico de barras de una variable categórica."""

        if self.df is None:
            print("Primero debes cargar los datos.")
            return

        columnas_validas = [
            "GRAVEDAD_ACCIDENTE",
            "CLASE_ACCIDENTE",
            "LLUVIA"
        ]

        if columna not in columnas_validas:
            print("Variable categórica no válida.")
            return

        frecuencias = self.df[columna].value_counts()

        plt.figure(figsize=(9, 5))
        ax = sns.barplot(
            x=frecuencias.index,
            y=frecuencias.values
        )

        # Mostrar la frecuencia encima de cada barra
        ax.bar_label(ax.containers[0], fmt="%.0f", padding=3)

        plt.title(f"Distribución de {columna}")
        plt.xlabel(columna)
        plt.ylabel("Cantidad de registros")
        plt.xticks(rotation=30, ha="right")
        plt.tight_layout()
        plt.show()

        
    
    def graficar_relacion(self, variable):
        """Grafica la relación entre una variable y los accidentes."""

        if self.df is None:
            print("Primero debes cargar los datos.")
            return

        columnas_validas = ["PRECIPITACION_MM", "COMPARENDOS"]

        if variable not in columnas_validas:
            print("Variable no válida.")
            return

        plt.figure(figsize=(8, 5))

        sns.regplot(
            data=self.df,
            x=variable,
            y="ACCIDENTES",
            scatter_kws={"alpha": 0.5},
            line_kws={"color": "red"}
        )

        plt.title(f"{variable} vs. ACCIDENTES")
        plt.xlabel(variable)
        plt.ylabel("Cantidad de accidentes")
        plt.tight_layout()
        plt.show()
    
        
    def graficar_matriz_correlacion(self):
        """Genera el mapa de calor de correlaciones."""

        if self.df is None:
            print("Primero debes cargar los datos.")
            return

        columnas = [
            "ACCIDENTES",
            "PRECIPITACION_MM",
            "COMPARENDOS"
        ]

        correlaciones = self.df[columnas].corr()

        plt.figure(figsize=(8, 6))
        sns.heatmap(
            correlaciones,
            annot=True,
            cmap="coolwarm",
            vmin=-1,
            vmax=1,
            fmt=".3f"
        )

        plt.title("Matriz de correlación")
        plt.tight_layout()
        plt.show()


    
    def graficar_matriz_dispersion(self):
        """Muestra las relaciones entre las variables numéricas."""
        if self.df is None:
            print("Primero debes cargar los datos.")
            return

        columnas = [
            "ACCIDENTES",
            "PRECIPITACION_MM",
            "COMPARENDOS"
        ]

        datos = self.df[columnas].sample(
            n=min(500, len(self.df)),
            random_state=42
        )

        grafico = sns.pairplot(
            datos,
            diag_kind="hist",
            corner=True,
            plot_kws={"alpha": 0.4, "s": 20}
        )

        grafico.fig.suptitle(
            "Matriz de dispersión de variables numéricas",
            y=1.02
        )

        plt.show()

    
    def detectar_outliers(self):
        """Detecta posibles valores atípicos usando el método IQR."""
        if self.df is None:
            print("Primero debes cargar los datos.")
            return

        columnas = [
            "ACCIDENTES",
            "PRECIPITACION_MM",
            "COMPARENDOS"
        ]

        print("DETECCIÓN DE VALORES ATÍPICOS (OUTLIERS)")

        for columna in columnas:
            q1 = self.df[columna].quantile(0.25)
            q3 = self.df[columna].quantile(0.75)
            iqr = q3 - q1

            limite_inferior = q1 - 1.5 * iqr
            limite_superior = q3 + 1.5 * iqr

            outliers = self.df[
                (self.df[columna] < limite_inferior) |
                (self.df[columna] > limite_superior)
            ]

            print(f"\nVariable: {columna}")
            print(f"Límite inferior: {limite_inferior:.2f}")
            print(f"Límite superior: {limite_superior:.2f}")
            print(f"Cantidad de posibles outliers: {len(outliers)}")

    
    def graficar_boxplot(self, columna):
        """Genera el diagrama de caja de una variable numérica."""
        if self.df is None:
            print("Primero debes cargar los datos.")
            return

        plt.figure(figsize=(8, 5))
        sns.boxplot(data=self.df, x=columna)
        plt.title(f"Diagrama de caja de {columna}")
        plt.xlabel(columna)
        plt.tight_layout()
        plt.show()

        
    
    
    def graficar_histograma(self, columna):
        """Genera el histograma de una variable numérica."""
        if self.df is None:
            print("Primero debes cargar los datos.")
            return

        if columna not in [
            "ACCIDENTES",
            "PRECIPITACION_MM",
            "COMPARENDOS"
        ]:
            print("Variable no válida.")
            return

        plt.figure(figsize=(8, 5))
        sns.histplot(data=self.df, x=columna, bins=20, kde=True)
        plt.title(f"Histograma de {columna}")
        plt.xlabel(columna)
        plt.ylabel("Frecuencia")
        plt.tight_layout()
        plt.show()

