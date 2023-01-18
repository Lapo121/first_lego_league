#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, GyroSensor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
import time

ev3 = EV3Brick()

#giroscopio = GyroSensor(Port.S2)
#motore_A = Motor(Port.A)
motore_B = Motor(Port.B)
motore_C = Motor(Port.C)
#motore_D = Motor(Port.D)
robot = DriveBase(motore_C, motore_B, 55, 145)

'''def aggiusta_angolazione(angolo_desiderato): 
    if giroscopio.angle() != angolo_desiderato:
        if giroscopio.angle() > angolo_desiderato:
            '''


def calcolo_distanza_rimanente(): ...
def movimento_avanti(distanza): ...
def movimento_indietro(distanza): ...
def posizione_gancio_base(): ...
def posizione_gancio_bassa(): ...
def posizione_leva_alta(): ...
def posizione_leva_base(): ...
def prima_missione(): ...
def rettilineo(): ...
def rotazione(angolo): ...

robot.straight(1000)