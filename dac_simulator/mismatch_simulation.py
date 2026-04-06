import numpy as np

# --- (Aquí van tus funciones generar_resistores_ladder y construir_matriz_Y) ---
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

def barrer_codigos_dac(n, R_nom, seed, V_ref=3.3):
    """
    Genera el ladder con mismatch y calcula V_out para todos los códigos posibles.
    
    Devuelve:
    - codigos: Array con los valores enteros (0 a 2^n - 1)
    - v_out_real: Array con las tensiones de salida calculadas
    """
    # 1. Fijar semilla para reproducibilidad
    np.random.seed(seed)
    
    # 2. Generar el circuito físico (Esto se hace UNA sola vez)
    R_g, R_h, R_v = generar_resistores_ladder(n=n, R_nom=R_nom)
    Y = construir_matriz_Y(n, R_g, R_h, R_v)
    
    # Invertimos la matriz Y para obtener la matriz de impedancias Z
    # V = Z * I
    Z = np.linalg.inv(Y)
    
    # 3. Preparar los arrays de salida
    num_codigos = 2**n
    codigos = np.arange(num_codigos)
    v_out_real = np.zeros(num_codigos)
    
    # 4. Barrido de todos los códigos
    for code in range(num_codigos):
        # Convertir el entero a un array binario de longitud n.
        # [::-1] invierte el string para que el índice 0 sea el LSB (b_0)
        b_str = format(code, f'0{n}b')[::-1]
        b = np.array([int(bit) for bit in b_str])
        
        # Calcular el vector de corrientes inyectadas por los switches
        I_in = b * V_ref * (1 / R_v)
        
        # Calcular todas las tensiones nodales multiplicando Z por I_in
        V_nodos = Z @ I_in
        
        # Guardar solo la tensión del último nodo (V_out)
        v_out_real[code] = V_nodos[-1]
        
    return codigos, v_out_real