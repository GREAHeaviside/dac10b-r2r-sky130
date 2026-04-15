v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 390 -370 390 -270 {lab=sw_out}
N 370 -370 390 -370 {lab=sw_out}
N 240 -370 280 -370 {lab=sel}
N 250 -90 290 -90 {lab=lower_bit}
N 470 -90 510 -90 {lab=upper_bit}
N 320 -330 320 -290 {lab=vss}
N 320 -450 320 -410 {lab=vdd}
N 590 -280 590 -240 {lab=vdd}
N 590 -180 590 -140 {lab=vss}
N 390 -370 430 -370 {lab=sw_out}
N 110 -350 130 -350 {lab=vdd}
N 110 -320 130 -320 {lab=vss}
N 110 -290 130 -290 {lab=sel}
N 110 -260 130 -260 {lab=lower_bit}
N 110 -230 130 -230 {lab=upper_bit}
N 270 -190 290 -190 {lab=vss}
C {/foss/designs/dac10b-r2r-sky130/xschem/uc_res_x3/uc_res_x3.sym} 270 -90 0 0 {name=x1}
C {/foss/designs/dac10b-r2r-sky130/xschem/inv_xN/inv_x64.sym} 320 -370 0 0 {name=x2[0:7]}
C {/foss/designs/dac10b-r2r-sky130/xschem/decap/decap.sym} 520 -160 0 0 {name=x1[0:23]}
C {lab_wire.sym} 590 -280 0 0 {name=p1 sig_type=std_logic lab=vdd}
C {lab_wire.sym} 590 -140 2 0 {name=p2 sig_type=std_logic lab=vss}
C {lab_wire.sym} 320 -450 0 0 {name=p3 sig_type=std_logic lab=vdd}
C {lab_wire.sym} 320 -290 2 0 {name=p4 sig_type=std_logic lab=vss}
C {lab_wire.sym} 430 -370 2 0 {name=p5 sig_type=std_logic lab=sw_out}
C {lab_wire.sym} 510 -90 2 0 {name=p6 sig_type=std_logic lab=upper_bit}
C {lab_wire.sym} 250 -90 0 0 {name=p7 sig_type=std_logic lab=lower_bit}
C {lab_wire.sym} 240 -370 0 0 {name=p8 sig_type=std_logic lab=sel}
C {iopin.sym} 110 -350 2 0 {name=p9 lab=vdd}
C {iopin.sym} 110 -320 2 0 {name=p10 lab=vss}
C {iopin.sym} 110 -290 2 0 {name=p11 lab=sel}
C {iopin.sym} 110 -260 2 0 {name=p12 lab=lower_bit}
C {iopin.sym} 110 -230 2 0 {name=p13 lab=upper_bit}
C {lab_wire.sym} 130 -260 2 0 {name=p14 sig_type=std_logic lab=lower_bit}
C {lab_wire.sym} 130 -230 2 0 {name=p15 sig_type=std_logic lab=upper_bit}
C {lab_wire.sym} 130 -320 2 0 {name=p16 sig_type=std_logic lab=vss}
C {lab_wire.sym} 130 -350 2 0 {name=p17 sig_type=std_logic lab=vdd}
C {lab_wire.sym} 130 -290 2 0 {name=p18 sig_type=std_logic lab=sel}
C {lab_wire.sym} 270 -190 0 0 {name=p19 sig_type=std_logic lab=vss}
