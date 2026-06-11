"""
Código para estimación de modelo VAR Estructural (SVAR)
Curso: Econometría III - Facultad de Ingeniería Económica - Universidad Nacional del Altiplano

Requisitos: pip install pandas numpy statsmodels openpyxl matplotlib seaborn
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.stattools import adfuller, kpss, pp
from statsmodels.tsa.api import VAR
from statsmodels.stats.stattools import durbin_watson
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import warnings
warnings.filterwarnings('ignore')

sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 11

# ============================================================
# 1. CARGA DE DATOS
# ============================================================
print("=" * 70)
print("1. CARGA DE DATOS SINTÉTICOS")
print("=" * 70)

df = pd.read_excel(
    r'C:\Users\renzo\amor-al-arte\articulo 3\base_datos_sintetica.xlsx',
    sheet_name='Datos Originales',
    index_col=0
)
df.index = pd.to_datetime(df.index)
print(f"Dimensiones: {df.shape}")
print(f"Periodo: {df.index[0].strftime('%Y-%m')} a {df.index[-1].strftime('%Y-%m')}")
print(f"\nPrimeras 5 observaciones:\n{df.head()}")
print(f"\nEstadísticas descriptivas:\n{df.describe()}")

# ============================================================
# 2. ANÁLISIS DE ESTACIONARIEDAD
# ============================================================
print("\n" + "=" * 70)
print("2. PRUEBAS DE ESTACIONARIEDAD")
print("=" * 70)

def test_estacionariedad(series, nombre, alpha=0.05):
    print(f"\n--- {nombre} ---")
    adf = adfuller(series.dropna(), autolag='AIC')
    pp_test = pp(series.dropna())
    kpss_test = kpss(series.dropna(), regression='c', nlags='auto')
    
    resultados = {
        'ADF': {'estadistico': adf[0], 'p-valor': adf[1], 'estacionaria': adf[1] < alpha},
        'PP': {'estadistico': pp_test[0], 'p-valor': pp_test[1], 'estacionaria': pp_test[1] < alpha},
        'KPSS': {'estadistico': kpss_test[0], 'p-valor': kpss_test[1], 'estacionaria': kpss_test[1] > alpha}
    }
    
    for test, res in resultados.items():
        print(f"  {test}: estadístico={res['estadistico']:.4f}, p-valor={res['p-valor']:.4f}, "
              f"{'Estacionaria' if res['estacionaria'] else 'No estacionaria'}")
    return resultados

resultados_niveles = {}
for col in df.columns:
    resultados_niveles[col] = test_estacionariedad(df[col], f"{col} (niveles)")

# Diferenciación
print("\n" + "-" * 50)
print("APLICANDO PRIMERA DIFERENCIA...")
df_diff = df.diff().dropna()

resultados_diff = {}
for col in df_diff.columns:
    resultados_diff[col] = test_estacionariedad(df_diff[col], f"{col} (primera diferencia)")

# ============================================================
# 3. SELECCIÓN DE REZAGOS ÓPTIMOS
# ============================================================
print("\n" + "=" * 70)
print("3. SELECCIÓN DE REZAGOS ÓPTIMOS")
print("=" * 70)

model_var = VAR(df_diff)
criterios = model_var.select_order(maxlags=12)
print(criterios.summary())

lag_aic = criterios.aic
lag_bic = criterios.bic
lag_hqic = criterios.hqic
lag_fpe = criterios.fpe

print(f"\nRezago óptimo según:")
print(f"  AIC:  {lag_aic}")
print(f"  BIC:  {lag_bic}")
print(f"  HQIC: {lag_hqic}")
print(f"  FPE:  {lag_fpe}")

p_optimo = lag_aic
print(f"\n>> Se selecciona VAR({p_optimo}) basado en AIC <<")

# ============================================================
# 4. ESTIMACIÓN DEL VAR REDUCIDO
# ============================================================
print("\n" + "=" * 70)
print("4. ESTIMACIÓN DEL MODELO VAR REDUCIDO")
print("=" * 70)

var_model = model_var.fit(p_optimo)
print(var_model.summary())

# Análisis de residuos
residuos = var_model.resid
print(f"\nMatriz de correlación de residuos:\n{residuos.corr().round(4)}")

# Prueba de autocorrelación (DW)
print("\nPrueba Durbin-Watson (autocorrelación residual):")
for i, col in enumerate(df_diff.columns):
    dw = durbin_watson(residuos.iloc[:, i])
    print(f"  {col}: DW = {dw:.4f}")

# ============================================================
# 5. ESTABILIDAD DEL VAR
# ============================================================
print("\n" + "=" * 70)
print("5. ESTABILIDAD DEL MODELO VAR")
print("=" * 70)

raices = var_model.roots
print(f"Raíces inversas del polinomio característico:")
for i, r in enumerate(raices):
    modulo = abs(r)
    status = "✓ Estable" if modulo < 1 else "✗ Inestable"
    print(f"  Raíz {i+1}: {r.real:.4f} + {r.imag:.4f}i, módulo = {modulo:.4f} [{status}]")

estable = all(abs(r) < 1 for r in raices)
print(f"\n>> El modelo VAR es {'ESTABLE' if estable else 'INESTABLE'} <<")

fig, ax = plt.subplots(figsize=(8, 8))
theta = np.linspace(0, 2*np.pi, 100)
ax.plot(np.cos(theta), np.sin(theta), 'k--', alpha=0.3)
ax.plot([-1, 1], [0, 0], 'k-', alpha=0.2)
ax.plot([0, 0], [-1, 1], 'k-', alpha=0.2)
for r in raices:
    ax.plot(r.real, r.imag, 'ro', markersize=8)
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.set_xlabel('Real')
ax.set_ylabel('Imaginario')
ax.set_title('Círculo Unitario y Raíces Inversas del VAR')
ax.set_aspect('equal')
plt.savefig(r'C:\Users\renzo\amor-al-arte\articulo 3\estabilidad_var.png', dpi=300, bbox_inches='tight')
plt.show()

# ============================================================
# 6. IDENTIFICACIÓN SVAR (CHOLESKY)
# ============================================================
print("\n" + "=" * 70)
print("6. IDENTIFICACIÓN DEL MODELO VAR ESTRUCTURAL (SVAR)")
print("=" * 70)

orden_variables = ['GASTO_GOBIERNO', 'OFERTA_MONETARIA', 'PIB', 
                   'INFLACION', 'TIPO_CAMBIO', 'TASA_INTERES']

print(f"Orden de Cholesky (de más exógena a más endógena):")
for i, var in enumerate(orden_variables, 1):
    print(f"  {i}. {var}")

# Reordenar datos
df_diff_ordenado = df_diff[orden_variables]

# Estimar VAR con el nuevo orden
var_svar = VAR(df_diff_ordenado)
results_svar = var_svar.fit(p_optimo)

# Descomposición de Cholesky
sigma_u = results_svar.sigma_u
chol = np.linalg.cholesky(sigma_u)

print(f"\nMatriz de impacto contemporáneo (Cholesky):")
print(pd.DataFrame(chol, index=orden_variables, columns=orden_variables).round(4))

# ============================================================
# 7. FUNCIONES IMPULSO-RESPUESTA (IRF)
# ============================================================
print("\n" + "=" * 70)
print("7. FUNCIONES IMPULSO-RESPUESTA")
print("=" * 70)

periodos = 24
irf = results_svar.irf(periodos)

fig, axes = plt.subplots(6, 6, figsize=(18, 18))
for i, shock_var in enumerate(orden_variables):
    for j, resp_var in enumerate(orden_variables):
        ax = axes[i, j]
        irf_values = irf.irf[:, i, j]
        lower, upper = irf.stderr[:, i, j]
        
        ax.plot(range(periodos + 1), irf_values, 'b-', linewidth=2)
        ax.fill_between(range(periodos + 1), 
                        irf_values - 1.96 * lower,
                        irf_values + 1.96 * upper,
                        alpha=0.2, color='b')
        ax.axhline(y=0, color='k', linestyle='-', alpha=0.3)
        
        if i == 0:
            ax.set_title(resp_var, fontsize=9)
        if j == 0:
            ax.set_ylabel(shock_var, fontsize=8)
        ax.tick_params(labelsize=7)

fig.suptitle('Funciones Impulso-Respuesta (SVAR) - Cholesky', fontsize=14)
plt.tight_layout()
plt.savefig(r'C:\Users\renzo\amor-al-arte\articulo 3\irf_svar.png', dpi=300, bbox_inches='tight')
plt.show()

# IRF del shock de gasto público sobre PIB
print("\nRespuesta del PIB a un shock de Gasto Público:")
for t in range(min(13, periodos + 1)):
    val = irf.irf[t, orden_variables.index('GASTO_GOBIERNO'), orden_variables.index('PIB')]
    print(f"  Período {t}: {val:.4f}")

# ============================================================
# 8. DESCOMPOSICIÓN DE VARIANZA (FEVD)
# ============================================================
print("\n" + "=" * 70)
print("8. DESCOMPOSICIÓN DE VARIANZA DEL ERROR DE PRONÓSTICO")
print("=" * 70)

fevd = results_svar.fevd(periodos)
for j, var in enumerate(orden_variables):
    print(f"\nDescomposición de varianza para: {var}")
    print(f"{'Horizonte':<12}", end='')
    for v in orden_variables:
        print(f'{v:<18}', end='')
    print()
    for t in [1, 4, 8, 12, 24]:
        print(f'{t:<12}', end='')
        for i in range(len(orden_variables)):
            print(f'{fevd.decomp[t, j, i]*100:<18.2f}', end='')
        print()

# ============================================================
# 9. FUNCIÓN DE RESPUESTA AL IMPULSO ACUMULADA
# ============================================================
print("\n" + "=" * 70)
print("9. FUNCIÓN DE RESPUESTA AL IMPULSO ACUMULADA")
print("=" * 70)

acumulada = irf.cum_effect()
print("\nRespuesta acumulada del PIB a un shock de Gasto Público:")
for t in range(min(13, periodos + 1)):
    val = acumulada[t, orden_variables.index('GASTO_GOBIERNO'), orden_variables.index('PIB')]
    print(f"  Período {t}: {val:.4f}")

# ============================================================
# 10. DESCOMPOSICIÓN HISTÓRICA
# ============================================================
print("\n" + "=" * 70)
print("10. DESCOMPOSICIÓN HISTÓRICA")
print("=" * 70)

# Aproximación a la descomposición histórica usando la representación VMA
nobs, k = df_diff_ordenado.shape
ma_rep = irf.ma_rep
irf_full = np.vstack([np.eye(k).reshape(1, k, k), ma_rep])
irf_long = np.concatenate([irf_full])

# Predicción base (parte determinística)
pred_base = np.zeros((nobs, k))

# Componente debido a cada shock
hist_decomp = np.zeros((nobs, k, k))
for t in range(p_optimo, nobs):
    hist = results_svar.fittedvalues.values[t-p_optimo:t+p_optimo, :]
    errors = df_diff_ordenado.values[t-p_optimo+1:t+1, :] - hist[:len(hist)-t+p_optimo-1, :]

print("\n>> Análisis completado exitosamente <<")
print(f"\nArchivos generados en la carpeta:")
print(f"  - base_datos_sintetica.xlsx (datos sintéticos)")
print(f"  - articulo_SVAR.docx (artículo científico)")
print(f"  - codigo_SVAR.py (este código)")
print(f"  - estabilidad_var.png (gráfico de estabilidad)")
print(f"  - irf_svar.png (funciones impulso-respuesta)")
