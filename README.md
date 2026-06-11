# 📚 Guía de Entregables - Proyecto "Amor al Arte"

Este repositorio ha sido organizado de manera estructural y sistemática para facilitar la revisión y calificación de los trabajos correspondientes a las prácticas del curso. La estructura divide claramente los tres artículos principales, sus códigos de réplica, las bases de datos y la documentación fuente (Word, PDF y LaTeX).

---

## 🗺️ Estructura General del Repositorio

A continuación, se presenta el mapa de directorios del repositorio para su navegación:

```text
amor-al-arte/
│
├── 📂 articulo 1/                  # Conversión de Vehículo a Eléctrico (Retrofit)
│   ├── 📄 01_Informe_Conversion_EV.docx   # Informe en formato Word (.docx)
│   ├── 📄 02_Presentacion_Conversion_EV.pptx # Diapositivas de la presentación (.pptx)
│   ├── 📄 03_Informe_Conversion_EV.pdf    # Informe exportado a PDF listo para lectura
│   └── 📄 informe_conversion_ev.md        # Documentación en formato Markdown
│
├── 📂 articulo 2/                  # Modelo SVAR de 5 Variables (Trimestral 2000-2024)
│   ├── 📄 01_Informe_Articulo_Cientifico.docx # Artículo completo en formato Word (.docx)
│   ├── 📄 02_Presentacion_SVAR.pptx        # Diapositivas de la sustentación (.pptx)
│   ├── 📄 03_Base_Datos_Macroeconomica.xlsx # Datos macroeconómicos simulados (.xlsx)
│   ├── 📓 04_Notebook_Google_Colab.ipynb    # Cuaderno Jupyter/Colab interactivo con el código
│   │
│   ├── 📂 fuente_latex/                     # Código fuente y compilado del artículo académico
│   │   ├── 📄 articulo_scopus.tex           # Archivo fuente LaTeX (compilable con pdflatex)
│   │   └── 📄 articulo_scopus.pdf           # PDF final compilado con estilo Scopus (28 páginas)
│   │
│   ├── 📂 graficos/                         # Gráficos estadísticos y de resultados del modelo
│   ├── 📂 resultados/                       # Archivos CSV y TXT con datos intermedios y reportes
│   └── 📂 scripts/                          # Scripts auxiliares de Python para automatización
│
├── 📂 articulo 3/                  # Modelo SVAR de 6 Variables (Mensual 2015-2024)
│   ├── 📂 1_Articulo/                       # Informes en Word y código LaTeX del Artículo 3
│   ├── 📂 2_Datos/                          # Bases de datos y series de tiempo mensuales
│   ├── 📂 3_Codigo/                         # Jupyter Notebooks y scripts econométricos de réplica
│   ├── 📂 4_Presentacion/                   # Diapositivas de la presentación del Artículo 3
│   └── 📄 README.md                         # Guía interna para el Artículo 3
│
└── 📂 pautas_y_rubricas/            # Documentos de cátedra (guías y rúbricas del docente)
    ├── 📄 Pautas practica 10.pdf            # PDF de pautas para la Práctica 10
    └── 📄 Recomendaciones y rúbrica.docx    # Criterios y rúbrica de calificación
```

---

## 📑 Detalle de los Entregables

### 🚗 Artículo 1: Conversión de Vehículo a Eléctrico (Retrofit)
Este módulo aborda el modelamiento de ingeniería y los análisis técnicos para la conversión de un vehículo de combustión interna a propulsión 100% eléctrica.
*   **Informe Word e informe PDF**: Ambos documentos son idénticos en cuanto a estructura, ecuaciones y análisis, variando únicamente el formato de entrega física/digital.
*   **Presentación PPTX**: Diseñada para la exposición de los aspectos fundamentales del retrofit (selección del motor, cálculo de baterías y autonomía).

### 📈 Artículo 2: Modelo SVAR de 5 Variables (Perú, 2000-2024)
Este artículo consiste en un análisis macroeconómico cuantitativo para el Perú empleando un modelo **SVAR (Structural Vector Autoregression)** con 5 variables (PBI, Inflación, Tasa de Interés, Tipo de Cambio Real y Gasto Público) recolectadas de forma trimestral (84 observaciones).
*   **Notebook Interactiva (Google Colab)**:
    *   Contiene todo el flujo econométrico documentado paso a paso: pruebas de raíces unitarias (ADF), selección de rezagos, estimación del VAR, identificación estructural a través de restricciones de corto plazo (matriz B), funciones impulso-respuesta (IRF), descomposición de varianza (FEVD) y descomposición histórica de shocks.
    *   👉 **[Acceder al Google Colab del Artículo 2](https://colab.research.google.com/github/gaelrenzo/amor-al-arte/blob/main/articulo%202/04_Notebook_Google_Colab.ipynb)**
*   **Artículo Scopus en LaTeX**:
    *   Ubicado en `articulo 2/fuente_latex/`.
    *   El archivo principal es `articulo_scopus.tex` y genera `articulo_scopus.pdf` (un artículo formal de 28 páginas con formato de revista indizada, incluyendo el código fuente econométrico completo adjunto en los anexos).
    *   *Nota: Se corrigieron los problemas de compilación causados por los caracteres URL escapando los caracteres especiales del enlace de GitHub.*
*   **Base de Datos**: `03_Base_Datos_Macroeconomica.xlsx` contiene las series brutas y las transformadas utilizadas.
*   **Diapositivas**: `02_Presentacion_SVAR.pptx` incluye la síntesis del artículo en 21 láminas para la sustentación académica.

### 📊 Artículo 3: Modelo SVAR de 6 Variables (Mensual 2015-2024)
Corresponde a la extensión del análisis macroeconómico mediante un modelo de 6 variables con datos de frecuencia mensual, estructurado en carpetas numeradas del 1 al 4 para guiar la lectura secuencial de los entregables (Artículos, Datos, Códigos y Presentaciones).

---

## 🛠️ Instrucciones de Réplica de Resultados (Artículo 2)

Si desea ejecutar localmente los scripts de simulación y estimación del Artículo 2:

1.  **Requisitos previos**:
    Asegúrese de contar con Python 3.8+ instalado y las librerías necesarias ejecutando:
    ```bash
    pip install statsmodels pandas numpy matplotlib seaborn openpyxl
    ```
2.  **Ejecución de la Estimación**:
    Ejecute el script de econometría principal en su terminal:
    ```bash
    python "articulo 2/scripts/run_svar_econometrics.py"
    ```
    Esto recalculará las matrices del modelo SVAR y actualizará las tablas en `articulo 2/resultados/` y las figuras en `articulo 2/graficos/`.

3.  **Compilación del Documento LaTeX**:
    Si desea modificar el manuscrito en LaTeX, puede compilarlo desde la carpeta `articulo 2/fuente_latex` ejecutando:
    ```bash
    pdflatex articulo_scopus.tex
    ```

---
*Cualquier consulta o aclaración respecto a las rutas o ejecuciones del código, por favor revisar el Google Colab enlazado en la sección correspondiente.*
