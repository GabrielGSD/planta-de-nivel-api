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
