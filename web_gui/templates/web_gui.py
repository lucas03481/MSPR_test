# web_gui/web_gui.py
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = '5825567071ab4632f867d459f46c4270'  # Changez ceci par une clé secrète sécurisée
app.static_folder = 'static'

class ScanForm(FlaskForm):
    ip_range = StringField('Plage d\'adresses IP')
    submit = SubmitField('Démarrer le Scan')

@app.route('/', methods=['GET', 'POST'])
def dashboard():
    form = ScanForm()

    if form.validate_on_submit():
        ip_range = form.ip_range.data
        # Enregistrez la plage d'adresses IP ou appelez la fonction du Harvester ici
        # ...

    # Récupérez les données de la base de données et les afficher sur le tableau de bord
    # ...

    return render_template('dashboard.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)

