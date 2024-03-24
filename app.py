from flask import Flask, render_template, request, redirect, session
import api

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('main.html')


@app.route('/perform_sentiment', methods=['post'])
def perform_ner():
    text = request.form.get('text')
    ai_response, chat_log, psychological_response_user, psychological_response_ai = api.ask_openai(user = 1, question= text)

    result = ''

    return render_template('main.html', response = ai_response, chat_log = chat_log, psychological_response_user = psychological_response_user, psychological_response_ai = psychological_response_ai)


app.run(debug=True)
