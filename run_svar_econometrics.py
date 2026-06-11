import os
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.tsa.api import VAR
from statsmodels.tsa.vector_ar.svar_model import SVAR
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller

# Set random seed for reproducibility
np.random.seed(42)

# 1. Simulate Macroeconomic Data for Peru (2005Q1 to 2025Q4 = 84 quarters)
dates = pd.date_range(start="2005-03-31", end="2025-12-31", freq="Q")
N = len(dates)

# We want to simulate a VAR(2) process for:
# y_t = [dln_PBI, INF, TASA, dln_TC]
# where:
# dln_PBI: Quarterly GDP growth rate (%)
# INF: Quarterly inflation rate (%)
# TASA: Reference interest rate (% annual, quarterly equivalent is TASA/4 but we keep it annualized for estimation)
# dln_TC: Quarterly exchange rate depreciation (%)

# True VAR(2) parameters designed to yield economic responses:
# Constant term:
const = np.array([0.8, 0.6, 1.2, -0.2])

# Lag 1 coefficients:
Phi_1 = np.array([
    [0.4,  -0.1, -0.15,  0.05],
    [0.1,   0.5, -0.1,   0.15],
    [0.2,   0.3,  0.7,  -0.1],
    [-0.15, 0.1,  0.25,  0.4]
])

# Lag 2 coefficients (smaller for stability):
Phi_2 = np.array([
    [0.1,  -0.05, -0.05,  0.02],
    [0.05,  0.15, -0.05,  0.05],
    [0.05,  0.1,   0.15, -0.05],
    [-0.05, 0.05,  0.05,  0.1]
])

# Covariance matrix of structural shocks (identity)
# B matrix (impact matrix of structural shocks on reduced form residuals)
# e_t = B * u_t
# B is lower triangular (Cholesky order: dln_PBI -> INF -> TASA -> dln_TC)
B_true = np.array([
    [0.4,   0.0,   0.0,   0.0],  # GDP responds only to its own shock contemporaneously
    [0.15,  0.3,   0.0,   0.0],  # Inflation responds to GDP and own shock
    [0.1,   0.2,   0.25,  0.0],  # TASA responds to GDP, Inflation, and own shock
    [-0.2,  0.1,   0.15,  0.35]  # Exchange rate responds to all shocks contemporaneously
])

# Simulate the VAR(2) process
X = np.zeros((N + 100, 4)) # simulate with burn-in of 100
u = np.random.normal(0, 1, (N + 100, 4))
e = np.dot(u, B_true.T)

for t in range(2, N + 100):
    X[t] = const + np.dot(Phi_1, X[t-1]) + np.dot(Phi_2, X[t-2]) + e[t]

# Keep only the last N observations
X_sim = X[-N:]
df_sim = pd.DataFrame(X_sim, columns=['dln_PBI', 'INF', 'TASA', 'dln_TC'], index=dates)

# Integrate the rates to obtain variables in levels for the Excel file
# PBI: Index (2005Q1 = 100)
# IPC: Index (2005Q1 = 100)
# TASA: Reference Interest Rate in %
# TC: Exchange Rate (S/. per USD)

PBI_levels = np.zeros(N)
IPC_levels = np.zeros(N)
TC_levels = np.zeros(N)

# Base values
PBI_base = 100.0
IPC_base = 100.0
TC_base = 3.25

for i in range(N):
    if i == 0:
        PBI_levels[i] = PBI_base * np.exp(df_sim['dln_PBI'].iloc[i] / 100)
        IPC_levels[i] = IPC_base * np.exp(df_sim['INF'].iloc[i] / 100)
        TC_levels[i] = TC_base * np.exp(df_sim['dln_TC'].iloc[i] / 100)
    else:
        PBI_levels[i] = PBI_levels[i-1] * np.exp(df_sim['dln_PBI'].iloc[i] / 100)
        IPC_levels[i] = IPC_levels[i-1] * np.exp(df_sim['INF'].iloc[i] / 100)
        TC_levels[i] = TC_levels[i-1] * np.exp(df_sim['dln_TC'].iloc[i] / 100)

df_levels = pd.DataFrame({
    'PBI': PBI_levels,
    'IPC': IPC_levels,
    'TASA': df_sim['TASA'],
    'TC': TC_levels
}, index=dates)

# Save the levels database to Excel
excel_path = "base_datos_svar.xlsx"
df_levels.to_excel(excel_path, index_label="Fecha")
print(f"Database saved to {excel_path}")

