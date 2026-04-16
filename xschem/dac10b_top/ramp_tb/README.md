# DAC R-2R 10-bit – DC Transfer Curve Simulation

This folder implements an automated workflow to generate the **static transfer curve** for the proyect. The flow combines schematic capture in xschem, netlist generation, and automated DC sweeps using Python and Bash.

---

*IMPORTANT: this test is under dac10b-r2r-sky130 proyect, read the enviroment requirements to run it* 

---
## Usage

### Step 1 – Generate Netlist

In xschem:

* Load the testbench schematic (`dac10b_top_tb_ramp.sch`).
* Set the simulation corner if needed (default is TT).
* Export the netlist (this will generate `dac10b_top_tb_ramp.spice`).

---

### Step 2 – Run Automated Sweep

Make the script executable using IIC OSIC TOOLS shell:

```bash
chmod +x run_sweep.sh
```

Run:

```bash
./run_sweep.sh
```

---

## Output

### `dac_transfer.csv`

Contains the DAC transfer curve:

```text
Code,Vout
0,0.000
...
1023,1.8
```

---

### Log files

```text
sim1_log.txt
sim2_log.txt
...
```

Each corresponds to a chunk of the sweep.

---

## Simulation Strategy

* Total codes: 1024 (10-bit DAC)
* Simulation is split into chunks (`CHUNK_SIZE`)
* Results are appended progressively
* Resume capability from last completed code

Due to the heavy computation required by the Sky130 PDK models, each chunk of codes has a computing time of approximately 5-10 minutes, practically using full processor capability (tested on a 13th Gen i3). This script allows you to split up the simulation of the full DAC at your convenience without losing progress.

---

## Internal Operation

1. Python generates SPICE control commands:

   * Sets digital inputs (`V_D[i]`)
   * Runs operating point (`op`)
   * Extracts `V(vout)`

2. ngspice executes the netlist

3. Results are appended to CSV

4. Loop continues until completion

---

## License

This project is licensed under the GNU General Public License v3.0.

See the `LICENSE` file for details.

---

## Author

GREA Heaviside (@GREAHeaviside)