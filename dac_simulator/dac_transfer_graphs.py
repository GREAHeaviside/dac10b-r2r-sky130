import matplotlib.pyplot as plt
import numpy as np

# 1. Configuración de parámetros
bits = 3
codigos = np.arange(2**bits)
V_LSB = 1.0 

# 2. DAC Ideal
V_ideal = codigos * V_LSB

# 3. DAC Real
V_real = np.array([0.0, 1.2, 2.1, 3.4, 4.0, 5.1, 5.9, 7.0])

# 4. Truco corregido para el último escalón
codigos_step = np.append(codigos, 2**bits)
V_ideal_step = np.append(V_ideal, V_ideal[-1])
V_real_step = np.append(V_real, V_real[-1])

# 5. Creación del gráfico en ESCALA DE GRISES
plt.figure(figsize=(10, 6))

# --- Recta de transferencia ideal (Identidad) ---
# Usamos linestyle=':' para un punteado de puntitos, bien distinto al de guiones
plt.plot([0, 2**bits], [0, (2**bits) * V_LSB], linestyle=':', color='black', linewidth=2.5, label='Transferencia Ideal Continua')

# --- Escalones ---
# Ideal: Gris y con guiones
plt.step(codigos_step, V_ideal_step, where='post', label='DAC Ideal (Escalonado)', linestyle='--', color='dimgray', linewidth=2)
# Real: Negro y línea sólida
plt.step(codigos_step, V_real_step, where='post', label='DAC Real (con DNL/INL)', linestyle='-', color='black', linewidth=2)

# --- Puntos de cambio de código ---
plt.plot(codigos, V_ideal, 'o', color='dimgray')
plt.plot(codigos, V_real, 'o', color='black')

# Estética y formato
plt.title('Función de Transferencia: DAC Ideal vs DAC Real', fontsize=14)
plt.xlabel('Código Digital de Entrada', fontsize=12)
plt.ylabel('Tensión Analógica de Salida [LSB]', fontsize=12)

plt.xticks(codigos_step) 
plt.yticks(np.arange(0, 9, 1))

# Grilla en gris clarito para no ensuciar
plt.grid(True, linestyle='--', alpha=0.5, color='gray')
plt.legend(fontsize=12)

# Guardar en alta calidad
plt.savefig('grafico_dac_grises.pdf', bbox_inches='tight', dpi=300)
plt.show()