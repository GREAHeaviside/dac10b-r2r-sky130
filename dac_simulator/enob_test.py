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
from mismatch_simulation import barrer_codigos_dac

def calcular_espectro_potencia(V_out):
    """
    Takes signal samples and computes the single-sided power spectrum.
    """
    N = len(V_out)
    
    V_ac = V_out - np.mean(V_out)
    
    V_fft = np.fft.fft(V_ac) / N
    
    P_doble = np.abs(V_fft)**2
    
    mitad = N // 2
    P_single = P_doble[:mitad].copy()
    
    P_single[1:] = P_single[1:] * 2
    
    return P_single

def calcular_metricas_espectrales(P_single, k_fund):
    """
    From the single-sided power spectrum, calculates SNR, THD, SINAD, and ENOB.
    """
    N_mitad = len(P_single)
    
    P_total = np.sum(P_single[1:])
    
    P_fund = P_single[k_fund]

    P_harm = 0.0
    for h in range(2, int(N_mitad / k_fund) + 1):
        idx_harm = h * k_fund
        if idx_harm < N_mitad:
            P_harm += P_single[idx_harm]
            
    P_noise = P_total - P_fund - P_harm
    
    P_noise = max(P_noise, 1e-15)
    P_harm = max(P_harm, 1e-15)
        
    snr_db = 10 * np.log10(P_fund / P_noise)

    thd_db = 10 * np.log10(P_harm / P_fund)

    sinad_db = 10 * np.log10(P_fund / (P_noise + P_harm))
    
    enob = (sinad_db - 1.76) / 6.02
    
    return snr_db, thd_db, sinad_db, enob

def generar_seno_digital(bits, N, k, amplitud=0.95):
    """
    Generates a digital sine wave sampled at N points, with k cycles over the N samples, and scaled to fit within the DAC's range.
    """
    n = np.arange(N)
    seno = np.sin(2 * np.pi * k * n / N)
    
    full_scale = 2**bits - 1
    offset = full_scale / 2.0
    
    A = amplitud * (full_scale / 2.0)
    
    D = np.round(offset + A * seno)
    
    return np.clip(D, 0, full_scale).astype(int)

def simular_dac(LUT, D):
    """
    Maps digital codes D to their corresponding analog voltages using the provided LUT (Look-Up Table).
    """
    return LUT[D]


if __name__ == "__main__":

    bits    = 10
    N       = 4096
    k       = 7
    R_nom   = 10000.0
    V_ref   = 3.3
    semilla = 15

    codigos, V_real = barrer_codigos_dac(n=bits, R_nom=R_nom, seed=semilla, V_ref=V_ref)

    D        = generar_seno_digital(bits, N, k, amplitud=0.95)
    V_out    = simular_dac(V_real, D)
    P_single = calcular_espectro_potencia(V_out)
    snr, thd, sinad, enob = calcular_metricas_espectrales(P_single, k)

    print("==== SPECTRAL RESULTS ====")
    print(f"Ideal resolution : {bits} bits")
    print(f"SNR              : {snr:.2f} dB")
    print(f"THD              : {thd:.2f} dB")
    print(f"SINAD            : {sinad:.2f} dB")
    print(f"ENOB             : {enob:.2f} bits")
    print("================================")

    # PSD Plot
    frecuencias = np.arange(len(P_single))
    P_db        = 10 * np.log10(np.maximum(P_single, 1e-15))
    P_dbc       = P_db - P_db[k]

    plt.figure(figsize=(10, 6))
    plt.plot(frecuencias, P_dbc, color='black', linewidth=0.8)
    plt.plot(k, P_dbc[k], 'o', color='blue', label='Fundamental Signal (k)')

    for h in range(2, 6):
        idx_harm = h * k
        if idx_harm < len(P_dbc):
            plt.plot(idx_harm, P_dbc[idx_harm], 'x', color='red', markersize=6)
    plt.plot([], [], 'x', color='red', label='Harmonics (INL)')

    plt.title(f'Power Spectral Density (FFT) - DAC of {bits} bits (ENOB: {enob:.2f})', fontsize=14)
    plt.xlabel('Frequency [Bins / MMultiples of k]', fontsize=12)
    plt.ylabel('Relative Magnitude [dBc]', fontsize=12)
    plt.ylim([-100, 5])
    plt.xlim([0, N // 2])
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()
    plt.tight_layout()
    plt.show()