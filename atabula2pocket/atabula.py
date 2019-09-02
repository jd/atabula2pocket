import os

import requests


def get_session():
    session = requests.Session()
    ret = session.post(
        # Don't forget the www or you get a 301 to it
        "https://www.atabula.com/mon-compte/",
        data={
            "username": os.getenv("ATABULA_USERNAME"),
            "password": os.getenv("ATABULA_PASSWORD"),
            "woocommerce-login-nonce": "29228d406d",
            "_wp_http_referer": "/mon-compte%/",
            "login": "Connection",
        },
        allow_redirects=False,
    )

    assert ret.status_code == 302

    return session
