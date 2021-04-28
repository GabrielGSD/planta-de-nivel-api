import numpy as np
import Dados.constantes as const
import control as con

numeroCasas = 3

def errorCalculate(sp, finalValue):
    return abs(round(sp - finalValue, 2))

def temOvershoot(array, pv):
    valorPossivel1 = round(pv*0.98, numeroCasas)
    valorPossivel2 = round(pv/0.98, numeroCasas)

    for value in array:
        if(value > valorPossivel2 or value < valorPossivel1):
		    return True

    return False

def accommodationPoint(array, pv):
    # Variaveis auxiliares
    melhorValor = 0

    valorPossivel1 = round(pv * 0.98, numeroCasas)
    valorPossivel2 = round(pv / 0.98, numeroCasas)

    for i in range(len(array)):
        newArray = array[i:]
        if (array[i] >= valorPossivel1 and array[i] <= valorPossivel2 and temOvershoot(newArray, pv) == False):
            melhorValor = array[i]
            break

    return melhorValor

def KpKi(sys):
    # Valores de Kp e Ki calculados a mão pelo método ->
    kp = 7.30010
    ki = 0.44721

    return kp, ki
