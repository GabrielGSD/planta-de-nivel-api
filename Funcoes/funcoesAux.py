import numpy as np
import Dados.dados as dados


def minimosQuadrados():
    entrada = dados.ENTRADA
    saida = dados.SAIDA

    [L, C] = np.shape(saida)
    if L > 1:
        F = np.array([saida[0:L-1, 0], entrada[0:L-1, 0]])
        J = saida[1:, 0]
    elif C > 1:
        F = np.array([saida[0][0:C-1, ], entrada[0][0:C-1, ]])
        J = saida[0][1:, ]

    FInverse = np.transpose(F)
    resposta = np.linalg.inv(F @ FInverse) @ F @ J

    return resposta


def pontoDeAcomodacao(array, pv):
    def verificaOvershoot(array1, pv1):
        aux1 = round(pv1 * 0.98, 3)
        aux2 = round(pv1 / 0.98, 3)

        for value in array1:
            if value > aux2 or value < aux1:
                return True
        return False

    aux3 = round(pv * 0.98, 3)
    aux4 = round(pv / 0.98, 3)
    aux = 0
    for i in range(len(array)):
        newArray = array[i:]
        if aux3 <= array[i] <= aux4 and verificaOvershoot(newArray, pv) == False:
            aux = array[i]
            break
    return aux



