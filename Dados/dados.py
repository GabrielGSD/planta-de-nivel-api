import scipy.io as sio
from numpy import arange
from Funcoes.minimosQuadrados import minimosQuadrados


def dados():
    x = sio.loadmat('Dados/amostras_equipe2.mat')
    return x['degrau0_2'], x['resp0_2'], x['tempo0_2']


# Constantes

AMPLITUDE = 50
OVERSHOOT = 0.10
TEMPO_ACOMODACAO = 70
TEMPO_AMOSTRAGEM = 0.2
KP = 4.923
KI = 0.271

ENTRADA, SAIDA, TEMPO = dados()
TEMPO_CALCULO = arange(0, (len(TEMPO[0]) * TEMPO_AMOSTRAGEM), TEMPO_AMOSTRAGEM)
COEFICIENTE_A1, COEFICIENTE_B1 = minimosQuadrados()

