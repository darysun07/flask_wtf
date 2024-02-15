from flask import Flask, request, url_for
from flask import render_template

app = Flask(__name__)


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Отбор астронавтов</title>
                  </head>
                  <body>
                    <h1 align="center"> Анкета претендента</h1>
                    <h2 align="center"> на участие в миссии </h2>
                    <div>
                        <form class="login_form" method="post">
                            <input type="text" class="form-control" id="surname" aria-describedby="surnameHelp" placeholder="Введите фамилию" name="surname">

                            <input type="text" class="form-control" id="name" aria-describedby="nameHelp" placeholder="Введите имя" name="name">
                            <div class="form-group">
                                <br><label for="classSelect">Какое у Вас образование?</label>
                                <select class="form-control" id="classSelect" name="class">
                                  <option>Начальное</option>
                                  <option>Среднее</option>
                                  <option>Высшее</option>
                                </select>
                              </div>
                                <br><label for="work">Какие у Вас есть профессии?</label>
                            <div class="form-group form-check">
                                <input type="checkbox" class="form-check-input" id="prof" name="prof1">
                                <label class="form-check-label" for="acceptRules">Инженер-исследователь</label>
                                <br><input type="checkbox" class="form-check-input" id="prof" name="prof2">
                                <label class="form-check-label" for="acceptRules">Пилот</label>
                                <br><input type="checkbox" class="form-check-input" id="prof" name="prof3">
                                <label class="form-check-label" for="acceptRules">Врач</label>
                                <br><input type="checkbox" class="form-check-input" id="prof" name="prof4">
                                <label class="form-check-label" for="acceptRules">Учитель</label>
                                <br><input type="checkbox" class="form-check-input" id="prof" name="prof5">
                                <label class="form-check-label" for="acceptRules">Метеоролог</label>
                            </div>

                            <div class="form-group">
                                <label for="form-check">Укажите пол</label>
                                <div class="form-check">
                                  <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                  <label class="form-check-label" for="male">
                                    Мужской
                                  </label>
                                </div>
                                <div class="form-check">
                                  <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                  <label class="form-check-label" for="female">
                                    Женский
                                  </label>
                                </div>
                            </div>

                            <div class="form-group">
                                <label for="about">Почему вы хотите принять участие в миссии?</label>
                                <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                            </div>

                            <div class="form-group form-check">
                                <input type="checkbox" class="form-check-input" id="acceptRules" name="hello">
                                <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                            </div>
                            <br><button type="submit" class="btn btn-primary">Отправить</button>
                        </form>
                    </div>
                  </body>
                </html>'''
    elif request.method == 'POST':
        print(request.form.get('surname', ""))
        print(request.form.get('name', ""))
        print(request.form.get('class', ""))
        print(request.form.get('prof1', ""))
        print(request.form.get('prof2', ""))
        print(request.form.get('prof3', ""))
        print(request.form.get('prof4', ""))
        print(request.form.get('prof5', ""))
        print(request.form.get('sex', ""))
        print(request.form.get('about', ""))
        print(request.form.get('hello', ""))
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')