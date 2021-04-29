from Funcoes.GanhoKpKi import accommodationPoint, errorCalculate, KpKi
from abc import ABC, abstractmethod
import Dados.dados as dados
import control as con


class Malha(ABC):
    def __init__(self, name):
        self.nome = name
        self.sys = con.TransferFunction(dados.COEFICIENTE_B1, [1, -dados.COEFICIENTE_A1], dados.TEMPO_AMOSTRAGEM)

        self.xout = []
        self.yout = []
        self.valorEstacionario = 0

        self.overshoot = 0
        self.overshootX = 0
        self.overshootY = 0

        self.tempo_acomodacao = 0
        self.valor_acomodacao = 0

        self.erroRegimePermanente = 0

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def returnData(self):
        pass


class Original(Malha):
    def __init__(self):
        super().__init__('original')

    def execute(self):
        self.xout = dados.TEMPO[0]
        self.yout = dados.SAIDA[0]
        self.valorEstacionario = self.yout[len(self.yout) - 1]

    def returnData(self):
        malha = {
            'valoresY': self.yout.tolist(),
            'valoresX': self.xout.tolist(),
        }
        return malha


class OriginalEmRespostaEntrada(Malha):
    def __init__(self):
        super().__init__('originalMinimoQuadrado')
        self.VALOR_ENTRADA = dados.ENTRADA[0][1]

    def execute(self):
        [self.xout, self.yout] = con.step_response(self.sys, dados.TEMPO)
        info = con.step_info(self.sys, self.xout)
        self.yout = self.yout * self.VALOR_ENTRADA
        self.valorEstacionario = info['SteadyStateValue'] * self.VALOR_ENTRADA
        self.tempo_acomodacao = info['SettlingTime']
        self.valor_acomodacao = accommodationPoint(self.yout, self.valorEstacionario)
        self.overshootX = info['PeakTime']
        self.overshootY = info['Peak'] * self.VALOR_ENTRADA
        self.overshoot = info['Overshoot']

        # Erro em regime permanente
        self.erroRegimePermanente = errorCalculate(self.VALOR_ENTRADA, self.valorEstacionario)

    def returnData(self):
        malha = {
            'valoresY': self.yout.tolist(),
            'valoresX': self.xout.tolist(),
            'tempoAcomodacao': self.tempo_acomodacao,
            'valorAcomodacao': self.valor_acomodacao,
            'erro': self.erroRegimePermanente
        }
        return malha


class Aberta(Malha):
    def __init__(self):
        super().__init__('malhaAberta')

    def execute(self):
        [self.xout, self.yout] = con.step_response(self.sys, dados.TEMPO_CALCULO)
        self.yout = self.yout * dados.AMPLITUDE
        info = con.step_info(self.sys, self.xout)
        self.valorEstacionario = info['SteadyStateValue'] * dados.AMPLITUDE
        self.tempo_acomodacao = info['SettlingTime']
        self.valor_acomodacao = accommodationPoint(self.yout, self.valorEstacionario)
        self.overshootX = info['PeakTime']
        self.overshootY = info['Peak'] * dados.AMPLITUDE
        self.overshoot = info['Overshoot']
        self.erroRegimePermanente = errorCalculate(dados.AMPLITUDE, self.valorEstacionario)

    def returnData(self):
        malha = {
            'valoresY': self.yout.tolist(),
            'valoresX': self.xout.tolist(),
            'tempoAcomodacao': self.tempo_acomodacao,
            'valorAcomodacao': self.valor_acomodacao,
            'erro': self.erroRegimePermanente
        }
        return malha


class Fechada(Malha):
    def __init__(self):
        super().__init__('malhaFechada')

    def execute(self):
        sysFechada = con.feedback(self.sys, 1)
        [self.xout, self.yout] = con.step_response(sysFechada, dados.TEMPO_CALCULO)
        self.yout = self.yout * dados.AMPLITUDE
        info = con.step_info(sysFechada, self.xout)
        self.valorEstacionario = info['SteadyStateValue'] * dados.AMPLITUDE
        self.tempo_acomodacao = info['SettlingTime']
        self.valor_acomodacao = accommodationPoint(self.yout, self.valorEstacionario)
        self.overshootX = info['PeakTime']
        self.overshootY = info['Peak'] * dados.AMPLITUDE
        self.overshoot = info['Overshoot']

        # Erro em regime permanente
        self.erroRegimePermanente = errorCalculate(dados.AMPLITUDE, self.valorEstacionario)

    def returnData(self):
        malha = {
            'valoresY': self.yout.tolist(),
            'valoresX': self.xout.tolist(),
            'tempoAcomodacao': self.tempo_acomodacao,
            'valorAcomodacao': self.valor_acomodacao,
            'erro': self.erroRegimePermanente
        }
        return malha


