v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 130 -280 130 -250 {lab=vdd}
N 40 -200 70 -200 {lab=D}
N 40 -140 70 -140 {lab=clk}
N 250 -200 290 -200 {lab=Q}
N 130 -90 130 -80 {lab=GND}
N 270 -200 270 -180 {lab=Q}
N 455 -340 455 -305 {lab=clk}
N 455 -245 455 -230 {lab=GND}
N 455 -190 455 -155 {lab=D}
N 455 -95 455 -80 {lab=GND}
N 270 -120 270 -100 {lab=GND}
N 380 -100 380 -80 {lab=GND}
N 380 -200 380 -160 {lab=vdd}
C {/foss/designs/dac10b-r2r-sky130/xschem/uc_latch/uc_latch.sym} 90 -110 0 0 {name=x1}
C {sky130_fd_pr/corner.sym} 0 -440 0 0 {name=CORNER only_toplevel=false corner=tt}
C {code_shown.sym} 120 -450 0 0 {name=NGSPICE only_toplevel=false value="
.option savecurrents
.control
save all
tran 1n 10u
plot V(clk)+4 V(D)+2 V(Q)
.endc
"}
C {lab_pin.sym} 290 -200 2 0 {name=p1 sig_type=std_logic lab=Q}
C {lab_pin.sym} 130 -280 2 0 {name=p2 sig_type=std_logic lab=vdd}
C {lab_pin.sym} 40 -200 0 0 {name=p4 sig_type=std_logic lab=D}
C {lab_pin.sym} 40 -140 0 0 {name=p5 sig_type=std_logic lab=clk}
C {gnd.sym} 130 -80 0 0 {name=l1 lab=GND}
C {vsource.sym} 455 -275 0 0 {name=Vclk value="PULSE(0 1.8 0 100p 100p 1u 2u)" savecurrent=false}
C {gnd.sym} 455 -230 0 0 {name=l4 lab=GND}
C {lab_pin.sym} 455 -340 2 0 {name=p6 sig_type=std_logic lab=clk}
C {vsource.sym} 455 -125 0 0 {name=Vdata value="PULSE(0 1.8 0 100p 100p 1.3u 3.1u)" savecurrent=false}
C {gnd.sym} 455 -80 0 0 {name=l5 lab=GND}
C {lab_pin.sym} 455 -190 2 0 {name=p7 sig_type=std_logic lab=D}
C {capa.sym} 270 -150 0 0 {name=C1
m=1
value=1p
footprint=1206
device="ceramic capacitor"}
C {gnd.sym} 270 -100 0 0 {name=l2 lab=GND}
C {vsource.sym} 380 -130 0 0 {name=V1 value=1.8 savecurrent=false}
C {gnd.sym} 380 -80 0 0 {name=l3 lab=GND}
C {lab_pin.sym} 380 -200 0 0 {name=p3 sig_type=std_logic lab=vdd}
