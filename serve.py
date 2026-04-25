#!/usr/bin/env python3
import os, sys
from http.server import HTTPServer, SimpleHTTPRequestHandler

os.chdir('/Users/takahirohayashi/Downloads/keys-pages')
httpd = HTTPServer(('', 8766), SimpleHTTPRequestHandler)
httpd.serve_forever()