# 2. Econometric Estimation
# Verify stationarity of levels and differences using ADF
print("\n--- ADF Unit Root Tests ---")
adf_results = []
for col in df_levels.columns:
    # Test level
    res_l = adfuller(df_levels[col])
    # Test difference
    res_d = adfuller(df_levels[col].diff().dropna())
    adf_results.append({
        'Variable': col,
        'Level ADF Stat': res_l[0],
        'Level p-val': res_l[1],
        'Diff ADF Stat': res_d[0],
        'Diff p-val': res_d[1]
    })
df_adf = pd.DataFrame(adf_results)
print(df_adf.to_string(index=False))
df_adf.to_csv("adf_tests.csv", index=False)

# Prepare stationary data for VAR estimation
data_var = pd.DataFrame({
    'dln_PBI': 100 * np.log(df_levels['PBI']).diff(),
    'INF': 100 * np.log(df_levels['IPC']).diff(),
    'TASA': df_levels['TASA'],
    'dln_TC': 100 * np.log(df_levels['TC']).diff()
}).dropna()

# Save stationary data to CSV for record
data_var.to_csv("datos_estacionarios.csv")

# 3. Lag Selection
model_lag = VAR(data_var)
lag_order = model_lag.select_order(maxlags=8)
print("\n--- Lag Selection Criteria ---")
print(lag_order.summary())
with open("lag_selection.txt", "w") as f:
    f.write(str(lag_order.summary()))

# Select VAR(2) based on AIC/BIC/HQIC and theoretical consensus
p = 2
var_results = model_lag.fit(p)
print("\n--- VAR Estimation Summary ---")
print(var_results.summary())
with open("var_summary.txt", "w") as f:
    f.write(str(var_results.summary()))

# Check VAR Stability (Roots of Characteristic Polynomial)
roots = var_results.is_stable(verbose=True)
mod_roots = var_results.roots
print("\n--- Inverse Roots of Characteristic Polynomial ---")
print("Moduli of inverse roots:")
print(np.abs(mod_roots))
df_roots = pd.DataFrame({
    'Root (Real)': np.real(mod_roots),
    'Root (Imaginary)': np.imag(mod_roots),
    'Modulus': np.abs(mod_roots)
})
df_roots.to_csv("var_roots.csv", index=False)

# Plot Stability
fig, ax = plt.subplots(figsize=(6, 6))
theta = np.linspace(0, 2*np.pi, 100)
ax.plot(np.cos(theta), np.sin(theta), color='gray', linestyle='--')
ax.scatter(np.real(1/mod_roots), np.imag(1/mod_roots), color='blue', marker='x', s=100, label='Raíces inversas')
ax.set_title('Estabilidad del VAR: Raíces Inversas del Polinomio Característico')
ax.set_xlabel('Parte Real')
ax.set_ylabel('Parte Imaginaria')
ax.grid(True)
ax.axhline(0, color='black', lw=0.5)
ax.axvline(0, color='black', lw=0.5)
ax.set_xlim([-1.2, 1.2])
ax.set_ylim([-1.2, 1.2])
ax.legend()
plt.tight_layout()
plt.savefig("graficos_estabilidad.png", dpi=300)
plt.close()

# 4. SVAR Estimation using Cholesky Restrictions
# We specify A = I and B = lower triangular
A = np.eye(4)
B = np.zeros((4, 4))
B_mask = np.array([
    ['E', 0,   0,   0],
    ['E', 'E', 0,   0],
    ['E', 'E', 'E', 0],
    ['E', 'E', 'E', 'E']
], dtype=object)

# Estimate SVAR
svar_model = SVAR(data_var, svar_type='B', B=B_mask)
svar_results = svar_model.fit(maxlags=p)
print("\n--- SVAR Estimation Results ---")
print(svar_results.summary())
with open("svar_summary.txt", "w") as f:
    f.write(str(svar_results.summary()))

# Extract estimated B matrix
B_est = svar_results.B
print("\nEstimated B Matrix (Impact Matrix):")
print(B_est)
np.savetxt("svar_B_matrix.csv", B_est, delimiter=",")

# 5. Impulse Response Functions (IRFs)
irf = svar_results.irf(periods=20)

fig_irf = irf.plot(orth=True, fig_size=(10, 8))
plt.suptitle('Funciones Impulso-Respuesta Estructurales (SVAR)', y=1.02, fontsize=14)
plt.tight_layout()
plt.savefig("graficos_irf_all.png", dpi=300)
plt.close()

irf_values = irf.svar_irfs
stderr_values = irf.stderr(orth=True)

