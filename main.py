import Funcoes.funcoes as malha
from flask import Flask, jsonify
from flask_cors import CORS

main = Flask(__name__)
CORS(main)


@main.route("/", methods=['GET'])
def home():
    malhaEntrada.execute()
    minimosQuadrados.execute()
    saidaMalhaAberta.execute()
    saidaMalhaFechada.execute()
    saidaMalhaFechadaComGanho.execute()
    saidaMalhaFechadaComGanhoPI.execute()

    malhas = {
        f'{malhaEntrada.nome}': malhaEntrada.returnData(),
        f'{minimosQuadrados.nome}': minimosQuadrados.returnData(),
        f'{saidaMalhaAberta.nome}': saidaMalhaAberta.returnData(),
        f'{saidaMalhaFechada.nome}': saidaMalhaFechada.returnData(),
        f'{saidaMalhaFechadaComGanho.nome}': saidaMalhaFechadaComGanho.returnData(),
        f'{saidaMalhaFechadaComGanhoPI.nome}': saidaMalhaFechadaComGanhoPI.returnData()
    }
    return jsonify(malhas)


if __name__ == '__main__':
    malhaEntrada = malha.MalhaEntrada()
    minimosQuadrados = malha.MinimosQuadrados()
    saidaMalhaAberta = malha.MalhaAberta()
    saidaMalhaFechada = malha.MalhaFechada()
    saidaMalhaFechadaComGanho = malha.MalhaFechadaComGanho()
    saidaMalhaFechadaComGanhoPI = malha.MalhaFechadaComGanhoPI()
    main.run(debug=True)
