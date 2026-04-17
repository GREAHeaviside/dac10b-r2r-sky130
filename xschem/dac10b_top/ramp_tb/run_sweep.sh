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


# Default iterations
ITERS=10

while [[ "$#" -gt 0 ]]; do
    case $1 in
        --iters) 
            ITERS="$2"
            shift 2
            ;;
        *) 
            echo "Usage: ./run_sweep.sh [--iters <number>]"
            exit 1 
            ;;
    esac
done

# Create timing_profile.csv if it doesn't exist
if [ ! -f timing_profile.csv ]; then
    echo "Code,StartTime,EndTime,Duration(s)" > timing_profile.csv
fi

SESSION_LOG="sim_session_$(date +%Y%m%d_%H%M%S).txt"
echo "=== Running $ITERS iterations. Log: $SESSION_LOG ==="

for ((i=1; i<=ITERS; i++)); do
    
    # Run the Python script to get the next code to simulate
    PY_OUT=$(python3 generate_dc_sweep.py)
    
    if [[ "$PY_OUT" == *"DONE"* ]]; then
        echo "¡All codes simulated (1024)! Exiting."
        break
    fi
    
    # Get the current code from the Python output
    CURRENT_CODE=$(echo "$PY_OUT" | grep "RUNNING_CODE" | cut -d':' -f2)
    
    # Begin timing
    START_DATE=$(date +"%Y-%m-%d %H:%M:%S")
    START_SECONDS=$(date +%s)
    
    echo "[$i/$ITERS] Simulating Code $CURRENT_CODE... (Started: $START_DATE)"
    
    # Run Ngspice and save its output to a temporary file
    ngspice -b -o temp_ngspice.log dac10b_top_tb_ramp.spice
    
    # Add the temporary log to the session log
    cat temp_ngspice.log >> "$SESSION_LOG"
    
    # End timing
    END_DATE=$(date +"%Y-%m-%d %H:%M:%S")
    END_SECONDS=$(date +%s)
    
    # calculate duration
    DURATION=$((END_SECONDS - START_SECONDS))
    
    echo "Completed in ${DURATION} seconds."
    echo "----------------------------------------"
    
    # Save timing info to CSV
    echo "$CURRENT_CODE,$START_DATE,$END_DATE,$DURATION" >> timing_profile.csv

done

# Limpiamos el archivo temporal
rm -f temp_ngspice.log
echo "Session completed."