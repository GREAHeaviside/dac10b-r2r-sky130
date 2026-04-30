# 10-Bit R-2R DAC in Sky130

![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)
![Python 3.x](https://img.shields.io/badge/Python-3.x-yellow.svg)
![PDK: Sky130](https://img.shields.io/badge/PDK-SkyWater_130nm-green.svg)
[![Tools: IIC OSIC Tools](https://img.shields.io/badge/Tools-IIC__OSIC__Tools_2024.11-8A2BE2.svg)](https://github.com/iic-jku/IIC-OSIC-TOOLS)

Currently in its final stage of publishing, this repository contains the analog design, schematics, and a custom Python simulation engine for a 10-bit R-2R Digital-to-Analog Converter (DAC). The hardware design is fully based on the open-source SkyWater 130nm PDK.

## Key Achievements

### 1. Analog Design (Xschem + Ngspice)
* Completed the full hierarchical schematic of the 10-bit R-2R DAC.
* Included all base primitives, bit-cells, logic controllers, and ramp testbenches.

### 2. Custom DAC Simulator Engine (Python)
* Developed a standalone Python mathematical engine to simulate R-2R mismatch, calculate static metrics (DNL/INL), and perform spectral analysis (ENOB, SNR, THD).
* Implements Pelgrom's Law for stochastic mismatch modeling.

## Planned Optimizations & Known Issues

**SPICE Simulation Times:**
Initially, computing times for the ramp testbench were extremely high due to Ngspice unwrapping all hierarchies into a flattened SPICE file on the fly. 
* **Improvement:** Developed a Python script that unwraps the hierarchy only once before simulation. 
* **Result:** Achieved simulation times of 2~3 minutes per code (Tested in the TT corner on an 11th Gen i3 with 12GB RAM).

## Roadmap / To-Do

- [ ] **GUI for the Simulator:** Working on a Graphical User Interface to quickly test and simulate $n$-bit DACs for didactic and academic purposes.
- [ ] **Improve Simulation Times:** Working on optimization methods to obtain full dynamic range simulation in a reasonable time (currently >2 days for the full range).
- [ ] **Sine and Transient Testbench:** Facing the same bottlenecks as static simulations. Working on ways to improve computing times for transient/sine simulations in order to obtain settling time and ENOB for a desired frequency.
- [ ] **Layout Integration:** Publish the physical implementation (GDSII) and post-layout verification steps.
