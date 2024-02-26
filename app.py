from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista in cui memorizzeremo le attività
todo_list = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Otteniamo l'attività dal form HTML
        task = request.form['task']
        # Aggiungiamo l'attività alla lista
        todo_list.append(task)
        # Reindirizziamo l'utente alla stessa pagina
        return redirect(url_for('index'))
    return render_template('index.html', todo_list=todo_list)

@app.route('/delete/<int:index>')
def delete(index):
    # Eliminiamo l'attività dalla lista utilizzando l'indice
    del todo_list[index]
    # Reindirizziamo l'utente alla stessa pagina
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
