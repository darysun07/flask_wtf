from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/training/<string:prof>')
def professia(prof):
    return render_template('prof.html', prof=prof)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
