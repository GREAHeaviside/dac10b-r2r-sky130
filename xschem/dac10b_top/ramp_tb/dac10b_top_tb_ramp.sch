v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 360 -340 360 -320 {lab=vdd}
N 600 -140 600 -120 {lab=GND}
N 600 -230 600 -200 {lab=vout}
N 510 -230 600 -230 {lab=vout}
N 710 -150 710 -120 {lab=GND}
N 360 -140 360 -120 {lab=GND}
N 710 -230 710 -210 {lab=vdd}
N 600 -260 600 -230 {lab=vout}
N 805 -250 805 -215 {lab=clk}
N 805 -155 805 -140 {lab=GND}
N 250 -240 280 -240 {lab=clk}
N 250 -200 280 -200 {lab=D[0:9]}
N 250 -260 280 -260 {lab=vdd}
C {/foss/designs/dac10b-r2r-sky130/xschem/dac10b_top/dac10b_top.sym} 260 -60 0 0 {name=x1}
C {lab_wire.sym} 360 -340 0 0 {name=p1 sig_type=std_logic lab=vdd}
C {capa.sym} 600 -170 0 0 {name=C1
m=1
value=50f
footprint=1206
device="ceramic capacitor"}
C {gnd.sym} 600 -120 0 0 {name=l1 lab=GND}
C {vsource.sym} 710 -180 0 0 {name=V1 value=1.8 savecurrent=false}
C {gnd.sym} 710 -120 0 0 {name=l2 lab=GND}
C {lab_wire.sym} 710 -230 0 0 {name=p3 sig_type=std_logic lab=vdd}
C {gnd.sym} 360 -120 0 0 {name=l3 lab=GND}
C {lab_wire.sym} 600 -260 0 1 {name=p2 sig_type=std_logic lab=vout}
C {vsource.sym} 805 -185 0 0 {name=Vclk value="PULSE(0 1.8 0 100p 100p 4.9n 10n)" savecurrent=false}
C {gnd.sym} 805 -140 0 0 {name=l4 lab=GND}
C {lab_pin.sym} 805 -250 2 0 {name=p6 sig_type=std_logic lab=clk}
C {lab_wire.sym} 250 -240 0 0 {name=p5 sig_type=std_logic lab=clk}
C {sky130_fd_pr/corner.sym} 530 -430 0 0 {name=CORNER only_toplevel=false corner=tt}
C {code_shown.sym} 730 -450 0 0 {name=NGSPICE only_toplevel=false value="
.include stimulus_dc.spice
.options reltol=1e-6 vntol=1u abstol=1p
.options itl1=500 itl2=200
.options cshunt=1f
.options acct
"}
C {lab_wire.sym} 250 -200 0 0 {name=p7 sig_type=std_logic lab=D[0:9]}
C {lab_wire.sym} 250 -260 0 0 {name=p4 sig_type=std_logic lab=vdd}
