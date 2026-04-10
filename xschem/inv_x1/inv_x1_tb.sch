v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N -150 160 -150 180 {lab=GND}
N -70 160 -70 180 {lab=GND}
N 30 40 30 60 {lab=GND}
N -150 70 -150 100 {lab=vdd}
N -70 70 -70 100 {lab=vin}
N -40 0 -10 0 {lab=vin}
N 30 -70 30 -40 {lab=vdd}
N 80 0 110 0 {lab=vout}
C {inv_x1.sym} 30 0 0 0 {name=x1}
C {vsource.sym} -150 130 0 0 {name=vdd value=1.8 savecurrent=false}
C {vsource.sym} -70 130 0 0 {name=vin value=0 savecurrent=false}
C {gnd.sym} -70 180 0 0 {name=l1 lab=GND}
C {gnd.sym} -150 180 0 0 {name=l2 lab=GND}
C {gnd.sym} 30 60 0 0 {name=l3 lab=GND}
C {lab_pin.sym} -70 70 0 0 {name=p1 sig_type=std_logic lab=vin}
C {lab_pin.sym} -40 0 0 0 {name=p2 sig_type=std_logic lab=vin}
C {lab_pin.sym} -150 70 0 0 {name=p3 sig_type=std_logic lab=vdd}
C {lab_pin.sym} 30 -70 0 0 {name=p4 sig_type=std_logic lab=vdd}
C {lab_pin.sym} 110 0 2 0 {name=p5 sig_type=std_logic lab=vout}
C {sky130_fd_pr/corner.sym} -10 140 0 0 {name=CORNER only_toplevel=false corner=tt}
C {code_shown.sym} 140 140 0 0 {name=NGSPICE only_toplevel=false value="
.include /foss/designs/dac10b-r2r-sky130/klayout/inv_x1/inv_x1.pex.spice
.option savecurrents
.control
save all
dc vin 0 1.8 0.01
wrdata output.csv v(vout) v(vin) i(vdd)
plot V(vin) V(vout)
.endc
"}
