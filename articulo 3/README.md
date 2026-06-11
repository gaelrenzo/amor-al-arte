# Artículo 3 — Modelo VAR Estructural (SVAR)

## Impacto de los choques macroeconómicos sobre la actividad económica peruana: Un análisis SVAR con datos sintéticos (2015-2024)

**Curso:** Econometría III  
**Universidad:** Universidad Nacional del Altiplano - Puno  
**Facultad:** Facultad de Ingeniería Económica

---

## Estructura de la carpeta

```
articulo 3/
├── 1_Articulo/                     ← Documentos del artículo
│   ├── articulo_SVAR.docx          ←   Word (APA 7ª ed.)
│   ├── articulo_SVAR_scopus.docx   ←   Word (formato Scopus)
│   ├── articulo_SVAR_scopus.pdf    ←   PDF compilado
│   └── latex/                      ←   Código fuente LaTeX
│       ├── articulo_SVAR_scopus.tex
│       └── referencias.bib
│
├── 2_Datos/                        ← Base de datos
│   └── base_datos_sintetica.xlsx   ←   Datos macroeconómicos 2015-2024
│
├── 3_Codigo/                       ← Código y scripts
│   ├── codigo_SVAR.py              ←   Código principal Python
│   ├── codigo_SVAR.ipynb           ←   Notebook Google Colab
│   ├── generar_base_datos.py       ←   Script para generar datos
│   ├── generar_articulo.py         ←   Script para generar Word APA
│   └── generar_scopus.py           ←   Script para generar Word Scopus
│
└── 4_Presentacion/                 ← Material de presentación
    └── presentacion_SVAR.md        ←   Guía de diapositivas (25 slides)
```

## Contenido del artículo

| Sección | Descripción |
|---------|-------------|
| Introducción | Contexto, problema, brecha, objetivos e hipótesis |
| Marco Teórico | Keynesianismo, monetarismo, teoría de choques, SVAR |
| Metodología | Diseño, variables, procedimiento econométrico, identificación Cholesky |
| Resultados | Estadísticas, estacionariedad, IRF, FEVD, descomposición histórica |
| Discusión | Comparación con literatura internacional y peruana |
| Conclusiones | Hallazgos principales, implicancias de política económica |
| Apéndices A-E | Matrices, tablas, diagnósticos, figuras, código |

## Variables del modelo

- **PIB** — Producto Bruto Interno (índice base 100)
- **INFLACION** — Tasa de inflación (%)
- **TIPO_CAMBIO** — Tipo de cambio nominal (S/./USD)
- **TASA_INTERES** — Tasa de interés de referencia (%)
- **OFERTA_MONETARIA** — Logaritmo de la oferta monetaria (M2)
- **GASTO_GOBIERNO** — Gasto público (índice)

## Orden de identificación (Cholesky)

1. Gasto Gobierno → 2. Oferta Monetaria → 3. PIB → 4. Inflación → 5. Tipo de Cambio → 6. Tasa de Interés

## Requisitos para ejecutar el código

```bash
pip install pandas numpy statsmodels openpyxl matplotlib seaborn python-docx
```
