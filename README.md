# Minería de Datos - Accidentes de Tránsito en Barranquilla

## Descripción

Proyecto de minería de datos enfocado en el análisis de accidentes de tránsito en Barranquilla, integrando información de accidentalidad, precipitación y comparendos para realizar procesos de transformación, escalamiento y reducción de datos.

## Objetivo

Analizar la relación entre los accidentes de tránsito, las condiciones de precipitación y los comparendos registrados en Barranquilla, aplicando técnicas de minería de datos para encontrar patrones y reducir la dimensionalidad de la información.

## Datasets

### 1. Accidentalidad en Barranquilla

Dataset obtenido de Datos Abiertos Colombia.

Contiene **28.523 registros y 11 columnas**:

* `FECHA_ACCIDENTE`
* `HORA_ACCIDENTE`
* `GRAVEDAD_ACCIDENTE`
* `CLASE_ACCIDENTE`
* `SITIO_EXACTO_ACCIDENTE`
* `CANT_HERIDOS_EN_SITIO_ACCIDENTE`
* `CANT_MUERTOS_EN_SITIO_ACCIDENTE`
* `CANTIDAD_ACCIDENTES`
* `AÑO_ACCIDENTE`
* `MES_ACCIDENTE`
* `DIA_ACCIDENTE`

### 2. Precipitación

Dataset obtenido de Datos Abiertos Colombia / IDEAM.

Contiene registros de precipitación para Barranquilla y variables relacionadas con las estaciones de medición, fecha, ubicación y unidad de medida.

La variable principal utilizada es `valorobservado`, correspondiente a la precipitación registrada en milímetros.

### 3. Comparendos

Dataset de comparendos de tránsito de Barranquilla.

Contiene **357.743 registros y 9 columnas**:

* `fecha_comparendo`
* `COD_INFRACCION`
* `DESC_INFRACCION`
* `TIPO_INFRACCION`
* `SERVICIO_VEHICULO_INFRACTOR`
* `CLASE_VEHICULO_INFRACTOR`
* `CANTIDAD_INFRACCIONES`
* `Tipo Camara`
* `Camara_y_direccion`

## Integración de los datos

Los tres datasets se procesan y relacionan mediante la fecha, obteniendo un único conjunto de datos:

`dataset/dataset_integrado.csv`

El dataset integrado contiene **3047 registros y 11 variables** relacionadas con accidentes, gravedad, clase de accidente, precipitación, lluvia y comparendos.

## Transformación y reducción

El proceso se encuentra organizado en la clase:

`src/transformacion.py`

Se realizan:

* Tratamiento de valores nulos.
* Codificación de variables categóricas.
* Comparación entre diferentes métodos de escalamiento.
* Escalamiento mediante `RobustScaler`.
* Reducción de dimensionalidad mediante PCA.

El proceso se documenta principalmente en:

`analisis/transformacion_escalabilidad.ipynb`

El análisis general del proyecto se encuentra en:

`analisis/analisis_datos.ipynb`

## PCA

Se seleccionaron **5 componentes principales**, conservando aproximadamente el **90,83 % de la varianza**.

El resultado se guarda en:

`dataset/dataset_reducido.csv`

El dataset reducido contiene **3047 registros y 7 columnas**:

* `FECHA`
* `PRECIPITACION_FALTANTE`
* `PC1`
* `PC2`
* `PC3`
* `PC4`
* `PC5`

## Visualizaciones

El proyecto incluye:

* Varianza acumulada de los componentes principales.
* Visualización de PC1 frente a PC2 para identificar patrones comportamentales.

## Estructura del proyecto

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
│   ├── dataset_integrado.csv
│   └── dataset_reducido.csv
│
├── src/
│   ├── __init__.py
│   ├── accidentes.py
│   ├── precipitacion.py
│   ├── comparendos.py
│   ├── integracion.py
│   └── transformacion.py
│
├── analisis/
│   ├── analisis_datos.ipynb
│   └── transformacion_escalabilidad.ipynb
│
└── README.md
```

## Resultado final

El proyecto permite integrar tres fuentes de información y aplicar un proceso de **transformación, escalamiento y reducción de dimensionalidad**, obteniendo un dataset reducido que conserva aproximadamente el **90,83 % de la variabilidad de los datos**.
