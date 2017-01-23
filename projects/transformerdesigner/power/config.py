#!/usr/bin/env python
import serial,time,sys,termios,os,csv



config='''
$0=10
$1=25
$2=7
$3=0
$4=0
$5=0
$6=0
$10=2
$11=100.000
$12=0.002
$13=1
$20=0
$21=0
$22=0
$23=0
$24=25.000
$25=500.000
$26=250
$27=1.000
$30=1000
$31=0
$32=1
$100=400.000
$101=40.802
$102=250.000
$110=3000.000
$111=6000.000
$112=500.000
$120=500.000
$121=75.000
$122=10.000
$130=160.000
$131=0.000
$132=200.000
$N0=G1G20G90F125
'''


port = serial.Serial('/dev/ttyUSB0',115200,timeout=1)

print port.readline()
print port.readline()
print port.readline()

for i in config.split("\n"):
    port.write(i+"\n")
    print port.readline()
    time.sleep(0.5)
