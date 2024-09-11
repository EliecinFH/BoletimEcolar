from flask import Flask # Importa a biblioteca

opp = Flask (__name__) # Inicializa a aplicação

@app.route('/') # Cria uma rota
def main():
    return 'Meu site em Flask :D'

if __name__ == '__main__':
    app.run(debug=True) # Executa a aplicação