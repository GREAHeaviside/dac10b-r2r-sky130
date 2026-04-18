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

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

v_high = 1.8
v_low = 0.0
MAX_CODE = 1023

start_code = 0
append_mode = True
last_vout = 0.0

if os.path.exists('dac_transfer.csv'):
    with open('dac_transfer.csv', 'r') as f:
        lines = f.readlines()
        if len(lines) > 1:
            last_line = lines[-1].strip()
            try:
                parts = last_line.split(',')
                last_code = int(parts[0])
                last_vout = float(parts[1])
                start_code = last_code + 1
                append_mode = True
            except (ValueError, IndexError):
                pass

if start_code > MAX_CODE:
    print("DONE")
    exit(0)

print(f"RUNNING_CODE:{start_code}")

with open('stimulus_dc.spice', 'w') as f:
    for i in range(10):
        f.write(f"V_D{i} D[{i}] 0 DC 0\n")

    if start_code > 0:
        f.write(f".nodeset V(vout)={last_vout}\n")

    f.write("\n.control\n")
    
    if not append_mode:
        f.write("echo \"Code,Vout\" > dac_transfer.csv\n")

    f.write("alter Vclk 1.8\n\n")

    bits = format(start_code, '010b')
    for i in range(10):
        bit_index = 9 - i 
        v_val = v_high if bits[bit_index] == '1' else v_low
        f.write(f"alter V_D{i} {v_val}\n")
    
    f.write("op\n")
    f.write(f"echo \"{start_code},$&V(vout)\" >> dac_transfer.csv\n")
    
    f.write("rusage all\n")
    
    f.write("destroy all\n")
    f.write("quit\n")
    f.write(".endc\n")