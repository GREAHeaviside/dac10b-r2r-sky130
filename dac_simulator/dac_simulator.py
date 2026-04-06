import matplotlib.pyplot as plt
import numpy as np

# Importamos el simulador matricial desde el módulo local
from mismatch_simulation import barrer_codigos_dac

# --- 1. Configuración de parámetros ---
bits = 10          
V_ref = 3.3       
R_nominal = 10000.0
semilla = 0

# --- 2. Generación de los datos ---
codigos, V_real = barrer_codigos_dac(n=bits, R_nom=R_nominal, seed=semilla, V_ref=V_ref)

V_LSB = V_ref / (2**bits)
V_ideal = codigos * V_LSB

# --- 3. Truco corregido para el último escalón (Gráfico 1) ---
codigos_step = np.append(codigos, 2**bits)
V_ideal_step = np.append(V_ideal, V_ideal[-1])
V_real_step = np.append(V_real, V_real[-1])

# --- 4. Cálculo de DNL e INL ---
DNL = np.zeros(len(codigos))
# El DNL del código 0 suele ser 0 por definición (no hay escalón previo)
for k in range(1, len(codigos)):
    escalon_real = V_real[k] - V_real[k-1]
    DNL[k] = (escalon_real / V_LSB) - 1.0

# INL (Endpoint-based asumiendo offset 0 y ganancia ideal)
INL = (V_real - V_ideal) / V_LSB

# =============================================================================
# GRÁFICO 1: Función de Transferencia (El que ya teníamos)
# =============================================================================
plt.figure(figsize=(10, 6))

plt.plot([0, 2**bits], [0, (2**bits) * V_LSB], linestyle=':', color='black', linewidth=2.5, label='Transferencia Ideal Continua')
plt.step(codigos_step, V_ideal_step, where='post', label='DAC Ideal', linestyle='--', color='dimgray', linewidth=2)
plt.step(codigos_step, V_real_step, where='post', label='DAC Real', linestyle='-', color='black', linewidth=2)
plt.plot(codigos, V_ideal, 'o', color='dimgray', markersize=4)
plt.plot(codigos, V_real, 'o', color='black', markersize=4)

plt.title(f'Función de Transferencia: DAC Ideal vs DAC Real ({bits} bits)', fontsize=14)
plt.xlabel('Código Digital de Entrada', fontsize=12)
plt.ylabel('Tensión Analógica de Salida [V]', fontsize=12)
plt.xticks(np.arange(0, 2**bits + 1, max(1, (2**bits)//8))) 
plt.yticks(np.linspace(0, V_ref, 9))
plt.grid(True, linestyle='--', alpha=0.5, color='gray')
plt.legend(fontsize=12)
plt.show()

# =============================================================================
# GRÁFICO 2: Perfiles de DNL e INL
# =============================================================================
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# Configuración visual para los tallos (stem)
markerline_format = {'marker': 'o', 'color': 'black', 'markersize': 5}
stemline_format = {'color': 'dimgray', 'linestyle': '-'}
baseline_format = {'color': 'black', 'linestyle': '-'}

# --- Subplot 1: DNL ---
markerline, stemlines, baseline = ax1.stem(codigos, DNL, basefmt=" ")
plt.setp(markerline, **markerline_format)
plt.setp(stemlines, **stemline_format)
ax1.axhline(0, color='black', linewidth=1.5) # Línea base en 0
ax1.axhline(0.5, color='gray', linestyle='--', alpha=0.5) # Límites comunes de diseño
ax1.axhline(-0.5, color='gray', linestyle='--', alpha=0.5)

ax1.set_title(f'Perfil de No Linealidad Diferencial (DNL) - {bits} bits', fontsize=13)
ax1.set_ylabel('DNL [LSB]', fontsize=12)
ax1.grid(True, linestyle='--', alpha=0.3, color='gray')

# --- Subplot 2: INL ---
markerline, stemlines, baseline = ax2.stem(codigos, INL, basefmt=" ")
plt.setp(markerline, **markerline_format)
plt.setp(stemlines, **stemline_format)
ax2.axhline(0, color='black', linewidth=1.5)
ax2.axhline(1.0, color='gray', linestyle='--', alpha=0.5)
ax2.axhline(-1.0, color='gray', linestyle='--', alpha=0.5)

ax2.set_title(f'Perfil de No Linealidad Integral (INL) - {bits} bits', fontsize=13)
ax2.set_xlabel('Código Digital de Entrada', fontsize=12)
ax2.set_ylabel('INL [LSB]', fontsize=12)
ax2.grid(True, linestyle='--', alpha=0.3, color='gray')

# Ajuste de eje X para ambos
plt.xticks(np.arange(0, 2**bits, max(1, (2**bits)//8))) 
plt.tight_layout()
plt.show()

# =============================================================================
# 3. GRÁFICO: Caracterización Completa (Perfiles DNL e INL con vlines)
# =============================================================================
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# --- Subplot 1: Perfil DNL (Usando vlines) ---
# vlines(x, ymin, ymax) traza líneas verticales finas y limpias
ax1.vlines(codigos, 0, DNL, color='black', linewidth=0.6, alpha=0.8, label='DNL')

ax1.axhline(0, color='black', linewidth=1.2) 
ax1.axhline(0.5, color='gray', linestyle='--', alpha=0.5) 
ax1.axhline(-0.5, color='gray', linestyle='--', alpha=0.5)

ax1.set_title(f'Perfil de No Linealidad Diferencial (DNL) - {bits} bits', fontsize=13)
ax1.set_ylabel('DNL [LSB]', fontsize=12)
ax1.set_ylim([-1.0, 1.0]) 
ax1.grid(True, linestyle='--', alpha=0.3, color='gray')
ax1.legend(loc='upper right')

# --- Subplot 2: Perfil INL (Usando vlines) ---
ax2.vlines(codigos, 0, INL, color='dimgray', linewidth=0.8, alpha=0.8, label='INL')

ax2.axhline(0, color='black', linewidth=1.2)
ax2.axhline(1.0, color='gray', linestyle='--', alpha=0.5)
ax2.axhline(-1.0, color='gray', linestyle='--', alpha=0.5)

ax2.set_title(f'Perfil de No Linealidad Integral (INL) - {bits} bits', fontsize=13)
ax2.set_xlabel('Código Digital de Entrada', fontsize=12)
ax2.set_ylabel('INL [LSB]', fontsize=12)
ax2.set_ylim([-2.0, 2.0]) 
ax2.grid(True, linestyle='--', alpha=0.3, color='gray')
ax2.legend(loc='upper right')

# Ajuste de ticks para el eje X
ax2.set_xticks(np.arange(0, 2**bits + 1, 256)) 

plt.tight_layout()
plt.show()