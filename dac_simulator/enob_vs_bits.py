import numpy as np
import matplotlib.pyplot as plt

from mismatch_simulation import barrer_codigos_dac
from enob_test import (
    generar_seno_digital,
    simular_dac,
    calcular_espectro_potencia,
    calcular_metricas_espectrales
)

# =========================
# CONFIGURACIÓN
# =========================
bits_list = list(range(4, 16))   # 4 a 12 bits
n_mc = 30                       # Monte Carlo por punto

N = 4096
k = 7

R_nom = 10000.0
V_ref = 3.3

# =========================
# SIMULACIÓN
# =========================
enob_data = []

for bits in bits_list:
    enob_mc = []

    for seed in range(n_mc):

        # 1. DAC con mismatch
        codigos, V_real = barrer_codigos_dac(
            n=bits,
            R_nom=R_nom,
            seed=seed,
            V_ref=V_ref
        )

        # 2. Señal
        D = generar_seno_digital(bits, N, k, amplitud=0.95)

        # 3. Salida DAC
        V_out = simular_dac(V_real, D)

        # 4. Espectro
        P_single = calcular_espectro_potencia(V_out)

        # 5. Métricas
        _, _, _, enob = calcular_metricas_espectrales(P_single, k)

        enob_mc.append(enob)

    enob_data.append(enob_mc)

# =========================
# GRÁFICO
# =========================
plt.figure(figsize=(10, 6))

# Boxplot
plt.boxplot(enob_data, positions=bits_list, widths=0.6)

# Línea ideal
plt.plot(bits_list, bits_list, '--', color='red', label='Ideal (ENOB = bits)')

plt.xlabel('Resolución nominal [bits]')
plt.ylabel('ENOB [bits]')
plt.title('ENOB vs Resolución con Mismatch (Monte Carlo)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()

plt.tight_layout()
plt.show()