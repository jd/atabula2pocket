import flask

from atabula2pocket import atabula
from atabula2pocket import secrets

application = flask.Flask(__name__)


session = atabula.get_session()

@application.route('/{}/<path:url>'.format(secrets.URL_PREFIX))
def hello(url):
    result = session.get("https://{}".format(url))
    if "text/html" in result.headers["content-type"]:
        content = result.text.replace("https://www.atabula.com", "https://{}/{}/www.atabula.com".format(
            secrets.APP_DOMAIN, secrets.URL_PREFIX)
        )
    else:
        content = result.content
    response = flask.Response(content)
    response.status_code = result.status_code
    response.headers["Content-Type"] = result.headers["Content-Type"]
    return response


if __name__ == '__main__':
    application.run(debug=True)
