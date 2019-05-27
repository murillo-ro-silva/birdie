from flask import Flask
from requests import get

app = Flask('__main__')
SITE_NAME = 'http://127.0.0.1:9200/birdie-wiki-final'

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):
  return get(f'{SITE_NAME}{path}').content

app.run(host='127.0.0.0', port=5050)