#!/usr/bin/env python

from flask import *
from flaskext.cache import Cache
from urbanparser import get_definitions
#import werkzeug.exceptions

app = Flask(__name__)
app.debug = True
cache = Cache(app)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/define')
def define_phrase():
	phrase = request.values.get("q", "")
	if not phrase:
		raise werkzeug.exceptions.BadRequest("Missing query parameter")
	defs = get_definitions(phrase)
	return jsonify(definitions = defs)

if __name__ == '__main__':
	app.run(host = '127.0.0.1')

