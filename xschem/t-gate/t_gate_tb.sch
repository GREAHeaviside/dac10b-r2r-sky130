v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 130 -110 130 -80 {lab=vdd}
N 130 -20 130 0 {lab=GND}
N -90 -10 -90 10 {lab=GND}
N 190 -110 190 -80 {lab=vin}
N 190 -20 190 0 {lab=GND}
N -90 -120 -90 -90 {lab=vdd}
N -170 -50 -140 -50 {lab=vin}
N -130 -100 -110 -100 {lab=GND}
N -110 -100 -110 -90 {lab=GND}
N -130 0 -110 0 {lab=vdd}
N -110 -10 -110 0 {lab=vdd}
N -60 -50 40 -50 {lab=vout}
N 0 20 0 30 {lab=GND}
N 0 -50 0 -40 {lab=vout}
N -170 -100 -170 -90 {lab=GND}
N -170 -100 -130 -100 {lab=GND}
C {vsource.sym} 130 -50 0 0 {name=V1 value=1.8 savecurrent=false}
C {gnd.sym} 130 0 0 0 {name=l1 lab=GND}
C {gnd.sym} -90 10 0 0 {name=l2 lab=GND}
C {vsource.sym} 190 -50 0 0 {name=V2 value=0 savecurrent=false}
C {gnd.sym} 190 0 0 0 {name=l3 lab=GND}
C {lab_pin.sym} 190 -110 0 0 {name=p1 sig_type=std_logic lab=vin}
C {lab_pin.sym} -90 -120 0 0 {name=p2 sig_type=std_logic lab=vdd}
C {lab_pin.sym} -170 -50 0 0 {name=p3 sig_type=std_logic lab=vin}
C {sky130_fd_pr/corner.sym} -210 -270 0 0 {name=CORNER only_toplevel=false corner=tt}
C {code_shown.sym} -80 -310 0 0 {name=NGSPICE only_toplevel=false value="
.option savecurrents
.control
save all
dc V2 0 1.8 0.01
plot V(vin) V(vout)
.endc
"}
C {lab_pin.sym} 130 -110 0 0 {name=p4 sig_type=std_logic lab=vdd}
C {lab_pin.sym} 40 -50 2 0 {name=p5 sig_type=std_logic lab=vout}
C {lab_pin.sym} -130 0 0 0 {name=p6 sig_type=std_logic lab=vdd}
C {gnd.sym} 0 30 0 0 {name=l4 lab=GND}
C {res.sym} 0 -10 0 0 {name=R1
value=1Meg
footprint=1206
device=resistor
m=1}
C {/foss/designs/dac10b-r2r-sky130/xschem/t-gate/t_gate.sym} -120 -50 0 0 {name=x1}
C {gnd.sym} -170 -90 0 0 {name=l5 lab=GND}
