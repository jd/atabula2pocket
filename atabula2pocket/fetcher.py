#!/usr/bin/env python
import logging
import os
import re
import sys

import pocket
import requests

from atabula2pocket import secrets
from atabula2pocket import atabula


logging.basicConfig()
LOG = logging.getLogger(__name__)

DEBUG = len(sys.argv) >= 2 and sys.argv[1] == '--debug'
POCKET_CONSUMER_KEY = "44549-fa6a1b90e0b637237765ba8a"


if DEBUG:
    try:
        import http.client as http_client
    except ImportError:
        # Python 2
        import httplib as http_client
    http_client.HTTPConnection.debuglevel = 1
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True


RE_ARTICLE_LINK = re.compile("<a href=\"https://(www.atabula.com/20../[^\"]+)\"")


def main():
    session = atabula.get_session()
    frontpage = session.get("https://atabula.com")

    access_token = os.getenv("POCKET_ACCESS_TOKEN")
    p = pocket.Pocket(POCKET_CONSUMER_KEY, access_token)

    already_in_pocket = p.get(domain=secrets.APP_DOMAIN, detailType="simple",
                              state="all")
    if already_in_pocket[0]['list']:
        articles_already_pushed = {
            entry['given_url']
            for entry in already_in_pocket[0]['list'].values()
        }
    else:
        articles_already_pushed = set()

    for line in frontpage.text.split("\n"):
        m = RE_ARTICLE_LINK.search(line)
        if m:
            link = "https://{}/{}/{}".format(
                secrets.APP_DOMAIN, secrets.URL_PREFIX, m.group(1),
            )
            if link not in articles_already_pushed:
                p.add(link)
                articles_already_pushed.add(link)


if __name__ == '__main__':
    main()
