from flask import Flask

from atabula2pocket import atabula
from atabula2pocket import secrets

app = Flask(__name__)


@app.route('/{}/<path:url>'.format(secrets.URL_PREFIX))
def hello(url):
    session = atabula.get_session()
    return session.get("https://{}".format(url)).content


if __name__ == '__main__':
    app.run(debug=True)
