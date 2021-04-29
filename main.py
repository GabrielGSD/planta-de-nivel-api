import Funcoes.funcoes as malha
from flask import Flask, jsonify
from flask_cors import CORS

main = Flask(__name__)
CORS(main)


@main.route("/", methods=['POST'])
def home():
    malhaOriginal.execute()
    malhaOriginalEmRespostaEntrada.execute()
    malhaAberta.execute()
    malhaFechada.execute()
    FechadaComGanho.execute()
    FechadaComGanhoIntegral.execute()

    # Formando o objeto que será enviado em formato JSON
    malhas = {
        f'{malhaOriginal.nome}': malhaOriginal.returnData(),
        f'{malhaOriginalEmRespostaEntrada.nome}': malhaOriginalEmRespostaEntrada.returnData(),
        f'{malhaAberta.nome}': malhaAberta.returnData(),
        f'{malhaFechada.nome}': malhaFechada.returnData(),
        f'{FechadaComGanho.nome}': FechadaComGanho.returnData(),
        f'{FechadaComGanhoIntegral.nome}': FechadaComGanhoIntegral.returnData()
    }
    return jsonify(malhas)


if __name__ == '__main__':
    malhaOriginal = malha.Original()
    malhaOriginalEmRespostaEntrada = malha.OriginalEmRespostaEntrada()
    malhaAberta = malha.Aberta()
    malhaFechada = malha.Fechada()
    FechadaComGanho = malha.FechadaComGanho()
    FechadaComGanhoIntegral = malha.FechadaComGanhoIntegral()
    main.run(debug=True)
