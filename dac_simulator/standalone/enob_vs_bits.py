# -----------------------------------------------------------------------------
# Copyright (C) 2026 Juan Carlos Alvarez Herrera
# Author: GREA Heaviside (@GREAHeaviside)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
# -----------------------------------------------------------------------------

import matplotlib.pyplot as plt

from ..mismatch_simulation import barrer_codigos_dac
from ..enob_test import (
    generar_seno_digital,
    simular_dac,
    calcular_espectro_potencia,
    calcular_metricas_espectrales
)

bits_list = list(range(4, 16))
n_mc = 30

N = 4096
k = 7

R_nom = 10000.0
V_ref = 3.3

enob_data = []

for bits in bits_list:
    enob_mc = []

    for seed in range(n_mc):

        codigos, V_real = barrer_codigos_dac(
            n=bits,
            R_nom=R_nom,
            seed=seed,
            V_ref=V_ref
        )

        D = generar_seno_digital(bits, N, k, amplitud=0.95)

        V_out = simular_dac(V_real, D)
        P_single = calcular_espectro_potencia(V_out)
        _, _, _, enob = calcular_metricas_espectrales(P_single, k)
        enob_mc.append(enob)

    enob_data.append(enob_mc)

plt.figure(figsize=(10, 6))

plt.boxplot(enob_data, positions=bits_list, widths=0.6)

plt.plot(bits_list, bits_list, '--', color='red', label='Ideal (ENOB = bits)')

plt.xlabel('Resolución nominal [bits]')
plt.ylabel('ENOB [bits]')
plt.title('ENOB vs Resolución con Mismatch (Monte Carlo)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()

plt.tight_layout()
plt.show()