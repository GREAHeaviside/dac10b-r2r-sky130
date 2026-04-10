v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 20 -70 70 -70 {lab=A}
N 20 -70 20 20 {lab=A}
N 20 20 70 20 {lab=A}
N 110 -40 110 -10 {lab=Y}
N 110 50 110 120 {lab=vss}
N 110 -160 110 -100 {lab=vdd}
N -60 -30 20 -30 {lab=A}
N 100 150 110 150 {lab=vss}
N 110 120 110 150 {lab=vss}
N 110 -180 110 -160 {lab=vdd}
N 100 -180 110 -180 {lab=vdd}
N -80 -30 -60 -30 {lab=A}
N 110 -30 190 -30 {lab=Y}
N 110 20 170 20 {lab=vss}
N 110 60 170 60 {lab=vss}
N 170 20 170 60 {lab=vss}
N 110 -70 160 -70 {lab=vdd}
N 110 -120 160 -120 {lab=vdd}
N 160 -120 160 -70 {lab=vdd}
C {sky130_fd_pr/nfet_01v8.sym} 90 20 0 0 {name=M2
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
C {ipin.sym} 100 -180 0 0 {name=p1 lab=vdd}
C {ipin.sym} 100 150 0 0 {name=p2 lab=vss}
C {opin.sym} 190 -30 0 0 {name=p3 lab=Y}
C {ipin.sym} -80 -30 0 0 {name=p4 lab=A}
C {sky130_fd_pr/pfet_01v8.sym} 90 -70 0 0 {name=M1
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
