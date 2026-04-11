v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 30 -100 70 -100 {lab=A}
N 110 -180 110 -140 {lab=vdd}
N 110 -60 110 -30 {lab=vss}
N 110 -30 110 -20 {lab=vss}
N 160 -100 200 -100 {lab=Y}
N 110 -190 110 -180 {lab=vdd}
N 110 -20 110 -10 {lab=vss}
C {/foss/designs/dac10b-r2r-sky130/xschem/inv_x1/inv_x1.sym} 110 -100 0 0 {name=x_inv[0:15]}
C {ipin.sym} 30 -100 0 0 {name=p1 lab=A}
C {ipin.sym} 110 -190 0 0 {name=p2 lab=vdd}
C {ipin.sym} 110 -10 0 0 {name=p3 lab=vss}
C {opin.sym} 200 -100 0 0 {name=p4 lab=Y}
