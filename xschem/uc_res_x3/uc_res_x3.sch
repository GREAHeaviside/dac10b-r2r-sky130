v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 200 -120 200 -100 {lab=#net1}
N 150 0 200 0 {lab=upper_bit}
N 200 -40 200 0 {lab=upper_bit}
N 200 0 260 0 {lab=upper_bit}
N 200 -140 200 -120 {lab=#net1}
N 200 -230 200 -200 {lab=sw_out}
N 200 -240 200 -230 {lab=sw_out}
N 140 0 150 0 {lab=upper_bit}
N 40 0 80 0 {lab=lower_bit}
N 10 -220 40 -220 {lab=sw_out}
N 10 -180 40 -180 {lab=upper_bit}
N 10 -140 40 -140 {lab=lower_bit}
N 30 0 40 0 {lab=lower_bit}
N 260 0 270 0 {lab=upper_bit}
N 150 -170 180 -170 {lab=vss}
N 150 -70 180 -70 {lab=vss}
N 110 -40 110 -20 {lab=vss}
N 110 -40 150 -40 {lab=vss}
N 150 -170 150 -40 {lab=vss}
N 10 -100 40 -100 {lab=vss}
C {sky130_fd_pr/res_xhigh_po_1p41.sym} 200 -170 0 0 {name=R1
L=14.1
model=res_xhigh_po_1p41
spiceprefix=X
mult=1}
C {sky130_fd_pr/res_xhigh_po_1p41.sym} 200 -70 0 0 {name=R2
L=14.1
model=res_xhigh_po_1p41
spiceprefix=X
mult=1}
C {sky130_fd_pr/res_xhigh_po_1p41.sym} 110 0 1 0 {name=R3
L=14.1
model=res_xhigh_po_1p41
spiceprefix=X
mult=1}
C {iopin.sym} 10 -220 2 0 {name=p1 lab=sw_out}
C {iopin.sym} 10 -180 2 0 {name=p2 lab=upper_bit}
C {iopin.sym} 10 -140 2 0 {name=p3 lab=lower_bit}
C {lab_wire.sym} 40 -220 2 0 {name=p4 sig_type=std_logic lab=sw_out}
C {lab_wire.sym} 200 -240 0 0 {name=p5 sig_type=std_logic lab=sw_out}
C {lab_wire.sym} 40 -180 2 0 {name=p6 sig_type=std_logic lab=upper_bit}
C {lab_wire.sym} 40 -140 2 0 {name=p7 sig_type=std_logic lab=lower_bit}
C {lab_wire.sym} 270 0 2 0 {name=p8 sig_type=std_logic lab=upper_bit}
C {lab_wire.sym} 30 0 2 1 {name=p9 sig_type=std_logic lab=lower_bit}
C {iopin.sym} 10 -100 2 0 {name=p10 lab=vss}
C {lab_wire.sym} 40 -100 2 0 {name=p11 sig_type=std_logic lab=vss}
C {lab_wire.sym} 150 -170 0 0 {name=p12 sig_type=std_logic lab=vss}
