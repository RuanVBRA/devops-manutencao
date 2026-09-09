from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Sistema de Manutenção</title>
        </head>
        <body>
            <h1>Sistema de Controle de Manutenção</h1>
            <p>Aplicação desenvolvida para a atividade prática de DevOps.</p>

            <h2>Veículos</h2>

            <ul>
                <li>ABC1D23 - Volvo</li>
                <li>DEF4G56 - Scania</li>
                <li>GHI7J89 - DAF</li>
            </ul>
        </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)