from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "CIAO, TUTTO HA  FUNZIONATO BENE"

if __name__ == "__main__":
    app.run()