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

import numpy as np
import matplotlib.pyplot as plt

from ..mismatch_simulation import barrer_codigos_dac

bits = 10
V_ref = 1.8
R_nom = 10000.0

n_mc = 1000

DNL_spec = 0.5
INL_spec = 0.5

dnl_worst_all = []
inl_worst_all = []

pass_dnl = 0
pass_inl = 0
pass_total = 0

for seed in range(n_mc):

    codigos, V_real = barrer_codigos_dac(
        n=bits,
        R_nom=R_nom,
        seed=seed,
        V_ref=V_ref
    )

    V_LSB = V_ref / (2**bits)
    V_ideal = codigos * V_LSB

    DNL = np.zeros(len(codigos))
    for k in range(1, len(codigos)):
        escalon_real = V_real[k] - V_real[k-1]
        DNL[k] = (escalon_real / V_LSB) - 1.0

    INL = (V_real - V_ideal) / V_LSB

    dnl_worst = np.max(np.abs(DNL))
    inl_worst = np.max(np.abs(INL))

    dnl_worst_all.append(dnl_worst)
    inl_worst_all.append(inl_worst)

    ok_dnl = dnl_worst < DNL_spec
    ok_inl = inl_worst < INL_spec

    if ok_dnl:
        pass_dnl += 1
    if ok_inl:
        pass_inl += 1
    if ok_dnl and ok_inl:
        pass_total += 1

yield_dnl = pass_dnl / n_mc
yield_inl = pass_inl / n_mc
yield_total = pass_total / n_mc

print("==== RESULTS ====")
print(f"Yield DNL   : {yield_dnl*100:.2f}%")
print(f"Yield INL   : {yield_inl*100:.2f}%")
print(f"Yield TOTAL : {yield_total*100:.2f}%")

plt.figure(figsize=(10, 5))

plt.hist(dnl_worst_all, bins=40, alpha=0.6, label='DNL worst')
plt.axvline(DNL_spec, linestyle='--', label='Spec DNL')

plt.hist(inl_worst_all, bins=40, alpha=0.6, label='INL worst')
plt.axvline(INL_spec, linestyle='--', label='Spec INL')

plt.xlabel("Error [LSB]")
plt.ylabel("Number of MC runs")
plt.title(f"Statistical distribution of DNL and INL worst-case values ({bits} bits, {n_mc} runs)")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)

plt.show()