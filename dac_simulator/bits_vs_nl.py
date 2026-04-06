import numpy as np
import matplotlib.pyplot as plt

from mismatch_simulation import barrer_codigos_dac


V_ref = 3.3
R_nom = 10000.0

bits_list = range(4, 13)
n_mc = 50

dnl_worst_mean = []
inl_worst_mean = []

dnl_worst_p95 = []
inl_worst_p95 = []


for bits in bits_list:
    print(f"Simulando {bits} bits...")

    dnl_worst_mc = []
    inl_worst_mc = []

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

        # --- Métricas worst-case ---
        dnl_worst_mc.append(np.max(np.abs(DNL)))
        inl_worst_mc.append(np.max(np.abs(INL)))

    # Estadísticas
    dnl_worst_mean.append(np.mean(dnl_worst_mc))
    inl_worst_mean.append(np.mean(inl_worst_mc))

    dnl_worst_p95.append(np.percentile(dnl_worst_mc, 95))
    inl_worst_p95.append(np.percentile(inl_worst_mc, 95))


plt.figure(figsize=(10, 6))

plt.plot(bits_list, dnl_worst_mean, 'o-', label='DNL worst (mean)')
plt.plot(bits_list, dnl_worst_p95, 's--', label='DNL worst (p95)')

plt.plot(bits_list, inl_worst_mean, 'o-', label='INL worst (mean)')
plt.plot(bits_list, inl_worst_p95, 's--', label='INL worst (p95)')

plt.axhline(0.5, linestyle='--', label='Límite típico DNL')
plt.axhline(1.0, linestyle=':', label='Límite típico INL')

plt.xlabel("Número de bits")
plt.ylabel("Error [LSB]")
plt.title("Worst-case DNL/INL vs Resolución (Monte Carlo)")
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()

plt.show()