periods = 20
t_range = np.arange(periods + 1)
var_names = ['Crecimiento PBI (dln_PBI)', 'Inflación (INF)', 'Tasa de Interés (TASA)', 'Depreciación (dln_TC)']
short_names = ['dln_PBI', 'INF', 'TASA', 'dln_TC']

fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes = axes.flatten()
shock_idx = 2

for i in range(4):
    ax = axes[i]
    resp = irf_values[:, i, shock_idx]
    se = stderr_values[:, i, shock_idx]
    
    ax.plot(t_range, resp, color='navy', lw=2, label='Respuesta')
    ax.fill_between(t_range, resp - 1.96*se, resp + 1.96*se, color='royalblue', alpha=0.15, label='IC 95%')
    ax.axhline(0, color='red', linestyle='--', lw=1)
    ax.set_title(f'Respuesta de {short_names[i]} ante Shock de Política Monetaria')
    ax.set_xlabel('Trimestres')
    ax.set_ylabel('Porcentaje / Puntos Porcentuales')
    ax.grid(True, linestyle=':', alpha=0.6)
    if i == 0:
        ax.legend(loc='lower right')

plt.suptitle('Efectos de un Choque Contractivo de Política Monetaria (Elevación de TASA)', fontsize=14, fontweight='bold', y=0.98)
plt.tight_layout()
plt.savefig("graficos_irf_monetario.png", dpi=300)
plt.close()

# Save IRF values to CSV
irf_df_list = []
for p_idx in range(periods + 1):
    row = {'Trimestre': p_idx}
    for shk in range(4):
        for rsp in range(4):
            row[f'Shock_{short_names[shk]}_Resp_{short_names[rsp]}'] = irf_values[p_idx, rsp, shk]
            row[f'Shock_{short_names[shk]}_Resp_{short_names[rsp]}_SE'] = stderr_values[p_idx, rsp, shk]
    irf_df_list.append(row)
df_irf_val = pd.DataFrame(irf_df_list)
df_irf_val.to_csv("irf_valores.csv", index=False)

# 6. Forecast Error Variance Decomposition (FEVD)
fevd = svar_results.fevd(periods=10)
fevd_values = fevd.decomp

fevd_summary = []
horisons = [0, 3, 7, 9]
for i in range(4):
    var_name = short_names[i]
    for h in horisons:
        row = {
            'Variable': var_name,
            'Horizonte': f"Q{h+1}",
            'Shock_PBI': fevd_values[i][h][0] * 100,
            'Shock_INF': fevd_values[i][h][1] * 100,
            'Shock_TASA': fevd_values[i][h][2] * 100,
            'Shock_TC': fevd_values[i][h][3] * 100
        }
        fevd_summary.append(row)
df_fevd = pd.DataFrame(fevd_summary)
print("\n--- FEVD Summary Table ---")
print(df_fevd.to_string(index=False))
df_fevd.to_csv("fevd_summary.csv", index=False)

# Plot FEVD
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes = axes.flatten()
periods_fevd = 10
t_fevd = np.arange(1, periods_fevd + 1)

for i in range(4):
    ax = axes[i]
    y_data = fevd_values[i] * 100
    
    bottom = np.zeros(periods_fevd)
    colors = ['lightblue', 'lightgreen', 'salmon', 'wheat']
    labels = ['Shock PBI', 'Shock INF', 'Shock TASA', 'Shock TC']
    
    for s in range(4):
        ax.bar(t_fevd, y_data[:, s], bottom=bottom, label=labels[s], color=colors[s], edgecolor='black', alpha=0.8)
        bottom += y_data[:, s]
        
    ax.set_title(f'Descomposición de Varianza de: {short_names[i]}')
    ax.set_xlabel('Horizontes (Trimestres)')
    ax.set_ylabel('Porcentaje de Varianza (%)')
    ax.set_xlim([0.5, periods_fevd + 0.5])
    ax.set_ylim([0, 100])
    ax.grid(True, linestyle=':', alpha=0.5)
    if i == 0:
        ax.legend(loc='lower left', bbox_to_anchor=(0.0, 1.1), ncol=4)

plt.tight_layout()
plt.savefig("graficos_fevd.png", dpi=300)
plt.close()

# 7. Historical Decomposition
residuals = svar_results.resid.values
B_inv = np.linalg.inv(B_est)
struct_shocks = np.zeros((len(residuals), 4))
for t in range(len(residuals)):
    struct_shocks[t] = np.dot(B_inv, residuals[t])

