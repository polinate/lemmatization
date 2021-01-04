import pymorphy2
morph = pymorphy2.MorphAnalyzer()
import json

from flask import Flask, request, abort, jsonify

import helper

flask_app = Flask(__name__)

text = "инфляция времени ел"

def lemmatize(text):
    words = text.split() # разбиваем текст на слова
    res = list()
    for word in words:
        p = morph.parse(word)[0]
        res.append(p.normal_form)

    return res


@flask_app.route('/words', methods=['POST'])
def get_words():
	message = request.args['sentence']
	res = lemmatize(message)
	result = {
	"error" : "0",
	"message" : "success",
	"answer" : res
	}
	return flask_app.response_class(response=json.dumps(result), mimetype='application/json')
 

  
if __name__ == "__main__":
   flask_app.run(host='0.0.0.0', port=5000, debug=True)