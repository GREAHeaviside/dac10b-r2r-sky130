import numpy as np
import matplotlib.pyplot as plt

from mismatch_simulation import barrer_codigos_dac

# =========================
# CONFIGURACIÓN
# =========================
bits = 10
V_ref = 3.3
R_nom = 10000.0

n_mc = 1000   # Monte Carlo grande para estadística

# Specs
DNL_spec = 0.5
INL_spec = 0.5

# Resultados
dnl_worst_all = []
inl_worst_all = []

pass_dnl = 0
pass_inl = 0
pass_total = 0

# =========================
# MONTE CARLO
# =========================
for seed in range(n_mc):

    codigos, V_real = barrer_codigos_dac(
        n=bits,
        R_nom=R_nom,
        seed=seed,
        V_ref=V_ref
    )

    V_LSB = V_ref / (2**bits)
    V_ideal = codigos * V_LSB

    # --- DNL ---
    DNL = np.zeros(len(codigos))
    for k in range(1, len(codigos)):
        escalon_real = V_real[k] - V_real[k-1]
        DNL[k] = (escalon_real / V_LSB) - 1.0

    # --- INL ---
    INL = (V_real - V_ideal) / V_LSB

    # --- Worst case ---
    dnl_worst = np.max(np.abs(DNL))
    inl_worst = np.max(np.abs(INL))

    dnl_worst_all.append(dnl_worst)
    inl_worst_all.append(inl_worst)

    # --- Evaluación ---
    ok_dnl = dnl_worst < DNL_spec
    ok_inl = inl_worst < INL_spec

    if ok_dnl:
        pass_dnl += 1
    if ok_inl:
        pass_inl += 1
    if ok_dnl and ok_inl:
        pass_total += 1

# =========================
# RESULTADOS
# =========================
yield_dnl = pass_dnl / n_mc
yield_inl = pass_inl / n_mc
yield_total = pass_total / n_mc

print("==== RESULTADOS ====")
print(f"Yield DNL   : {yield_dnl*100:.2f}%")
print(f"Yield INL   : {yield_inl*100:.2f}%")
print(f"Yield TOTAL : {yield_total*100:.2f}%")

# =========================
# HISTOGRAMAS
# =========================
plt.figure(figsize=(10, 5))

plt.hist(dnl_worst_all, bins=40, alpha=0.6, label='DNL worst')
plt.axvline(DNL_spec, linestyle='--', label='Spec DNL')

plt.hist(inl_worst_all, bins=40, alpha=0.6, label='INL worst')
plt.axvline(INL_spec, linestyle='--', label='Spec INL')

plt.xlabel("Error [LSB]")
plt.ylabel("Cantidad de muestras")
plt.title("Distribución estadística de DNL/INL (10 bits)")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)

plt.show()