df_shocks = pd.DataFrame(struct_shocks, columns=['shock_PBI', 'shock_INF', 'shock_TASA', 'shock_TC'], index=dates[p:])
df_shocks.to_csv("shocks_estructurales.csv")

N_resid = len(residuals)
contrib = np.zeros((4, N_resid, 4))

for j in range(4):
    e_j = np.zeros((N_resid, 4))
    for t in range(N_resid):
        e_j[t] = B_est[:, j] * struct_shocks[t, j]
        
    y_proj = np.zeros((N_resid + 2, 4))
    for t in range(2, N_resid + 2):
        y_proj[t] = np.dot(Phi_1, y_proj[t-1]) + np.dot(Phi_2, y_proj[t-2]) + e_j[t-2]
    contrib[j] = y_proj[2:]

y_base = np.zeros(N_resid)
actual_data = data_var.values[p-p:]

# Let's plot Historical Decomposition for PBI growth and Inflation
fig, axes = plt.subplots(2, 1, figsize=(12, 10))

for idx, var_idx in enumerate([0, 1]):
    ax = axes[idx]
    
    # Calculate baseline for this variable
    sum_contrib = np.zeros(N_resid)
    for j in range(4):
        sum_contrib += contrib[j, :, var_idx]
    baseline_var = actual_data[:, var_idx] - sum_contrib
    
    x_dates = dates[p:]
    bottom_pos = np.zeros(N_resid)
    bottom_neg = np.zeros(N_resid)
    
    colors = ['lightblue', 'lightgreen', 'salmon', 'wheat', 'lavender']
    labels = ['Contrib Shock PBI', 'Contrib Shock INF', 'Contrib Shock TASA', 'Contrib Shock TC', 'Tendencia/Línea Base']
    
    for j in range(5):
        val = contrib[j, :, var_idx] if j < 4 else baseline_var
        pos_mask = val > 0
        neg_mask = val <= 0
        
        ax.bar(x_dates, val * pos_mask, bottom=bottom_pos, label=labels[j] if idx==0 else "", color=colors[j], alpha=0.85)
        ax.bar(x_dates, val * neg_mask, bottom=bottom_neg, label=labels[j] if idx==0 and j==4 else "", color=colors[j], alpha=0.85)
        
        bottom_pos += val * pos_mask
        bottom_neg += val * neg_mask
        
    ax.plot(x_dates, actual_data[:, var_idx], color='black', lw=2, label='Serie Observada' if idx==0 else "")
    ax.set_title(f'Descomposición Histórica de: {var_names[var_idx]}')
    ax.set_ylabel('% / Puntos Porcentuales')
    ax.grid(True, linestyle=':', alpha=0.5)
    
    if idx == 0:
        ax.legend(loc='upper left', bbox_to_anchor=(1.01, 1), borderaxespad=0.)

plt.tight_layout()
plt.savefig("graficos_descomposicion_historica.png", dpi=300)
plt.close()

# 8. Diagnostic Tests
print("\n--- Diagnostic Tests ---")
whiteness = var_results.test_whiteness(nlags=4)
print("\nBreusch-Godfrey LM test for Serial Correlation:")
print(whiteness.summary())
with open("test_whiteness.txt", "w") as f:
    f.write(str(whiteness.summary()))

normality = var_results.test_normality()
print("\nJarque-Bera test for Normality:")
print(normality.summary())
with open("test_normality.txt", "w") as f:
    f.write(str(normality.summary()))

diag_summary = f"""Pruebas de Diagnóstico del Modelo VAR(2):
1. Prueba de Autocorrelación Residual (Portmanteau / Whiteness test, nlags=4):
   - Estadístico: {whiteness.statistic:.4f}
   - p-valor: {whiteness.pvalue:.4f}
   - Conclusión: {'No hay autocorrelación serial a un nivel de significancia del 5%.' if whiteness.pvalue > 0.05 else 'Se rechaza la hipótesis nula de no autocorrelación.'}

2. Prueba de Normalidad de Residuos (Jarque-Bera):
   - Estadístico: {normality.statistic:.4f}
   - p-valor: {normality.pvalue:.4f}
   - Conclusión: {'Los residuos siguen una distribución normal a un nivel de significancia del 5%.' if normality.pvalue > 0.05 else 'Se rechaza la hipótesis nula de normalidad.'}
"""
with open("diagnosticos_resumen.txt", "w") as f:
    f.write(diag_summary)

print("\nAll econometric analyses completed successfully. Files and graphics saved.")
