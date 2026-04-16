#!/usr/bin/bash

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


# Search highest existing log number to avoid overwriting
# If no logs exist, start at 1

ITER=$(ls sim*_log.txt 2>/dev/null | grep -o '[0-9]\+' | sort -n | tail -1)
if [ -z "$ITER" ]; then
    ITER=1
else
    ITER=$((ITER + 1))
fi

echo "Beginning DAC test sweep === LOG FILE: sim${ITER}_log.txt"

while true; do
    echo "----------------------------------------"
    echo "Iteration number $ITER..."
    
    # Run the Python script to generate the stimulus file and check if we are done
    PY_OUT=$(python3 generate_dc_sweep.py)
    echo "$PY_OUT"
    
    # If the Python script indicates we are done, break the loop
    if [[ "$PY_OUT" == *"DONE"* ]]; then
        echo "Successfully completed all simulations. Exiting."
        break
    fi
    
    # Run ngspice in batch mode
    echo "Running ngspice..."
    ngspice -b -o "sim${ITER}_log.txt" dac10b_top_tb_ramp.spice
    
    # Increment the counter for the next log
    ITER=$((ITER + 1))
done
