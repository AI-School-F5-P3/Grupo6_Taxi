from flask import Flask, render_template, request, redirect, url_for, session
from model import Taximetro

app = Flask(__name__)
app.secret_key = 'supersecretkey'
app.config['SESSION_TYPE'] = 'filesystem'

taximetro = Taximetro(user="default_user")  # Proporciona un argumento de usuario válido

@app.route('/')
def index():
    fare = taximetro.fare_total
    feedback = session.pop('feedback', 'Esperando instrucciones...')
    total_time = session.pop('total_time', None)
    return render_template('index.html', fare=fare, feedback=feedback, total_time=total_time)

@app.route('/start', methods=['POST'])
def start():
    taximetro.clear()  # Asegúrate de reiniciar el taxímetro
    taximetro.start()
    session['feedback'] = 'Iniciando nueva carrera...'
    return redirect(url_for('index'))

@app.route('/stop', methods=['POST'])
def stop():
    taximetro.stop()
    session['feedback'] = 'Carrera detenida.'
    return redirect(url_for('index'))

@app.route('/continue_road', methods=['POST'])
def continue_road():
    taximetro.continue_road()
    session['feedback'] = 'Carrera en movimiento.'
    return redirect(url_for('index'))

@app.route('/finalize_ride', methods=['POST'])
def finalize_ride():
    total_fare = taximetro.finish_road()
    total_time = str(taximetro.end_time - taximetro.start_time)
    session['feedback'] = 'Carrera finalizada'.format(total_fare, total_time)
    session['total_time'] = total_time
    return redirect(url_for('index'))

@app.route('/reset', methods=['POST'])
def reset():
    taximetro.clear()
    session['feedback'] = 'Taxímetro reiniciado.'
    return redirect(url_for('index'))

@app.route('/history')
def history():
    history = taximetro.get_history()
    return render_template('history.html', history=history)

if __name__ == "__main__":
    app.run(debug=True)
