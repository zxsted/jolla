#!/usr/bin/env python
# -*- coding: utf-8 -*-


class HTTPError(Exception):
    error_code = None
    value = ''

    def __init__(self, info=None):
        self.info = info
        if self.info:
            print '<' + self.info + '>'


class HTTP404Error(HTTPError):
    error_code = 404

    def __init__(self, info=None):
        if info:
            HTTPError.__init__(self, info)
        else:
            HTTPError.__init__(self)
        self.error_header = '404 NOT FOUND'

    def __str__(self):
        return "<404 NOT FOUND>"


class HTTP502Error(HTTPError):
    error_code = 502

    def __str__(self):
        return "<502 SERVER ERROR>"


class HTTP403Error(HTTPError):
    error_code = 403

    def __init__(self, info=None):
        if info:
            HTTPError.__init__(self, info)
        else:
            HTTPError.__init__(self)
        self.error_header = '403 Forbidden'

    def __str__(self):
        return "<403 FORBBIDEN>"


class HTTP500Error(HTTPError):
    error_code = 500

    def __str__(self):
        return "<server error>"


class HTTP400Error(HTTPError):
    error_code = 400

    def __init__(self, info=None):
        if info:
            HTTPError.__init__(self, info)
        else:
            HTTPError.__init__(self)
        self.error_header = '400 Bad Request'

    def __str__(self):
        return "<400 Bad Request>"