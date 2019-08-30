# -*- coding: utf-8 -*-
"""
:copyright: (c) 2019 by better-requests (c) 2012 by Kenneth Reitz.
:license: Apache2, see LICENSE for more details.
"""

from requests import Session as _Session

from requests.compat import Callable
# noinspection PyUnresolvedReferences
from requests.sessions import SessionRedirectMixin, session


# noinspection PyUnusedLocal
def _raise_for_status(res, *args, **kwargs):
    res.raise_for_status()


class Session(_Session):
    """A Requests session.

    Provides cookie persistence, connection-pooling, and configuration.

    Basic Usage::

      >>> import requests
      >>> with requests.Session() as s:
      >>>     s.get('https://httpbin.org/get')
      <Response [200]>
    """

    default_timeout = 30.05
    auto_raise_for_status = True

    def __init__(self, *args, **kwargs):
        # noinspection PyArgumentList
        super(Session, self).__init__(*args, **kwargs)

        self.default_timeout = Session.default_timeout
        self.auto_raise_for_status = Session.auto_raise_for_status

    def prepare_request(self, request, *args, **kwargs):
        """Constructs a :class:`PreparedRequest <PreparedRequest>` for
        transmission and returns it. The :class:`PreparedRequest` has settings
        merged from the :class:`Request <Request>` instance and those of the
        :class:`Session`.

        :param request: :class:`Request` instance to prepare with this
            session's settings.
        :rtype: requests.PreparedRequest
        """

        # noinspection PyArgumentList
        req = super(Session, self).prepare_request(request, *args, **kwargs)

        # Auto raise_for_status
        if self.auto_raise_for_status:
            if req.hooks is None:
                req.hooks = {}

            hook = [_raise_for_status]

            old_hook = req.hooks.get('response')
            if old_hook is None:
                pass
            elif hasattr(old_hook, '__iter__'):
                hook.extend(old_hook)
            elif isinstance(old_hook, Callable):
                hook.append(old_hook)

            req.hooks['response'] = hook

        return req

    def send(self, request, *args, **kwargs):
        """Send a given PreparedRequest.

        :rtype: requests.Response
        """

        # Set default timeout, None -> default, zero -> None
        timeout = kwargs.get('timeout')
        if timeout is None:
            kwargs['timeout'] = self.default_timeout
        elif timeout == 0:
            kwargs['timeout'] = None

        # noinspection PyArgumentList
        return super(Session, self).send(request, *args, **kwargs)
