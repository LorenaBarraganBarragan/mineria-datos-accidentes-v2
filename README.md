# Minería de Datos - Accidentes de Tránsito en Barranquilla

## 1. Descripción del proyecto

Este proyecto desarrolla un proceso de minería de datos sobre los accidentes de tránsito registrados en Barranquilla, Colombia, integrando información de accidentalidad, precipitación y comparendos.

El propósito es explorar el comportamiento de los accidentes, identificar patrones en los datos y analizar posibles relaciones entre la cantidad de accidentes, las condiciones de precipitación y los comparendos registrados.

El proyecto incluye la preparación, limpieza, integración, transformación y análisis exploratorio de los conjuntos de datos.

## 2. Objetivo general

Analizar los datos de accidentalidad en Barranquilla mediante técnicas de minería de datos para describir su comportamiento y explorar relaciones entre los accidentes de tránsito, la precipitación y los comparendos.

### Objetivos específicos

- Explorar y describir los conjuntos de datos utilizados.
- Identificar problemas de calidad, valores faltantes y posibles valores atípicos.
- Limpiar e integrar los datos mediante la variable temporal.
- Aplicar técnicas de transformación, escalamiento y reducción de dimensionalidad.
- Analizar la distribución de las variables y sus relaciones mediante gráficos estadísticos.
- Interpretar los resultados sin asumir relaciones causales que no estén demostradas.

## 3. Conjuntos de datos

### 3.1. Accidentalidad en Barranquilla

- **Fuente:** Datos Abiertos Colombia.
- **Formato:** CSV.
- **Registros originales:** 28.523.
- **Columnas originales:** 11.

Principales variables:

- `FECHA_ACCIDENTE`
- `HORA_ACCIDENTE`
- `GRAVEDAD_ACCIDENTE`
- `CLASE_ACCIDENTE`
- `SITIO_EXACTO_ACCIDENTE`
- `CANT_HERIDOS_EN_SITIO_ACCIDENTE`
- `CANT_MUERTOS_EN_SITIO_ACCIDENTE`
- `CANTIDAD_ACCIDENTES`
- `AÑO_ACCIDENTE`
- `MES_ACCIDENTE`
- `DIA_ACCIDENTE`

### 3.2. Precipitación en Barranquilla

- **Fuente:** IDEAM / Datos Abiertos Colombia.
- **Formato:** CSV.
- **Registros originales reportados:** 50.000.
- **Municipio de interés:** Barranquilla.

La variable principal es `valorobservado`, que representa la precipitación registrada en milímetros (mm).

La información meteorológica se utiliza para explorar posibles relaciones entre las condiciones de precipitación y la accidentalidad. Los valores faltantes deben distinguirse de los registros que realmente representan ausencia de precipitación.

### 3.3. Comparendos en Barranquilla

- **Formato:** CSV.
- **Registros originales reportados:** 357.743.
- **Columnas originales:** 9.

Principales variables:

- `fecha_comparendo`
- `COD_INFRACCION`
- `DESC_INFRACCION`
- `TIPO_INFRACCION`
- `SERVICIO_VEHICULO_INFRACTOR`
- `CLASE_VEHICULO_INFRACTOR`
- `CANTIDAD_INFRACCIONES`
- `Tipo Camara`
- `Camara_y_direccion`

Los comparendos se utilizan para explorar su comportamiento y su posible asociación con la cantidad de accidentes registrados.

## 4. Preparación y transformación de los datos

El proceso de preparación contempla las siguientes actividades:

1. Carga e inspección de los conjuntos de datos originales.
2. Limpieza y normalización de las variables.
3. Conversión y organización de las fechas.
4. Integración de la información de accidentalidad, precipitación y comparendos.
5. Tratamiento de valores faltantes y creación de indicadores cuando corresponde.
6. Codificación de variables categóricas.
7. Escalamiento de variables numéricas.
8. Aplicación de análisis de componentes principales (PCA) para reducir la dimensionalidad.

Los conjuntos de datos limpios, preparados, integrados y reducidos cumplen funciones diferentes dentro del proceso y deben utilizarse de acuerdo con la etapa del análisis.

## 5. Análisis exploratorio de datos (EDA)

El análisis exploratorio se desarrolla en el notebook `analisis/eda_accidentes_barranquilla.ipynb`, utilizando el conjunto de datos `dataset/dataset_limpio_eda.csv`.

El conjunto de datos utilizado en esta etapa contiene **3.047 registros y 12 columnas**.

La variable objetivo del análisis es `ACCIDENTES`, que representa la cantidad de accidentes en cada registro temporal.

### 5.1. Análisis univariado

Se elaboraron gráficos para estudiar individualmente las variables numéricas y categóricas.

**Histogramas**

Se generaron histogramas para:

- `ACCIDENTES`
- `PRECIPITACION_MM`
- `COMPARENDOS`

Estos gráficos permiten examinar la distribución de los valores, sus concentraciones y la presencia de observaciones alejadas del comportamiento más frecuente.

**Diagramas de caja (boxplots)**

