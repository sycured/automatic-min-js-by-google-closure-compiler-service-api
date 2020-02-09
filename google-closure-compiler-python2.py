#!/usr/bin/env python2
# coding: utf-8

"""Automatic min JS by Google Closure Compiler Service API."""

import httplib
import sys
import urllib

INPUT = sys.argv[1]
OUTPUT = INPUT.split('.js')[0] + '.min.js'

FILE_IN = open(INPUT, 'r')
STRING = FILE_IN.read()
FILE_IN.close()

PARAMS = urllib.urlencode([
    ('js_code', STRING),
    ('compilation_level', 'SIMPLE_OPTIMIZATIONS'),
    ('output_format', 'text'),
    ('output_info', 'compiled_code'),
])

HEADERS = {'Content-type': 'application/x-www-form-urlencoded'}
CONN = httplib.HTTPConnection('closure-compiler.appspot.com')
CONN.request('POST', '/compile', PARAMS, HEADERS)
RESPONSE = CONN.getresponse()
DATA = RESPONSE.read()
CONN.close()
FILE_OUT = open(OUTPUT, 'w')
FILE_OUT.write(DATA)
FILE_OUT.close()
