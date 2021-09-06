from flask import *
from whatsapp import whatsapp
import json

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        bot = whatsapp(request.json)
        return bot.processing()
    if request.method == 'GET':
        return render_template('home.html')


if(__name__) == '__main__':
    app.run(debug=True, host='0.0.0.0')
