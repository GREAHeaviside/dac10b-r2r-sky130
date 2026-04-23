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

import sys
import os
from dac_logic import DAC

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_menu(dac: DAC):
    clear_screen()
    print("\n" + "="*40)
    print("         R-2R DAC SIMULATOR      ")
    print("="*40)
    print(f" [CURRENT STATE]")
    print(f" Resolution : {dac.bits} bits | Vref : {dac.vref} V | Fs : {dac.fs/1e6} MHz")
    print(f" Nominal R  : {dac.r_nom} Ohm | Pelgrom (A_rho): {dac.a_rho}")
    print(f" W: {dac.w} um | L: {dac.l} um")
    print("-" * 40)
    print(" [SYSTEM PARAMETERS]")
    print("  1) Set resolution (bits)")
    print("  2) Set reference voltage (Vref)")
    print("  3) Set clock frequency (Fs)")
    print(" [PHYSICAL PARAMETERS]")
    print("  4) Set nominal resistor value (R)")
    print("  5) Set geometry (W, L) and Pelgrom constant")
    print(" [DATA GENERATION]")
    print("  6) Generate DAC (Monte Carlo / Mismatch)")
    print("  7) Load DAC curve from CSV")
    print("  8) Save current DAC curve to CSV")
    print(" [STATIC ANALYSIS]")
    print("  9) Show maximum DNL and INL")
    print(" 10) Plot transfer function and error profiles")
    print(" [DYNAMIC ANALYSIS]")
    print(f" 11) Set test signal (bin k={dac.f_in_k}  ->  f_in = {dac.f_in_hz/1e3:.2f} kHz)")
    print(" 12) Calculate SINAD and ENOB")
    print(" 13) Plot Power Spectrum (FFT)")
    print("  0) Exit")
    print("="*40)

def main():
    dac = DAC()
    while True:
        print_menu(dac)
        option = input("Choose an option: ")
        try:
            if option == '1':
                clear_screen()
                dac.set_bits(int(input("New resolution (bits): ")))
                input("\nPress Enter to return to the menu...")

            elif option == '2':
                clear_screen()
                dac.set_vref(float(input("New Vref (V): ")))
                input("\nPress Enter to return to the menu...")
                
            elif option == '3':
                clear_screen()
                dac.set_fs(float(input("New clock frequency Fs (Hz): ")))
                input("\nPress Enter to return to the menu...")
                
            elif option == '4':
                clear_screen()
                dac.set_r_nom(float(input("New nominal R value (Ohms): ")))
                input("\nPress Enter to return to the menu...")
                
            elif option == '5':
                clear_screen()
                w     = float(input("New width W (um): "))
                l     = float(input("New length L (um): "))
                a_rho = float(input("New Pelgrom constant A_rho: "))
                dac.set_geometria(w, l, a_rho)
                input("\nPress Enter to return to the menu...")
                
            elif option == '6':
                clear_screen()
                seed = int(input("Enter a seed (integer, e.g., 42): "))
                dac.generar(seed)
                input("\nPress Enter to return to the menu...")

            elif option == '7':
                clear_screen()
                filename = input("File name (e.g., dac_data.csv): ")
                dac.cargar_csv(filename)
                input("\nPress Enter to return to the menu...")

            elif option == '8':
                clear_screen()
                filename = input("File name to save (e.g., my_dac.csv): ")
                dac.guardar_csv(filename)
                input("\nPress Enter to return to the menu...")

            elif option == '9':
                clear_screen()
                dac.ver_metricas_estaticas()
                input("\nPress Enter to return to the menu...")

            elif option == '10':
                clear_screen()
                dac.graficar_transferencia()
                dac.graficar_dnl_inl()
                input("\nPress Enter to return to the menu...")

            elif option == '11':
                clear_screen()
                k = int(input("New coherence bin k (prime integer, e.g., 7): "))
                dac.set_bin_k(k)
                input("\nPress Enter to return to the menu...")

            elif option == '12':
                clear_screen()
                dac.ver_metricas_dinamicas()
                input("\nPress Enter to return to the menu...")
                
            elif option == '13':
                clear_screen()
                dac.graficar_espectro()
                input("\nPress Enter to return to the menu...")

            elif option == '0':
                clear_screen()
                print("Exiting simulator...")
                sys.exit(0)

            else:
                clear_screen()
                print("\n[!] Invalid option.")
                input("\nPress Enter to return to the menu...")

        except Exception as e:
            clear_screen()
            print(f"[!] Error: {e}")
            input("\nPress Enter to return to the menu...")

if __name__ == "__main__":
    main()