# Artículo 3 — Modelo VAR Estructural (SVAR)

## Impacto de los choques macroeconómicos sobre la actividad económica peruana: Un análisis SVAR con datos sintéticos (2015-2024)

**Curso:** Econometría III  
**Universidad:** Universidad Nacional del Altiplano - Puno  
**Facultad:** Facultad de Ingeniería Económica  
**Docente:** [Nombre del docente]

---

## Contenido de la carpeta

| Archivo | Descripción |
|---------|-------------|
| `articulo_SVAR.docx` | Artículo científico completo en formato Word (APA 7ª ed.) |
| `articulo_SVAR_scopus.docx` | Artículo científico formateado para revista indexada en Scopus |
| `base_datos_sintetica.xlsx` | Base de datos macroeconómica sintética (2015-2024, 120 obs. mensuales, 6 variables) |
| `codigo_SVAR.py` | Código Python completo para estimación del modelo SVAR |
| `codigo_SVAR.ipynb` | Notebook de Google Colab para ejecución interactiva |
| `presentacion_SVAR.md` | Guía de 25 diapositivas para presentación en PowerPoint |
| `generar_base_datos.py` | Script para generar la base de datos sintética |
| `generar_articulo.py` | Script para generar el artículo en Word |

## Variables del modelo

- **PIB:** Producto Bruto Interno (índice base 100)
- **INFLACION:** Tasa de inflación (%)
- **TIPO_CAMBIO:** Tipo de cambio nominal (S/./USD)
- **TASA_INTERES:** Tasa de interés de referencia (%)
- **OFERTA_MONETARIA:** Logaritmo de la oferta monetaria (M2)
- **GASTO_GOBIERNO:** Gasto público (índice)

## Metodología

1. Pruebas de raíz unitaria (ADF, PP, KPSS)
2. Selección óptima de rezagos (AIC, BIC, HQIC, FPE)
3. Estimación del modelo VAR reducido
4. Verificación de estabilidad (raíces inversas del polinomio característico)
5. Identificación SVAR mediante descomposición de Cholesky
6. Funciones Impulso-Respuesta (IRF)
7. Descomposición de Varianza del Error de Pronóstico (FEVD)
8. Descomposición Histórica

## Orden de identificación (Cholesky)

1. Gasto Gobierno → 2. Oferta Monetaria → 3. PIB → 4. Inflación → 5. Tipo de Cambio → 6. Tasa de Interés

## Requisitos

```
pip install pandas numpy statsmodels openpyxl matplotlib seaborn python-docx
```
