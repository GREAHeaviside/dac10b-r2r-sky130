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

def generar_resistores_ladder(n=10, R_nom=10000, A_R=0.002, W=1.0, L=25.0):
    sigma_R_rel = A_R / np.sqrt(W * L)
    sigma_2R_rel = sigma_R_rel / np.sqrt(2)
    
    delta_G  = np.random.normal(0, sigma_R_rel)
    delta_hk = np.random.normal(0, sigma_R_rel, n)
    delta_vk = np.random.normal(0, sigma_2R_rel, n)
    
    R_g = R_nom * (1 + delta_G)
    R_h = R_nom * (1 + delta_hk)
    R_v = (2 * R_nom) * (1 + delta_vk)
    return R_g, R_h, R_v

def construir_matriz_Y(n, R_g, R_h, R_v):
    Y = np.zeros((n, n))
    for i in range(n):
        for k in range(n):
            if i == k:
                if k == 0:
                    Y[i, k] = (1 / (R_h[0] + R_g)) + (1 / R_v[0]) + (1 / R_h[1])
                elif k == n - 1:
                    Y[i, k] = (1 / R_h[n-1]) + (1 / R_v[n-1])
                else:
                    Y[i, k] = (1 / R_h[k]) + (1 / R_v[k]) + (1 / R_h[k+1])
            elif i == k + 1:
                Y[i, k] = -1 / R_h[i]
            elif i == k - 1:
                Y[i, k] = -1 / R_h[k]
            else:
                Y[i, k] = 0.0
    return Y

def barrer_codigos_dac(n, R_nom, seed, V_ref=3.3, A_R=0.002, W=1.0, L=25.0):
    """
    Generates the real output voltages of an R-2R ladder DAC for all possible digital codes, given a set of parameters and a random seed for reproducibility.
    Parameters:
    - n: Number of bits (resolution) of the DAC.
    - R_nom: Nominal resistance value for the resistors in the ladder.
    - seed: Random seed for reproducibility of the resistor variations.
    - V_ref: Reference voltage for the DAC.
    - A_R: Process variation parameter for the resistors.
    - W: Width of the resistors (for variation calculation).
    - L: Length of the resistors (for variation calculation).
    Returns:
    - codigos: Array of digital codes (from 0 to 2^n - 1).
    - v_out_real: Array of real output voltages corresponding to each digital code
    """
    np.random.seed(seed)
    
    R_g, R_h, R_v = generar_resistores_ladder(n=n, R_nom=R_nom, A_R=A_R, W=W, L=L)
    Y = construir_matriz_Y(n, R_g, R_h, R_v)

    Z = np.linalg.inv(Y)
    
    num_codigos = 2**n
    codigos = np.arange(num_codigos)
    v_out_real = np.zeros(num_codigos)
    
    for code in range(num_codigos):
        b_str = format(code, f'0{n}b')[::-1]
        b = np.array([int(bit) for bit in b_str])
        
        I_in = b * V_ref * (1 / R_v)
        
        V_nodos = Z @ I_in

        v_out_real[code] = V_nodos[-1]
        
    return codigos, v_out_real