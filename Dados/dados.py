import scipy.io as sio


def dados():
    # Carregando o arquivo mat
    x = sio.loadmat('amostras_equipe2.mat')
    return x['degrau0_2'], x['resp0_2'], x['tempo0_2']