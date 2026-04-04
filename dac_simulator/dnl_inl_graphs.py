import matplotlib.pyplot as plt
import numpy as np

# 1. Parámetros (DAC de 3 bits perfecto en extremos)
bits = 3
codigos = np.arange(2**bits)
V_LSB = 1.0 
V_real = np.array([0.0, 1.2, 2.1, 3.4, 4.0, 5.1, 5.9, 7.0])

# 2. CÁLCULO DE DNL E INL 
dnl = (np.diff(V_real) / V_LSB) - 1
codigos_dnl = codigos[:-1] 
inl = (V_real / V_LSB) - codigos

# 3. PLOTEO DE RESULTADOS
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# --- Gráfico de DNL ---
ax1.stem(codigos_dnl, dnl, basefmt="k-", linefmt="b-", markerfmt="bo")
ax1.set_title('No-Linealidad Diferencial (DNL)', fontsize=14)
ax1.set_ylabel('DNL [LSB]', fontsize=12)
ax1.grid(True, linestyle=':', alpha=0.7)
ax1.axhline(0.5, color='r', linestyle='--', alpha=0.5)
ax1.axhline(-0.5, color='r', linestyle='--', alpha=0.5)

# Bucle para agregar el texto (y) en el DNL con LÓGICA DE POSICIÓN DINÁMICA
for x, y in zip(codigos_dnl, dnl):
    # Condición para decidir offset y alineación vertical (va)
    if y >= 0:
        # Valor positivo: Texto ARRIBA (10), alineación inferior (bottom)
        y_offset_dinamico = 10
        va_dinamico = 'bottom'
    else:
        # Valor negativo: Texto ABAJO (-10), alineación superior (top)
        y_offset_dinamico = -10
        va_dinamico = 'top'
    
    # Aplicamos va y xytext dinámicos en la anotación
    ax1.annotate(f'{y:+.1f}', (x, y), textcoords="offset points", 
                 xytext=(0, y_offset_dinamico), ha='center', va=va_dinamico, fontsize=10)

# --- Gráfico de INL ---
ax2.stem(codigos, inl, basefmt="k-", linefmt="g-", markerfmt="go")
ax2.set_title('No-Linealidad Integral (INL)', fontsize=14)
ax2.set_xlabel('D', fontsize=12)
ax2.set_ylabel('INL [LSB]', fontsize=12)
ax2.grid(True, linestyle=':', alpha=0.7)
ax2.axhline(0.5, color='r', linestyle='--', alpha=0.5)
ax2.axhline(-0.5, color='r', linestyle='--', alpha=0.5)

# Bucle para agregar el texto (y) en el INL con LÓGICA DE POSICIÓN DINÁMICA
for x, y in zip(codigos, inl):
    # Condición para decidir offset y alineación vertical (va)
    if y >= 0:
        # Valor positivo: Texto ARRIBA (10), alineación inferior (bottom)
        y_offset_dinamico = 10
        va_dinamico = 'bottom'
    else:
        # Valor negativo: Texto ABAJO (-10), alineación superior (top)
        y_offset_dinamico = -10
        va_dinamico = 'top'
        
    ax2.annotate(f'{y:+.1f}', (x, y), textcoords="offset points", 
                 xytext=(0, y_offset_dinamico), ha='center', va=va_dinamico, fontsize=10)

plt.xticks(codigos)
plt.tight_layout()
plt.savefig('dnl_inl_plot.png', bbox_inches='tight', dpi=300)
plt.show()