class FechadaComGanhoIntegral(Malha):
    def __init__(self):
        super().__init__('malhaFechadaControlador')
        self.kp = 0
        self.ki = 0

    def execute(self):
        self.kp, self.ki = KpKi(self.sys)
        sysAux = con.TransferFunction([1, 0], [1, -1], dados.TEMPO_AMOSTRAGEM)
        sysControlador = sysAux * self.ki * dados.TEMPO_AMOSTRAGEM + self.kp
        sysGanhoIntegral = con.feedback(sysControlador * self.sys, 1)
        [self.xout, self.yout] = con.step_response(sysGanhoIntegral, dados.TEMPO_CALCULO)
        self.yout = self.yout * dados.AMPLITUDE
        info = con.step_info(sysGanhoIntegral, self.xout)
        self.valorEstacionario = info['SteadyStateValue'] * dados.AMPLITUDE
        self.tempo_acomodacao = info['SettlingTime']
        self.valor_acomodacao = accommodationPoint(self.yout, self.valorEstacionario)
        self.overshootX = info['PeakTime']
        self.overshootY = info['Peak'] * dados.AMPLITUDE
        self.overshoot = info['Overshoot']

        # Erro em regime permanente
        self.erroRegimePermanente = errorCalculate(dados.AMPLITUDE, self.valorEstacionario)

    def returnData(self):
        malha = {
            'valoresY': self.yout.tolist(),
            'valoresX': self.xout.tolist(),
            'overshoot': self.overshoot,
            'overshootX': self.overshootX,
            'overshootY': self.overshootY,
            'tempoAcomodacao': self.tempo_acomodacao,
            'valorAcomodacao': self.valor_acomodacao,
            'erro': self.erroRegimePermanente,
            'kiRecomendado': self.ki,
            'kpRecomendado': self.kp,
        }

        return malha


# ********************************************************************************************************************


class FechadaComGanho(Malha):

    def __init__(self):
        super().__init__('malhaFechadaGanhoProporcional')
        self.kp = 0
        self.ki = 0

    def execute(self):
        # Calculando os valores dos ganhos
        self.kp, self.ki = KpKi(self.sys)

        # Atribuindo o ganho
        sysGanho = self.sys * self.kp

        # Realimentando a malha
        sysFechada = con.feedback(sysGanho, 1)

        # Resposta ao degrau
        [self.xout, self.yout] = con.step_response(sysFechada, dados.TEMPO_CALCULO)

        # "Alterando" amplitude do degrau
        self.yout = self.yout * dados.AMPLITUDE

        # Pegando as informações sobre o sistema
        info = con.step_info(sysFechada, self.xout)

        # Pegando o valor de estado estacionário
        self.valorEstacionario = info['SteadyStateValue'] * dados.AMPLITUDE

        # Ponto de acomodação
        self.tempo_acomodacao = info['SettlingTime']
        self.valor_acomodacao = accommodationPoint(self.yout, self.valorEstacionario)

        # Overshoot
        self.overshootX = info['PeakTime']
        self.overshootY = info['Peak'] * dados.AMPLITUDE
        self.overshoot = info['Overshoot']

        # Erro em regime permanente
        self.erroRegimePermanente = errorCalculate(dados.AMPLITUDE, self.valorEstacionario)

    def returnData(self):
        malha = {
            'valoresY': self.yout.tolist(),
            'valoresX': self.xout.tolist(),
            'overshoot': self.overshoot,
            'overshootX': self.overshootX,
            'overshootY': self.overshootY,
            'tempoAcomodacao': self.tempo_acomodacao,
            'valorAcomodacao': self.valor_acomodacao,
            'erro': self.erroRegimePermanente
        }

        return malha
