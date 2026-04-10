v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 140 120 180 120 {lab=#net1}
N 180 -70 220 -70 {lab=#net1}
N 140 -70 180 -70 {lab=#net1}
N 40 120 60 120 {lab=#net2}
N 30 -70 60 -70 {lab=#net3}
N -80 -70 -60 -70 {lab=Q}
N 310 -70 340 -70 {lab=Q}
N 300 40 300 60 {lab=vdd}
N -20 -130 -20 -110 {lab=vdd}
N 260 -130 260 -110 {lab=vdd}
N 110 -130 110 -110 {lab=vdd}
N -20 60 -20 80 {lab=vdd}
N 110 60 110 80 {lab=vdd}
N 30 120 40 120 {lab=#net2}
N -20 -30 -20 -10 {lab=vss}
N 110 -30 110 -10 {lab=vss}
N 260 -30 260 -10 {lab=vss}
N 110 160 110 180 {lab=vss}
N -20 160 -20 180 {lab=vss}
N 180 120 200 120 {lab=#net1}
N 200 -70 200 120 {lab=#net1}
N -80 120 -60 120 {lab=D}
N -80 -160 -80 -70 {lab=Q}
N -80 -160 350 -160 {lab=Q}
N 350 -160 350 -70 {lab=Q}
N 340 -70 350 -70 {lab=Q}
N 350 -70 380 -70 {lab=Q}
N -220 -160 -190 -160 {lab=vdd}
N -220 -130 -190 -130 {lab=vss}
N -220 -100 -190 -100 {lab=clk}
N -220 -70 -190 -70 {lab=D}
N -220 -40 -190 -40 {lab=Q}
N 240 100 260 100 {lab=clk}
N 90 -30 90 80 {lab=nclk}
N 90 30 100 30 {lab=nclk}
N 90 160 90 180 {lab=clk}
N 90 -130 90 -110 {lab=clk}
N 350 100 370 100 {lab=nclk}
N 300 140 300 170 {lab=vss}
C {/foss/designs/dac10b-r2r-sky130/xschem/t-gate/t_gate.sym} 80 -70 0 0 {name=x1}
C {/foss/designs/dac10b-r2r-sky130/xschem/t-gate/t_gate.sym} 80 120 0 0 {name=x2}
C {/foss/designs/dac10b-r2r-sky130/xschem/inv_x1/inv_x1.sym} 260 -70 0 0 {name=x3}
C {/foss/designs/dac10b-r2r-sky130/xschem/inv_x1/inv_x1.sym} -20 -70 0 0 {name=x4}
C {/foss/designs/dac10b-r2r-sky130/xschem/inv_x1/inv_x1.sym} -20 120 0 0 {name=x5}
C {/foss/designs/dac10b-r2r-sky130/xschem/inv_x1/inv_x1.sym} 300 100 0 0 {name=x6}
C {ipin.sym} -220 -100 0 0 {name=p1 lab=clk}
C {ipin.sym} -220 -160 0 0 {name=p2 lab=vdd}
C {ipin.sym} -220 -130 0 0 {name=p3 lab=vss}
C {lab_wire.sym} -190 -160 2 0 {name=p4 sig_type=std_logic lab=vdd}
C {lab_wire.sym} 300 40 0 0 {name=p8 sig_type=std_logic lab=vdd}
C {lab_wire.sym} -20 -130 0 0 {name=p9 sig_type=std_logic lab=vdd}
C {lab_wire.sym} 260 -130 0 0 {name=p10 sig_type=std_logic lab=vdd}
C {lab_wire.sym} 110 -130 0 1 {name=p5 sig_type=std_logic lab=vdd}
C {lab_wire.sym} -20 60 0 0 {name=p6 sig_type=std_logic lab=vdd}
C {lab_wire.sym} 110 60 0 1 {name=p7 sig_type=std_logic lab=vdd}
C {lab_wire.sym} -20 -10 2 0 {name=p11 sig_type=std_logic lab=vss}
C {lab_wire.sym} 110 -10 2 0 {name=p12 sig_type=std_logic lab=vss}
C {lab_wire.sym} 260 -10 2 0 {name=p13 sig_type=std_logic lab=vss}
C {lab_wire.sym} 110 180 2 0 {name=p14 sig_type=std_logic lab=vss}
C {lab_wire.sym} -20 180 2 0 {name=p15 sig_type=std_logic lab=vss}
C {lab_wire.sym} 240 100 2 1 {name=p16 sig_type=std_logic lab=clk}
C {lab_wire.sym} 370 100 0 1 {name=p17 sig_type=std_logic lab=nclk}
C {lab_wire.sym} 100 30 0 1 {name=p18 sig_type=std_logic lab=nclk}
C {lab_wire.sym} 380 -70 0 1 {name=p19 sig_type=std_logic lab=Q}
C {lab_wire.sym} -80 120 2 1 {name=p20 sig_type=std_logic lab=D}
C {lab_wire.sym} 90 180 2 1 {name=p21 sig_type=std_logic lab=clk}
C {lab_wire.sym} 90 -130 0 0 {name=p22 sig_type=std_logic lab=clk}
C {lab_wire.sym} -190 -130 2 0 {name=p23 sig_type=std_logic lab=vss}
C {lab_wire.sym} -190 -100 2 0 {name=p24 sig_type=std_logic lab=clk}
C {ipin.sym} -220 -70 0 0 {name=p25 lab=D}
C {lab_wire.sym} -190 -70 2 0 {name=p26 sig_type=std_logic lab=D}
C {opin.sym} -220 -40 2 0 {name=p27 lab=Q}
C {lab_wire.sym} -190 -40 2 0 {name=p28 sig_type=std_logic lab=Q}
C {lab_wire.sym} 300 170 2 0 {name=p29 sig_type=std_logic lab=vss}
