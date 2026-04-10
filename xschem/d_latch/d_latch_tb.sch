v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 110 -220 110 -190 {lab=vdd}
N 20 -140 50 -140 {lab=D}
N 20 -80 50 -80 {lab=clk}
N 170 -140 210 -140 {lab=Q}
N 110 -30 110 -20 {lab=GND}
N 190 -140 190 -120 {lab=Q}
N 415 -290 415 -255 {lab=clk}
N 415 -195 415 -180 {lab=GND}
N 415 -140 415 -105 {lab=D}
N 415 -45 415 -30 {lab=GND}
N 190 -60 190 -40 {lab=GND}
N 320 -60 320 -40 {lab=GND}
N 320 -160 320 -120 {lab=vdd}
C {d_latch.sym} 70 -50 0 0 {name=x1}
C {sky130_fd_pr/corner.sym} 0 -370 0 0 {name=CORNER only_toplevel=false corner=tt}
C {code_shown.sym} 120 -380 0 0 {name=NGSPICE only_toplevel=false value="
.option savecurrents
.control
save all
tran 1n 10u
plot V(clk)+4 V(D)+2 V(Q)
.endc
"}
C {lab_pin.sym} 210 -140 2 0 {name=p1 sig_type=std_logic lab=Q}
C {lab_pin.sym} 110 -220 2 0 {name=p2 sig_type=std_logic lab=vdd}
C {lab_pin.sym} 20 -140 0 0 {name=p4 sig_type=std_logic lab=D}
C {lab_pin.sym} 20 -80 0 0 {name=p5 sig_type=std_logic lab=clk}
C {gnd.sym} 110 -20 0 0 {name=l1 lab=GND}
C {vsource.sym} 415 -225 0 0 {name=Vclk value="PULSE(0 1.8 0 100p 100p 1u 2u)" savecurrent=false}
C {gnd.sym} 415 -180 0 0 {name=l4 lab=GND}
C {lab_pin.sym} 415 -290 2 0 {name=p6 sig_type=std_logic lab=clk}
C {vsource.sym} 415 -75 0 0 {name=Vdata value="PULSE(0 1.8 0 100p 100p 1.3u 3.1u)" savecurrent=false}
C {gnd.sym} 415 -30 0 0 {name=l5 lab=GND}
C {lab_pin.sym} 415 -140 2 0 {name=p7 sig_type=std_logic lab=D}
C {capa.sym} 190 -90 0 0 {name=C1
m=1
value=1p
footprint=1206
device="ceramic capacitor"}
C {gnd.sym} 190 -40 0 0 {name=l2 lab=GND}
C {vsource.sym} 320 -90 0 0 {name=V1 value=1.8 savecurrent=false}
C {gnd.sym} 320 -40 0 0 {name=l3 lab=GND}
C {lab_pin.sym} 320 -160 0 0 {name=p3 sig_type=std_logic lab=vdd}
