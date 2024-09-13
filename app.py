from flask import Flask, request, render_template  # Importa a biblioteca


app = Flask(__name__)  # Inicializa a aplicação


# Rota principal que processa as notas e calcula o resultado
@app.route('/', methods=['GET'])  # Nova rota
def main():
    # Obtém o nome do aluno apartir dos parâmetros da URL
    nome_aluno = request.args.get('nome_aluno', 'Aluno')

    # Dicionário para armazenar as notas
    notas = {}
    materias = ['biologia', 'geografia', 'historia', 'literatura', 'matematica', 'portugues']
    
    # Obtém as notas das matérias a partir dos parâmetros da URL
    for materia in materias:
        nota = request.args.get(materia)
        if nota:
            try:
                notas[materia] = float(nota)
            except ValueError:
                notas[materia] = 'Nota inválida'


    # Calcula a média das notas válidas
    notas_validas = [nota for nota in notas.values() if isinstance(nota, float)]
    if notas_validas:
        media = sum(notas_validas) / len(notas_validas)
    else:
        media = 0

    # Formata a média para duas casas decimais
    media_formatada = f"{media:.1f}"

    # Determina o resultado com base na média

    if media >= 6:
        resultado = 'Aprovado'
    elif media >= 4:
        resultado = 'Recuperação'
    else:
        resultado = 'Reprovado' 

    # Renderiza o template HTML com os dados calculados
    return render_template('index.html', nome_aluno=nome_aluno, media=media_formatada, resultado=resultado, notas=notas)


if __name__ == '__main__':
    app.run(debug=True)  # Executa a aplicação
