v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 200 -180 200 -160 {lab=#net1}
N 200 -100 200 -70 {lab=vss}
N 200 -260 200 -240 {lab=Y}
N 200 -260 280 -260 {lab=Y}
N 280 -280 280 -260 {lab=Y}
N 120 -260 200 -260 {lab=Y}
N 120 -280 120 -260 {lab=Y}
N 120 -360 120 -340 {lab=vdd}
N 120 -360 280 -360 {lab=vdd}
N 280 -360 280 -340 {lab=vdd}
N 280 -260 310 -260 {lab=Y}
N 200 -400 200 -360 {lab=vdd}
N 120 -310 140 -310 {lab=vdd}
N 140 -360 140 -310 {lab=vdd}
N 280 -310 310 -310 {lab=vdd}
N 310 -360 310 -310 {lab=vdd}
N 280 -360 310 -360 {lab=vdd}
N 40 -310 80 -310 {lab=A}
N 200 -310 240 -310 {lab=B}
N 120 -210 160 -210 {lab=A}
N 120 -130 160 -130 {lab=B}
N 200 -130 220 -130 {lab=vss}
N 200 -70 220 -70 {lab=vss}
N 200 -70 200 -40 {lab=vss}
N 220 -130 220 -70 {lab=vss}
N 220 -210 220 -130 {lab=vss}
N 200 -210 220 -210 {lab=vss}
N 0 -40 30 -40 {lab=xxx}
N 0 -70 30 -70 {lab=B}
N 0 -100 30 -100 {lab=A}
N 0 -130 30 -130 {lab=vss}
N 0 -160 30 -160 {lab=vdd}
C {sky130_fd_pr/nfet_01v8.sym} 180 -130 0 0 {name=M2
W=1
L=0.17
nf=1
mult=1
ad="\{int((nf+1)/2) * W/nf * 0.29\}"
pd="\{2*int((nf+1)/2) * (W/nf + 0.29)\}"
as="\{int((nf+2)/2) * W/nf * 0.29\}"
ps="\{2*int((nf+2)/2) * (W/nf + 0.29)\}"
nrd="\{0.29 / W\}" nrs="\{0.29 / W\}"
sa=0 sb=0 sd=0
model=nfet_01v8
spiceprefix=X
}
C {sky130_fd_pr/pfet_01v8.sym} 100 -310 0 0 {name=M1
W=1
L=0.17
nf=1
mult=1
ad="\{int((nf+1)/2) * W/nf * 0.29\}"
pd="\{2*int((nf+1)/2) * (W/nf + 0.29)\}"
as="\{int((nf+2)/2) * W/nf * 0.29\}"
ps="\{2*int((nf+2)/2) * (W/nf + 0.29)\}"
nrd="\{0.29 / W\}" nrs="\{0.29 / W\}"
sa=0 sb=0 sd=0
model=pfet_01v8
spiceprefix=X}
C {sky130_fd_pr/nfet_01v8.sym} 180 -210 0 0 {name=M3
W=1
L=0.17
nf=1
mult=1
ad="\{int((nf+1)/2) * W/nf * 0.29\}"
pd="\{2*int((nf+1)/2) * (W/nf + 0.29)\}"
as="\{int((nf+2)/2) * W/nf * 0.29\}"
ps="\{2*int((nf+2)/2) * (W/nf + 0.29)\}"
nrd="\{0.29 / W\}" nrs="\{0.29 / W\}"
sa=0 sb=0 sd=0
model=nfet_01v8
spiceprefix=X
}
C {sky130_fd_pr/pfet_01v8.sym} 260 -310 0 0 {name=M4
W=1
L=0.17
nf=1
mult=1
ad="\{int((nf+1)/2) * W/nf * 0.29\}"
pd="\{2*int((nf+1)/2) * (W/nf + 0.29)\}"
as="\{int((nf+2)/2) * W/nf * 0.29\}"
ps="\{2*int((nf+2)/2) * (W/nf + 0.29)\}"
nrd="\{0.29 / W\}" nrs="\{0.29 / W\}"
sa=0 sb=0 sd=0
model=pfet_01v8
spiceprefix=X}
C {ipin.sym} 0 -160 0 0 {name=p1 lab=vdd}
C {ipin.sym} 0 -130 0 0 {name=p2 lab=vss}
C {ipin.sym} 0 -100 0 0 {name=p3 lab=A}
C {ipin.sym} 0 -70 0 0 {name=p4 lab=B}
C {opin.sym} 0 -40 2 0 {name=p5 lab=Y}
C {lab_wire.sym} 30 -160 2 0 {name=p6 sig_type=std_logic lab=vdd}
C {lab_wire.sym} 30 -130 2 0 {name=p7 sig_type=std_logic lab=vss}
C {lab_wire.sym} 30 -100 2 0 {name=p8 sig_type=std_logic lab=A}
C {lab_wire.sym} 30 -70 2 0 {name=p9 sig_type=std_logic lab=B}
C {lab_wire.sym} 30 -40 2 0 {name=p10 sig_type=std_logic lab=Y}
C {lab_wire.sym} 200 -400 0 0 {name=p11 sig_type=std_logic lab=vdd}
C {lab_wire.sym} 200 -40 2 0 {name=p12 sig_type=std_logic lab=vss}
C {lab_wire.sym} 40 -310 0 0 {name=p13 sig_type=std_logic lab=A}
C {lab_wire.sym} 200 -310 0 0 {name=p14 sig_type=std_logic lab=B}
C {lab_wire.sym} 120 -210 0 0 {name=p15 sig_type=std_logic lab=A}
C {lab_wire.sym} 120 -130 0 0 {name=p16 sig_type=std_logic lab=B}
C {lab_wire.sym} 310 -260 2 0 {name=p17 sig_type=std_logic lab=Y}
