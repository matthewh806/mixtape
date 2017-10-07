from flask import Flask, render_template

app = Flask(__name__)

@app.route('/mixtape')
def mixtape():
    return render_template('mixtape.html')