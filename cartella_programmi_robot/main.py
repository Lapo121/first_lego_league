#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, GyroSensor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
import time

robot_base_settings = (128, 512, 135, 543)

ev3 = EV3Brick()

#giroscopio = GyroSensor(Port.S2)
#motore_A = Motor(Port.A)
motore_B = Motor(Port.B)
motore_C = Motor(Port.C)
#motore_D = Motor(Port.D)
robot = DriveBase(motore_C, motore_B, 55, 108)

'''def aggiusta_angolazione(angolo_desiderato): 
    if giroscopio.angle() != angolo_desiderato:
        if giroscopio.angle() > angolo_desiderato:
            robot.stop()
            robot.turn(angolo_desiderato)
            robot.stop()
        else:
            robot.stop()
            robot.turn(angolo_desiderato)
            robot.stop()'''

def calcolo_distanza_rimanente():
    '''
    controllare un metodo migliore perché in questo modo si prende solo il valore del motore B
    e si esclude quello del motore C che potrebbe essere molto diverso

    TODO:
    Capire bene seconda parte codice
    '''
    gradi_conteggiati = motore_B.angle()
    if gradi_conteggiati > 0:
        return (gradi_conteggiati / 360) * 17.2
    return ((gradi_conteggiati * -1) / 360) * 17.2 

def movimento_avanti(distanza):
    robot.stop()
    robot.settings(straight_speed = robot_base_settings[0] // 2)
    robot.straight(distanza)
    robot.stop()
    robot.settings(*robot_base_settings)
    
def movimento_indietro(distanza):
    robot.stop()
    robot.settings(straight_speed = robot_base_settings[0] // 2)
    robot.straight(distanza * -1)
    robot.stop()
    robot.settings(*robot_base_settings)

'''def posizione_gancio_base():
    gradi_conteggiati = motore_A.angle()
    if gradi_conteggiati < 0:
        motore_A = Motor(Port.A, Direction.COUNTERCLOCKWISE)
        motore_A.run_target(gradi_conteggiati, gradi_conteggiati)
        motore_A = Motor(Port.A, Direction.CLOCKWISE)
    else:
        motore_A.run_target(gradi_conteggiati, gradi_conteggiati)

def posizione_gancio_bassa():
    posizione_gancio_base()
    motore_A = Motor(Port.A, Direction.COUNTERCLOCKWISE)
    motore_A.run_target(80, 240)
    motore_A = Motor(Port.A, Direction.CLOCKWISE)'''

def posizione_leva_alta(): ...
def posizione_leva_base(): ...
def prima_missione(): ...
def rettilineo(): ...
def rotazione(angolo): ...
