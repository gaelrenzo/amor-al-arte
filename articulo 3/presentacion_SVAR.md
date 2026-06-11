# PRESENTACIÓN - ARTÍCULO CIENTÍFICO SVAR
## Impacto de los choques macroeconómicos sobre la actividad económica peruana: Un análisis SVAR con datos sintéticos (2015-2024)

**Curso:** Econometría III  
**Universidad:** Universidad Nacional del Altiplano  
**Facultad:** Facultad de Ingeniería Económica  
**Docente:** [Nombre del docente]

---

## Diapositiva 1: Portada
- Título del artículo
- Curso y universidad
- Autor y docente
- Fecha

## Diapositiva 2: Estructura de la Presentación
1. Introducción
2. Marco Teórico
3. Materiales y Métodos
4. Resultados
5. Discusión
6. Conclusiones
7. Referencias

## Diapositiva 3: Introducción - Contexto
- Importancia del análisis de choques macroeconómicos
- Desafíos de la macroeconomía moderna
- Relevancia para economías emergentes
- Referencia: Sims (1980), Blanchard & Perotti (2002)

## Diapositiva 4: Introducción - Problema y Brecha
- Problema: necesidad de comprender mecanismos de transmisión en Perú
- Brecha: escasez de estudios integrales SVAR con múltiples variables
- Vacío en la literatura peruana

## Diapositiva 5: Objetivos e Hipótesis
- **General:** Analizar impacto de choques macroeconómicos sobre PIB peruano
- **Específicos:** IRF, FEVD, descomposición histórica
- **Hipótesis:** Choques fiscales y monetarios son principales fuentes de fluctuación del PIB

## Diapositiva 6: Marco Teórico - Keynesiano
- Demanda agregada y multiplicador fiscal
- Keynes (1936), Blanchard (2017), Mankiw (2020)
- Política fiscal efectiva en corto plazo
- Rigideces nominales y capacidad ociosa

## Diapositiva 7: Marco Teórico - Monetarista
- Friedman (1968): rol de la oferta monetaria
- Mecanismos de transmisión monetaria
- Canal de tasa de interés, crédito y tipo de cambio
- Taylor (1995), Bernanke & Blinder (1992)

## Diapositiva 8: Marco Teórico - SVAR
- VAR reducido vs VAR estructural
- Identificación de choques estructurales
- Descomposición de Cholesky
- Sims (1980), Kilian & Lütkepohl (2017)

## Diapositiva 9: Materiales y Métodos - Datos
- **Período:** 2015-2024 (mensual, 120 obs.)
- **Variables:** PIB, Inflación, TC, TI, M2, Gasto Público
- **Fuente:** Datos sintéticos generados en Excel
- Propósito académico y metodológico

## Diapositiva 10: Materiales y Métodos - Variables
| Variable | Descripción |
|----------|-------------|
| PIB | Producto Bruto Interno (índice) |
| INFL | Tasa de inflación (%) |
| TC | Tipo de cambio nominal |
| TI | Tasa de interés de referencia (%) |
| M2 | Oferta monetaria (log) |
| G | Gasto público (índice) |

## Diapositiva 11: Materiales y Métodos - Estrategia Econométrica
1. Pruebas de estacionariedad (ADF, PP, KPSS)
2. Selección de rezagos (AIC, BIC, HQIC, FPE)
3. Estimación VAR reducido
4. Verificación de estabilidad
5. Identificación SVAR (Cholesky)
6. Funciones Impulso-Respuesta (IRF)
7. Descomposición de Varianza (FEVD)
8. Descomposición Histórica

## Diapositiva 12: Materiales y Métodos - Identificación SVAR
**Orden de Cholesky (más exógena → más endógena):**
1. Gasto Gobierno (no responde contemporáneamente)
2. Oferta Monetaria
3. PIB
4. Inflación
5. Tipo de Cambio
6. Tasa de Interés (responde a todas)

## Diapositiva 13: Resultados - Estadísticas Descriptivas
- PIB promedio: 102.47, σ = 2.85
- Inflación promedio: 3.52%, σ = 0.98%
- TC promedio: 3.82 S/./USD
- TI promedio: 5.12%

## Diapositiva 14: Resultados - Pruebas de Estacionariedad
- Todas las variables: I(1) en niveles
- Estacionarias en primera diferencia al 5%
- Consistente con Nelson & Plosser (1982)
- VAR estimado en primeras diferencias

## Diapositiva 15: Resultados - Selección de Rezagos
- AIC: VAR(4), BIC: VAR(2), HQIC: VAR(2)
- Se selecciona VAR(4) para eliminar autocorrelación
- Consistente con Lütkepohl (2005)

## Diapositiva 16: Resultados - Estabilidad del VAR
- Todas las raíces dentro del círculo unitario
- Módulo máximo: 0.89
- **Conclusión:** Modelo estable
- IRF y FEVD son válidas

## Diapositiva 17: Resultados - Funciones Impulso-Respuesta
- **Shock de gasto público → PIB:** +0.45% inmediato, máximo +0.72% en t+3
- **Shock de tasa de interés → PIB:** -0.38% máximo en t+4 a t+6
- **Shock de oferta monetaria → PIB:** efecto positivo moderado
- Convergencia gradual (≈18 meses)

## Diapositiva 18: Resultados - FEVD (12 meses)
| Variable | Contribución al PIB |
|----------|-------------------|
| Gasto Público | 28.5% |
| Oferta Monetaria | 16.3% |
| Inflación | 12.1% |
| Tasa de Interés | 9.8% |
| Tipo de Cambio | 7.2% |
| Propio PIB | 26.1% |

## Diapositiva 19: Resultados - Descomposición Histórica
- Choques de gasto público: contribución positiva en 2021-2022
- Choques contractivos de TI: efecto negativo en 2023
- Coherente con el contexto macroeconómico peruano

## Diapositiva 20: Discusión - Principales Hallazgos
- Consistente con: Blanchard & Perotti (2002), Auerbach & Gorodnichenko (2012)
- Multiplicadores fiscales significativos
- Efectos contractivos de política monetaria confirmados
- Christiano, Eichenbaum & Evans (1999), Bernanke & Blinder (1992)

## Diapositiva 21: Discusión - Implicancias
- **Política fiscal:** Instrumento efectivo para estabilización
- **Política monetaria:** Efectiva para control inflacionario
- **Coordinación:** Fundamental para maximizar efectividad
- Limitaciones: datos sintéticos, identificación recursiva

## Diapositiva 22: Conclusiones
1. Choques fiscales y monetarios explican ~45% variabilidad del PIB
2. IRF confirman mecanismos de transmisión teóricos
3. Política fiscal: efectos más persistentes
4. Política monetaria: efectos transitorios
5. Coordinación de políticas es crucial

## Diapositiva 23: Recomendaciones
- Investigaciones futuras con datos reales
- Modelos SVAR con parámetros variables en el tiempo (Primiceri, 2005)
- Identificación con restricciones de signo (Uhlig, 2005)
- Incorporar sector externo

## Diapositiva 24: Referencias Clave
- Blanchard & Perotti (2002). QJE.
- Christiano, Eichenbaum & Evans (1999). Handbook of Macroeconomics.
- Kilian & Lütkepohl (2017). Cambridge University Press.
- Sims (1980). Econometrica.
- Primiceri (2005). Review of Economic Studies.

## Diapositiva 25: Gracias
- ¿Preguntas?
- Enlace al código: Google Colab
- Enlace a la base de datos
