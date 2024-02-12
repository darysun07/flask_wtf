from flask import Flask
from flask import render_template
import json

app = Flask(__name__)


@app.route('/list_prof/<list>')
def list_prof(list):
    with open("templates/list_prof.json", "rt", encoding="utf8") as f:
        news_list = json.loads(f.read())
    print(news_list)
    return render_template('prof.html', list_prof=news_list, list=list)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
