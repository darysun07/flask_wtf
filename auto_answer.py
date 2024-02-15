from flask import Flask, render_template

app = Flask(__name__)


@app.route('/answer')
@app.route('/auto_answer')
def auto_answer():
    data = dict()
    data["title"] = 'Анкета'
    data["surname"] = 'Wathy'
    data["name"] = 'Mark'
    data["education"] = 'выше среднего'
    data["profession"] = 'штурман марсохода'
    data["sex"] = 'male'
    data["motivation"] = 'Всегда мечтал застрять на Марсе!'
    data["ready"] = 'True'
    return render_template('auto_answer.html', **data)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')