v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 220 -140 260 -140 {lab=#net1}
N 350 -140 370 -140 {lab=#net2}
N 460 -140 480 -140 {lab=#net3}
N 570 -140 590 -140 {lab=#net4}
N 160 -220 160 -190 {lab=vdd}
N 300 -220 300 -180 {lab=vdd}
N 410 -220 410 -180 {lab=vdd}
N 520 -220 520 -180 {lab=vdd}
N 630 -220 630 -180 {lab=vdd}
N 160 -220 630 -220 {lab=vdd}
N 160 -30 160 -0 {lab=vss}
N 300 -100 300 0 {lab=vss}
N 410 -100 410 0 {lab=vss}
N 520 -100 520 0 {lab=vss}
N 630 -100 630 0 {lab=vss}
N 160 -0 630 0 {lab=vss}
N 60 -80 100 -80 {lab=strb}
N 60 -140 100 -140 {lab=denb}
N 680 -140 740 -140 {lab=sel}
N 300 -240 300 -220 {lab=vdd}
N 250 -20 250 -0 {lab=vss}
N 100 -300 130 -300 {lab=denb}
N 100 -390 130 -390 {lab=vdd}
N 100 -330 130 -330 {lab=strb}
N 100 -360 130 -360 {lab=vss}
N 100 -270 130 -270 {lab=sel}
C {/foss/designs/dac10b-r2r-sky130/xschem/d_latch/d_latch.sym} 120 -50 0 0 {name=x_dlatch_1}
C {/foss/designs/dac10b-r2r-sky130/xschem/inv_xN/inv_x4.sym} 520 -140 0 0 {name=x1}
C {/foss/designs/dac10b-r2r-sky130/xschem/inv_x1/inv_x1.sym} 300 -140 0 0 {name=x2}
C {/foss/designs/dac10b-r2r-sky130/xschem/inv_x1/inv_x1.sym} 410 -140 0 0 {name=x3}
C {/foss/designs/dac10b-r2r-sky130/xschem/inv_xN/inv_x16.sym} 630 -140 0 0 {name=x4}
C {ipin.sym} 100 -330 0 0 {name=p1 lab=strb}
C {ipin.sym} 100 -390 0 0 {name=p2 lab=vdd}
C {ipin.sym} 100 -360 0 0 {name=p3 lab=vss}
C {ipin.sym} 100 -300 0 0 {name=p25 lab=denb}
C {opin.sym} 100 -270 2 0 {name=p27 lab=sel}
C {lab_wire.sym} 60 -140 0 0 {name=p4 sig_type=std_logic lab=denb}
C {lab_wire.sym} 60 -80 0 0 {name=p5 sig_type=std_logic lab=strb}
C {lab_wire.sym} 300 -240 0 0 {name=p6 sig_type=std_logic lab=vdd}
C {lab_wire.sym} 250 -20 0 0 {name=p7 sig_type=std_logic lab=vss}
C {lab_wire.sym} 740 -140 2 0 {name=p8 sig_type=std_logic lab=sel}
C {lab_wire.sym} 130 -300 2 0 {name=p9 sig_type=std_logic lab=denb}
C {lab_wire.sym} 130 -390 2 0 {name=p10 sig_type=std_logic lab=vdd}
C {lab_wire.sym} 130 -330 2 0 {name=p11 sig_type=std_logic lab=strb}
C {lab_wire.sym} 130 -360 2 0 {name=p12 sig_type=std_logic lab=vss}
C {lab_wire.sym} 130 -270 2 0 {name=p13 sig_type=std_logic lab=sel}
