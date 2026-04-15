v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 300 -190 340 -190 {lab=vdd}
N 300 -280 300 -190 {lab=vdd}
N 380 -190 430 -190 {lab=vss}
N 430 -190 430 -80 {lab=vss}
N 380 -160 380 -80 {lab=vss}
N 380 -80 430 -80 {lab=vss}
N 140 -190 160 -190 {lab=vss}
N 140 -190 140 -80 {lab=vss}
N 140 -80 380 -80 {lab=vss}
N 200 -160 200 -130 {lab=vdd}
N 200 -130 240 -130 {lab=vdd}
N 240 -130 280 -130 {lab=vdd}
N 280 -130 300 -130 {lab=vdd}
N 300 -190 300 -130 {lab=vdd}
N 200 -250 200 -220 {lab=vdd}
N 200 -250 300 -250 {lab=vdd}
N 70 -260 100 -260 {lab=vss}
N 70 -290 100 -290 {lab=vdd}
N 300 -80 300 -50 {lab=vss}
N 380 -250 380 -220 {lab=vss}
N 380 -250 430 -250 {lab=vss}
N 430 -250 430 -190 {lab=vss}
N 200 -190 300 -190 {lab=vdd}
C {sky130_fd_pr/nfet_01v8.sym} 360 -190 0 0 {name=M2
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
C {sky130_fd_pr/pfet_01v8.sym} 180 -190 0 0 {name=M1
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
C {lab_wire.sym} 300 -280 0 0 {name=p1 sig_type=std_logic lab=vdd}
C {lab_wire.sym} 300 -50 2 0 {name=p2 sig_type=std_logic lab=vss}
C {iopin.sym} 70 -290 2 0 {name=p3 lab=vdd}
C {iopin.sym} 70 -260 2 0 {name=p4 lab=vss}
C {lab_wire.sym} 100 -290 2 0 {name=p5 sig_type=std_logic lab=vdd}
C {lab_wire.sym} 100 -260 2 0 {name=p6 sig_type=std_logic lab=vss}
