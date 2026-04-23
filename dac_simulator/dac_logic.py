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
from enob_test import (
    generar_seno_digital,
    simular_dac,
    calcular_espectro_potencia,
    calcular_metricas_espectrales
)

class DAC:
    def __init__(self):
        self.bits   = 10
        self.vref   = 3.3
        self.fs     = 100e6

        self.r_nom  = 10000.0
        self.a_rho  = 0.002
        self.w      = 1.0
        self.l      = 25.0

        self.f_in_k = 7       
        self.N      = 4096    

        self.codigos = None
        self.v_real  = None

        self.dnl    = None
        self.inl    = None
        self.snr    = None
        self.thd    = None
        self.sinad  = None
        self.enob   = None

    def _hay_datos(self):
        if self.codigos is None or self.v_real is None:
            print("[!] NO DATA IN MEMORY. GENERATE OR LOAD A DAC CURVE FIRST.")
            return False
        return True

    def _v_lsb(self):
        return self.vref / (2 ** self.bits)

    def _v_ideal(self):
        return self.codigos * self._v_lsb()

    @property
    def f_in_hz(self):
        return self.f_in_k * self.fs / self.N

    def set_bits(self, bits: int):
        self.bits = bits
        print(f">> Resolution updated to {self.bits} bits.")

    def set_vref(self, vref: float):
        self.vref = vref
        print(f">> Vref updated to {self.vref} V.")

    def set_fs(self, fs: float):
        self.fs = fs
        print(f">> Fs updated to {self.fs / 1e6} MHz.")

    def set_r_nom(self, r_nom: float):
        self.r_nom = r_nom
        print(f">> Nominal R updated to {self.r_nom} Ohm.")

    def set_geometria(self, w: float, l: float, a_rho: float):
        self.w     = w
        self.l     = l
        self.a_rho = a_rho
        print(f">> Geometry updated: W={self.w} um, L={self.l} um, A_rho={self.a_rho}.")

    def generar(self, semilla: int):
        print("\n>> Generating DAC with mismatch...")
        self.codigos, self.v_real = barrer_codigos_dac(
            n     = self.bits,
            R_nom = self.r_nom,
            seed  = semilla,
            V_ref = self.vref,
            A_R   = self.a_rho,
            W     = self.w,
            L     = self.l
        )
        self.dnl = self.inl = None
        self.snr = self.thd = self.sinad = self.enob = None
        print(f">> {self.bits} bits DAC generated with mismatch")

    def cargar_csv(self, archivo: str):
        print("\n>> Loading curve from CSV...")
        datos         = np.loadtxt(archivo, delimiter=',', skiprows=1)
        self.codigos  = datos[:, 0]
        self.v_real   = datos[:, 1]
        self.bits     = int(np.log2(len(self.codigos)))
        self.dnl = self.inl = None
        self.snr = self.thd = self.sinad = self.enob = None
        print(f">> Loaded ({len(self.codigos)} codes). Resolution: {self.bits} bits.")

    def guardar_csv(self, archivo: str):
        if not self._hay_datos():
            return
        print("\n>> Saving curve to CSV...")
        datos = np.column_stack((self.codigos, self.v_real))
        np.savetxt(archivo, datos, delimiter=',', header='Code,V_out', comments='')
        print(f">> Curve saved successfully to '{archivo}'!")

    def _calcular_dnl_inl(self):
        v_lsb   = self._v_lsb()
        v_ideal = self._v_ideal()

        dnl = np.zeros(len(self.codigos))
        for k in range(1, len(self.codigos)):
            escalon_real = self.v_real[k] - self.v_real[k - 1]
            dnl[k] = (escalon_real / v_lsb) - 1.0

        inl = (self.v_real - v_ideal) / v_lsb

        self.dnl = dnl
        self.inl = inl

    def ver_metricas_estaticas(self):
        if not self._hay_datos():
            return
        if self.dnl is None:
            self._calcular_dnl_inl()

        dnl_max = np.max(np.abs(self.dnl))
        inl_max = np.max(np.abs(self.inl))

        print("\n==== Distortion Metrics ====")
        print(f"  DNL maximum : {dnl_max:.4f} LSB")
        print(f"  INL maximum : {inl_max:.4f} LSB")
        print("============================")

    def graficar_transferencia(self):
        """Plots the ideal vs real DAC transfer function."""
        if not self._hay_datos():
            return
 
        v_lsb   = self._v_lsb()
        v_ideal = self._v_ideal()
 
        codigos_step = np.append(self.codigos, 2 ** self.bits)
        v_ideal_step = np.append(v_ideal, v_ideal[-1])
        v_real_step  = np.append(self.v_real, self.v_real[-1])
 
        fig, ax = plt.subplots(figsize=(10, 6))
 
        ax.plot([0, 2**self.bits], [0, (2**self.bits) * v_lsb],
                linestyle=':', color='#AAAAAA', linewidth=2,
                label='Ideal continuous transfer', zorder=1)
 
        ax.step(codigos_step, v_ideal_step, where='post',
                linestyle='--', color='#4C9BE8', linewidth=1.8,
                label='Ideal DAC', zorder=2)
 
        ax.step(codigos_step, v_real_step, where='post',
                linestyle='-', color='#E84C4C', linewidth=1.8,
                label='Real DAC', zorder=3)
 
        ax.set_title(f'Ideal and Real DAC outputs for {self.bits} bits',
                     fontsize=14, pad=12)
        ax.set_xlabel('Input code', fontsize=12)
        ax.set_ylabel('Output voltage [V]', fontsize=12)
        ax.set_xlim([0, 2**self.bits])
        ax.set_ylim([-0.05 * self.vref, 1.05 * self.vref])
        ax.set_xticks(np.arange(0, 2**self.bits + 1, max(1, (2**self.bits) // 8)))
        ax.set_yticks(np.linspace(0, self.vref, 9))
        ax.grid(True, linestyle='--', alpha=0.4, color='gray')
        ax.legend(fontsize=11, loc='upper left')
        fig.tight_layout()
        plt.show()
 
    def graficar_dnl_inl(self):
        """Plots DNL and INL profiles as continuous lines with discrete markers."""
        if not self._hay_datos():
            return
        if self.dnl is None:
            self._calcular_dnl_inl()
 
        dnl_max = np.max(np.abs(self.dnl))
        inl_max = np.max(np.abs(self.inl))
 
        dnl_margin = max(1.0, dnl_max * 1.1)
        inl_margin = max(1.5, inl_max * 1.1)
 
        n_codes     = len(self.codigos)
        marker_step = max(1, n_codes // 64)
        mask        = np.zeros(n_codes, dtype=bool)
        mask[::marker_step] = True
 
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(11, 8), sharex=True)
        fig.suptitle(f'DNL / INL Profile  —  {self.bits}-bit DAC',
                     fontsize=14, y=1.01)
 
        ax1.plot(self.codigos, self.dnl,
                 color='#4C9BE8', linewidth=1.2, alpha=0.9, label=f'DNL  (max={dnl_max:.3f} LSB)', zorder=3)
        ax1.plot(self.codigos[mask], self.dnl[mask],
                 'o', color='#4C9BE8', markersize=3, alpha=0.7, zorder=4)
        ax1.fill_between(self.codigos, self.dnl, 0,
                         color='#4C9BE8', alpha=0.12)
        ax1.axhline(0,    color='black',      linewidth=1.0)
        ax1.axhline( 0.5, color='#E84C4C', linestyle='--', linewidth=1.2,
                     alpha=0.8, label='Spec ±0.5 LSB')
        ax1.axhline(-0.5, color='#E84C4C', linestyle='--', linewidth=1.2, alpha=0.8)
        ax1.set_ylabel('DNL [LSB]', fontsize=12)
        ax1.set_ylim([-dnl_margin, dnl_margin])
        ax1.legend(fontsize=10, loc='upper right')
        ax1.grid(True, linestyle='--', alpha=0.35, color='gray')
 
        ax2.plot(self.codigos, self.inl,
                 color='#2ECC71', linewidth=1.2, alpha=0.9, label=f'INL  (max={inl_max:.3f} LSB)', zorder=3)
        ax2.plot(self.codigos[mask], self.inl[mask],
                 'o', color='#2ECC71', markersize=3, alpha=0.7, zorder=4)
        ax2.fill_between(self.codigos, self.inl, 0,
                         color='#2ECC71', alpha=0.12)
        ax2.axhline(0,    color='black',      linewidth=1.0)
        ax2.axhline( 1.0, color='#E84C4C', linestyle='--', linewidth=1.2,
                     alpha=0.8, label='Spec ±1.0 LSB')
        ax2.axhline(-1.0, color='#E84C4C', linestyle='--', linewidth=1.2, alpha=0.8)
        ax2.set_xlabel('Input code []', fontsize=12)
        ax2.set_ylabel('INL [LSB]', fontsize=12)
        ax2.set_ylim([-inl_margin, inl_margin])
        ax2.legend(fontsize=10, loc='upper right')
        ax2.grid(True, linestyle='--', alpha=0.35, color='gray')
 
        ax2.set_xticks(np.arange(0, 2**self.bits + 1, max(1, (2**self.bits) // 8)))
        fig.tight_layout()
        plt.show()


    def set_bin_k(self, k: int):
        self.f_in_k = k
        print(f">> Test tone updated: k={self.f_in_k}  →  f_in = {self.f_in_hz/1e3:.2f} kHz")

    def _calcular_enob_interno(self):
        D       = generar_seno_digital(self.bits, self.N, self.f_in_k, amplitud=0.95)
        v_out   = simular_dac(self.v_real, D)
        p_single = calcular_espectro_potencia(v_out)
        self.snr, self.thd, self.sinad, self.enob = calcular_metricas_espectrales(p_single, self.f_in_k)
        return p_single

    def ver_metricas_dinamicas(self):
        if not self._hay_datos():
            return
        self._calcular_enob_interno()

        print("\n==== DYNAMIC METRICS ====")
        print(f"  Nominal Resolution : {self.bits} bits")
        print(f"  SNR                : {self.snr:.2f} dB")
        print(f"  THD                : {self.thd:.2f} dB")
        print(f"  SINAD              : {self.sinad:.2f} dB")
        print(f"  ENOB               : {self.enob:.2f} bits")
        print("=========================")

    def graficar_espectro(self):
        if not self._hay_datos():
            return

        p_single = self._calcular_enob_interno()

        resolucion_espectral = self.fs / self.N 
        
        frecuencias_hz = np.arange(len(p_single)) * resolucion_espectral
        frecuencias_mhz = frecuencias_hz / 1e6
        
        p_db  = 10 * np.log10(np.maximum(p_single, 1e-15))
        p_dbc = p_db - p_db[self.f_in_k]

        plt.figure(figsize=(10, 6))
        
        plt.plot(frecuencias_mhz, p_dbc, color='black', linewidth=0.8)
        
        frec_fund_mhz = self.f_in_k * resolucion_espectral / 1e6
        plt.plot(frec_fund_mhz, p_dbc[self.f_in_k], 'o', color='blue', label='Fundamental Tone')

        for h in range(2, 6):
            idx = h * self.f_in_k
            if idx < len(p_dbc):
                frec_armonico_mhz = idx * resolucion_espectral / 1e6
                plt.plot(frec_armonico_mhz, p_dbc[idx], 'x', color='red', markersize=6)
                
        plt.plot([], [], 'x', color='red', label='Harmonics')

        plt.title(f'Power Spectrum - DAC {self.bits} bits  |  ENOB: {self.enob:.2f}', fontsize=14)
        
        plt.xlabel('Frequency [MHz]', fontsize=12)
        plt.ylabel('Relative Magnitude [dBc]', fontsize=12)
        
        plt.ylim([-100, 5])
        plt.xlim([0, (self.fs / 2) / 1e6]) 
        
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.legend()
        plt.tight_layout()
        plt.show()