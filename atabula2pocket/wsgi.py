from flask import Flask

from atabula2pocket import atabula
from atabula2pocket import secrets

application = Flask(__name__)


@application.route('/{}/<path:url>'.format(secrets.URL_PREFIX))
def hello(url):
    session = atabula.get_session()
    text = session.get("https://{}".format(url)).text
    return text.replace("www.atabula.com", "{}/{}".format(
        secrets.APP_DOMAIN, secrets.URL_PREFIX)
    )


if __name__ == '__main__':
    application.run(debug=True)