Se elaboraron diagramas de caja para las mismas tres variables numéricas. Se utilizaron para examinar la mediana, los cuartiles, la dispersión y los posibles valores atípicos.

**Gráficos de barras**

Se analizaron las frecuencias de las variables categóricas:

- `GRAVEDAD_ACCIDENTE`
- `CLASE_ACCIDENTE`
- `LLUVIA`

Cada gráfico cuenta con una interpretación dentro del notebook.

### 5.2. Análisis bivariado

Se generaron diagramas de dispersión para estudiar las siguientes relaciones:

- `PRECIPITACION_MM` frente a `ACCIDENTES`.
- `COMPARENDOS` frente a `ACCIDENTES`.

Los gráficos incluyen una línea de tendencia lineal para facilitar la observación de las relaciones entre las variables.

### 5.3. Matriz de correlación

Se calculó el coeficiente de correlación de Pearson entre las tres variables numéricas.

| Variables | Correlación |
|---|---:|
| Accidentes y precipitación | 0,063 |
| Accidentes y comparendos | 0,134 |
| Precipitación y comparendos | 0,018 |

Los resultados indican asociaciones lineales positivas muy débiles entre accidentes y precipitación, y entre accidentes y comparendos. La relación lineal entre precipitación y comparendos es prácticamente nula.

Estos coeficientes son descriptivos y no permiten establecer causalidad.

### 5.4. Matriz de dispersión

Se elaboró una matriz de dispersión (*pairplot*) para visualizar conjuntamente las distribuciones de las variables numéricas y sus relaciones por pares.

Esta visualización complementa la matriz de correlación y permite observar la concentración de los valores, la dispersión y posibles patrones en los datos.

### 5.5. Hallazgos descriptivos

Entre los resultados del análisis exploratorio se destacan:

- La cantidad promedio de accidentes es de aproximadamente 9,36 por registro, con una mediana de 8.
- La precipitación presenta una alta concentración de valores en cero y algunos registros elevados.
- La cantidad promedio de comparendos es de aproximadamente 208,90 por registro.
- La clase de accidente más frecuente es el choque.
- En la variable `LLUVIA` existe una proporción importante de registros clasificados como `Sin dato`, lo que limita las conclusiones sobre la presencia de lluvia.

Los resultados describen el conjunto de datos analizado y no deben interpretarse como evidencia de causalidad.

## 6. Tecnologías utilizadas

- **Python:** desarrollo del proceso de análisis.
- **Pandas:** carga, limpieza, transformación y manipulación de datos.
- **Matplotlib:** construcción de visualizaciones.
- **Seaborn:** gráficos estadísticos, diagramas de caja, dispersión y mapas de calor.
- **Jupyter Notebook:** ejecución documentada del análisis.
- **Visual Studio Code:** entorno de desarrollo.
- **Git y GitHub:** control de versiones y almacenamiento del proyecto.
- **Scikit-learn:** escalamiento y reducción de dimensionalidad mediante PCA, cuando corresponda a la etapa de transformación.

## 7. Estructura del proyecto

La estructura general del repositorio incluye los siguientes componentes. Los nombres de archivos pueden variar según los avances de cada etapa.

```text
mineria-datos-accidentes-v2/
│
├── dataset/
│   ├── Accidentalidad_en_Barranquilla_20260830.csv
│   ├── precipitacion_barranquilla.csv
│   ├── Comparendos_Barranquilla.csv
│   ├── Accidentalidad_en_Barranquilla_limpio.csv
│   ├── precipitacion_barranquilla_limpio.csv
│   ├── Comparendos_Barranquilla_limpio.csv
│   ├── dataset_limpio_eda.csv
│   ├── dataset_integrado.csv
│   ├── dataset_reducido.csv
│   └── dataset_categorizado_arbol.csv
│
├── src/
│   ├── __init__.py
│   ├── accidentes.py
│   ├── precipitacion.py
│   ├── comparendos.py
│   ├── integracion.py
│   ├── eda.py
│   ├── transformacion.py
│   ├── preparador_arbol.py
│   └── modelo_arbol_decision.py
│
├── analisis/
│   ├── analisis_datos.ipynb
│   ├── eda_accidentes_barranquilla.ipynb
│   ├── transformacion_escalabilidad.ipynb
│   └── arbol_decision_accidentes.ipynb
│
├── docs/
│   └── diagramas/
│       └── arbol_decision_accidentes.png
│
└── README.md
```

## 8. Ejecución del análisis exploratorio

1. Clonar o descargar el repositorio.
2. Instalar Python y las dependencias necesarias.
3. Abrir el proyecto en Visual Studio Code.
4. Abrir el notebook `analisis/eda_accidentes_barranquilla.ipynb`.
5. Verificar que la ruta del archivo `dataset/dataset_limpio_eda.csv` corresponda con la estructura local del proyecto.
6. Seleccionar el kernel de Python y ejecutar las celdas en orden.

El notebook documenta el análisis, las visualizaciones y las interpretaciones obtenidas a partir de los datos.

## 9. Conclusiones generales

El análisis exploratorio permite describir la distribución de los accidentes, la precipitación y los comparendos, así como identificar posibles valores atípicos y limitaciones en la calidad de la información.

