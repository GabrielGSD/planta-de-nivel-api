import numpy as np
import Dados.constantes as const


def minimosQuadrados():

    # Carregando entrada e saída
    entrada = const.ENTRADA
    saida = const.SAIDA

    # Pegar numero de linhas e colunas
    [L, C] = np.shape(saida)

    if (L>1):
        F = np.array([saida[0:L-1,0], entrada[0:L-1,0]])
        J = saida[1:,0]
    elif (C>1):
        F = np.array([saida[0][0:C-1,], entrada[0][0:C-1,]])
        J = saida[0][1:,]

    FInverse = np.transpose(F) # Realizando a transposta

    # Realizando operação
    resultado = np.linalg.inv(F @ FInverse) @ F @ J

    return resultado