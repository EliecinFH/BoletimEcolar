### Boletim Escola
 ## Documentação do código
 * Python(Flask)
---
#### Descrição
Este código python utiliza o fremework Flask para criar uma aplicação web que calcula e exibe o boletim escolas e a média de um aluno com base nas notas inseridas. 
* Python
* Importações: Importa o Flask e funções nescessárias.  
  ` from flask import Flask, request, render_template `  
* Rota principal: Define a rota principal que processa as notas e calcula o resultado.  
  ` @app.route('/', methods=['GET']) `  
* Cálculo da média: Calcula a média das notas válidas.  
  `  notas_validas = [nota for nota in notas.values() if isinstance(nota, float)]
    if notas_validas:
        media = sum(notas_validas) / len(notas_validas)
    else:
        media = 0 `  
* Formatar a média: Formatação da média em uma casa decimal antes de passá-la para o template.  
  `media_formatada = f"{media:.2f}"`  
* Determinação do resultado: Define o resultado (Aprovado, Recuperação, Reprovado) com base na média.  
  ` if media >= 6:
        resultado = 'Aprovado'
    elif media >= 4:
        resultado = 'Recuperação'
    else:
        resultado = 'Reprovado' `  
* Renderização do template: Renderiza o template HTML com os dados calculados.  
`  return render_template('index.html', nome_aluno=nome_aluno, media=media_formatada, resultado=resultado, notas=notas) `  
