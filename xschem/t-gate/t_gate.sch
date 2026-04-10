v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 0 0 70 0 {lab=V1}
N 0 -180 0 0 {lab=V1}
N 0 -180 70 -180 {lab=V1}
N 130 0 200 0 {lab=V2}
N 130 -180 200 -180 {lab=V2}
N 200 -180 200 0 {lab=V2}
N -40 -90 0 -90 {lab=V1}
N 200 -90 240 -90 {lab=V2}
N 100 -180 100 -100 {lab=vdd}
N 100 -100 220 -100 {lab=vdd}
N 100 -80 100 0 {lab=vss}
N 100 -80 220 -80 {lab=vss}
N 220 -80 220 0 {lab=vss}
N 220 0 240 0 {lab=vss}
N 220 -180 220 -100 {lab=vdd}
N 220 -180 240 -180 {lab=vdd}
N 100 40 100 60 {lab=A}
N 100 -260 100 -220 {lab=#net1}
N 70 -260 100 -260 {lab=#net1}
N -40 -260 -20 -260 {lab=A}
N 20 -220 20 -200 {lab=vss}
N 20 -320 20 -300 {lab=vdd}
N 20 -320 220 -320 {lab=vdd}
N 220 -320 220 -180 {lab=vdd}
N 20 -200 20 80 {lab=vss}
N 20 80 220 80 {lab=vss}
N 220 0 220 80 {lab=vss}
N -20 60 100 60 {lab=A}
N -30 60 -20 60 {lab=A}
N -30 -260 -30 60 {lab=A}
C {sky130_fd_pr/nfet_01v8.sym} 100 20 3 0 {name=M2
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
C {sky130_fd_pr/pfet_01v8.sym} 100 -200 1 0 {name=M1
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
C {iopin.sym} -40 -90 2 0 {name=p1 lab=V1}
C {iopin.sym} 240 -90 0 0 {name=p2 lab=V2}
C {ipin.sym} -40 -260 0 0 {name=p3 lab=A}
C {ipin.sym} 240 -180 2 0 {name=p5 lab=vdd}
C {ipin.sym} 240 0 2 0 {name=p6 lab=vss}
C {/foss/designs/dac10b-r2r-sky130/xschem/inv_x1/inv_x1.sym} 20 -260 0 0 {name=x1}
