# -*- coding: utf-8 -*-
"""
better-requests
~~~~~~~~~~~~~~~~~~~~~

better-requests
usage:

   >>> import better_requests as requests
   >>> r = requests.get('https://www.python.org')
   >>> 'Python is a programming language' in r.content
   True

:copyright: (c) 2019 by better-requests (c) 2012 by Kenneth Reitz.
:license: Apache2, see LICENSE for more details.

"""
from .__version__ import __title__, __description__, __version__, __license__
from .sessions import Session
from .api import request, get, head, post, patch, put, delete, options

# noinspection PyUnresolvedReferences
from requests import utils, packages, adapters, auth, certs, compat, cookies, exceptions, help, hooks, models, status_codes, structures
# noinspection PyUnresolvedReferences
from requests.models import Request, Response, PreparedRequest
# noinspection PyUnresolvedReferences
from requests.status_codes import codes
# noinspection PyUnresolvedReferences
from requests.exceptions import (
    RequestException, Timeout, URLRequired,
    TooManyRedirects, HTTPError, ConnectionError,
    FileModeWarning, ConnectTimeout, ReadTimeout
)