Las correlaciones calculadas son débiles, por lo que no se identifica una asociación lineal fuerte entre las variables numéricas analizadas. Además, la cantidad de registros clasificados como `Sin dato` en la variable de lluvia limita las comparaciones relacionadas con las condiciones meteorológicas.

Estos resultados constituyen una base descriptiva para continuar con las etapas de transformación y reducción de dimensionalidad. Las conclusiones deben interpretarse teniendo en cuenta la calidad, la cobertura temporal y las características de los datos disponibles.

## 10. Estado del proyecto

El proyecto cuenta con conjuntos de datos originales y procesados, scripts de transformación y un notebook dedicado al análisis exploratorio de datos.

Se han desarrollado visualizaciones univariadas y bivariadas, acompañadas de interpretaciones, y se calcularon correlaciones para examinar las relaciones entre las variables principales.

Las siguientes actividades deben continuar según los requerimientos académicos y las etapas pendientes del proceso de minería de datos.

## 11. Árbol de decisión para la clasificación de accidentes

Se desarrolló un modelo de clasificación mediante un árbol de decisión para identificar días con una cantidad baja o alta de accidentes de tránsito en Barranquilla.

### 11.1. Objetivo del modelo

Clasificar los registros diarios en dos categorías según la cantidad de accidentes:

- **Clase 0 – Accidentes bajos:** 8 accidentes o menos.
- **Clase 1 – Accidentes altos:** más de 8 accidentes.

El umbral de 8 accidentes se estableció tomando como referencia la mediana obtenida en el análisis exploratorio de datos.

El modelo no predice el número exacto de accidentes ni determina si habrá personas fallecidas.

### 11.2. Variables utilizadas

El modelo utiliza las siguientes variables predictoras:

- `COMPARENDOS`: cantidad de comparendos registrados.
- `CLASE_ACCIDENTE`: clase del accidente, representada mediante variables binarias.
- `CLASE_VEHICULO_INFRACTOR`: clase del vehículo del infractor, representada mediante variables binarias.
- `SERVICIO_VEHICULO_INFRACTOR`: servicio del vehículo, representado mediante variables binarias.

Las variables categóricas se codificaron previamente en el conjunto de datos `dataset/dataset_categorizado_arbol.csv`.

### 11.3. Preparación y entrenamiento

La preparación de las variables se encuentra en `src/preparador_arbol.py` y el desarrollo del modelo se documenta en el notebook `analisis/arbol_decision_accidentes.ipynb`.

Los datos se dividieron en dos conjuntos:

| Conjunto | Registros | Porcentaje |
|---|---:|---:|
| Entrenamiento | 2.437 | 80 % |
| Prueba | 610 | 20 % |
| **Total** | **3.047** | **100 %** |

Se utilizó `DecisionTreeClassifier` de Scikit-learn, con una profundidad máxima de cuatro niveles y `random_state=42` para mantener reproducible la división y el entrenamiento.

### 11.4. Evaluación del modelo

Los resultados obtenidos fueron los siguientes:

| Métrica | Resultado |
|---|---:|
| Accuracy de entrenamiento | 57,49 % |
| Accuracy de prueba | 61,31 % |
| Registros de prueba clasificados correctamente | 374 de 610 |

La matriz de confusión fue:

| Resultado | Cantidad |
|---|---:|
| Verdaderos negativos | 219 |
| Falsos positivos | 112 |
| Falsos negativos | 124 |
| Verdaderos positivos | 155 |

El modelo clasificó correctamente 219 registros de accidentes bajos y 155 de accidentes altos. Sin embargo, clasificó incorrectamente 124 registros de accidentes altos como accidentes bajos.

Estos resultados indican que el modelo presenta un rendimiento limitado y que debe mejorarse antes de utilizarse para apoyar decisiones operativas.

### 11.5. Reglas de decisión

Entre las reglas identificadas se encuentran:

- Cuando la variable `CLASE_ACCIDENTE_Choque` es 0, el modelo clasifica el registro como accidentes bajos.
- Cuando hay choques, los comparendos superan 95,5, el vehículo del infractor corresponde a un automóvil y los comparendos superan 217,5, el modelo clasifica el registro como accidentes altos.

Estas reglas describen patrones identificados por el algoritmo y no demuestran relaciones causales.

### 11.6. Diagramas generados

Los diagramas del modelo se guardan en la carpeta `docs/diagramas/`:

- `arbol_decision_accidentes.png`: visualización del árbol de decisión.
- `matriz_confusion_accidentes.png`: matriz de confusión para evaluar las predicciones.

### 11.7. Conclusión del modelo

El árbol de decisión permite explorar cómo se relacionan las clases de accidentes, los comparendos y las características de los vehículos con la clasificación de la accidentalidad diaria. Su accuracy de prueba del 61,31 % muestra que todavía presenta dificultades para distinguir entre días de accidentalidad baja y alta. Por tanto, se pueden evaluar ajustes en las variables predictoras, la profundidad del árbol y otros parámetros para mejorar su desempeño.
