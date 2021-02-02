from flask import Flask, render_template, request

app = Flask(__name__, template_folder="./src/views")

@app.route("/", methods=["GET", "POST"])
def home():
    if (request.method == "GET"):
        return render_template("index.html")
    else:
        if (request.form['num1'] != '' and request.form['num2'] != ''):
            num1 = request.form['num1']
            num2 = request.form['num2']

            if (request.form['opc'] == 'soma'):
                soma = int(num1) + int(num2)
                return {
                    'Resultado': str(soma)
                }

            elif(request.form['opc'] == 'subtracao'):
                subtracao = int(num1) - int(num2)
                return {
                    'Resultado': str(subtracao)
                }

            elif(request.form['opc'] == 'multiplicacao'):
                multiplicacao = int(num1) * int(num2)
                return {
                    'Resultado': str(multiplicacao)
                }

            else:
                divisao = int(num1) / int(num2)
                return {
                    'Resultado': str(divisao)
                }

        else:
            return {
                'Erro': 'É necessário digitar os dois valores!'
            }

#@app.route("/<int:id>")
#def Home_id(id):
#    return str(id +1)       

@app.errorhandler(404)
def not_found(error):
    return render_template("error.html")



app.run(port=8080, debug=True)

