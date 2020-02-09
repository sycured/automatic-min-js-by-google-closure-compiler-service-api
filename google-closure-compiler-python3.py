#!/usr/bin/env python3
# coding: utf-8

"""Automatic min JS by Google Closure Compiler Service API."""

import http.client
import sys
import urllib

INPUT = sys.argv[1]
OUTPUT = INPUT.split('.js')[0] + '.min.js'

with open(INPUT, 'r') as input_file:
    STRING = input_file.read()

PARAMS = urllib.parse.urlencode([
    ('js_code', STRING),
    ('compilation_level', 'SIMPLE_OPTIMIZATIONS'),
    ('output_format', 'text'),
    ('output_info', 'compiled_code'),
])

HEADERS = {'Content-type': 'application/x-www-form-urlencoded'}
CONN = http.client.HTTPConnection('closure-compiler.appspot.com')
CONN.request('POST', '/compile', PARAMS, HEADERS)
RESPONSE = CONN.getresponse()
DATA = RESPONSE.read().decode('utf-8')
CONN.close()

with open(OUTPUT, 'w') as output_file:
    print(DATA, file=output_file)
