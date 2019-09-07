import os
import re

import requests

NONCE = re.compile(
    "name=\"woocommerce-login-nonce\"\s+value=\"([^\"]+)\""
)

def get_session():
    login_url = "https://www.atabula.com/mon-compte/"
    session = requests.Session()
    login_page = session.get(login_url)
    nonce = NONCE.search(login_page.text).group(1)

    ret = session.post(
        # Don't forget the www or you get a 301 to it
        login_url,
        data={
            "username": os.getenv("ATABULA_USERNAME"),
            "password": os.getenv("ATABULA_PASSWORD"),
            "woocommerce-login-nonce": nonce,
            "_wp_http_referer": "/mon-compte%/",
            "login": "Connection",
        },
        allow_redirects=False,
    )

    assert ret.status_code == 302

    return session
