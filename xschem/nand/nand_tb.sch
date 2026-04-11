v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 90 -290 90 -270 {lab=GND}
N 90 -390 90 -370 {lab=vdd}
N 40 -340 60 -340 {lab=A}
N 40 -320 60 -320 {lab=B}
N 150 -330 190 -330 {lab=Y}
N 190 -330 230 -330 {lab=Y}
N 180 -330 180 -320 {lab=Y}
N 180 -260 180 -240 {lab=GND}
N 90 -270 90 -250 {lab=GND}
N 60 -70 60 -40 {lab=GND}
N 60 -160 60 -130 {lab=A}
N 280 -70 280 -40 {lab=GND}
N 280 -160 280 -130 {lab=B}
N 510 -60 510 -40 {lab=GND}
N 510 -160 510 -120 {lab=vdd}
C {nand.sym} 80 -330 0 0 {name=x1}
C {lab_pin.sym} 90 -390 0 0 {name=p1 sig_type=std_logic lab=vdd}
C {lab_pin.sym} 40 -340 0 0 {name=p3 sig_type=std_logic lab=A}
C {lab_pin.sym} 40 -320 0 0 {name=p4 sig_type=std_logic lab=B}
C {capa.sym} 180 -290 0 0 {name=C1
m=1
value=50f
footprint=1206
device="ceramic capacitor"}
C {gnd.sym} 180 -240 0 0 {name=l1 lab=GND}
C {gnd.sym} 90 -250 0 0 {name=l2 lab=GND}
C {lab_pin.sym} 230 -330 2 0 {name=p2 sig_type=std_logic lab=Y}
C {gnd.sym} 60 -40 0 0 {name=l3 lab=GND}
C {vsource.sym} 60 -100 0 0 {name=V1 value="PULSE(0 1.8 0 100p 100p 1u 2u)" savecurrent=false}
C {vsource.sym} 280 -100 0 0 {name=V2 value="PULSE(0 1.8 0 100p 100p 2u 4u)" savecurrent=false}
C {lab_pin.sym} 60 -160 0 0 {name=p5 sig_type=std_logic lab=A}
C {gnd.sym} 280 -40 0 0 {name=l4 lab=GND}
C {lab_pin.sym} 280 -160 0 0 {name=p6 sig_type=std_logic lab=B}
C {sky130_fd_pr/corner.sym} 270 -340 0 0 {name=CORNER only_toplevel=false corner=tt}
C {code_shown.sym} 390 -350 0 0 {name=NGSPICE only_toplevel=false value="
.option savecurrents
.control
save all
tran 1n 10u
plot V(A)+4 V(B)+2 V(Y)
.endc
"}
C {vsource.sym} 510 -90 0 0 {name=V3 value=1.8 savecurrent=false}
C {gnd.sym} 510 -40 0 0 {name=l5 lab=GND}
C {lab_pin.sym} 510 -160 0 0 {name=p7 sig_type=std_logic lab=vdd}
