from flask import Flask, request, redirect, url_for

app = Flask(__name__)

veiculos = [
    {
        "placa": "ABC1D23",
        "marca": "Volvo",
        "modelo": "FH 540"
    },
    {
        "placa": "DEF4G56",
        "marca": "Scania",
        "modelo": "R 450"
    },
    {
        "placa": "GHI7J89",
        "marca": "DAF",
        "modelo": "XF 530"
    }
]


@app.route("/", methods=["GET"])
def home():
    mensagem = request.args.get("mensagem", "")

    lista_veiculos = ""

    for veiculo in veiculos:
        lista_veiculos += f"""
            <tr>
                <td>{veiculo["placa"]}</td>
                <td>{veiculo["marca"]}</td>
                <td>{veiculo["modelo"]}</td>
            </tr>
        """

    return f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
        <head>
            <meta charset="UTF-8">
            <title>Sistema de Manutenção</title>
        </head>

        <body>
            <h1>Sistema de Controle de Manutenção</h1>

            <p>
                Aplicação desenvolvida para a atividade prática de DevOps.
            </p>

            <hr>

            <h2>Cadastrar veículo</h2>

            <form action="/veiculos" method="POST">

                <label for="placa">Placa:</label>
                <input
                    type="text"
                    id="placa"
                    name="placa"
                    placeholder="Ex.: ABC1D23"
                    required
                >

                <br><br>

                <label for="marca">Marca:</label>
                <input
                    type="text"
                    id="marca"
                    name="marca"
                    placeholder="Ex.: Volvo"
                    required
                >

                <br><br>

                <label for="modelo">Modelo:</label>
                <input
                    type="text"
                    id="modelo"
                    name="modelo"
                    placeholder="Ex.: FH 540"
                    required
                >

                <br><br>

                <button type="submit">Cadastrar veículo</button>

            </form>

            <br>

            <p>{mensagem}</p>

            <hr>

            <h2>Veículos cadastrados</h2>

            <table border="1" cellpadding="8">
                <thead>
                    <tr>
                        <th>Placa</th>
                        <th>Marca</th>
                        <th>Modelo</th>
                    </tr>
                </thead>

                <tbody>
                    {lista_veiculos}
                </tbody>
            </table>

        </body>
    </html>
    """


@app.route("/veiculos", methods=["POST"])
def cadastrar_veiculo():
    placa = request.form.get("placa", "").strip().upper()
    marca = request.form.get("marca", "").strip()
    modelo = request.form.get("modelo", "").strip()

    if not placa or not marca or not modelo:
        return redirect(
            url_for(
                "home",
                mensagem="Erro: todos os campos são obrigatórios."
            )
        )

    for veiculo in veiculos:
        if veiculo["placa"] == placa:
            return redirect(
                url_for(
                    "home",
                    mensagem="Erro: já existe um veículo com essa placa."
                )
            )

    novo_veiculo = {
        "placa": placa,
        "marca": marca,
        "modelo": modelo
    }

    veiculos.append(novo_veiculo)

    return redirect(
        url_for(
            "home",
            mensagem="Veículo cadastrado com sucesso!"
        )
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)