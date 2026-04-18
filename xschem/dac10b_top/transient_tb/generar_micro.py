import math

# Parámetros
v_high = 1.8
v_low = 0.0
t_step = 10e-9
t_trans = 100e-12

start_code = 511
end_code = 514 # Para llegar al 513

with open('stimulus_micro.spice', 'w') as f:
    f.write('* Estímulos DAC - Micro Sweep (511-513)\n')
    pwl_data = {i: [] for i in range(10)}

    for step, code in enumerate(range(start_code, end_code)):
        bits = format(code, '010b')
        t_current = step * t_step
        
        for i in range(10):
            bit_index = 9 - i 
            v_out = v_high if bits[bit_index] == '1' else v_low
            pwl_data[i].append(f"{t_current} {v_out}")
            pwl_data[i].append(f"{t_current + t_step - t_trans} {v_out}")

    for i in range(10):
        puntos_str = " ".join(pwl_data[i])
        f.write(f"V_D{i} D[{i}] 0 PWL({puntos_str})\n")
