============
 atabula2pocket
============

This program is designed to weekly import Atabula_ articles to your Pocket_
account.

.. _Atabula: https://atabula.com
.. _Pocket: https://pocket.co

How to use it
-------------

1. Install it using `python setup.py` or any method you like
2. You need to obtain a Pocket access token. Run `get-pocket-token.py` and
   follow the instructions.
3. Export those variables in your environment::

    export ATABULA_USERNAME=<username>
    export ATABULA_PASSWORD=<password>
    export POCKET_ACCESS_TOKEN=<token from get-pocket-token.py>

4. Run `atabula2pocket.py`
