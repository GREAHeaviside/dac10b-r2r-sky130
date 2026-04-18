v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 750 -390 790 -390 {lab=sw_out[0:9]}
N 750 -220 790 -220 {lab=ladder[1:9],dac_out}
N 500 -220 530 -220 {lab=ladder[0:9]}
N 340 -390 370 -390 {lab=denb[0:9]}
N 340 -330 370 -330 {lab=strb}
N 710 -630 710 -610 {lab=vdd}
N 710 -530 710 -510 {lab=vss}
N 650 -580 680 -580 {lab=D[0:9]}
N 650 -560 680 -560 {lab=en}
N 770 -570 810 -570 {lab=denb[0:9]}
N 430 -480 430 -460 {lab=vdd}
N -70 -520 -40 -520 {lab=vdd}
N -70 -490 -40 -490 {lab=vss}
N -70 -460 -40 -460 {lab=en}
N -70 -430 -40 -430 {lab=strb}
N 790 -390 810 -390 {lab=sw_out[0:9]}
N -70 -400 -40 -400 {lab=D[0:9]}
N 430 -260 430 -250 {lab=vss}
N -70 -370 -40 -370 {lab=dac_out}
N 180 -250 180 -230 {lab=vss}
N 180 -330 180 -310 {lab=ladder[0]}
N 180 -230 180 -220 {lab=vss}
N 180 -530 180 -500 {lab=vss}
N 180 -620 180 -590 {lab=vss}
N 140 -560 160 -560 {lab=vss}
N 130 -280 160 -280 {lab=vss}
C {/foss/designs/dac10b-r2r-sky130/xschem/uc_bit_cell/uc_bit_cell.sym} 150 -180 0 0 {name=x1[0:9]}
C {/foss/designs/dac10b-r2r-sky130/xschem/nand/nand.sym} 700 -570 0 0 {name=x2[0:9]}
C {lab_wire.sym} 710 -630 0 0 {name=p1 sig_type=std_logic lab=vdd}
C {lab_wire.sym} 710 -510 2 1 {name=p2 sig_type=std_logic lab=vss}
C {lab_wire.sym} 650 -560 2 1 {name=p3 sig_type=std_logic lab=en}
C {lab_wire.sym} 650 -580 0 0 {name=p4 sig_type=std_logic lab=D[0:9]}
C {lab_wire.sym} 810 -570 2 0 {name=p5 sig_type=std_logic lab=denb[0:9]}
C {lab_wire.sym} 430 -480 0 0 {name=p6 sig_type=std_logic lab=vdd}
C {iopin.sym} -70 -520 2 0 {name=p8 lab=vdd}
C {iopin.sym} -70 -490 2 0 {name=p9 lab=vss}
C {lab_wire.sym} -40 -520 2 0 {name=p10 sig_type=std_logic lab=vdd}
C {lab_wire.sym} -40 -490 2 0 {name=p11 sig_type=std_logic lab=vss}
C {ipin.sym} -70 -460 0 0 {name=p12 lab=en}
C {lab_wire.sym} -40 -460 2 0 {name=p13 sig_type=std_logic lab=en}
C {ipin.sym} -70 -430 0 0 {name=p14 lab=strb}
C {lab_wire.sym} -40 -430 2 0 {name=p15 sig_type=std_logic lab=strb}
C {lab_wire.sym} 340 -330 0 0 {name=p16 sig_type=std_logic lab=strb}
C {lab_wire.sym} 340 -390 0 0 {name=p17 sig_type=std_logic lab=denb[0:9]}
C {lab_wire.sym} 810 -390 2 0 {name=p18 sig_type=std_logic lab=sw_out[0:9]}
C {lab_wire.sym} -40 -400 2 0 {name=p21 sig_type=std_logic lab=D[0:9]}
C {ipin.sym} -70 -400 0 0 {name=p22 lab=D[0:9]}
C {lab_wire.sym} 500 -220 2 1 {name=p27 sig_type=std_logic lab=ladder[0:9]}
C {lab_wire.sym} 430 -250 2 1 {name=p7 sig_type=std_logic lab=vss}
C {lab_wire.sym} 790 -220 2 0 {name=p28 sig_type=std_logic lab=ladder[1:9],dac_out}
C {opin.sym} -70 -370 2 0 {name=p29 lab=dac_out}
C {lab_wire.sym} -40 -370 2 0 {name=p30 sig_type=std_logic lab=dac_out}
C {sky130_fd_pr/res_xhigh_po_1p41.sym} 180 -280 0 0 {name=R2
L=14.1
model=res_xhigh_po_1p41
spiceprefix=X
mult=1}
C {lab_wire.sym} 180 -220 2 1 {name=p31 sig_type=std_logic lab=vss}
C {lab_wire.sym} 180 -330 0 1 {name=p32 sig_type=std_logic lab=ladder[0]}
C {sky130_fd_pr/res_xhigh_po_1p41.sym} 180 -560 0 0 {name=R_dummy[0:4]
L=14.1
model=res_xhigh_po_1p41
spiceprefix=X
mult=1}
C {lab_wire.sym} 180 -500 2 1 {name=p33 sig_type=std_logic lab=vss}
C {lab_wire.sym} 180 -620 0 0 {name=p34 sig_type=std_logic lab=vss}
C {lab_wire.sym} 140 -560 2 1 {name=p35 sig_type=std_logic lab=vss}
C {lab_wire.sym} 130 -280 2 1 {name=p19 sig_type=std_logic lab=vss}
