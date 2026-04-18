v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 470 -280 500 -280 {lab=#net1}
N 480 -110 500 -110 {lab=lower_bit}
N 690 -110 710 -110 {lab=upper_bit}
N 260 -280 290 -280 {lab=denb}
N 260 -220 290 -220 {lab=strb}
N 100 -300 120 -300 {lab=denb}
N 100 -260 120 -260 {lab=strb}
N 100 -110 130 -110 {lab=upper_bit}
N 100 -140 130 -140 {lab=lower_bit}
N 100 -170 130 -170 {lab=vss}
N 100 -200 130 -200 {lab=vdd}
N 350 -350 350 -330 {lab=vdd}
N 550 -350 550 -320 {lab=vdd}
N 350 -170 350 -150 {lab=vss}
N 550 -240 550 -210 {lab=vss}
N 830 -240 830 -220 {lab=vdd}
N 830 -160 830 -140 {lab=vss}
N 100 -80 130 -80 {lab=sw_out}
N 690 -280 710 -280 {lab=sw_out}
C {/foss/designs/dac10b-r2r-sky130/xschem/uc_res+sw/uc_res+sw.sym} 220 -80 0 0 {name=x1}
C {/foss/designs/dac10b-r2r-sky130/xschem/uc_latch/uc_latch.sym} 310 -190 0 0 {name=x2}
C {/foss/designs/dac10b-r2r-sky130/xschem/decap/decap.sym} 760 -140 0 0 {name=x3[0:44]}
C {ipin.sym} 100 -300 0 0 {name=p1 lab=denb}
C {lab_wire.sym} 120 -300 2 0 {name=p2 sig_type=std_logic lab=denb}
C {lab_wire.sym} 260 -280 0 0 {name=p3 sig_type=std_logic lab=denb}
C {ipin.sym} 100 -260 0 0 {name=p4 lab=strb}
C {lab_wire.sym} 120 -260 2 0 {name=p5 sig_type=std_logic lab=strb}
C {lab_wire.sym} 260 -220 0 0 {name=p6 sig_type=std_logic lab=strb}
C {iopin.sym} 100 -200 2 0 {name=p7 lab=vdd}
C {iopin.sym} 100 -170 2 0 {name=p8 lab=vss}
C {iopin.sym} 100 -140 2 0 {name=p9 lab=lower_bit}
C {iopin.sym} 100 -110 2 0 {name=p10 lab=upper_bit}
C {lab_wire.sym} 130 -200 2 0 {name=p11 sig_type=std_logic lab=vdd}
C {lab_wire.sym} 130 -170 2 0 {name=p12 sig_type=std_logic lab=vss}
C {lab_wire.sym} 130 -140 2 0 {name=p13 sig_type=std_logic lab=lower_bit}
C {lab_wire.sym} 130 -110 2 0 {name=p14 sig_type=std_logic lab=upper_bit}
C {lab_wire.sym} 350 -350 0 0 {name=p15 sig_type=std_logic lab=vdd}
C {lab_wire.sym} 550 -350 0 0 {name=p16 sig_type=std_logic lab=vdd}
C {lab_wire.sym} 350 -150 2 0 {name=p17 sig_type=std_logic lab=vss}
C {lab_wire.sym} 550 -210 2 0 {name=p18 sig_type=std_logic lab=vss}
C {lab_wire.sym} 830 -240 0 0 {name=p19 sig_type=std_logic lab=vdd}
C {lab_wire.sym} 830 -140 2 0 {name=p20 sig_type=std_logic lab=vss}
C {lab_wire.sym} 480 -110 0 0 {name=p21 sig_type=std_logic lab=lower_bit}
C {lab_wire.sym} 710 -110 0 1 {name=p22 sig_type=std_logic lab=upper_bit}
C {lab_wire.sym} 130 -80 2 0 {name=p24 sig_type=std_logic lab=sw_out}
C {lab_wire.sym} 710 -280 2 0 {name=p25 sig_type=std_logic lab=sw_out}
C {iopin.sym} 100 -80 2 0 {name=p23 lab=sw_out}
