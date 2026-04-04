import numpy as np
import matplotlib.pyplot as plt
from mismatch_simulation import barrer_codigos_dac

def calcular_espectro_potencia(V_out):
    """
    Toma la señal en el tiempo, elimina la continua y calcula 
    el espectro de potencia de banda única (Single-Sided).
    """
    N = len(V_out)
    
    # 1. Matar la continua (DC offset) en el dominio del tiempo
    V_ac = V_out - np.mean(V_out)
    
    # 2. Calcular la FFT y normalizar por N
    # Normalizar por N es vital para que las amplitudes no dependan 
    # de cuántas muestras tomaste.
    V_fft = np.fft.fft(V_ac) / N
    
    # 3. Calcular la potencia (Doble Banda)
    P_doble = np.abs(V_fft)**2
    
    # 4. Convertir a Banda Única (Single-Sided)
    # Nos quedamos solo con la primera mitad (frecuencias positivas)
    mitad = N // 2
    P_single = P_doble[:mitad].copy()
    
    # 5. Compensación de energía
    # Multiplicamos por 2 todos los bines (excepto DC) para no perder 
    # la energía que estaba en la mitad negativa del espectro que tiramos.
    P_single[1:] = P_single[1:] * 2
    
    return P_single

def calcular_metricas_espectrales(P_single, k_fund):
    """
    A partir del espectro de potencia Single-Sided, calcula 
    las potencias de la señal, ruido y distorsión, y devuelve
    las métricas estándar.
    """
    N_mitad = len(P_single)
    
    # 1. Potencia Total (Excluyendo el bin 0 de DC por seguridad extrema)
    P_total = np.sum(P_single[1:])
    
    # 2. Potencia de la Fundamental (La señal útil)
    P_fund = P_single[k_fund]
    
    # 3. Potencia de Distorsión Armónica (THD)
    # Buscamos los múltiplos enteros de k_fund hasta llegar al límite de Nyquist
    P_harm = 0.0
    for h in range(2, int(N_mitad / k_fund) + 1):
        idx_harm = h * k_fund
        if idx_harm < N_mitad:
            P_harm += P_single[idx_harm]
            
    # 4. Potencia de Ruido (El resto del "pasto")
    # Es la energía total menos la señal y menos los armónicos
    P_noise = P_total - P_fund - P_harm
    
    # Protecciones numéricas para evitar advertencias de log(0) o valores negativos
    # por errores de precisión de punto flotante.
    P_noise = max(P_noise, 1e-15)
    P_harm = max(P_harm, 1e-15)
        
    # 5. Cálculo de Métricas en dB
    # Relación Señal a Ruido (Solo el pasto)
    snr_db = 10 * np.log10(P_fund / P_noise)
    
    # Distorsión Armónica Total (Los picos armónicos relativos a la fundamental)
    # Suele dar un número negativo (ej. -70 dBc)
    thd_db = 10 * np.log10(P_harm / P_fund)
    
    # Relación Señal a Ruido y Distorsión (Pasto + Picos)
    sinad_db = 10 * np.log10(P_fund / (P_noise + P_harm))
    
    # 6. Número Efectivo de Bits (ENOB)
    enob = (sinad_db - 1.76) / 6.02
    
    return snr_db, thd_db, sinad_db, enob

def generar_seno_digital(bits, N, k, amplitud=0.95):
    """
    Genera los códigos digitales de una senoidal coherente.
    """
    n = np.arange(N)
    seno = np.sin(2 * np.pi * k * n / N)
    
    # Rango del DAC
    full_scale = 2**bits - 1
    offset = full_scale / 2.0
    
    # Escalamos la amplitud (0.95 para dejar un 5% de margen y no saturar)
    A = amplitud * (full_scale / 2.0)
    
    # Cuantización (redondeo al entero más cercano)
    D = np.round(offset + A * seno)
    
    # Cliping por seguridad, asegurando que sean enteros
    return np.clip(D, 0, full_scale).astype(int)

def simular_dac(LUT, D):
    """
    Mapea el vector de códigos digitales a tensiones analógicas reales.
    """
    return LUT[D]

# =========================
# CONFIGURACIÓN
# =========================
bits = 10
N = 4096         # Potencia de 2
k = 7            # Número primo (Coherente)
R_nom = 10000.0
V_ref = 3.3
semilla = 15     # Cambiá esto para ver distintos "lotes de fabricación"

# =========================
# EJECUCIÓN
# =========================
# 1. Extraer la curva estática real del DAC
codigos, V_real = barrer_codigos_dac(n=bits, R_nom=R_nom, seed=semilla, V_ref=V_ref)

# 2. Generar estímulo y simular
D = generar_seno_digital(bits, N, k, amplitud=0.95)
V_out = simular_dac(V_real, D)

# 3. Procesamiento Espectral
P_single = calcular_espectro_potencia(V_out)
snr, thd, sinad, enob = calcular_metricas_espectrales(P_single, k)

print("==== RESULTADOS ESPECTRALES ====")
print(f"Resolución Ideal : {bits} bits")
print(f"SNR              : {snr:.2f} dB")
print(f"THD              : {thd:.2f} dB")
print(f"SINAD            : {sinad:.2f} dB")
print(f"ENOB             : {enob:.2f} bits")
print("================================")

# =========================
# GRÁFICO (Power Spectral Density)
# =========================
# Convertir el eje X a "Bins" o frecuencia normalizada
frecuencias = np.arange(len(P_single))

# Para graficar, pasamos la potencia a dB relativos a la portadora (dBc).
# Esto significa que el pico de nuestra fundamental será el nivel "0 dB".
P_db = 10 * np.log10(np.maximum(P_single, 1e-15))
P_dbc = P_db - P_db[k] 

plt.figure(figsize=(10, 6))

# Dibujar el espectro
plt.plot(frecuencias, P_dbc, color='black', linewidth=0.8)

# Marcar el tono fundamental
plt.plot(k, P_dbc[k], 'o', color='blue', label='Señal Fundamental (k)')

# Marcar los primeros armónicos (2k, 3k, 4k, 5k) para ver la distorsión
for h in range(2, 6):
    idx_harm = h * k
    if idx_harm < len(P_dbc):
        plt.plot(idx_harm, P_dbc[idx_harm], 'x', color='red', markersize=6)

# Truco para que el label de armónicos aparezca solo una vez en la leyenda
plt.plot([], [], 'x', color='red', label='Armónicos (INL)')

plt.title(f'Espectro de Potencia (FFT) - DAC de {bits} bits (ENOB: {enob:.2f})', fontsize=14)
plt.xlabel('Frecuencia [Bins / Múltiplos de k]', fontsize=12)
plt.ylabel('Magnitud Relativa [dBc]', fontsize=12)

# Ajustar límites del gráfico
plt.ylim([-100, 5])
plt.xlim([0, N//2])

plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()